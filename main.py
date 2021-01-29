import json
import os

import discord
import requests

# Discord bot that prints stock prices
# author: Stefano Taillefert

# The text channel you want the bot to post in
channel_protection = True
bot_channel = "bot-spam"

# The command to trigger the bot (one word only)
command = "$stonk"

client = discord.Client()

def get_quote(symbol):
  response = requests.get("https://query1.finance.yahoo.com/v7/finance/quote?lang=en-US&symbols=" + symbol)
  json_data = json.loads(response.text)

  if len(json_data['quoteResponse']['result']) == 0:
    # Symbol not found
    return False

  quote = json_data['quoteResponse']['result'][0]
  output = quote['symbol'] + ": "

  if quote['marketState'] == "PRE":
    output += "[PRE] " + str(quote['preMarketPrice']) + " ("
    if quote['preMarketChangePercent'] > 0:
        output += "+"
    output += str(round(quote['preMarketChangePercent'], 2)) + "%)"
  elif quote['marketState'] == "POST":
    output += "[POST] " + str(quote['postMarketPrice']) + " ("
    if quote['postMarketChangePercent'] > 0:
        output += "+"
    output += str(round(quote['postMarketChangePercent'], 2)) + "%)"
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
  # Prevent messages from the bot itself
  if message.author == client.user:
    return

  # If channel protection is enabled, check if right channel
  if channel_protection and str(message.channel) != str(bot_channel):
    return

  # Listen only for correct commands
  if not message.content.startswith(command):
    return
  
  # Check that we get only one symbol
  if len(message.content.split()) != 2:
    answer = "Error. Only one stock supported at the moment. Usage: `$stonk SYMBOL`"
  else:
    answer = get_quote(message.content.split()[1])

    # Check that the symbol is actually valid
    if answer == False:
      answer = "Error: unknown symbol"

  await message.channel.send(answer)

client.run(os.getenv('DISC_BOT_TOKEN'))
