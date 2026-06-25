# CC-缓存保活

为 Claude Code 提供 5m 缓存保活。使长对话的缓存命中率大幅提升，减少长对话产生的成本。优势在于直接复用内置功能进行静默保活，无需代理，且不污染主对话。

⚠️ **风险与免责声明**

风险尚不明确；您需对由此产生的后果承担全部责任。

1. 仅适用于 2.1.185 版本。
2. 不提供任何额外更新，也没有熔断机制。
3. 仅适用于 5 分钟的缓存。
4. 在缓存中保留较长时间可能会违反用户协议。

本项目仅用于教育和研究目的，旨在演示如何维持缓存有效性、如何优化 Claude Code 缓存以实现缓存命中率提升，以及如何复用缓存。

⚠️ **关于模型使用的重要免责声明：**
将此项目与 Anthropic 的官方模型结合使用可能会违反 Anthropic 的《服务条款》。我们不鼓励、不支持也不建议将此工具与 Anthropic 的官方 API 结合使用。
如果您选择这样做，则需自行承担所有合规和运营风险。

---

## 前提条件
- **平台**：Windows （此静态补丁专门针对 Windows 本地原生可执行程序 `claude.exe`）。
- **Claude Code 版本**：必须为官方的 `v2.1.185`（通过 SHA-256 哈希值进行精确匹配校验）。
- **运行环境**：已安装 Python 3.x。

## 使用方法
1. 关闭所有正在运行的 **Claude Code** 终端。
2. 运行补丁脚本：
   ```bash
   python Patch-X5-v2.9-v2.1.185-Static.py
   ```
3. 脚本会自动校验 `claude.exe` 的哈希值，并在同目录下自动创建名为 `claude.exe.x5patch-bak` 的备份文件，然后应用修改。

## 如何回滚/恢复原版
如果您需要卸载补丁或在使用中遇到问题，可以随时恢复原始文件：
1. 关闭 **Claude Code**。
2. 进入 Claude 的安装目录（通常在 `C:\Users\<您的用户名>\.local\bin`）。
3. 删除已修改的 `claude.exe`。
4. 将备份文件 `claude.exe.x5patch-bak` 重命名还原为 `claude.exe`。
   *(或者，您可以在 PowerShell 终端中直接运行以下命令完成一键恢复)*：
   ```powershell
   Remove-Item "$env:USERPROFILE\.local\bin\claude.exe" -Force
   Rename-Item "$env:USERPROFILE\.local\bin\claude.exe.x5patch-bak" "claude.exe"
   ```
