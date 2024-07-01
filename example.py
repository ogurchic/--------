import speech_recognition as sr
import os


def execute_command(command):
    commands = {
        ('создать папку', 'сделай папку', 'Создай папку', 'Создать папку', 'Сделай папку', 'создай папку'):os.mkdir,
        ('удали папку', 'удалить папку', 'сотри папку','Удали папку', 'Удалить папку', 'Сотри папку'):os.rmdir,
        ('ткрой хром', 'ткрой Chrome', 'апусти хром', 'апусти Chrome'):lambda:os.system("\"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe\""),
        ('ткрой яднекс', 'апусти Яндекс', 'ткрой Яндекс', 'апусти яндекс '):lambda:os.system("\"C:\\Users\\reyst\\AppData\\Local\\Yandex\\YandexBrowser\\Application\\browser.exe\"")
    }

    for cmd_tuple, function in commands.items():
        for cmd in cmd_tuple:
            if cmd in command:
                if cmd in ['создать папку', 'сделай папку', 'Создай папку', 'Создать папку', 'Сделай папку', 'создай папку', 
                          'удали папку', 'удалить папку', 'сотри папку','Удали папку', 'Удалить папку', 'Сотри папку']:
                    # предполагается, что имя папки следует после команды
                    folder_name = command.split(cmd)[-1].strip()
                    function(folder_name)  # передаем folder_name в качестве аргумента
                    return f'Команда "{cmd}" "{folder_name}"выполнена'
                else:
                    result = function()
                    return f'Результат команды "{cmd}": {result}'

    return 'Извините, я не понял вашу команду.'
 

r = sr.Recognizer()
mic = sr.Microphone()

sr.LANGUAGE ='ru-RU'

with mic as source:
    r.adjust_for_ambient_noise(source)
    print("Скажите что-нибудь...")
    audio = r.listen(source)

text = r.recognize_google(audio, language='ru-RU')
print(text)
response = execute_command(text)
print(response)