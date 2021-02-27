# StonksBot

### A bot that LIKES THE STOCK 🚀🚀

To install the requirements, run `pip install --no-cache-dir -r requirements.txt`.

Check the options at the beginning of `main.py` for some config like custom command or dedicated channel.

To run it, simply yeet the bot token in a system environment variable named `DISC_BOT_TOKEN` and then run `python main.py`. Easy.


## Usage

`$stonk [ticker]`

That's it. Literally.


## Docker? Docker!

Create a .env with the bot token as `DISC_BOT_TOKEN`, then build and run the image:

`docker build . -t stonksbot`

`docker run --name stonksbot --env-file .env stonksbot`
