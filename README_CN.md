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
- **Claude Code 版本**：必须为官方的 `v2.1.185`（您可以在终端运行 `claude --version` 来确认当前版本）。

## 使用方法
您可以使用编译好的可执行文件（推荐）或直接运行 Python 脚本来应用补丁。

### 方法一：使用编译好的可执行文件（推荐）
1. 关闭所有正在运行的 **Claude Code** 终端。
2. 前往 [Releases](https://github.com/romantcig/Claude-Code-Cache-Keepalive/releases) 页面下载打包好的 `Patch-X5-v2.9-v2.1.185-Static.exe` 文件。
3. 双击或在终端运行该 `.exe` 文件。它会自动校验 `claude.exe` 并完成备份与修补。
*(此方法无需安装 Python)。*

### 方法二：使用 Python 脚本（需要安装 Python 3.x）
1. 关闭所有正在运行的 **Claude Code** 终端。
2. 下载 `Patch-X5-v2.9-v2.1.185-Static.py`。
3. 在终端中运行脚本：
   ```bash
   python Patch-X5-v2.9-v2.1.185-Static.py
   ```

## 如何回滚/恢复原版
补丁脚本和可执行文件均内置了一键还原功能，您可以非常方便地撤销补丁：

### 方法 A：通过命令行还原（推荐）
1. 关闭 **Claude Code**。
2. 根据您的使用方式运行还原命令：
   * **若您使用的是脚本**：
     ```bash
     python Patch-X5-v2.9-v2.1.185-Static.py --restore
     ```
   * **若您使用的是可执行文件**：
     ```cmd
     Patch-X5-v2.9-v2.1.185-Static.exe --restore
     ```

### 方法 B：手动还原
如果您希望手动操作：
1. 关闭 **Claude Code**。
2. 进入 Claude 的安装目录（通常在 `C:\Users\<您的用户名>\.local\bin`）。
3. 删除已修改的 `claude.exe`。
4. 将备份文件 `claude.exe.x5patch-bak` 重命名还原为 `claude.exe`。

## 致谢
本项目感谢 [LINUX DO 社区](https://linux.do/) 提供的开源推广支持。
