import curses
import random
import json
import os
import time

BOARD_SIZE = 3

def init_board():
    return [[" " for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def available_moves(board):
    return [(x, y) for x in range(BOARD_SIZE) for y in range(BOARD_SIZE) if board[x][y] == " "]

def make_move(board, move, player):
    x, y = move
    board[x][y] = player

def check_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(BOARD_SIZE):
        if all([board[row][col] == player for row in range(BOARD_SIZE)]):
            return True
    if all([board[i][i] == player for i in range(BOARD_SIZE)]) or \
       all([board[i][BOARD_SIZE - 1 - i] == player for i in range(BOARD_SIZE)]):
        return True
    return False

def game_over(board):
    return check_winner(board, "X") or check_winner(board, "O") or not available_moves(board)

def evaluate(board):
    if check_winner(board, "X"):
        return 1
    elif check_winner(board, "O"):
        return -1
    else:
        return 0
    
def prompt_for_initials(stdscr):
    """Poproś gracza o wpisanie inicjałów."""
    stdscr.addstr("\nWpisz swoje inicjały (3 litery): ")
    stdscr.refresh()
    initials = stdscr.getstr(0, len("Wpisz swoje inicjały (3 litery): "), 3).decode('utf-8')
    return initials

def format_time(seconds):
    """Formatuje czas z sekund na hh:mm:ss."""
    return time.strftime('%H:%M:%S', time.gmtime(seconds))

def add_score_to_json(initials, time_elapsed, char_player, level):
    """Dodaje wynik gracza do pliku JSON."""
    filename = "wyniki_kolko_i_krzyzyk.json"
    try:
        if os.path.exists(filename):
            with open(filename, "r") as file:
                scores = json.load(file)
        else:
            scores = {"nowicjusz": [], "latwy": [], "sredni": [], "trudny": [], "niezwyciezony": []}

        score_data = {"nazwa": initials, "czas": format_time(time_elapsed), "char_player": char_player}
        scores[level].append(score_data)
        scores[level] = sorted(scores[level], key=lambda x: x['czas']) 

        with open(filename, "w") as file:
            json.dump(scores, file, indent=4)
    except IOError as e:
        print("Wystąpił błąd przy zapisie wyniku: ", e)

def minimax(board, depth, alpha, beta, is_maximizing):
    if depth == 0 or game_over(board):
        return evaluate(board)

    if is_maximizing:
        max_eval = float('-inf')
        for move in available_moves(board):
            make_move(board, move, "X")
            eval = minimax(board, depth - 1, alpha, beta, False)
            make_move(board, move, " ")
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in available_moves(board):
            make_move(board, move, "O")
            eval = minimax(board, depth - 1, alpha, beta, True)
            make_move(board, move, " ")
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def best_move(board, level, ai_player):
    if level == 1: 
        return random.choice(available_moves(board))
    else:
        if level == 5:
            difficulty = len(available_moves(board))
        else:
            difficulty = level 
        best_score = float('-inf') if ai_player == "X" else float('inf')
        moves = available_moves(board)
        best_moves = []

        for move in moves:
            make_move(board, move, ai_player)
            if ai_player == "X":
                score = minimax(board, difficulty, float('-inf'), float('inf'), False)
                if score > best_score:
                    best_score = score
                    best_moves = [move]
                elif score == best_score:
                    best_moves.append(move)
            else:
                score = minimax(board, difficulty, float('-inf'), float('inf'), True)
                if score < best_score:
                    best_score = score
                    best_moves = [move]
                elif score == best_score:
                    best_moves.append(move)
            make_move(board, move, " ") 
            
        return random.choice(best_moves) if best_moves else None


def draw_board(stdscr, board, cursor_pos):
    stdscr.clear()
    rows, cols = stdscr.getmaxyx() 
    board_width = 4 * BOARD_SIZE - 1
    board_height = 2 * BOARD_SIZE - 1
    start_y = (rows - board_height) // 2
    start_x = (cols - board_width) // 2

    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            cell = board[i][j]
            x = start_x + j * 4
            y = start_y + i * 2
            if (i, j) == cursor_pos:
                stdscr.attron(curses.A_REVERSE)
            stdscr.addstr(y, x, cell)
            if (i, j) == cursor_pos:
                stdscr.attroff(curses.A_REVERSE)
            if j < BOARD_SIZE - 1:
                stdscr.addstr(y, x + 1, " │ ")

    for i in range(1, BOARD_SIZE):
        y = start_y + i * 2 - 1
        stdscr.addstr(y, start_x, "──┼───┼──"[:(board_width - 1)])

    stdscr.refresh()


def player_move(board, cursor_pos):
    x, y = cursor_pos
    if board[x][y] == " ":
        return True
    return False

def update_cursor(key, cursor_pos):
    x, y = cursor_pos
    if key in [curses.KEY_UP, ord('w')] and x > 0:
        x -= 1
    elif key in [curses.KEY_DOWN, ord('s')] and x < BOARD_SIZE - 1:
        x += 1
    elif key in [curses.KEY_LEFT, ord('a')] and y > 0:
        y -= 1
    elif key in [curses.KEY_RIGHT, ord('d')] and y < BOARD_SIZE - 1:
        y += 1
    return x, y

def winners(board):
    if check_winner(board, "X"):
        winner = "X"
    elif check_winner(board, "O"):
        winner = "O"
    else:
        winner = "Remis"
    return winner

def choose_side(stdscr):
    sides = ['X', 'O']
    current_selection = 0
    while True:
        stdscr.clear()
        stdscr.addstr("Wybierz stronę:\n")
        for idx, side in enumerate(sides):
            if idx == current_selection:
                stdscr.attron(curses.A_REVERSE)
            stdscr.addstr(f"{side}\n")
            if idx == current_selection:
                stdscr.attroff(curses.A_REVERSE)
        stdscr.refresh()
        
        key = stdscr.getch()
        if key in [curses.KEY_UP, ord('w')] and current_selection > 0:
            current_selection -= 1
        elif key in [curses.KEY_DOWN, ord('s')] and current_selection < len(sides) - 1:
            current_selection += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            return sides[current_selection]

def play_game(stdscr, level, player):
    board = init_board()
    cursor_pos = (0, 0) 
    current_player = 'X'
    ai_player = 'O' if player == 'X' else 'X' 

    if player == 'O':
        ai_move = best_move(board, level, ai_player)
        make_move(board, ai_move, current_player)
        current_player = 'O' 

    player_time = 0

    while True:
        draw_board(stdscr, board, None) 
        stdscr.refresh()

        if game_over(board):
            winner = winners(board)
            break

        if current_player == player:
            player_start_time = time.time()
            while True:
                key = stdscr.getch()
                if key in [curses.KEY_UP, ord('w'), curses.KEY_DOWN, ord('s'),
                           curses.KEY_LEFT, ord('a'), curses.KEY_RIGHT, ord('d')]:
                    cursor_pos = update_cursor(key, cursor_pos)
                    draw_board(stdscr, board, cursor_pos) 
                    stdscr.refresh()
                elif key == 10:  
                    if player_move(board, cursor_pos):
                        make_move(board, cursor_pos, player)
                        current_player = ai_player 
                        break 
            player_end_time = time.time()
            player_time += player_end_time - player_start_time
        else:
            ai_move = best_move(board, level, ai_player)
            make_move(board, ai_move, ai_player)
            current_player = player 

    if winner == player:
        initials = prompt_for_initials(stdscr)
        add_score_to_json(initials, player_time, player, get_difficulty_level_name(level))
    draw_board(stdscr, board, None) 
    rows, cols = stdscr.getmaxyx()
    message = f"Zwycięzca: {winner}" if winner != "Remis" else "Remis"
    stdscr.addstr(rows // 2 + BOARD_SIZE + 2, (cols - len(message)) // 2, message)
    stdscr.refresh()
    stdscr.getch()

def load_scores():
    filename = "wyniki_kolko_i_krzyzyk.json"
    if os.path.exists(filename):
        with open(filename, "r") as file:
            scores = json.load(file)
    else:
        scores = {"nowicjusz": [], "latwy": [], "sredni": [], "trudny": [], "niezwyciezony": []}
    return scores



def save_score(score):
    scores = load_scores()
    scores.append(score)
    with open("wyniki_kolko_i_krzyzyk.json", "w") as file:
        json.dump(scores, file, indent=4)

def display_scores(stdscr):
    scores = load_scores()
    stdscr.clear()
    stdscr.addstr(0, 0, "Tablica wyników:\n")
    for level, level_scores in scores.items():
        stdscr.addstr(f"Poziom {level.capitalize()}:\n")
        top_scores = sorted(level_scores, key=lambda x: x['czas'])[:5]
        for idx, score in enumerate(top_scores, start=1):
            stdscr.addstr(f"{idx}. {score['nazwa']} - {score['czas']} - {score['char_player']}\n")
        stdscr.addstr("\n")
    stdscr.refresh()
    stdscr.getch()

def settings_menu(stdscr, current_level, current_side):
    levels = ["nowicjusz", "latwy", "sredni", "trudny", "niezwyciezony"]
    sides = ['X', 'O']
    level_index = levels.index(current_level)
    side_index = sides.index(current_side)

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Ustawienia:\n")
        stdscr.addstr(2, 0, "Wybierz poziom trudności:\n")

        for idx, level in enumerate(levels):
            if idx == level_index:
                stdscr.attron(curses.A_REVERSE)
            stdscr.addstr(f"{level}\n")
            if idx == level_index:
                stdscr.attroff(curses.A_REVERSE)

        stdscr.addstr(10, 0, "Wybierz stronę:\n")
        for idx, side in enumerate(sides):
            if idx == side_index:
                stdscr.attron(curses.A_REVERSE)
            stdscr.addstr(f"{side}\n")
            if idx == side_index:
                stdscr.attroff(curses.A_REVERSE)

        stdscr.refresh()

        key = stdscr.getch()
        if key in [curses.KEY_UP, ord('w')]:
            if level_index > 0:
                level_index -= 1
            else:
                side_index = (side_index - 1) % len(sides)
        elif key in [curses.KEY_DOWN, ord('s')]:
            if level_index < len(levels) - 1:
                level_index += 1
            else:
                side_index = (side_index + 1) % len(sides)
        elif key in [curses.KEY_LEFT, ord('a')]:
            side_index = (side_index - 1) % len(sides)
        elif key in [curses.KEY_RIGHT, ord('d')]:
            side_index = (side_index + 1) % len(sides)
        elif key == curses.KEY_ENTER or key in [10, 13]:
            break
    
    save_settings(level_index+1, sides[side_index])
    return level_index+1, sides[side_index]

def save_settings(lvl, side):
    """Zapisuje ustawienia gry do pliku JSON."""
    with open("ustawienia_kolko_i_krzyzyk.json", "w") as file:
        json.dump({"level": lvl, "side": side}, file, indent=4)

def load_settings():
    """Wczytuje ustawienia gry z pliku JSON."""
    try:
        with open("ustawienia_kolko_i_krzyzyk.json", "r") as file:
            settings = json.load(file)
            return settings
    except (FileNotFoundError, json.JSONDecodeError):
        return {"level": 1, "side": "X"}

def get_difficulty_level_name(level):
    """Zwraca nazwę poziomu trudności na podstawie numeru poziomu."""
    levels = {1: "nowicjusz", 2: "latwy", 3: "sredni", 4: "trudny", 5: "niezwyciezony"}
    return levels.get(level, "nieznany")

def main(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()
    
    settings = load_settings()
    current_level = settings["level"]
    current_side = settings["side"]


    menu_items = ["Graj", "Tablica wyników", "Ustawienia", "Wyjdź z gry"]
    current_selection = 0

    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        for idx, item in enumerate(menu_items):
            x = w//2 - len(item)//2
            y = h//2 - len(menu_items)//2 + idx
            if idx == current_selection:
                stdscr.attron(curses.A_REVERSE)
            stdscr.addstr(y, x, item)
            if idx == current_selection:
                stdscr.attroff(curses.A_REVERSE)

        key = stdscr.getch()

        if key in [curses.KEY_UP, ord('w')] and current_selection > 0:
            current_selection -= 1
        elif key in [curses.KEY_DOWN, ord('s')] and current_selection < len(menu_items) - 1:
            current_selection += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            choice = menu_items[current_selection]
            if choice == "Wyjdź z gry":
                break
            elif choice == "Ustawienia":
                current_level, current_side = settings_menu(stdscr, get_difficulty_level_name(current_level), current_side)
            elif choice == "Tablica wyników":
                display_scores(stdscr)
            elif choice == "Graj":
                play_game(stdscr, current_level, current_side)

        stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(main)
