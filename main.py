import sys

from utils.core import Bot
from utils.logging import Logger, setup_logs_handler
from utils.assets import BOT_TOKEN


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
    await bot.load_extensions()

    Logger.ok('Qbase', f'Wake up protocols successfully initialized.\n'
                       f'  * Prefix: {bot.prefix}\n'
                       f'  * Ping: {round(client.latency * 100, 1)}ms\n')


Logger.info('Qbase', 'Connecting to Discord...')
client.run(BOT_TOKEN)
