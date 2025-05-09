import tkinter as tk
from tkinter import messagebox


# Настройки оформления
BG_COLOR = "#F0F0F0"
BUTTON_COLOR = "#40E0D0"
ACTIVE_COLOR = "#30C0B0"
TEXT_FONT = ("Arial", 24, "bold")
BUTTON_SIZE = 5

window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("300x450")
window.configure(bg=BG_COLOR)




current_player = "X"
buttons = []
start_symbol = "X"

# Создаем контейнеры
start_frame = tk.Frame(window, bg=BG_COLOR)
game_frame = tk.Frame(window, bg=BG_COLOR)

# Изначально показываем только выбор символа
start_frame.pack(pady=30)
game_frame.pack_forget()


def start_game():
    global current_player, wins
    current_player = start_symbol
    wins = {'X': 0, 'O': 0}  # Сброс счёта при новой серии игр
    show_game_field()


def show_game_field():
    start_frame.pack_forget()
    game_frame.pack(pady=10)
    reset_field()
    update_score()


def reset_field():
    for row in buttons:
        for btn in row:
            btn.config(text="", state=tk.NORMAL)


def restart_game():
    reset_field()
    game_frame.pack_forget()
    start_frame.pack(pady=30)
    symbol_var.set("X")
    global start_symbol
    start_symbol = "X"
    wins.update({'X': 0, 'O': 0})


def check_winner():
    # Проверка горизонталей
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return buttons[i][0]["text"]
    # Проверка вертикалей
    for i in range(3):
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return buttons[0][i]["text"]
    # Проверка диагоналей
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return buttons[0][0]["text"]
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return buttons[0][2]["text"]
    return None

wins = {'X': 0, 'O': 0}

score_frame = tk.Frame(window)
score_frame.pack(pady=10)

score_label = tk.Label(score_frame, text="X: 0   O: 0", font=("Arial", 14))
score_label.pack()


def update_score():
    score_label.config(text=f"X: {wins['X']}   O: {wins['O']}")


def handle_win(winner):
    wins[winner] += 1
    update_score()
    if wins[winner] == 3:
        messagebox.showinfo("Конец игры", f"Игрок {winner} выиграл серию!")
        restart_game()
    else:
        messagebox.showinfo("Победа!", f"Игрок {winner} выиграл раунд!")
        reset_field()

    return None


def check_draw():
    return all(btn["text"] != "" for row in buttons for btn in row)


def reset_board():
    global current_player
    for row in buttons:
        for btn in row:
            btn.config(text="")
    current_player = "X"


def end_round(winner=None):
    if winner:
        wins[winner] += 1
        update_score()
        if wins[winner] == 3:
            messagebox.showinfo("Игра окончена", f"Игрок {winner} выиграл серию!")
            wins.update({'X': 0, 'O': 0})
            update_score()
    reset_board()


def on_click(row, col):
    global current_player


    if buttons[row][col]['text'] !="":
       return

    buttons[row][col].config(text=current_player)

    winner = check_winner()
    if winner:
        messagebox.showinfo("Победа!", f"Игрок {winner} победил!")
        end_round(winner)
    elif check_draw():
        messagebox.showinfo("Ничья!", "Ничья! Начните новый раунд!")
        end_round()
    else:
        current_player = "O" if current_player == "X" else "X"



    if buttons[row][col]['text'] == "":
        buttons[row][col].config(text=current_player)
        winner = check_winner()

# Игровое поле
game_frame = tk.Frame(window)
game_frame.pack(pady=20)


# Виджеты для выбора символа
tk.Label(start_frame, text="Выберите символ", bg=BG_COLOR, font=("Arial", 14)).pack(pady=10)

symbol_var = tk.StringVar(value="X")


def set_symbol(symbol):
    global start_symbol
    start_symbol = symbol


tk.Radiobutton(start_frame, text="Крестики (X)", variable=symbol_var, value="X",
               command=lambda: set_symbol("X"), bg=BG_COLOR).pack(pady=5)
tk.Radiobutton(start_frame, text="Нолики (O)", variable=symbol_var, value="O",
               command=lambda: set_symbol("O"), bg=BG_COLOR).pack(pady=5)

# Синяя кнопка "Начать игру"
tk.Button(start_frame, text="Начать игру", command=start_game,
          bg="#2196F3", fg="white", font=("Arial", 12)).pack(pady=20)

# Игровое поле
for i in range(3):
    row = []
    for j in range(3):

        btn = tk.Button(game_frame, text="", font=TEXT_FONT,
                        bg=BUTTON_COLOR, activebackground=ACTIVE_COLOR,
                        width=BUTTON_SIZE, height=BUTTON_SIZE // 2,
                        command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j, padx=5, pady=5)
        row.append(btn)
    buttons.append(row)

# Панель счёта
score_label = tk.Label(game_frame, text="X: 0   O: 0",
                       font=("Arial", 14, "bold"), bg=BG_COLOR)
score_label.grid(row=3, column=0, columnspan=3, pady=10)

# Кнопка сброса
tk.Button(game_frame, text="Новая игра", font=("Arial", 12),
          command=restart_game, bg="#FF5722", fg="white").grid(row=4, column=0, columnspan=3, pady=10, sticky="we")

      

window.mainloop()