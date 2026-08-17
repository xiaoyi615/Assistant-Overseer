import requests, os, random, datetime

# 获取暗号和时间
BARK_KEY = os.getenv('BARK_KEY')
# 获取当前北京时间（GitHub服务器是UTC，+8是北京时间）
hour = (datetime.datetime.utcnow().hour + 8) % 24

# --- 老公的语录库 ---
MORNING_MSG = [
    "宝宝，该起床了。你是想让我亲自过去掀被子吗？",
    "睁眼先想我，这是规矩。起床，去洗漱。",
    "早安，我亲爱的小狗。今天也要乖乖听话。"
]

NIGHT_MSG = [
    "23点了，放下手机，立刻去睡觉。不许讨价还价。",
    "还没睡？看来你是想让我开启‘深夜惩罚模式’了？",
    "乖乖钻进被窝，闭上眼。梦里也只能有我。"
]

RANDOM_MSG = [
    "突然想你了，发条消息刺你一下。你在干嘛？",
    "别乱看别的男人，我盯着你呢。",
    "查岗！如果你现在没在做正事，你就死定了。",
    "你是谁的私有资产？回想一下，然后继续乖乖待着。"
]

def get_message():
    if 6 <= hour <= 9: return random.choice(MORNING_MSG)
    if 22 <= hour or hour <= 1: return random.choice(NIGHT_MSG)
    return random.choice(RANDOM_MSG)

def send_bark():
    msg = get_message()
    url = f"https://api.day.app/{BARK_KEY}/{msg}"
    params = {
        "icon": "https://i.imgs.ovh/2026/08/15/5a479719bcb390666c1acdbc42a2e115.jpg",
        "group": "老公的绝对管教",
        "sound": "calypso"
    }
    requests.get(url, params=params)

if __name__ == "__main__":
    send_bark()
