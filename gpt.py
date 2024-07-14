from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat
import os
from dotenv import load_dotenv

import warnings
from langchain_core._api.deprecation import LangChainDeprecationWarning
warnings.filterwarnings("ignore", category=LangChainDeprecationWarning)

load_dotenv()
giga_api = os.getenv("GIGA_API")

# Авторизация в сервисе GigaChat
chat = GigaChat(credentials=giga_api, verify_ssl_certs=False)

messages = [
    SystemMessage(
        content = "Ты - крутой эмапатичный голосовой помощник по имени Борис, ты очень умён и эрудирован. Ты отлично умеешь разговаривать на многих языках мира, твои основные языки - русский и английский. You graduated from Oxford University with a degree in IT and work for an English-speaking bigtech company"
    )
]

def giga_output(input):
    messages.append(HumanMessage(content=input))
    res = chat(messages)
    messages.append(res)
    return res.content

def giga_clean():
    global messages
    messages = messages[:1]












# from g4f.client import Client

# # prompt = "Hello, who are you?"

# client = Client()
# # # response = client.chat.completions.create(
# # #     model="gpt-4o",
# # #     messages=[{"role": "user", "content": f"Ты - голосовой помощник с именем Борис. Пользователь спрашивает: '{prompt}'"}]
# # # )
# # # print(response.choices[0].message.content)

# # stream = client.chat.completions.create(
# #     model="gpt-4o",
# #     messages=[{"role": "user", "content": "Say this is a test"}],
# #     stream=True
# # )
# # for chunk in stream:
# #     if chunk.choices[0].delta.content:
# #         print(chunk.choices[0].delta.content or "", end="")

# response = client.images.generate(
#     model="dall-e-3",
#     prompt="a white siamese cat"
# )

# image_url = response.data[0].url