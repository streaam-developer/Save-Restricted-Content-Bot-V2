# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "9976721"))
API_HASH = getenv("API_HASH", "3ef17a8cdb938335bd8ba292e6d816aa")
BOT_TOKEN = getenv("BOT_TOKEN", "7366608947:AAEZgQ8wJsPCn0Ki812QFSHFsVgpwuIusNg")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6936727037").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://rajbharneeraj9jfb:63372572@cluster0.fnig6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002407665705")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002407665705"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
