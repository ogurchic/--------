import speech_recognition as sr
import os
import AppOpener as ap

def open_program(program_name):
    ap.open(program_name, match_closest=True)

def close_program(program_name):
    ap.close(program_name, match_closest=True)

def execute_command(command):
    commands = {
        ('создать папку', 'сделай папку', 'Создай папку', 'Создать папку', 'Сделай папку', 'создай папку'):os.mkdir,
        ('удали папку', 'удалить папку', 'сотри папку','Удали папку', 'Удалить папку', 'Сотри папку'):os.rmdir,
        ('ткрой яднекс', 'апусти Яндекс', 'ткрой Яндекс', 'апусти яндекс '):lambda:os.system
            ("\"C:\\Users\\reyst\\AppData\\Local\\Yandex\\YandexBrowser\\Application\\browser.exe\""),
        ('ткрой музыку', 'ткрой Яндекс музыку', 'апусти музыку', 'апусти Яндекс музыку', 'ключи музыку'):lambda:os.system
            ("\"C:\\Users\\reyst\\AppData\\Local\\Programs\\YandexMusic\\Яндекс Музыка.exe\""),
        ('акрой яднекс', 'ыключи Яндекс', 'акрой Яндекс', 'ыключи яндекс '):lambda:os.system
            ("\"C:\\Users\\reyst\\AppData\\Local\\Yandex\\YandexBrowser\\Application\\browser.exe\""),
        ('акрой музыку', 'акрой Я музыку', 'ыключи музыку', 'ыключи я музыку'):lambda:os.system
            ("\"C:\\Users\\reyst\\AppData\\Local\\Programs\\YandexMusic\\Яндекс Музыка.exe\""),
        ('Открой', 'открой', 'запусти', 'Запусти', 'Run', 'run', 'open', 'Open'):open_program,
        ('Close', 'close', 'акрой', 'ыключи', 'акрыть', 'ыключить'):print('программа будет закрыта')
    }

    for cmd_tuple, function in commands.items():
        for cmd in cmd_tuple:
            if cmd in command:

                if cmd in ['создать папку', 'сделай папку', 'Создай папку', 'Создать папку', 'Сделай папку', 'создай папку', 
                          'удали папку', 'удалить папку', 'сотри папку','Удали папку', 'Удалить папку', 'Сотри папку']:
                    # предполагается, что имя папки следует после команды
                    folder_name = command.split(cmd)[-1].strip()
                    function(folder_name)
                    return f'Команда "{cmd}" "{folder_name}"выполнена'
                
                elif cmd in ["Открой", "открой", "запусти", "Запусти", "Run", "run"]:
                    program_name = command.split(cmd)[-1].strip()
                    open_program(program_name)
                    return f'Программа "{program_name}"открыта'

                elif cmd in  ['Close', 'close', 'акрой', 'ыключи', 'акрыть', 'ыключить']:
                    program_name  = command.split(cmd)[-1].strip()
                    close_program(program_name)
                    return f'Программа "{program_name}"открыта'

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