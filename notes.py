import os

def check_file():
    # Путь к файлу
    file_path = "notes.txt"

    # Проверяем, существует ли файл
    if not os.path.isfile(file_path):
        # Если файл не существует, создаем его
        with open(file_path, "w"):
            pass

def add_note(text):
    check_file()
    with open("notes.txt", "a") as file:
        # Получаем текущее количество строк (заметок) в файле
        num_lines = sum(1 for line in open('notes.txt'))
        # Добавляем заметку с порядковым номером
        file.write(str(num_lines + 1) + ". " + text + "\n")

def delete_note(note_number):
    check_file()
    try:
        with open("notes.txt", "r") as file:
            lines = file.readlines()
        with open("notes.txt", "w") as file:
            for i, line in enumerate(lines):
                # Удаляем заметку, если ее номер совпадает с указанным
                if i != note_number - 1:
                    file.write(line)
                else:
                    # Если заметка удалена, уменьшаем номера всех следующих заметок
                    for j in range(i, len(lines) - 1):
                        lines[j + 1] = str(int(lines[j + 1].split(".")[0]) - 1) + "." + lines[j + 1][lines[j + 1].index(" "):]
                    file.writelines(lines[i + 1:])
                    break
    except:
        return 'Не удалось удалить заметку, проверьте, правильный ли номер вы указали'
    
def read_notes():
    with open("notes.txt", "r") as file:
        lines = file.readlines()
        notes = ""
        for i, line in enumerate(lines):
            notes += f"Заметка {line.strip()}\n"
        return notes
