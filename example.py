#example.py
# -*- coding: utf-8 -*-
#not for sales

import speech_recognition as sr
import os
import AppOpener as ap
from gpt import giga_output, giga_clean
from weather import weather_output
import webbrowser
import pyttsx3
import text_to_voice as v
import news
import notes
import datetime
import win32api
import time
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def set_volume(volume):
    if volume < 1 or volume > 100:
        print("выберете значение между 1 и 100")
        return

    # Получаем все активные аудиоустройства
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume_control = cast(interface, POINTER(IAudioEndpointVolume))

    # Устанавливаем громкость
    volume_control.SetMasterVolumeLevelScalar(volume / 100, None)

def play_pause():
    VK_MEDIA_PLAY_PAUSE = 0xB3
    hwcode = win32api.MapVirtualKey(VK_MEDIA_PLAY_PAUSE, 0)
    win32api.keybd_event(VK_MEDIA_PLAY_PAUSE, hwcode)

def next_media():
    VK_MEDIA_NEXT_TRACK = 0xB0
    hwcode = win32api.MapVirtualKey(VK_MEDIA_NEXT_TRACK, 0)
    win32api.keybd_event(VK_MEDIA_NEXT_TRACK, hwcode)

def prev_media():
    VK_MEDIA_PREV_TRACK = 0xB1
    hwcode = win32api.MapVirtualKey(VK_MEDIA_PREV_TRACK, 0)
    win32api.keybd_event(VK_MEDIA_PREV_TRACK, hwcode)
    time.sleep(1)
    win32api.keybd_event(VK_MEDIA_PREV_TRACK, hwcode)

def whats_time():
    # Получаем текущее время
    current_time = datetime.datetime.now()
    # Выводим текущее время
    return f"Текущее время: {current_time.strftime("%H:%M:%S")}"

# Функция для озвучивания текста
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def open_program(program_name):
    ap.open(program_name, match_closest=True)

def close_program(program_name):
    ap.close(program_name, match_closest=True)

def web_search(search_phrase):
    url = "https://yandex.ru/search/?text=" + search_phrase
    return webbrowser.open_new_tab(url)

def youtube_search(search_phrase):
    url = "https://www.youtube.com/results?search_query=" + search_phrase
    return webbrowser.open_new_tab(url)


def execute_command(command):
    commands = {
        ('создать папку', 'сделай папку', 'создай папку'):os.mkdir,
        ('удали папку', 'удалить папку', 'сотри папку'):os.rmdir,
        ('открой музыку', 'запусти музыку', 'включи музыку', 'открой я музык'):lambda:os.system
            ("\"C:\\Users\\reyst\\AppData\\Local\\Programs\\YandexMusic\\Яндекс Музыка.exe\""),
        ('закрой музыку', 'закрой я музык', 'выключи музыку', 'выключи я музыку'):lambda:os.system
            ("\"C:\\Users\\reyst\\AppData\\Local\\Programs\\YandexMusic\\Яндекс Музыка.exe\""),
        ('открой программу', 'запусти', 'run', 'open'):open_program,
        ('close', 'закрой', 'выключи', 'закрыть', 'выключить'):close_program,
        ('найди в браузере', 'найди в интернете', 'поиск в интернете'):web_search,
        ('weather', 'погода', 'погоду', 'погоде'):lambda:weather_output(),
        ('открой в youtube', 'найди в youtube', 'найди на youtube'):youtube_search,
        ('прочитай новости', 'что по новостям'):lambda:news.read_news(),
        ('открой новости', 'покажи новости'):news.open_news,
        ('прочитай заметки', 'прочитать заметки', "покажи заметки", "открой заметки"):lambda:notes.read_notes(),
        ('добавить заметку', 'напиши новую заметку', "добавь замектку", "добавь новую заметку"):notes.add_note,
        ('удалить заметку', 'удали заметку', "сотри заметку", "стереть заметку"):notes,
        ('который час', 'сколько время', 'подскажи время'):lambda:whats_time(),
        ('play', 'pause', 'плей', 'пауза', "поставь на паузу", "продолжай играть"):lambda:play_pause(),
        ('next', 'следующий трек', 'переключи музыку', 'давай дальше'):lambda:next_media(),
        ('prev', 'предыдущий трек'):lambda:prev_media(),
        ('установи громкость на ', 'поставь громкость', 'громкость на ', 'установи уровень громкости на '):set_volume
    }

    command = command.lower()

    for cmd_tuple, function in commands.items(): # проходимся по словарю с командами
        for cmd in cmd_tuple:
            if cmd in command:
                
                try: # обработчик исключений

                    if cmd in ['создать папку', 'сделай папку', 'создай папку', 
                            'удали папку', 'удалить папку', 'сотри папку']:
                        # предполагается, что имя папки следует после команды
                        folder_name = command.split(cmd)[-1].strip()
                        function(folder_name)
                        return f'Команда "{cmd}" "{folder_name}"выполнена'
                    
                    if cmd in ['открой', 'запусти', 'run', 'open']:
                        program_name = command.split(cmd)[-1].strip()
                        open_program(program_name)
                        return f'Программа "{program_name}" открыта'

                    if cmd in  ['close', 'закрой', 'выключи', 'закрыть', 'выключить']:
                        program_name  = command.split(cmd)[-1].strip()
                        close_program(program_name)
                        return f'Программа "{program_name}" закрыта'
                    
                    if cmd in ['найди в браузере', 'найди в интернете', 'поиск в интернете']:
                        prompt = command.split(cmd)[-1].strip()
                        web_search(prompt)
                        return f'Поиск по запросу "{prompt}" выполнен'

                    if cmd in ['открой в youtube', 'найди в youtube', 'найди на youtube']:
                        prompt = command.split(cmd)[-1].strip()
                        youtube_search(prompt)
                        return f'Поиск в YouTube по запросу "{prompt}" выполнен'
                    
                    if cmd in ['открой новости', 'покажи новости']:
                        news.open_news()
                        return 'Новости открыты'
                    
                    if cmd in ['добавить заметку', 'напиши новую заметку', "добавть замектку"]:
                        text = command.split(cmd)[-1].strip()
                        notes.add_note(text)
                        return 'Заметка добавленна'
                        
                    if cmd in ['удалить заметку', 'удали заметку', "сотри заметку", "стереть заметку"]:
                        number = int(command.split(cmd)[-1].strip())
                        notes.delete_note(number)
                        return 'Заметка удалена'
                    
                    if cmd in ['установи громкость на ', 'поставь громкость', 'громкость ', 'громкость на ']:
                        volume_level = int(command.split(cmd)[-1].strip())
                        set_volume(volume_level)
                        return f'Уровень громкости - {volume_level}'

                    else:
                        result = function()
                        return f'Результат команды "{cmd}": {result}'
                    
                except Exception as e:
                    return f'Произошла ошибка при выполнении команды "{cmd}": {str(e)}, попробуйте задать запрос по-друггому'
    output = giga_output(command)      
    return output       

def recognition():
    r = sr.Recognizer()
    mic = sr.Microphone()

    sr.LANGUAGE ='ru-RU'

    stop_words = ['stop', 'стоп', 'хватит', 'прекрати', 'ончай', 'спасибо', 'Всё, спасибо', 'ватит, спасибо',  
                  'остановись', 'прекращай', 'а зелёный Оптимус Прайм огурец', 'пошёл в ', 'иди в']

    giga_clean()

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
                #speak(response)  # Озвучиваем ответ
                v.text_to_speech(response)
                print(response)
                return response