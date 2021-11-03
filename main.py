import json
import os

import discord
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option
import requests


# Discord bot that prints stock prices
# author: Stefano Taillefert

client = discord.Client(intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True)


def get_quote(symbol):
    response = requests.get(
        "https://stonks.soulsbros.ch/actions/api.php?symbols=" + symbol
    )
    json_data = json.loads(response.text)

    if len(json_data["quoteResponse"]["result"]) == 0:
        # Symbol not found
        return "Stock ticker `" + symbol + "` not found"

    quote = json_data["quoteResponse"]["result"][0]
    output = quote["symbol"] + ": "

    if quote["marketState"] == "PRE":
        output += "[PRE] " + str(quote["preMarketPrice"]) + " ("
        if quote["preMarketChangePercent"] > 0:
            output += "+"
        output += str(round(quote["preMarketChangePercent"], 2)) + "%)"
    elif quote["marketState"] == "POST":
        output += "[POST] " + str(quote["postMarketPrice"]) + " ("
        if quote["postMarketChangePercent"] > 0:
            output += "+"
        output += str(round(quote["postMarketChangePercent"], 2)) + "%)"
    else:
        output += str(quote["regularMarketPrice"]) + " ("
        if quote["regularMarketChangePercent"] > 0:
            output += "+"
        output += str(round(quote["regularMarketChangePercent"], 2)) + "%)"
    return output


@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))


@slash.slash(
    name="stock",
    description="Get the current price of a given stock",
    options=[
        create_option(
            name="ticker",
            description="Stock ticker (e.g. GME)",
            option_type=3,  # string
            required=True,
        )
    ],
)
async def stock(ctx, ticker: str):
    await ctx.send(f"{get_quote(ticker)}")


client.run(os.getenv("STONKSBOT_TOKEN"))
