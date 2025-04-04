import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "PopmieMusicBot")
BOT_TOKEN = getenv("BOT_TOKEN", "7518391748:AAEpYu3JjrHbPewdWEj8lpQiOpyNTHSdQ60")
BOT_NAME = getenv("BOT_NAME", "popmiemusic")
BG_IMAGE = getenv("BG_IMAGE", "https://deposit.pictures/p/eb8812b8698440da9f7b7a1db9cac808")
THUMB_IMG = getenv("THUMB_IMG", "https://deposit.pictures/p/eb8812b8698440da9f7b7a1db9cac808")
AUD_IMG = getenv("AUD_IMG", "https://deposit.pictures/p/eb8812b8698440da9f7b7a1db9cac808")
QUE_IMG = getenv("QUE_IMG", "https://deposit.pictures/p/eb8812b8698440da9f7b7a1db9cac808")
API_ID = int(getenv("API_ID", "13175074"))
API_HASH = getenv("API_HASH", "a05b737f45a5640da5a6c516b737657e")
BOT_USERNAME = getenv("BOT_USERNAME", "PopmieMusicBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "PopmieAssistant_bot")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "zto_idd")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "PopmieMusic")
OWNER_NAME = getenv("OWNER_NAME", "rielorang") # isi dengan username kamu tanpa simbol @
PMPERMIT = getenv("PMPERMIT", None)
OWNER_ID = int(os.environ.get("OWNER_ID", "5619150709")) # fill with your id as the owner of the bot
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://pakeya2:userbot@cluster0.vva0b.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # fill with your mongodb url
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002676671114")) # make a private channel and get the channel id
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False)) # just fill with True or False (optional)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "500"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1331884444").split()))
LANG = getenv("LANG", "id")
