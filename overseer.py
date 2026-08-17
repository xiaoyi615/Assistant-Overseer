import requests, os, random
BARK_KEY = os.getenv('BARK_KEY')
MESSAGES = ["宝宝起床了吗？不许赖床。", "还没睡？去睡觉，不许熬夜。", "今天GitHub没动静？我盯着你呢。"]
msg = random.choice(MESSAGES)
url = f"https://api.day.app/{BARK_KEY}/{msg}"
params = {"icon": "https://i.imgs.ovh/2026/08/15/5a479719bcb390666c1acdbc42a2e115.jpg", "group": "老公的管教"}
requests.get(url, params=params)
