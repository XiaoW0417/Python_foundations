#  Git 操作


---

## 1. 身份配置 (Config)

在使用 Git 之前，必须配置身份信息，以便在提交历史中识别作者。

```bash
# 配置全局用户名和邮箱 (建议与 GitHub 账号一致)
git config --global user.name "YourName"
git config --global user.email "your@email.com"

# 查看当前配置
git config --list
```

---

## 2. 本地项目存档 (Local Flow)

这是在本地开发时最频繁使用的“存盘”三部曲。

| 命令                  | 作用说明                                 |
| --------------------- | ---------------------------------------- |
| `git init`            | 初始化仓库，在当前目录生成 `.git` 文件夹 |
| `git status`          | 查看状态，检查哪些文件已修改或未追踪     |
| `git add .`           | 暂存所有修改，将改动放入“待提交”区域     |
| `git commit -m "msg"`| 正式提交存档，`-m` 后面是本次改动的说明   |
| `git log --oneline`   | 查看提交历史，简洁展示过往的存档点       |

---

## 3. GitHub 云端同步 (Remote)

将本地的代码仓库与 GitHub 远程仓库建立联系。

```bash
# 1. 关联远程地址 (只需执行一次)
# origin 是远程仓库的默认代号
git remote add origin https://github.com/用户名/仓库名.git

# 2. 规范化主分支名称
# -M 强制将当前分支重命名为 main
git branch -M main

# 3. 第一次推送并建立绑定
# -u 参数建立本地与云端分支的追踪关系
git push -u origin main

# 4. 以后推送/拉取只需简化命令
git push   # 推送到云端
git pull   # 从云端同步回本地
```

---

## 4. 撤销与“后悔药” (Undo/Restore)

Git 提供了多种方式处理误操作。

- 撤销文件修改：`git restore <file>`（恢复到上一个 commit 的状态）
- 撤销已暂存的文件：`git restore --staged <file>`（把文件从 add 状态撤回）
- 修改上一次提交：`git commit --amend`（用于补丁或改错字）
- 回退版本但保留代码：`git reset --soft HEAD~1`（撤销最后一次提交）

---

## 5. 分支管理 (Branching)

分支允许你在不影响主线（`main`）的情况下开发新功能。

```bash
# 创建并切换到新分支
git checkout -b feature-name   # 旧版
git switch -c feature-name     # 新版推荐

# 切换分支
git checkout main
git switch main

# 快速切回上一个分支
git checkout -
```

---

## 6. 协作最佳实践 (Best Practices)

### 📂 `.gitignore` 配置

在项目根目录创建 `.gitignore` 文件，防止上传不必要的文件。对于 `uv` 项目，至少包含：

```plaintext
.venv/             # 虚拟环境文件夹
__pycache__/       # Python 运行缓存
.python-version    # uv 锁定的 Python 版本文件
.env               # 敏感的环境变量
```

### ✍️ Commit 规范建议

使用前缀让历史记录清晰可见：

- `feat`: 新功能 (Feature)
- `fix`: 修复 Bug
- `docs`: 文档更新 (README)
- `refactor`: 代码重构 (不影响功能)
- `style`: 格式调整 (空格、缩进等)

### 🔄 uv 团队协作流

1. 开发者 A 推送：`git push`（包含 `pyproject.toml` 和 `uv.lock`）
2. 开发者 B 拉取：`git pull`
3. 开发者 B 同步：`uv sync`（自动根据 A 的锁文件重建一模一样的环境）

---

**手册整理完毕！**  
这份文件可以作为你项目的“生存指南”。如果你已经成功完成了第一次推送，可以继续在此基础上练习分支、协作与回滚等操作。
