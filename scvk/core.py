from vkbottle import Bot, load_blueprints_from_package
import psycopg2 as ps
from config import DB_URI, token
import time

def bot_run(folder):
	print("SybroCore | VK Version | Version 0.1.0a")
	time.sleep(2)
	print("SybroCore | Thanks for using this core! (This core using vkbottle library)")
	time.sleep(2)
	bot = Bot(token)	

	for cog in load_blueprints_from_package("cogs"):
	    cog.load(bot)

	bot.run_forever()