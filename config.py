import os
from dotenv import load_dotenv
import sys

class BotConfig:
    def __init__(self, envpath) -> None:
        self.envpath = envpath
        self.SetDotEnv()
        self.GetBotEnv()

    def SetDotEnv(self):
        try:
            load_dotenv(dotenv_path=self.envpath)
        except Exception as ex: 
            print(ex)
            sys.exit(1)

    def GetBotEnv(self):
        self.token = os.getenv("BOT_TOKEN", "default bot token")
        self.admin_tg_id = os.getenv("ADMIN_TG_ID", "322323")
        self.telegram_group_id = int(os.getenv("GROUP_ID", "4323424"))
        self.sleep_time = os.getenv('SLEEP_TIME', 600) # This part is given in minutes. 600 min = 10 hour
