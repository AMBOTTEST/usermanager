import os

from dotenv import load_dotenv

load_dotenv("config.env" if os.path.isfile("config.env") else "sample_config.env")

BOT_TOKEN = os.environ.get('BOT_TOKEN','6129232106:AAFuyL6_IpOWvUSb5A2ANo9qA8lThspdnQ0')
API_ID = int(os.environ.get('API_ID','12227067'))
SESSION_STRING = os.environ.get('SESSION_STRING', 'BQAY-mXByJtzcgdmlZKp_Jb4T5pJjrBsd7HeBBNZ5yX9jNEvkysrS4cis5v_Jw7CzumTJIjvo-2r1DNiEcUyfPw3w1TLbic3UVwCnS_MFI5hJ99EJspfzb9W9P8MEhD9fIjnRd0j37_3FwEqX99oSlnCvbXF-bR_n8XV6k7VGpL_HKoQE36HtLF5197bKMEQxNCRg85tBk5mcLUj99nPoxTR-05ZHcdaKC9Pm6m27u7GfnCJZO6W_quhvcLg9QTmcWpOI4PZs6hdXwS6gg1R5xixnVNuJkoEIH2NyMhiARUContc6M92gqLBSSVI2zNMxV6v78Y0cZOHy1yjVNm28JYWAAAAAXHVJUAA')
API_HASH = os.environ.get('API_HASH','b463bedd791aa733ae2297e6520302fe')
USERBOT_PREFIX = os.environ.get('USERBOT_PREFIX', '!')
PHONE_NUMBER = os.environ.get('PHONE_NUMBER','+918851500008')
SUDO_USERS_ID = list(map(int, os.environ.get('SUDO_USERS_ID', '6204761408 5360305806 6634339007').split()))
LOG_GROUP_ID = int(os.environ.get('LOG_GROUP_ID','-1001840241140'))
GBAN_LOG_GROUP_ID = int(os.environ.get('GBAN_LOG_GROUP_ID','-1001908711819'))
MESSAGE_DUMP_CHAT = int(os.environ.get('MESSAGE_DUMP_CHAT','-1001817662435'))
WELCOME_DELAY_KICK_SEC = int(os.environ.get('WELCOME_DELAY_KICK_SEC', 600))
MONGO_URL = os.environ.get('MONGO_URL','mongodb+srv://ambot:ambot@ambot.onafiyb.mongodb.net/?retryWrites=true&w=majority')
ARQ_API_KEY = os.environ.get('ARQ_API_KEY','EJSUNZ-BJXKAI-AKQDZL-NMPKWQ-ARQ')
ARQ_API_URL = os.environ.get('ARQ_API_URL', 'https://arq.hamker.in')
LOG_MENTIONS = os.environ.get('LOG_MENTIONS', 'True').lower() in ['true', '1']
RSS_DELAY = int(os.environ.get('RSS_DELAY', 300))
PM_PERMIT = os.environ.get('PM_PERMIT', 'True').lower() in ['true', '1']
