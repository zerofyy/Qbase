import os
import glob

import discord
from discord.ext import commands

from utils.logging import Logger


class Bot:
    """ Singleton representation of the Discord bot client. """

    _instance = None
    prefix: str = None
    client: commands.Bot = None


    def __new__(cls) -> 'Bot':
        """ Create a new Bot instance and set up the Discord bot client, unless an instance already exists. """

        if cls._instance is None:
            cls._instance = super(Bot, cls).__new__(cls)

            cls._instance.prefix = '>' if os.environ.get('USER', os.environ.get('USERNAME')) == 'offic' else '?'

            cls._instance.client = commands.Bot(
                command_prefix = cls._instance.prefix,
                intents = discord.Intents.all(),
                allowed_mentions = discord.AllowedMentions(everyone = False, roles = False, replied_user = False),
                case_insensitive = True
            )

            Logger.ok('BotClient', 'Successfully created the Discord bot client.')

        return cls._instance


    async def load_extensions(self) -> None:
        """ Load all extensions. """

        Logger.info('BotClient', 'Loading extensions...')

        for ext in glob.glob('extensions/*'):
            if ext.startswith('__'):
                continue

            ext = ext[11:-3]

            try:
                await self.client.load_extension(f'extensions.{ext}')
                Logger.ok('BotClient', f'  * Extension "{ext}" loaded successfully.')

            except commands.ExtensionNotFound:
                Logger.error('BotClient', f'  * Extension "{ext}" could not be found.')

            except commands.ExtensionAlreadyLoaded:
                Logger.error('BotClient', f'  * Extension "{ext}" is already loaded.')

            except commands.NoEntryPointError:
                Logger.error('BotClient', f'  * Extension "{ext}" is missing a setup function.')

            except commands.ExtensionFailed:
                Logger.error('BotClient', f'  * Extension "{ext}" encountered an error while loading.')

        Logger.ok('BotClient', 'Finished loading extensions.')



__all__ = ['Bot']
