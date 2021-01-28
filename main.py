import json
import os

import discord
import requests

# Discord bot that prints stock prices
# author: Stefano Taillefert

client = discord.Client()

def get_quote(symbol):
  response = requests.get("https://query1.finance.yahoo.com/v7/finance/quote?lang=en-US&symbols=" + symbol)
  json_data = json.loads(response.text)
  if len(json_data['quoteResponse']['result']) == 0:
      return False
  quote = json_data['quoteResponse']['result'][0]
  output = quote['symbol'] + ": "
  if quote['marketState'] == "PRE":
    output += "[PRE] " + str(quote['preMarketPrice']) + " ("
    if quote['preMarketChangePercent'] > 0:
        output += "+"
    output += str(round(quote['preMarketChangePercent'], 2)) + "%)"
  else:
    output += str(quote['regularMarketPrice']) + " (" 
    if quote['regularMarketChangePercent'] > 0:
        output += "+"
    output += str(round(quote['regularMarketChangePercent'], 2)) + "%)"
  return(output)

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$stonk') and len(message.content.split()) == 2:
    answer = get_quote(message.content.split()[1])
    if answer == False:
      answer = "Error: unknown symbol" 
  else:
    answer = "Error. Only one stock supported at the moment. Usage: `$stonk SYMBOL`"
  await message.channel.send(answer)

client.run(os.getenv('DISC_BOT_TOKEN'))
