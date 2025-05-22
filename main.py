__version__ = "1.0"

import asyncio
import os
from pathlib import Path
from typing import Any

import discord
import dotenv
from disckit import CogEnum, UtilConfig
from disckit.cogs import dis_load_extension

from core import Bot

bot_intents = discord.Intents.default()
bot_env = dotenv.dotenv_values()
BOT_TOKEN = bot_env["BOT_TOKEN"]


async def load_extensions(bot: Bot) -> None:
    for folder in os.listdir("cogs/"):
        cog_folder = Path("cogs/", folder)
        for file in os.listdir(cog_folder):
            if file.endswith(".py"):
                cog_dir = cog_folder / file
                await bot.load_extension(".".join(cog_dir.parts)[:-3])
                print(f"Loading Extension: {cog_dir.name}")


async def custom_status(bot: Bot, *args: Any) -> tuple[str, ...]:
    # Note: The global bot instance will always be passed onto the function
    # as it's first argument when being called, so you will have to add the
    # bot as the first parameter in the function for it to work as intended.

    version: str = args[0]

    return (
        # Prefixed by "Listening to " by the discord activity type.
        f"version {version}!",
        "humans.",
        "Slash commands!",
    )


async def main() -> None:
    bot = Bot(
        intents=bot_intents,
        status=discord.Status.idle,
    )

    UtilConfig.BUG_REPORT_CHANNEL = 1316547285856817244
    UtilConfig.STATUS_FUNC = (
        custom_status,
        (__version__,),
    )  # Don't forget to pass in the arguments you want to supply in the second element of the tuple.
    UtilConfig.STATUS_COOLDOWN = 600
    UtilConfig.LEMMA_TRANS_COMMANDS = {
        discord.Locale.hindi: "translations/commands/hindi/hi-games.json"
    }

    await load_extensions(bot=bot)
    await dis_load_extension(bot, CogEnum.ERROR_HANDLER, CogEnum.STATUS_HANDLER)

    await bot.start(token=BOT_TOKEN)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exited with KeyboardInterrupt")
