import os

from dotenv import load_dotenv

load_dotenv("config.env" if os.path.isfile("config.env") else "sample_config.env")

BOT_TOKEN = os.environ.get('BOT_TOKEN','6129232106:AAFuyL6_IpOWvUSb5A2ANo9qA8lThspdnQ0')
API_ID = int(os.environ.get('API_ID','12227067'))
SESSION_STRING = os.environ.get('SESSION_STRING', 'BQBK_OJaKpW6e8YUtTEobxZ1DeJ8llQc4GP-xszJ8oykdhNNqh1QkaQbK35lgg5kAbke_u67TDSR_ANLMOHJ5f31fHoBIKRQTQ5h1YlW8tXme2LzxfvtjOEeEIsoGcYLsF8Uiz6GlCjUPs0hFJyRmrpq89uvAyYLGPb1A7bECdqHkuMEG87vGSO05-oQ2TIgPK3ZuRwfmoZS610FmqzxZsdn4HvDgxVGj7YuYyGtvhOzmOrdwxBrzMhjWGaGlZYNNmLu53Sr-eDgR_u5EGPVI0qCNuzSkrBwCjwCwDpRjjl9uhzsxERG6H-dMWPNyBI_eQw8eF_c-Ov6xqHUM1AX18VBAAAAAYtv-r8A')
API_HASH = os.environ.get('API_HASH','b463bedd791aa733ae2297e6520302fe')
USERBOT_PREFIX = os.environ.get('USERBOT_PREFIX', '.')
PHONE_NUMBER = os.environ.get('PHONE_NUMBER','+919906801528')
SUDO_USERS_ID = list(map(int, os.environ.get('SUDO_USERS_ID', '6204761408 5360305806 6634339007').split()))
LOG_GROUP_ID = int(os.environ.get('LOG_GROUP_ID','-1001817662435'))
GBAN_LOG_GROUP_ID = int(os.environ.get('GBAN_LOG_GROUP_ID','-1001817662435'))
MESSAGE_DUMP_CHAT = int(os.environ.get('MESSAGE_DUMP_CHAT','-1001817662435'))
WELCOME_DELAY_KICK_SEC = int(os.environ.get('WELCOME_DELAY_KICK_SEC', 600))
MONGO_URL = os.environ.get('MONGO_URL','mongodb+srv://AM:AM@am.9zeddhx.mongodb.net/?retryWrites=true&w=majority')
ARQ_API_KEY = os.environ.get('ARQ_API_KEY','EJSUNZ-BJXKAI-AKQDZL-NMPKWQ-ARQ')
ARQ_API_URL = os.environ.get('ARQ_API_URL', 'https://arq.hamker.in')
LOG_MENTIONS = os.environ.get('LOG_MENTIONS', 'True').lower() in ['true', '1']
RSS_DELAY = int(os.environ.get('RSS_DELAY', 300))
PM_PERMIT = os.environ.get('PM_PERMIT', 'True').lower() in ['true', '1']
