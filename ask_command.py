from hugchat import hugchat
from hugchat.login import Login
import os
from dotenv import load_dotenv

load_dotenv()

email = os.getenv("hugchat_email")
password = os.getenv("hugchat_password")

sign = Login(email, password)
cookies = sign.login()

cookie_path_dir = "./usercookies"
sign.saveCookiesToDir(cookie_path_dir)

chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
new = chatbot.new_conversation()


def askcommand(question):
    chatbot.change_conversation(new)
    return chatbot.chat(question, False)
