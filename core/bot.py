from discord.ext import commands

# from disckit.utils.translator import LemmaTranslator
from typing import Any


class Bot(commands.Bot):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(command_prefix=None, **kwargs)

    async def setup_hook(self) -> None:
        ...
        # await self.tree.set_translator(LemmaTranslator(self))
        # await LemmaTranslator.setup(self, self.tree)

    async def on_ready(self) -> None:
        print(f"\n{self.user.name} is Online!\n")

        # Uncomment these when you run the bot for the first time.
        # Use the `/sync` command onwards and comment this back.

        # cmds = await self.tree.sync()
        # print(f"Synced {len(cmds)} commands.")
