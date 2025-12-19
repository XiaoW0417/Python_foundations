# Python 学习笔记

## 1. 虚拟环境管理
用于隔离不同项目的依赖库（推荐使用 `uv venv` 或内置 `venv`）。

- **使用 uv 创建环境**: `uv venv` (默认创建 `.venv` 目录)
- **指定 Python 版本创建**: `uv venv --python 3.13`
- **内置 venv 创建**: `python3 -m venv venv`
- **激活环境**: `source .venv/bin/activate` 或 `source venv/bin/activate` (macOS/Linux)
- **退出环境**: `deactivate`
- **检查当前环境**: `which python` (查看 python 路径是否在 venv 文件夹内)

## 2. Python 版本管理 (uv)
`uv` 可以安装与管理多个 Python 版本，并与项目绑定。

- **安装 uv** (macOS/Linux): `curl -LsSf https://astral.sh/uv/install.sh | sh` [docs.astral.sh/uv](https://docs.astral.sh/uv/) 
- **安装最新 Python**: `uv python install`  [docs.astral.sh/uv 安装 Python](https://docs.astral.sh/uv/guides/install-python/)
- **安装特定版本**: `uv python install 3.13` 或 `uv python install 3.13.0`
- **查看已安装版本**: `uv python list`
- **升级版本（预览）**: `uv python upgrade` 或 `uv python upgrade 3.13`
- **在项目中固定版本**: `uv python pin 3.13` (创建 `.python-version`)  [docs: Python versions](https://docs.astral.sh/uv/concepts/python-versions/)
- **在命令中选择版本**: 大多数命令支持 `--python 3.13`，如 `uv venv --python 3.13`
- **注意 PATH**: `uv` 会把已安装的 Python 可执行文件放到 `~/.local/bin`，确保该目录在 `PATH` 中；可运行 `uv tool update-shell` 自动配置。

## 3. 常用 Python3 命令

### 基础运行
- **运行脚本**: `python3 script.py`
- **进入交互模式**: `python3` (输入 `exit()` 或 `Ctrl+D` 退出)
- **查看版本**: `python3 --version`
- **运行单行代码**: `python3 -c "print('Hello')"`

### 模块与工具 (-m)
**`-m` (run module as a script)**: 让 Python 找到指定模块并执行它。这能确保使用的是当前 Python 环境下的工具，避免版本混淆（例如使用 `python3 -m pip` 而不是直接用 `pip`）。

- **启动简易 HTTP 服务器**: `python3 -m http.server 8000` (当前目录作为网站根目录)
- **查看模块路径**: `python3 -m site`
- **格式化 JSON**: `echo '{"a":1}' | python3 -m json.tool`

### 包管理 (uv 推荐)
`uv` 提供兼容 `pip` 的接口，速度更快、可复用缓存；也支持基于 `pyproject.toml` 的项目管理。

- **pip 兼容接口**:
  - 安装包: `uv pip install pandas`
  - 安装 requirements.txt: `uv pip install -r requirements.txt`
  - 列出包: `uv pip list`
  - 导出包列表: `uv pip freeze > requirements.txt`
- **项目式管理**:
  - 创建项目: `uv init myproj`
  - 添加依赖: `uv add requests` (安装requests库，添加到 `pyproject.toml` 中，同步lock)
  - 生成锁文件: `uv lock`（单独修改toml之后才需要）
  - 同步安装: `uv sync` (同步toml中的环境)
  - 运行脚本/工具: `uv run script.py` （在当前环境中运行，没环境时会自动装环境）
- **工具运行/安装**:
  - 临时运行工具: `uvx ruff --version`
  - 安装为可执行工具: `uv tool install ruff`

## 4. 常见问题排查

### 为什么 uv 指定版本没生效？
- 检查 `.python-version` 是否存在且版本正确：`cat .python-version`
- 检查 `PATH` 是否包含 `~/.local/bin`：`echo $PATH`
- 查看 uv 识别的版本：`uv python list`

1.  **临时解决**: 在命令中直接指定版本。
    `uv venv --python 3.13`
2.  **永久解决**: 使用 `uv python pin 3.13` 固定项目版本，并确保 `~/.local/bin` 在 `PATH` 中；必要时重启终端。

## 5. IDE 配置（VS Code 示例）
- 选择解释器：`Cmd+Shift+P` → `Python: Select Interpreter` → 指向 `.venv/bin/python` 或 `env_py_foundation/bin/python`
- 项目固化：在 `.vscode/settings.json` 中设置
  ```
  {
    "python.defaultInterpreterPath": ".venv/bin/python"
  }
  ```
