# Water Accounting and Unaccounted Water in the Cornwall-on-Hudson Water System, 2019–2025

独立研究工作区 · 初始搭建日期：2026-10-19（America/New_York）

为什么 2024–2025 年总供水量变化较小，计费用水量与未核算水量却变化明显？先建立口径一致的 2019–2025 年水量账目，识别需要部门核对的记录。

**当前阶段：研究前基础搭建。** 这不是已完成的研究，也不是供水部门已确认的数据产品。

从 [START_HERE.md](START_HERE.md) 进入。研究范围见 [research/brief.md](research/brief.md)，下一步见 [research/TASKS.md](research/TASKS.md)，agent 分工见 [agents/README.md](agents/README.md)。

## 快速开始

```sh
uv sync --locked
make check
make fetch
make preflight
```

`make fetch` 访问公开原始来源并保存本地快照；`make preflight` 生成搭建期诊断。原始文件和行级衍生数据不提交 Git。克隆仓库后需重新抓取本地原始数据。Python 3.11+；依赖记录在 `uv.lock`。

另可运行 `make extract` 生成带物理页码的自动文本。优先使用已安装的 Poppler `pdftotext`，否则回退到 pypdf；2019 年复杂 PDF 需要 Poppler。若它不在 PATH，使用 `PDFTOTEXT=/absolute/path/to/pdftotext make extract`。自动抽取不代表人工复核。

## 目录

- `.codex/agents/`：项目范围的真实 Codex custom-agent 配置，继承用户模型和权限。
- `research/`：研究范围、分析计划、证据／来源清单、任务和决策。
- `data/seed/`、`data/schema/`、`data/manifests/`：可版本控制的种子表、结构和抓取收据。
- `data/raw/`、`data/interim/`、`data/processed/`、`data/restricted/`：只在本地保留的原始或行级数据。
- `src/`、`scripts/`、`tests/`：可复现方法与关键研究口径检查。
- `reports/`：可以审阅的汇总结果；不含逐户地址或坐标。

研究拟服务 Cornwall-on-Hudson Water Department；尚未取得部门台账或联系部门。AI 协助搭建和分析须在将来对外成果中披露。无自动监控、无人值守研究或后台模型任务。
