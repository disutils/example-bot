from discord.ext import commands


class Bot(commands.Bot):
    def __init__(self, **kwargs) -> None:
        super().__init__(command_prefix=None, **kwargs)

    async def on_ready(self) -> None:
        print("Example Bot Online!")

        # Uncomment these when you run the bot for the first time.
        # Use the `/sync` command onwards and commend this back.
        cmds = await self.tree.sync()
        print(f"Synced {len(cmds)} commands.")
