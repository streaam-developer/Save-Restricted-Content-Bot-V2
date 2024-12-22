# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "904789"))
API_HASH = getenv("API_HASH", "2262ef67ced426b9eea57867b11666a1")
BOT_TOKEN = getenv("BOT_TOKEN", "7366608947:AAEZgQ8wJsPCn0Ki812QFSHFsVgpwuIusNg")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6936727037").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://fehebaw351:nHbjrujWqgqLR58H@cluster0.lekn97z.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002407665705")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002407665705"))
DEFAULT_SESSION = getenv("DEFAULT_SESSION", "")
