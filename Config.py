import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "28837889"))
    API_HASH = os.environ.get("API_HASH", "9d5e9c5b8abcf8b7b930abd259de254e")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6917745995:AAHMvlwLbjAVl-2gPf_cdkQ2JFeB6Do7jrM" )
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOGgBuxTKmwBKSa9SIBo5ALJD3I5cE4OCMVgjJN08AILsOOiER_CysirCtnwgvgRnDqOQFeSfY321RyiXFryRAkmoDAJHc83JShowdMRoMakOu-wXMxFZwnjkp-o5KENBPrcOyBzbKJWUFxHple6cNkbjVgizgqcabw056aKsn8eFdRn_AwaCNOE0bMs05JRWRIrJaaJRE32FCxAHlMgTpwI5K5xUCFRuY0FjlR4S03vUXP2D1n6vhb-FoKd4rJ0MqeHQOoJy0h2LriH0Wz8s5u7YbDI_4Aa8urNmrY0Ef7iHeUgq5Ue2vaYTEJQDzkPzWssjqd7gCVQ-4pqmoJ92jkQVEpQ=" )
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "INFINITE_X_MUSIC_BOT")
    SUPPORT = os.environ.get("SUPPORT", "GAURAV_BOTS") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "GAURAV_BOTS") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/6de19b47dd55da5414352.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "6510541968")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
