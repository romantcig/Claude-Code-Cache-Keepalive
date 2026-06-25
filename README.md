[中文](https://github.com/romantcig/Claude-Code-Cache-Keepalive/blob/main/README_CN.md)

# Claude-Code-Cache-Keepalive
Provide a 5m cache keep-alive for Claude Code. This significantly improves the cache hit rate for long conversations and reduces the costs associated with them. The advantage is that it directly reuses built-in functionality for silent keep-alive, requires no proxy, and does not interfere with the main conversation.

⚠️ **Risks & Disclaimers**

Risks are unknown; you assume all responsibility for the consequences.

1. Applies only to version 2.1.185.
2. No additional updates are provided, and there is no circuit-breaker mechanism.
3. Applies only to a 5-min cache validity period.
4. Keeping content in cache for an extended period may violate the user agreement.

This project is intended solely for educational and research purposes and aims to demonstrate how to maintain cache validity, how to optimize the Claude Code cache to improve cache hit rates, and how to reuse the cache.

⚠️ **Important Disclaimer Regarding Model Use:**
Using this project in conjunction with Anthropic’s official models may violate Anthropic’s Terms of Service. We do not encourage, support, or recommend using this tool in conjunction with Anthropic’s official API.
If you choose to do so, you will be solely responsible for all compliance and operational risks.

---

## Prerequisites
- **Platform**: Windows (This static patch specifically targets the native Windows executable `claude.exe`).
- **Claude Code Version**: Exact `v2.1.185` (You can check your version by running `claude --version` in your terminal).

## Usage / Installation
You can patch your Claude Code using either the compiled executable or the Python script directly.

### Method 1: Via Compiled Executable (Recommended)
1. Close any running instances of **Claude Code**.
2. Go to the [Releases](https://github.com/romantcig/Claude-Code-Cache-Keepalive/releases) page and download the compiled `Patch-X5-v2.9-v2.1.185-Static.exe` binary.
3. Run the downloaded `.exe` file. It will automatically verify the target file, back it up, and apply the patch.
*(No Python installation required).*

### Method 2: Via Python Script (Requires Python 3.x)
1. Close any running instances of **Claude Code**.
2. Download `Patch-X5-v2.9-v2.1.185-Static.py`.
3. Run the script in your terminal:
   ```bash
   python Patch-X5-v2.9-v2.1.185-Static.py
   ```

## How to Rollback / Restore
Our script and executable have a built-in one-click restore feature. You can easily revert the patch:

### Method A: Via Command Line (Recommended)
1. Close **Claude Code**.
2. Run the restore command depending on how you applied the patch:
   * **If you used the script**:
     ```bash
     python Patch-X5-v2.9-v2.1.185-Static.py --restore
     ```
   * **If you used the executable**:
     ```cmd
     Patch-X5-v2.9-v2.1.185-Static.exe --restore
     ```

### Method B: Manual Restore
If you prefer to restore manually:
1. Close **Claude Code**.
2. Go to the Claude executable directory (typically `C:\Users\<YourUsername>\.local\bin`).
3. Delete the patched `claude.exe`.
4. Rename the backup file `claude.exe.x5patch-bak` back to `claude.exe`.

## Acknowledgements
This project gratefully acknowledges the [LINUX DO Community](https://linux.do/) for their open-source promotion support.
