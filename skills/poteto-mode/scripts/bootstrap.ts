import { existsSync, readFileSync } from "node:fs";
import { join } from "node:path";

if (typeof Bun === "undefined") {
  throw new Error("pstack helper tooling requires Bun; no dependency installation was attempted.");
}

const scriptsDirectory = import.meta.dir;
const commanderPackagePath = join(scriptsDirectory, "node_modules", "commander", "package.json");

export function ensureDependenciesInstalled(): void {
  const expected = JSON.parse(readFileSync(join(scriptsDirectory, "package.json"), "utf8")).dependencies.commander;
  if (existsSync(commanderPackagePath)) {
    const installed = JSON.parse(readFileSync(commanderPackagePath, "utf8")).version;
    if (installed === expected) return;
  }
  throw new Error(
    "Missing reviewed pstack helper dependency. After source review and authorization, run " +
    "`bun install --frozen-lockfile --production --ignore-scripts` in " +
    `${scriptsDirectory}. No installer or network request was started.`
  );
}
