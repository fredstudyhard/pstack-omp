#!/usr/bin/env python3
"""Native OMP skill installation, validation and provenance; standard library only."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
OWNER = "fredstudyhard/pstack-omp"
MARKER = ".pstack-omp.json"
PRIMARY_SKILLS = frozenset("pstack-" + name for name in (
    "poteto-mode", "poteto-help", "how", "why", "architect", "arena",
    "interrogate", "swarm", "unslop", "deslop", "create-verification-skill",
    "maintain-verification-skill", "show-me-your-work", "typescript-best-practices",
))


def skill_sources(root=ROOT):
    return sorted(path.parent for path in (root / "skills").glob("*/SKILL.md"))


def frontmatter(text):
    match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.S)
    if not match:
        raise ValueError("missing frontmatter")
    result = {}
    for line in match[1].splitlines():
        field = re.match(r"^([\w-]+):\s*(.*)$", line)
        if field:
            result[field[1]] = field[2].strip().strip('\"\'')
    return result


def inventory(root=ROOT):
    result = []
    for source in skill_sources(root):
        data = frontmatter((source / "SKILL.md").read_text())
        name = data.get("name", "")
        if name != "pstack-" + source.name or not re.fullmatch(r"pstack-[a-z0-9-]+", name):
            raise ValueError(f"invalid native name: {source}: {name}")
        if not data.get("description"):
            raise ValueError(f"missing description: {source}")
        result.append((name, source))
    if not result:
        raise ValueError("no native skills found")
    return result


def source_files(source):
    dependency = source / "scripts/node_modules/commander/package.json"
    if any(path.is_symlink() for path in (dependency, *dependency.parents)):
        raise ValueError(f"refusing linked dependency source: {dependency}")
    if dependency.exists():
        package = json.loads(dependency.read_text())
        if package.get("name") != "commander" or package.get("version") != "14.0.0":
            raise ValueError("Only the reviewed commander@14.0.0 production dependency may be materialized")
    for path in sorted(source.rglob("*")):
        parts = path.relative_to(source).parts
        if any(part in {"__pycache__", ".git"} for part in parts):
            continue
        if "node_modules" in parts and parts[:3] != ("scripts", "node_modules", "commander"):
            continue
        if path.is_symlink():
            raise ValueError(f"source symlink is not installable: {path}")
        if path.is_file():
            yield path


def digest(source):
    hasher = hashlib.sha256()
    for path in source_files(source):
        hasher.update(path.relative_to(source).as_posix().encode() + b"\0")
        hasher.update(path.read_bytes() + b"\0")
    return hasher.hexdigest()


def safe_destination(path, regular_file=False):
    if ".." in path.parts:
        raise ValueError(f"refusing parent traversal: {path}")
    for item in (path, *path.parents):
        if item.is_symlink():
            raise ValueError(f"refusing symlink destination or ancestor: {item}")
    if path.exists():
        if regular_file and not path.is_file():
            raise ValueError(f"refusing non-regular file: {path}")
        if path.is_file() and path.stat().st_nlink != 1:
            raise ValueError(f"refusing hard-linked destination: {path}")


def owned(destination):
    marker = destination / MARKER
    try:
        safe_destination(destination)
        safe_destination(marker, regular_file=True)
        data = json.loads(marker.read_text())
        files = data.get("files")
        return (
            data.get("owner") == OWNER
            and isinstance(files, dict)
            and all(isinstance(key, str) and not Path(key).is_absolute() and ".." not in Path(key).parts
                    and isinstance(value, str) for key, value in files.items())
        )
    except (OSError, ValueError, AttributeError):
        return False


def installed_path(path, root):
    short, *parts = path.relative_to(root / "skills").parts
    name = "pstack-" + short
    if name in PRIMARY_SKILLS:
        return Path(name, *parts)
    if parts == ["SKILL.md"]:
        parts = ["GUIDE.md"]
    return Path("pstack-poteto-mode", "references", "library", short, *parts)


def installed_content(path, source, entries):
    payload = path.read_bytes()
    if "node_modules" in path.relative_to(source).parts or path.suffix not in {".md", ".mjs", ".js", ".ts", ".sh", ".py", ".json"}:
        return payload
    root = source.parent.parent
    text = payload.decode("utf-8")
    names = {name for name, _ in entries}
    internal = names - PRIMARY_SKILLS

    def relative_reference(match):
        original = Path(os.path.abspath(path.parent / match[0]))
        try:
            original.relative_to(root / "skills")
        except ValueError:
            return match[0]
        if not original.exists():
            return match[0]
        relative = os.path.relpath(installed_path(original, root), installed_path(path, root).parent)
        return relative if relative.startswith(".") else "./" + relative

    text = re.sub(r"(?<![\w:/])(?:\.\.?/)+(?:[\w.-]+/)*[\w.-]+", relative_reference, text)

    def internal_uri(match):
        name, suffix = match[1], match[2]
        if name not in internal:
            return match[0]
        relative = suffix.lstrip("/") if suffix else "GUIDE.md"
        if relative == "SKILL.md":
            relative = "GUIDE.md"
        return "skill://pstack-poteto-mode/references/library/" + name.removeprefix("pstack-") + "/" + relative

    text = re.sub(r"skill://(pstack-[a-z0-9-]+)(/[\w./-]+)?", internal_uri, text)
    text = re.sub(r"/skill:(pstack-[a-z0-9-]+)", lambda match:
                  "/skill:pstack-poteto-mode " + match[1].removeprefix("pstack-")
                  if match[1] in internal else match[0], text)
    if path == source / "SKILL.md":
        enabled = source.name and "pstack-" + source.name in PRIMARY_SKILLS
        value = "true" if enabled else "false"
        if re.search(r"(?m)^enabled:", text):
            text = re.sub(r"(?m)^enabled:.*$", "enabled: " + value, text, count=1)
        else:
            text = text.replace("---\n", "---\nenabled: " + value + "\n", 1)
    return text.encode("utf-8")


def install(target, root=ROOT, dry_run=False):
    target = Path(target).expanduser().absolute()
    safe_destination(target)
    entries = inventory(root)
    plans = {}
    for name, source in entries:
        for path in source_files(source):
            relative = installed_path(path, root)
            owner = relative.parts[0]
            member = Path(*relative.parts[1:]).as_posix()
            if member in plans.setdefault(owner, {}):
                raise ValueError(f"duplicate materialized path: {relative}")
            plans[owner][member] = (path, source)
    if any(name not in {entry for entry, _ in entries} for name in plans):
        raise ValueError("internal guides require the pstack-poteto-mode source")
    existing = {}
    for name in {entry for entry, _ in entries} | plans.keys():
        destination = target / name
        if destination.exists() or destination.is_symlink():
            if not owned(destination):
                raise ValueError(f"collision, preserving unowned path: {destination}")
            old = json.loads((destination / MARKER).read_text())
            expected = old["files"]
            if name not in plans:
                entrypoint = destination / "SKILL.md"
                safe_destination(entrypoint, regular_file=True)
                if not entrypoint.is_file() or hashlib.sha256(entrypoint.read_bytes()).hexdigest() != expected.get("SKILL.md"):
                    raise ValueError(f"untracked or edited retired entrypoint, preserving: {entrypoint}")
            for relative in plans.get(name, {}):
                output = destination / relative
                safe_destination(output, regular_file=True)
                if output.exists() and relative not in expected:
                    raise ValueError(f"unowned installed file, preserving: {output}")
            for relative, checksum in expected.items():
                item = destination / relative
                safe_destination(item, regular_file=True)
                if item.exists() and hashlib.sha256(item.read_bytes()).hexdigest() != checksum:
                    raise ValueError(f"local installed edit, preserving: {item}")
            existing[name] = old
    if dry_run:
        return {"status": "DRY_RUN", "root": str(target), "skills": sorted(plans),
                "internal_guides": len(entries) - len(plans)}
    target.mkdir(parents=True, exist_ok=True)
    for name, files in plans.items():
        destination = target / name
        destination.mkdir(exist_ok=True)
        checksums = {}
        for relative, (path, source) in files.items():
            output = destination / relative
            output.parent.mkdir(parents=True, exist_ok=True)
            payload = installed_content(path, source, entries)
            output.write_bytes(payload)
            shutil.copymode(path, output)
            checksums[relative] = hashlib.sha256(payload).hexdigest()
        (destination / MARKER).write_text(json.dumps({"owner": OWNER, "files": checksums}, indent=2) + "\n")
    retired = []
    for name, old in existing.items():
        if name in plans:
            continue
        entrypoint = target / name / "SKILL.md"
        entrypoint.write_text(disabled_text(entrypoint.read_text()))
        old["files"]["SKILL.md"] = hashlib.sha256(entrypoint.read_bytes()).hexdigest()
        old["disabled"] = True
        old["retired_to"] = "pstack-poteto-mode/references/library/" + name.removeprefix("pstack-") + "/GUIDE.md"
        (target / name / MARKER).write_text(json.dumps(old, indent=2) + "\n")
        retired.append(name)
    return {"status": "INSTALLED", "root": str(target), "count": len(plans),
            "internal_guides": len(entries) - len(plans), "retired": retired, "deleted": 0}


def disabled_text(text):
    if re.search(r"(?m)^enabled:", text):
        return re.sub(r"(?m)^enabled:.*$", "enabled: false", text, count=1)
    return text.replace("---\n", "---\nenabled: false\n", 1)


def disable(target, root=ROOT):
    entries = inventory(root)
    target = Path(target).expanduser().absolute()
    safe_destination(target)
    for name, _ in entries:
        destination = target / name
        if destination.exists() or destination.is_symlink():
            if not owned(destination):
                raise ValueError(f"refusing unowned path: {destination}")
            path = destination / "SKILL.md"
            metadata = json.loads((destination / MARKER).read_text())
            safe_destination(path, regular_file=True)
            if not path.is_file():
                raise ValueError(f"refusing missing entrypoint: {path}")
            if hashlib.sha256(path.read_bytes()).hexdigest() != metadata["files"].get("SKILL.md"):
                raise ValueError(f"local installed edit, preserving: {path}")
    changed = []
    for name, _ in entries:
        path = target / name / "SKILL.md"
        if path.is_file():
            path.write_text(disabled_text(path.read_text()))
            marker = path.parent / MARKER
            metadata = json.loads(marker.read_text())
            metadata["files"]["SKILL.md"] = hashlib.sha256(path.read_bytes()).hexdigest()
            metadata["disabled"] = True
            marker.write_text(json.dumps(metadata, indent=2) + "\n")
            changed.append(name)
    return {"status": "DISABLED", "count": len(changed), "deleted": 0, "root": str(target)}


def check(root=ROOT):
    entries = inventory(root)
    issues = []
    materialized = {installed_path(path, root) for _, source in entries for path in source_files(source)}
    materialized |= {parent for path in list(materialized) for parent in path.parents}
    for name, source in entries:
        entry = (source / "SKILL.md").read_text()
        if "omp-runtime.md" not in entry:
            issues.append(f"{name}: missing runtime contract")
        for path in source.rglob("*.md"):
            if "node_modules" in path.relative_to(source).parts:
                continue
            for target in re.findall(r"\[[^\]]*\]\(([^\s)]+)(?:\s+[^)]*)?\)", path.read_text()):
                if "://" in target or target.startswith(("#", "mailto:")):
                    continue
                target = target.split("#", 1)[0]
                if target and not (path.parent / target).exists():
                    issues.append(f"{path.relative_to(root)}: broken link: {target}")
            rendered = installed_content(path, source, entries).decode("utf-8")
            for target in re.findall(r"\[[^\]]*\]\(([^\s)]+)(?:\s+[^)]*)?\)", rendered):
                if "://" in target or target.startswith(("#", "mailto:")):
                    continue
                target = target.split("#", 1)[0]
                resolved = Path(os.path.normpath(str(installed_path(path, root).parent / target)))
                if target and resolved not in materialized:
                    issues.append(f"{path.relative_to(root)}: broken materialized link: {target}")
    if issues:
        raise ValueError("\n".join(issues))
    return {"status": "PASS", "skills": len(entries), "entrypoints": sum(name in PRIMARY_SKILLS for name, _ in entries), "internal_guides": sum(name not in PRIMARY_SKILLS for name, _ in entries), "principles": sum(name.startswith("pstack-principle-") for name, _ in entries), "playbooks": len(list((root / "skills/poteto-mode/playbooks").glob("*.md")))}


def doctor(root=ROOT):
    tools = {name: shutil.which(name) for name in ("omp", "git", "python3", "bun", "gh", "skillspector")}
    required = ("omp", "git", "python3")
    return {"status": "PASS" if all(tools[name] for name in required) else "BLOCKED", "tools": tools, "optional": {"bun": "PR watcher and orchestration helpers only", "gh": "authorized GitHub workflows only", "skillspector": "absent is NOT a security pass; see security evidence"}, "repo": str(root)}


def manifest(root=ROOT):
    return {name: {"path": str(source.relative_to(root)), "sha256": digest(source)} for name, source in inventory(root)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("check", "doctor", "install", "disable", "manifest"))
    parser.add_argument("--target", type=Path, default=Path.home() / ".omp/agent/skills")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    try:
        if args.action == "install":
            result = install(args.target, dry_run=args.dry_run)
        elif args.action == "disable":
            result = disable(args.target)
        else:
            result = globals()[args.action]()
        print(json.dumps(result, indent=2))
        return 1 if result.get("status") == "BLOCKED" else 0
    except (ValueError, OSError) as error:
        print(str(error), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
