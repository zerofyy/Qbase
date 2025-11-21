import sys
import time

from utils.core import Bot
from utils.logging import Logger, setup_logs_handler
from utils.assets import Emojis, BOT_TOKEN

time_start = time.time()


Logger.info('Qbase', 'Initializing wake up protocols...')


setup_logs_handler()

bot = Bot()
client = bot.client


Logger.info('Qbase', 'Creating redirection hook for critical errors...')
def redirected_exception_hook(exctype, value, traceback):
    Logger.error('Crash Report', f'Type: {exctype}\nValue: {value}\nTraceback: {traceback}')

sys.excepthook = redirected_exception_hook


@client.event
async def on_ready():
    ext_loaded, ext_total = await bot.load_extensions()

    ping = round(client.latency * 100, 1)
    if ping > 50:
        ping_emoji = Emojis.ping_bad
    elif ping > 25:
        ping_emoji = Emojis.ping_ok
    else:
        ping_emoji = Emojis.ping_good

    time_taken = round(time.time() - time_start, 1)

    bot_info = await client.application_info()
    await bot_info.owner.send(
        f'{Emojis.reload} **Qbase is Online!**\n'
        f'> {Emojis.slash} `Prefix:` **{bot.prefix}**\n'
        f'> {ping_emoji} `Ping:` **{ping}**\n'
        f'> {Emojis.time} `Time Taken:` **{time_taken} sec**\n'
        f'> {Emojis.folder} `Extensions Loaded:` **{ext_loaded} / {ext_total}**'
    )

    Logger.ok('Qbase', 'Wake up protocols successfully initialized.')


Logger.info('Qbase', 'Connecting to Discord...')
client.run(BOT_TOKEN)
