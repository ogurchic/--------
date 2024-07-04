import speech_recognition as sr
import os
import AppOpener as ap

# -*- coding: utf-8 -*-

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
        ('Close', 'close', 'акрой', 'ыключи', 'акрыть', 'ыключить'):close_program
    }

    for cmd_tuple, function in commands.items():
        for cmd in cmd_tuple:
            if cmd in command:
                
                try:

                    if cmd in ['создать папку', 'сделай папку', 'Создай папку', 'Создать папку', 'Сделай папку', 'создай папку', 
                            'удали папку', 'удалить папку', 'сотри папку','Удали папку', 'Удалить папку', 'Сотри папку']:
                        # предполагается, что имя папки следует после команды
                        folder_name = command.split(cmd)[-1].strip()
                        function(folder_name)
                        return f'Команда "{cmd}" "{folder_name}"выполнена'
                    
                    if cmd in ["Открой", "открой", "запусти", "Запусти", "Run", "run"]:
                        program_name = command.split(cmd)[-1].strip()
                        open_program(program_name)
                        return f'Программа "{program_name}"открыта'

                    if cmd in  ['Close', 'close', 'акрой', 'ыключи', 'акрыть', 'ыключить']:
                        program_name  = command.split(cmd)[-1].strip()
                        close_program(program_name)
                        return f'Программа "{program_name}"открыта'

                    else:
                        result = function()
                        return f'Результат команды "{cmd}": {result}'
                    
                except Exception as e:
                    return f'Произошла ошибка при выполнении команды "{cmd}": {str(e)}, попробуйте задать запрос по-друггому'
                
    return 'Извините, я не понял вашу команду.'
 
r = sr.Recognizer()
mic = sr.Microphone()

sr.LANGUAGE ='ru-RU'

stop_words = ['stop', 'стоп', 'хватит', 'прекрати', 'кончай', 'спасибо', 'всё, спасибо', 'хватит, спасибо',  'остановись', 'а зелёный Оптимус Прайм огурец', 'иди нахуй', 'пошёл нахуй', 'пошёл в пизду']

while True:
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("Скажите что-нибудь...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language='ru-RU')
    except sr.UnknownValueError:
        break
    except sr.RequestError as e:
        print("Не удалось запросить результаты у службы Google Speech Recognition; {0}".format(e))
        break
    else:
        print(text)
        if text.lower() in stop_words:
            break
        else:
            response = execute_command(text)