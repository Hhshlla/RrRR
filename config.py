from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "20752294")) #لا تغير هاذة القيمة
API_HASH = getenv("API_HASH", "ebb4f01abedd3287192bf3acbd6161c0")#لا تغير هاذة القيمة
BOT_TOKEN = getenv("BOT_TOKEN", "7761062755:AAEjHNgR6YxXpjPN0de_O8TRg3dtaCjyVc0")
SESSION_NAME = getenv("SESSION_NAME", "AgG3g3kARqGgPKCOKYsP_r1Z50PHCiNM8iqADHg8xJrNwpVT8a4ce6rPUmTUWtJ6Xa6Bp4XnGWjbqC0XJt_ddg6l1H0nk-ZoDwjtciIjX54IPVsMbG-SD4Y_jOVQUiOWcZjBcjRNAf3UijmRISYDxXVQM1q74LPAHwiEGdwBunoDiGqJC7VU_iNC7ciK4hafZbJApNv7CQtwoTTz2El032gU_H_NU1loeCUxXoH3UQW5oKx9mEBQy9Gbtzf7_hguXyhXS5MxlEXeby6ePk56dbog3iaUdA_-8wp0Kb65HiAi3dX2OMruRiBZWHR6ILM6-RZpJ1Yz1eewkkKm7c5a0yWysLlGdwAAAAF3k0FNAA")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "qd_dh") # @ هنا ضع يوزر حسابك بدون 
ALIVE_NAME = getenv("ALIVE_NAME", "𝗦𝗮𝗘𝗳𝗢𝗿 🇮🇶.") # هنا ضع اسم حسابك
BOT_USERNAME = getenv("BOT_USERNAME", "Seroohbot") # @ هنا ضع يوزر البوت بدون 
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/X02lx/RrRRR") 
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main") #لا تغير هاذة القيمة
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60")) #لا تغير هاذة القيمة
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "vv5qvv") # @ هنا ضغ يوزر كروبك بدون 
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "xii66qe") # @ هنا ضغ يوزر قناتك بدون

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "6301106509").split()))
                                             #هنا ضع ايدي المطور فوق و الاعلئ
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
