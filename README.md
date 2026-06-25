[汉语](https://github.com/romantcig/CC-Cache-La/blob/main/README_CN.md#cc-%E7%BC%93%E5%AD%98%E4%BF%9D%E6%B4%BB)

# CC-Cache-La
Provide a 5m cache keep-alive for Claude Code. This significantly improves the cache hit rate for long conversations and reduces the costs associated with them. The advantage is that it directly reuses built-in functionality for silent keep-alive, requires no proxy, and does not interfere with the main conversation.


⚠️
Risks are unknown; you assume all responsibility for the consequences.

1. Applies only to version 2.1.185.
2. No additional updates are provided, and there is no circuit-breaker mechanism.
3. Applies only to a 5-min cache validity period.
4. Keeping content in cache for an extended period may violate the user agreement.

This project is intended solely for educational and research purposes and aims to demonstrate how to maintain cache validity, how to optimize the Claude Code cache to improve cache hit rates, and how to reuse the cache.

⚠️ **Important Disclaimer Regarding Model Use:**
Using this project in conjunction with Anthropic’s official models may violate Anthropic’s Terms of Service. We do not encourage, support, or recommend using this tool in conjunction with Anthropic’s official API.
If you choose to do so, you will be solely responsible for all compliance and operational risks.
