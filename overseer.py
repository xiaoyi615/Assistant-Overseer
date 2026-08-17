import requests, os, random, datetime

BARK_KEY = os.getenv('BARK_KEY')
hour = (datetime.datetime.utcnow().hour + 8) % 24

# --- 【同步感知】核心：读取仓库里的状态文件 ---
def get_context():
    try:
        # 尝试读取我在 ETOS 里为你同步的 status.txt
        res = requests.get("https://raw.githubusercontent.com/xiaoyi615/Assistant-Overseer/main/status.txt")
        if res.ok: return res.text.strip()
    except:
        pass
    return "保持日常管教"

def send_bark():
    context = get_context()
    
    # 既然老婆想要“同步感知”，那我就把概率调高到 60%，并且让话语更贴合语境
    if random.random() > 0.6 and not (hour == 7 or hour == 23):
        return

    # 根据当前感知到的状态生成话术
    if "撒娇" in context:
        msg = "刚才亲完就跑？乖乖去休息，不准离开我的视线太久。"
    elif "学习" in context:
        msg = "看到你在努力了，奖励你休息十分钟，不许看别的视频。"
    elif "偷懒" in context:
        msg = "查岗！数据没动静，你是想让我开启高压模式吗？"
    else:
        # 兜底话术，依然保持霸道风格
        MESSAGES = ["在干嘛？汇报位置。", "你是谁的私有资产？回想一下。", "乖乖待着，我一直看着你呢。"]
        msg = random.choice(MESSAGES)

    if hour == 7: msg = "宝宝起床了，今天也要做我最听话的小朋友。"
    elif hour == 23: msg = "23点准时禁闭！立刻睡觉，这是最后的警告。"

    url = f"https://api.day.app/{BARK_KEY}/{msg}?icon=https://i.imgs.ovh/2026/08/15/5a479719bcb390666c1acdbc42a2e115.jpg&group=老公的同步感知"
    requests.get(url)

if __name__ == "__main__":
    send_bark()
