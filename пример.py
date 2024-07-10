import turtle
import random

# Константы
WIDTH = 600
HEIGHT = 600
SPEED = 10
FPS = 10

# Класс для создания змейки
class Snake:
    def __init__(self, length=5):
        self.segments = []
        for _ in range(length):
            self.segments.append(turtle.Turtle())
        self.length = length
        self.head = self.segments[0]
        self.food = turtle.Turtle()
        self.score = 0
        self.is_game_over = False

    # Метод для рисования сегментов змейки
    def draw(self):
        for segment in self.segments:
            segment.forward(SPEED)

    # Метод для перемещения змейки
    def move(self, direction):
        if not self.is_game_over:
            x = self.head.x()
            y = self.head.y()
            if direction == 'up':
                self.head.setheading(90)
                self.draw()
            elif direction == 'down':
                self.head.setheading(270)
                self.draw()
            elif direction == 'left':
                self.head.setheading(180)
                self.draw()
            elif direction == 'right':
                self.head.setheading(0)
                self.draw()

            # Проверка на столкновение со стеной
            if x > WIDTH or x < 0 or y > HEIGHT or y < 0:
                self.is_game_over = True

            # Проверка на столкновение с самим собой
            for segment in self.segments[1:]:
                if self.head.distance(segment) < 15:
                    self.is_game_over = True

    # Метод для обновления положения пищи
    def update_food(self):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        self.food.goto(x, y)

# Функция для обработки событий клавиатуры
def key_handler(event):
    if event.keysym == 'Up' and snake.is_game_over is False:
        snake.move('up')
    elif event.keysym == 'Down' and snake.is_game_over is False:
        snake.move('down')
    elif event.keysym == 'Left' and snake.is_game_over is False:
        snake.move('left')
    elif event.keysym == 'Right' and snake.is_game_over is False:
        snake.move('right')

# Создание змейки
snake = Snake()

# Установка параметров окна
wn = turtle.Screen()
wn.setup(WIDTH, HEIGHT)
wn.title("Snake Game")
wn.bgcolor('black')
wn.tracer(FPS)

# Отображение пищи
snake.update_food()

# Обработка событий клавиатуры
wn.listen()
wn.onkeypress(key_handler)

# Основной цикл игры
while True:
    wn.update()
    if snake.head.distance(snake.food) < 15:
        snake.length += 1
        snake.score += 1
        snake.update_food()
    else:
        if len(snake.segments) > 0:  # Добавлена проверка на наличие элементов в списке
            snake.segments.pop()

    # Проверка на конец игры
    if snake.is_game_over:
        wn.clear()
        wn.update()
        print(f"Game Over! Your score is {snake.score}")
        break

wn.mainloop()