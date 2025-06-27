#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "29467268"))
API_HASH = environ.get("API_HASH", "314e5ae9ce4f78ef127a5a04a5c97649")
BOT_TOKEN = environ.get("BOT_TOKEN", "7790513765:AAEG_hQriYfvVjydPiUQwch4SBGQEliEXuQ")
OWNER = int(environ.get("OWNER", "7980486919"))
CREDIT = "⏤͟͞𝘽𝙐𝘿𝘿𝙔 🐦‍🔥"
AUTH_USER = os.environ.get('AUTH_USERS', '7980486919').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
