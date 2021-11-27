import os

from discord import Intents
from discord.ext import commands

import settings


class ModswireBot(commands.Bot):
    def __init__(self) -> None:
        self.DEBUG = settings.DEBUG
        self.version = settings.VERSION

        intents = Intents(guilds=True, messages=True, reactions=True, bans=True)
        if not self.DEBUG:          # we don't have members intent on debug bot
            intents.members = True  # so we enable it on prod bot only

        super().__init__(command_prefix='!', intents=intents, slash_commands=settings.IS_SLASH)
        self.load_cogs('cogs')
    
    def load_cogs(self, path: str) -> None:
        for cog in settings.PRELOAD:
            self.load_extension(cog)
        for fn in os.listdir(path):
            if not fn.endswith('.py') or fn.startswith('__'):
                continue
            self.load_extension(path+'.'+fn[:-3])
    