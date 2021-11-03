# StonksBot

### A bot that LIKES THE STOCK 🚀🚀

To install the requirements, run `pip install --no-cache-dir -r requirements.txt`.

Check the options at the beginning of `main.py` for some options like custom command or dedicated channel.

To run it, simply yeet the bot token in a system environment variable named `STONKSBOT_TOKEN` and then run `python main.py`. Easy.


## Usage

`/stonk [ticker]`

That's it. Literally.


## Docker? Docker!

Create a `.env` file with the bot token as `STONKSBOT_TOKEN`, then build or pull the image and run it:

`docker build . -t stonksbot` or `docker pull steeven9/stonksbot`

`docker run --name stonksbot --env-file .env stonksbot`
