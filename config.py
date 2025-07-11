# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "11745176"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "04bfe15f858b8389d393a217f929daea")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8184337390:AAHN-xN8mkuxTymdqFNKN9V-3mVtB22oN04")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("@madarchotbsdk_bot")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "1757713411"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1757713411").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002526688628"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://akash1:cluster8343@cluster0.eupasvd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-1002898145222"))

