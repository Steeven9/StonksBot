import os

import discord
import yfinance as yf
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option

# Discord bot that prints stock prices
# author: Stefano Taillefert

bot_token = os.getenv("STONKSBOT_TOKEN")
if bot_token == None:
    raise ValueError("Discord token not found!")

client = discord.Client(intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True)


def get_quote(tickers: str):
    stocks = yf.Tickers(tickers)
    result = []

    tickers_list = tickers.split()
    for ticker in tickers_list:
        stock = stocks.tickers[ticker.upper()].info
        result.append({"name": "Name", "value": stock["shortName"]})
        result.append({
            "name": "Current",
            "value": f"{stock['currentPrice']} {stock['currency']}",
            "inline": True
        })
        result.append({
            "name": "Daily low",
            "value": f"{stock['dayLow']} {stock['currency']}",
            "inline": True
        })
        result.append({
            "name": "Daily high",
            "value": f"{stock['dayHigh']} {stock['currency']}",
            "inline": True
        })

    return result


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name="/stock 🏳️‍🌈"))
    print("Logged in as {0.user}".format(client))


@slash.slash(
    name="stock",
    description="Get the current price of one or more given stocks",
    options=[
        create_option(
            name="tickers",
            description="One or more stock tickers (e.g. gme aapl)",
            option_type=3,  # string
            required=True,
        )
    ],
)
async def stock(ctx, tickers: str):
    data = get_quote(tickers)
    embed_data = {
        "title": "Stock prices",
        "footer": {
            "text": "github.com/Steeven9/Stonksbot"
        },
        "fields": data
    }
    embed = discord.Embed().from_dict(embed_data)
    await ctx.send(embed=embed)


client.run(bot_token)
