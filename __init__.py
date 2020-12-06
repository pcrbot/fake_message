from hoshino import Service
from .fake_mes import produce_fake_mes

sv = Service("消息造假")


@sv.on_prefix("假消息")
async def fake_mes(bot, ev):

    mes = ev["raw_message"][3:].strip()
    data = produce_fake_mes(mes)

    await bot.send_group_forward_msg(group_id=ev['group_id'], messages=data)


