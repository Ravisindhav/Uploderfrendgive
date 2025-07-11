# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "27660379"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "19c71c27733f0954371085198855125a")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8138308196:AAFssD4sb6v84eiVCzXl3WFLl05rSTUPlDc")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("uploderfrendgive_bot")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "5459854363"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5459854363").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002761572365"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://sindhavravi11:%24Sind1234567890@cluster0.bwlgbx3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-1002761572365"))

