from telethon import TelegramClient, errors
from dotenv import load_dotenv
import time
import os

# API details
load_dotenv()
api_id = os.getenv("29085825")
api_hash = os.getenv("a164d6ce4e6fc8b3bfc4fed1140ffbef")
api_name = os.getenv("LegendHunters")
# Account connection
client = TelegramClient(api_name, api_id, api_hash)


async def main():
    me = await client.get_me()
    # Read message from file and send to a list of scraped groups
    with open("message.txt", "r", encoding="utf-8") as m:
        message = m.read()

    with open("groups.txt", "r") as groups:
        for group in groups:
            try:
                formatted_group = int(group.strip("\n"))
                await client.send_message(formatted_group, message)
                print("Message sent successfully!")
                time.sleep(30)  # You can modify delay as you wish

            except:
                print("Unknown error occured while sending messages!")


with client:
    client.loop.run_until_complete(main())
