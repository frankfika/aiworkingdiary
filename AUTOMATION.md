# 自动化执行说明

本仓库已集成一个基础的自动化框架，支持按照固定时间运行任务：

## 结构
- `automation/tasks.json`：任务配置文件（可编辑你的指令合集）
- `scripts/auto_worker.py`：Python执行器，读取并执行任务
- `.github/workflows/auto-worker.yml`：GitHub Actions定时工作流

## 使用方法
1. 编辑 `automation/tasks.json`，添加或调整任务：
   - `type: update_timestamp`：更新时间戳到文件
   - `type: shell`：执行Shell命令（谨慎使用）
2. 推送变更到远程仓库。
3. GitHub Actions会按计划自动运行（默认每30分钟）。你也可以在仓库的`Actions`页面手动触发。

## 机密与令牌
- 如需调用外部API，可在GitHub仓库 `Settings -> Secrets and variables -> Actions` 添加密钥，例如 `OPENAI_API_KEY`，并在工作流中以环境变量使用。
- 当前工作流已授予 `contents: write` 权限，用于回写生成的文件。

## 注意事项
- 所有自动执行都在GitHub的容器内运行，不在本机执行。
- Shell任务可能带来风险，请确保命令安全且幂等。
- 如需更高频率或复杂编排，可扩展 `auto_worker.py` 支持更多任务类型与错误重试。

## 在Trae本地自动运行（可选）
如果你希望在Trae内本地持续执行任务（IDE开启时），可使用守护脚本：

- 启动：
  - 在仓库根目录运行 `python3 scripts/trae_daemon.py`
  - 可通过设置环境变量 `INTERVAL_SECONDS` 调整执行间隔（默认900秒）。
- 日志：
  - 查看 `automation/trae_daemon.log` 获取运行日志与错误信息。
- 停止：
  - 关闭进程或在Trae停止正在运行的命令。

注意：Trae本地守护依赖IDE处于运行状态。如果需要真正“24/7”无IDE、无电脑在线，建议使用上面的 GitHub Actions 定时工作流，或在macOS使用 LaunchAgent 配置系统级定时任务。