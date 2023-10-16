from nonebot import logger
import toml
config_toml = toml.load("pyproject.toml")
adapters = []
for adapter in config_toml["tool"]["nonebot"]["adapters"]:
    adapters.append(adapter["name"])

# 加载适配器内容
load_adapters = []
for adapter in adapters:
    if adapter == "OneBot V11":
        from nonebot.adapters.onebot.v11 import (
            Bot as Bot,
            MessageEvent as MessageEvent,
            GroupMessageEvent as GroupMessageEvent,
            MessageSegment as MessageSegment
        )
        load_adapters.append(adapter)
        break
    elif adapter == "RedProtocol":
        from nonebot.adapters.red import (
            Bot as Bot,
            MessageEvent as MessageEvent,
            GroupMessageEvent as GroupMessageEvent,
            MessageSegment as MessageSegment
        )
        load_adapters.append(adapter)
        break
    else:
        logger.info(f"nonebot_plugin_bili_push插件不支持适配器{adapter},将不处理该适配器的消息")

