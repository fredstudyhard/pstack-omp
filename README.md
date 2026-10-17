# pstack for OMP

Lauren Tan（poteto）的 pstack 工程工作流程，完整移植到 **Oh My Pi（OMP）**。以 Michael Denyer 的維護版為 fork 基底，改用 OMP 原生工具與角色，不需要 Claude Code、Pi extension 或另一份模型設定。

## 開始體驗

需求：OMP、Python 3、Git。Bun 與 GitHub CLI 只用於對應的 PR／長任務 helpers。

```sh
python3 tools/omp.py doctor
python3 tools/omp.py check
python3 tools/omp.py install --dry-run
python3 tools/omp.py install
```

需要完整的 PR watcher／orchestration helpers 時，先明確取得已審查、固定版本的 production dependency，再重新 materialize：

```sh
(cd skills/poteto-mode/scripts && bun install --frozen-lockfile --production --ignore-scripts)
python3 tools/omp.py install
```

安裝器只會連同固定的 `commander@14.0.0` 複製必要 dependency，不執行安裝／lifecycle scripts；缺依賴時 helpers 會停止並給出 setup 指令，不自行上網。

安裝只寫入自己擁有的 `~/.omp/agent/skills/pstack-*`。全域只註冊 14 個主入口，另外 50 份流程／原則作為主入口下的按需 guides；完整能力仍保留。由舊版升級時只停用舊的全域入口，不刪移檔案。既有非本工具擁有的同名路徑或本機修改會阻擋更新；不修改模型、provider、chezmoi 或其他 runtime 設定。重新啟動 OMP，或開新 session，再使用：

```text
/skill:pstack-poteto-mode 修復這個問題，先實際重現，再找根因、修正與驗證。
/skill:pstack-how 說明這個專案的請求如何進入並寫入資料。
/skill:pstack-interrogate 審查目前的變更，列出有證據的問題。
/skill:pstack-poteto-help 我想做一次效能調查，該如何開始？
```

不需要開啟全域 always-on 模式。明確進入 pstack 的任務會使用它的 playbook；一般聊天與原有技能不被取代。

工程工作流以 pstack 命名為主：review 用 `pstack-interrogate`（預設一般審查，深度／多模型另選模式）、文章去制式化用 `pstack-unslop`、程式清理／簡化用 `pstack-deslop`、團隊派工用 `pstack-swarm`。專業操作、安全審查及授權治理仍獨立，不全部改姓 pstack。

低頻流程透過主入口指定，例如 `/skill:pstack-poteto-mode bro`。內部原則可讀 `skill://pstack-poteto-mode/references/library/principle-prove-it-works/GUIDE.md`，不再使用舊的獨立 skill 名稱。

### 一個可親自操作的修復任務

```sh
python3 tools/demo.py
```

它建立一個獨立的合成 issue-desk Git repo，提供 workspace 與啟動指令。跟著輸出進入 OMP，看它透過真正 CLI 重現分頁錯誤、修正、驗證，再交付結果。沒有真實帳號、資料或外部 API；不會改動你的產品 repo。每次執行建立新工作區，不覆蓋既有進度。

Repo 隨附可直接執行的 [verification skill 範例](examples/issue-desk/verification/SKILL.md)。可觀察 28 次真正 CLI 驗證與檔案副作用檢查：

```sh
python3 examples/issue-desk/verification/scripts/verify.py
```

## 完整範圍

- 54 個原版 skills 全部保留，包括 24 個 principles；另保留維護版的 10 個公開 workflows。
- 23 個任務 playbooks，涵蓋調查、bug、功能、重構、效能、架構比較、驗證、PR、長任務、交接與恢復。
- `arena` 比較解法，`swarm` 分割工作；使用 OMP 原生 `task` 與既有角色。
- 真實介面驗證、專案 verification skill／feature map、盲評流程與可恢復 checkpoint。
- Cursor bot routine 改為受控的 OMP RPC 控制頁 authoring workflow；無背景 owner 時使用明確 checkpoint/resume，不宣稱雲端自動喚醒。

這些是 workflow 能力，不是自帶每個產品的權限、整合或品質保證。使用前請依 [驗證入口與覆蓋界線](docs/omp-verification.md) 執行；實際產品或發布另行驗收。

## 安全與回復

上游指示不授予外部寫入、憑證存取、發布、刪除或付費資源權限。必需的獨立審查無法執行時，該 gate 保持關閉。沒有自動 merge、cron、無限 polling、偷偷重試或第二套模型 registry。

```sh
python3 tools/omp.py disable
```

`disable` 僅把本工具擁有的 entrypoints 標為停用，**不刪除或移動 `.omp` 內容**。新 session 不再發現它們。重新執行 `install` 可啟用已審查的來源；若本機安裝檔有額外修改，會停止而不覆蓋。

若你的既有 OMP user configuration 已選擇停用被取代的通用入口，整包停用後也要從其 canonical config source 恢復它們；這不是安裝器可擅自修改的設定。chezmoi 管理者應重新 render／scoped apply 該 target。不要停用或刪除安全、領域操作與治理 guard。

## 維護

- [原生 runtime contract](skills/poteto-mode/references/omp-runtime.md)
- [完整功能與來源清單](docs/omp-capabilities.json)
- [移植決策與差異](docs/omp-porting.md)
- [更新、驗證與回復](docs/omp-maintenance.md)
- [來源、版本與完整性](tools/omp-provenance.json)

原始 pstack © Lauren Tan；先前移植與補充 © Michael Denyer、Cursor。保留 [MIT license](LICENSE)、[Cursor team kit license](LICENSE-cursor-team-kit)、[thermos license](LICENSE-thermos) 與 [NOTICE](NOTICE.md)。本 fork 非 Cursor、OMP 或原作者官方發行版。
