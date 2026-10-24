"""篝火：安装完成后，打印本机接入命令路径和客户端配置示例（不读取、不保存任何密钥）。"""
import json
import os
import sys

bin_dir = os.path.dirname(sys.executable)
ext = ".exe" if os.name == "nt" else ""
platforms = {
    "doudian": ["DOUDIAN_APP_KEY", "DOUDIAN_APP_SECRET", "DOUDIAN_SHOP_ID", "DOUDIAN_ACCESS_TOKEN"],
    "jd": ["JD_APP_KEY", "JD_APP_SECRET", "JD_ACCESS_TOKEN"],
    "taobao": ["TAOBAO_APP_KEY", "TAOBAO_APP_SECRET", "TAOBAO_ACCESS_TOKEN"],
}
servers = {}
for name, keys in platforms.items():
    cmd = os.path.join(bin_dir, f"mcp-cn-{name}{ext}")
    servers[f"cn-{name}"] = {"command": cmd, "env": {k: "在这里填你自己的值" for k in keys}}

print()
print("安装完成。本工具是「AI 工具接入协议（MCP）」服务，不会自己弹出界面，需要在支持该协议的 AI 客户端里配置后使用。")
print("在 AI 客户端（Claude 桌面版、Cherry Studio、Cline 等）的接入配置里加入下面的内容，")
print("把「在这里填你自己的值」换成你在平台开放平台申请到的凭证；只配置你用到的平台。")
print("凭证只写在你自己电脑上的客户端配置里。")
print("其余平台命令同理：mcp-cn-pinduoduo、mcp-cn-kuaishou、mcp-cn-xiaohongshu、mcp-cn-weixin-store、mcp-cn-oceanengine，")
print("它们所需的环境变量名见 .env.example。")
print()
print(json.dumps({"mcpServers": servers}, ensure_ascii=False, indent=2))
print()
try:
    input("按回车关闭这个窗口")
except EOFError:
    pass
