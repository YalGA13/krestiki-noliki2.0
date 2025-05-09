import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("300x400")

current_player = "X"
buttons = []
wins = {'X': 0, 'O': 0}  # Счётчик побед

# Создаём фрейм для счётчика
score_frame = tk.Frame(window)
score_frame.pack(pady=10)

# Метка для отображения счёта
score_label = tk.Label(score_frame, text="X: 0   O: 0", font=("Arial", 14))
score_label.pack()


def update_score():
    score_label.config(text=f"X: {wins['X']}   O: {wins['O']}")


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


def check_draw():
    # Проверка на ничью
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
            wins['X'] = wins['O'] = 0
            update_score()
    reset_board()


def on_click(row, col):
    global current_player
    if buttons[row][col]['text'] != "":
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


# Создание игрового поля
game_frame = tk.Frame(window)
game_frame.pack(pady=20)

for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(game_frame, text="", font=("Arial", 20),
                        width=5, height=2,
                        command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j, padx=2, pady=2)
        row.append(btn)
    buttons.append(row)

# Кнопка сброса
reset_btn = tk.Button(window, text="Новая игра", font=("Arial", 12),
                      command=lambda: [reset_board(), wins.update({'X': 0, 'O': 0}), update_score()])
reset_btn.pack(pady=10)

window.mainloop()