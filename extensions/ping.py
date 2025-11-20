import time

from discord.ext import commands

from utils.core import Bot
from utils.assets import Emojis


client = Bot().client


@commands.hybrid_command(
    name = 'ping',
    description = "Check the bot's ping and response time.",
    aliases = [],
    with_app_command = True
)
async def command(ctx: commands.Context):
    dc_time = time.time()
    await ctx.typing(ephemeral = True)
    dc_time = round((time.time() - dc_time) * 100, 2)

    ping = round(client.latency * 100, 2)
    if ping > 50:
        ping_emoji = Emojis.ping_bad
    elif ping > 25:
        ping_emoji = Emojis.ping_ok
    else:
        ping_emoji = Emojis.ping_good


    await ctx.reply(f'{ping_emoji} **Ping:** {ping}ms'
                    f'\n{Emojis.time} **Discord Response Time:** {dc_time}ms', ephemeral = True)


async def setup(bot: commands.Bot):
    bot.add_command(command)
