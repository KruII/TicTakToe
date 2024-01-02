import curses
import random
import json
import os
import time


class TicTacToe:
    '''
    ╔════════════════════════════════════════════════════════════════════════════════╗
    ║PL: Klasa reprezentująca grę w kółko i krzyżyk.                                 ║
    ╠════════════════════════════════════════════════════════════════════════════════╣
    ║EN: Class representing the Tic-Tac-Toe game.                                    ║
    ╠════════════════════════════════════════════════════════════════════════════════╣
    ║                                                             ID IN READ ME: 02  ║
    ╚════════════════════════════════════════════════════════════════════════════════╝
    '''

    '''
    ╔════════════════════════════════════════════════════════════════════════════════╗
    ║PL: Stałe plików konfiguracyjnych.                                              ║
    ╠════════════════════════════════════════════════════════════════════════════════╣
    ║EN: Constants for configuration files.                                          ║
    ╠════════════════════════════════════════════════════════════════════════════════╣
    ║                                                             ID IN READ ME: 03  ║
    ╚════════════════════════════════════════════════════════════════════════════════╝
    '''
    SCORES_FILE = "wyniki_kolko_i_krzyzyk.json"
    SETTINGS_FILE = "ustawienia_kolko_i_krzyzyk.json"

    '''
    ╔════════════════════════════════════════════════════════════════════════════════╗
    ║PL: Mapowanie poziomów trudności.                                               ║
    ╠════════════════════════════════════════════════════════════════════════════════╣
    ║EN: Mapping of difficulty levels.                                               ║
    ╠════════════════════════════════════════════════════════════════════════════════╣
    ║                                                             ID IN READ ME: 04  ║
    ╚════════════════════════════════════════════════════════════════════════════════╝
    '''
    LEVELS = {
               1: "nowicjusz",          # NOOB
               2: "latwy",              # EASY
               3: "sredni",             # MEDIUM
               4: "trudny",             # HARD
               5: "niezwyciezony"       # INPOSSIBLE
             }
    
    def __init__(self, screen):
        '''
        ╔════════════════════════════════════════════════════════════════════════════════╗
        ║PL: Inicjalizuje pustą planszę gry.                                             ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║PARAMETRY:                                                                      ║
        ║    Brak                                                                        ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║ZWRACA:                                                                         ║
        ║    Dwuwymiarowa lista reprezentująca pustą planszę do gry (list of lists)      ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║EN: Initializes an empty game board.                                            ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║PARAMETERS:                                                                     ║
        ║    None                                                                        ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║RETURNS:                                                                        ║
        ║    A two-dimensional list representing an empty game board (list of lists)     ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║                                                             ID IN READ ME: 05  ║
        ╚════════════════════════════════════════════════════════════════════════════════╝
        '''
        self.screen =           screen
        self.board_size =       3
        self.board =            self.init_board()
        self.current_level =    self.load_settings().get("level", 1)
        self.current_side =     self.load_settings().get("side", "X")
        self.ai_player =        'O' if self.current_side == 'X'\
                                else 'X' 
        self.winner =           "Remis"

    def init_board(self):
        '''
        ╔════════════════════════════════════════════════════════════════════════════════╗
        ║PL: Inicjalizuje pustą planszę do gry w kółko i krzyżyk.                        ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║PARAMETRY:                                                                      ║
        ║    Brak                                                                        ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║ZWRACA:                                                                         ║
        ║    Pusta plansza gry jako dwuwymiarowa lista (list of lists)                   ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║EN: Initializes an empty Tic-Tac-Toe game board.                                ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║PARAMETERS:                                                                     ║
        ║    None                                                                        ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║RETURNS:                                                                        ║
        ║    An empty game board as a two-dimensional list (list of lists)               ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║                                                             ID IN READ ME: 06  ║
        ╚════════════════════════════════════════════════════════════════════════════════╝
        '''
        return [[" " for _ in range(self.board_size)] for _ in range(self.board_size)]

    def load_settings(self):
        '''
        ╔════════════════════════════════════════════════════════════════════════════════╗
        ║PL: Wczytuje ustawienia gry z pliku JSON.                                       ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║PARAMETRY:                                                                      ║
        ║    Brak                                                                        ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║ZWRACA:                                                                         ║
        ║    Słownik z ustawieniami gry, domyślnie: {"level": 1, "side": "X"}            ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║EN: Loads game settings from a JSON file.                                       ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║PARAMETERS:                                                                     ║
        ║    None                                                                        ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║RETURNS:                                                                        ║
        ║    A dictionary with game settings, defaults to: {"level": 1, "side": "X"}     ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║                                                             ID IN READ ME: 07  ║
        ╚════════════════════════════════════════════════════════════════════════════════╝
        '''
        try:
            with open("ustawienia_kolko_i_krzyzyk.json", "r") as file:
                settings = json.load(file)
                return settings
        except (FileNotFoundError, json.JSONDecodeError):
            return {"level": 1, "side": "X"}

        
    def __main__(self):
        '''
        ╔════════════════════════════════════════════════════════════════════════════════╗
        ║PL: Główna pętla gry, wyświetla menu i obsługuje akcje użytkownika.             ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║PARAMETRY:                                                                      ║
        ║    Brak                                                                        ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║ZWRACA:                                                                         ║
        ║    Nic, funkcja wykonuje akcje na podstawie wyboru użytkownika.                ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║EN: Main game loop, displays the menu and handles user actions.                 ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║PARAMETERS:                                                                     ║
        ║    None                                                                        ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║RETURNS:                                                                        ║
        ║    Nothing, the function performs actions based on user's choice.              ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║                                                             ID IN READ ME: 08  ║
        ╚════════════════════════════════════════════════════════════════════════════════╝
        '''
        curses.curs_set(0)
        self.screen.clear()
        self.screen.refresh()

        menu_items = [
                       "Graj", 
                       "Tablica wyników", 
                       "Ustawienia", 
                       "Wyjdź z gry"
                     ]
        current_selection = 0

        while True:
            self.screen.clear()
            h, w = self.screen.getmaxyx()
            for idx, item in enumerate(menu_items):
                x = w//2 - len(item)//2
                y = h//2 - len(menu_items)//2 + idx
                if idx == current_selection:
                    self.screen.attron(curses.A_REVERSE)
                self.screen.addstr(y, x, item)
                if idx == current_selection:
                    self.screen.attroff(curses.A_REVERSE)

            key = self.screen.getch()

            if key in [curses.KEY_UP, ord('w')] and current_selection > 0:
                current_selection -= 1
            elif key in [curses.KEY_DOWN, ord('s')] and current_selection < len(menu_items) - 1:
                current_selection += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                choice = menu_items[current_selection]
                if choice == "Wyjdź z gry":
                    break
                elif choice == "Ustawienia":
                    self.settings_menu()
                elif choice == "Tablica wyników":
                    self.display_scores()
                elif choice == "Graj":
                    self.play_game()

            self.screen.refresh()
            
    def settings_menu(self):
        '''
        ╔════════════════════════════════════════════════════════════════════════════════╗
        ║PL: Wyświetla menu ustawień gry, pozwalając wybrać poziom trudności i stronę.   ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║PARAMETRY:                                                                      ║
        ║    Brak                                                                        ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║ZWRACA:                                                                         ║
        ║    Brak. Ustawienia są zapisywane wewnątrz funkcji.                            ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║EN: Displays the game's settings menu, allowing the selection of difficulty     ║
        ║    level and side.                                                             ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║PARAMETERS:                                                                     ║
        ║    None                                                                        ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║RETURNS:                                                                        ║
        ║    None. Settings are saved within the function.                               ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║                                                             ID IN READ ME: 09  ║
        ╚════════════════════════════════════════════════════════════════════════════════╝
        '''
        levels = ["nowicjusz", "latwy", "sredni", "trudny", "niezwyciezony"]
        sides = ['X', 'O']
        level_index = levels.index(self.get_difficulty_level_name())
        side_index = sides.index(self.current_side)

        while True:
            self.screen.clear()
            self.screen.addstr(0, 0, "Ustawienia:\n")
            self.screen.addstr(2, 0, "Wybierz poziom trudności:\n")

            for idx, level in enumerate(levels):
                if idx == level_index:
                    self.screen.attron(curses.A_REVERSE)
                self.screen.addstr(f"{level}\n")
                if idx == level_index:
                    self.screen.attroff(curses.A_REVERSE)

            self.screen.addstr(10, 0, "Wybierz stronę:\n")
            for idx, side in enumerate(sides):
                if idx == side_index:
                    self.screen.attron(curses.A_REVERSE)
                self.screen.addstr(f"{side}\n")
                if idx == side_index:
                    self.screen.attroff(curses.A_REVERSE)

            self.screen.refresh()

            key = self.screen.getch()
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
        
        self.current_level, self.current_side = level_index+1, sides[side_index]
        self.save_settings()
        
    def get_difficulty_level_name(self):
        '''
        ╔════════════════════════════════════════════════════════════════════════════════╗
        ║PL: Zwraca nazwę poziomu trudności na podstawie numeru poziomu.                 ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║PARAMETRY:                                                                      ║
        ║    Brak                                                                        ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║ZWRACA:                                                                         ║
        ║    Nazwa poziomu trudności (str).                                              ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║EN: Returns the name of the difficulty level based on its number.               ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║PARAMETERS:                                                                     ║
        ║    None                                                                        ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║RETURNS:                                                                        ║
        ║    The name of the difficulty level (str).                                     ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║                                                             ID IN READ ME: 10  ║
        ╚════════════════════════════════════════════════════════════════════════════════╝
        '''
        return self.LEVELS.get(self.current_level, "nieznany")
    
    def save_settings(self):
        '''
        ╔════════════════════════════════════════════════════════════════════════════════╗
        ║PL: Zapisuje bieżące ustawienia gry do pliku konfiguracyjnego.                  ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║PARAMETRY:                                                                      ║
        ║    Brak                                                                        ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║ZWRACA:                                                                         ║
        ║    Brak.                                                                       ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║EN: Saves the current game settings to the configuration file.                  ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║PARAMETERS:                                                                     ║
        ║    None                                                                        ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║RETURNS:                                                                        ║
        ║    None.                                                                       ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║                                                             ID IN READ ME: 11  ║
        ╚════════════════════════════════════════════════════════════════════════════════╝
        '''
        with open(self.SETTINGS_FILE, "w") as file:
            json.dump({"level": self.current_level, "side": self.current_side}, file, indent=4)
            
    def display_scores(self):
        '''
        ╔════════════════════════════════════════════════════════════════════════════════╗
        ║PL: Wyświetla tablicę wyników gry na ekranie.                                   ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║PARAMETRY:                                                                      ║
        ║    Brak                                                                        ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║ZWRACA:                                                                         ║
        ║    Brak. Funkcja wyświetla wyniki na ekranie, ale nic nie zwraca.              ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║EN: Displays the game's score board on the screen.                              ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║PARAMETERS:                                                                     ║
        ║    None                                                                        ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║RETURNS:                                                                        ║
        ║    None. The function displays results on the screen but does not return       ║
        ║    anything.                                                                   ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║                                                             ID IN READ ME: 12  ║
        ╚════════════════════════════════════════════════════════════════════════════════╝
        '''
        scores = self.load_scores()
        self.screen.clear()
        self.screen.addstr(0, 0, "Tablica wyników:\n")
        for level, level_scores in scores.items():
            self.screen.addstr(f"Poziom {level.capitalize()}:\n")
            top_scores = sorted(level_scores, key=lambda x: x['czas'])[:5]
            for idx, score in enumerate(top_scores, start=1):
                self.screen.addstr(f"{idx}. {score['nazwa']} - {score['czas']} - {score['char_player']}\n")
            self.screen.addstr("\n")
        self.screen.refresh()
        self.screen.getch()
        
    def load_scores(self):
        '''
        ╔════════════════════════════════════════════════════════════════════════════════╗
        ║PL: Wczytuje wyniki gry z pliku JSON.                                           ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║PARAMETRY:                                                                      ║
        ║    Brak                                                                        ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║ZWRACA:                                                                         ║
        ║    Słownik zawierający wyniki gry.                                             ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║EN: Loads the game scores from a JSON file.                                     ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║PARAMETERS:                                                                     ║
        ║    None                                                                        ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║RETURNS:                                                                        ║
        ║    A dictionary containing game scores.                                        ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║                                                             ID IN READ ME: 13  ║
        ╚════════════════════════════════════════════════════════════════════════════════╝
        '''
        if os.path.exists(self.SCORES_FILE):
            with open(self.SCORES_FILE, "r") as file:
                scores = json.load(file)
        else:
            scores = {"nowicjusz": [], "latwy": [], "sredni": [], "trudny": [], "niezwyciezony": []}
        return scores

    def play_game(self):
        '''
        ╔════════════════════════════════════════════════════════════════════════════════╗
        ║PL: Rozpoczyna i zarządza rozgrywką w kółko i krzyżyk.                          ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║PARAMETRY:                                                                      ║
        ║    Brak                                                                        ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║ZWRACA:                                                                         ║
        ║    Brak. Funkcja zarządza całym procesem gry.                                  ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║EN: Starts and manages the Tic-Tac-Toe game.                                    ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║PARAMETERS:                                                                     ║
        ║    None                                                                        ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║RETURNS:                                                                        ║
        ║    None. The function manages the entire game process.                         ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║                                                             ID IN READ ME: 14  ║
        ╚════════════════════════════════════════════════════════════════════════════════╝
        '''
        self.board = self.init_board()
        cursor_pos = (0, 0) 
        current_player = 'X'
        self.ai_player = 'O' if self.current_side == 'X' else 'X' 

        if self.current_side == 'O':
            self.make_move(current_player)
            current_player = 'O' 

        player_time = 0

        while True:
            self.draw_board(None) 
            self.screen.refresh()

            if self.check_winner():
                break

            if current_player == self.current_side:
                player_start_time = time.time()
                while True:
                    key = self.screen.getch()
                    if key in [curses.KEY_UP, ord('w'), curses.KEY_DOWN, ord('s'),
                            curses.KEY_LEFT, ord('a'), curses.KEY_RIGHT, ord('d')]:
                        cursor_pos = self.update_cursor(key, cursor_pos)
                        self.draw_board(cursor_pos) 
                        self.screen.refresh()
                    elif key == 10:  
                        if self.player_move(cursor_pos):
                            self.make_move(current_player, cursor_pos)
                            current_player = self.ai_player
                            break 
                player_end_time = time.time()
                player_time += player_end_time - player_start_time
            else:
                self.make_move(current_player)
                current_player = self.current_side

        if self.winner == self.current_side:
            initials = self.prompt_for_initials()
            self.add_score_to_json(initials, player_time)
        self.draw_board(None) 
        rows, cols = self.screen.getmaxyx()
        message = f"Zwycięzca: {self.winner}" if self.winner != "Remis" else "Remis"
        self.screen.addstr(rows // 2 + self.board_size + 2, (cols - len(message)) // 2, message)
        self.screen.refresh()
        self.screen.getch()
        
    def make_move(self, player, move = None):
        '''
        ╔════════════════════════════════════════════════════════════════════════════════╗
        ║PL: Wykonuje ruch na planszy.                                                   ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║PARAMETRY:                                                                      ║
        ║    player (str):                                                               ║
        ║       Znak gracza wykonującego ruch ('X' lub 'O')                              ║
        ║    move (tuple, opcjonalne):                                                   ║
        ║       Pozycja ruchu na planszy (x, y)                                          ║
        ║       Jeśli nie podano, ruch jest dobierany automatycznie                      ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║ZWRACA:                                                                         ║
        ║    Nic, aktualizuje planszę po wykonaniu ruchu.                                ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║EN: Makes a move on the board.                                                  ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║PARAMETERS:                                                                     ║
        ║    player (str):                                                               ║
        ║       The player making the move ('X' or 'O')                                  ║
        ║    move (tuple, optional):                                                     ║
        ║       The position of the move on the board (x, y)                             ║
        ║       If not provided, the move is selected automatically                      ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║RETURNS:                                                                        ║
        ║    None, updates the board after the move.                                     ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║                                                             ID IN READ ME: 15  ║
        ╚════════════════════════════════════════════════════════════════════════════════╝
        '''
        x, y = move if move is not None else self.best_move()
        self.board[x][y] = player
        
    def best_move(self):
        '''
        ╔════════════════════════════════════════════════════════════════════════════════╗
        ║PL: Wybiera najlepszy ruch w grze wykorzystując algorytm Minimax.               ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║PARAMETRY:                                                                      ║
        ║    Brak                                                                        ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║ZWRACA:                                                                         ║
        ║    Najlepszy ruch jako krotkę (tuple).                                         ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║EN: Selects the best move in the game using the Minimax algorithm.              ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║PARAMETERS:                                                                     ║
        ║    None                                                                        ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║RETURNS:                                                                        ║
        ║    The best move as a tuple (tuple).                                           ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║                                                             ID IN READ ME: 16  ║
        ╚════════════════════════════════════════════════════════════════════════════════╝
        '''
        if not self.available_moves():
            return None
        if self.current_level == 1: 
            return random.choice(self.available_moves())
        else:
            if self.current_level == 5:
                difficulty = len(self.available_moves())
            else:
                difficulty = self.current_level
            best_score = float('-inf') if self.ai_player == "X" else float('inf')
            moves = self.available_moves()
            best_moves = []

            for move in moves:
                self.make_move(self.ai_player, move)
                if self.ai_player == "X":
                    score = self.minimax(difficulty, float('-inf'), float('inf'), False)
                    if score > best_score:
                        best_score = score
                        best_moves = [move]
                    elif score == best_score:
                        best_moves.append(move)
                else:
                    score = self.minimax(difficulty, float('-inf'), float('inf'), True)
                    if score < best_score:
                        best_score = score
                        best_moves = [move]
                    elif score == best_score:
                        best_moves.append(move)
                self.make_move(" ", move) 
                
            return random.choice(best_moves) if best_moves else None
        
    def available_moves(self):
        '''
        ╔════════════════════════════════════════════════════════════════════════════════╗
        ║PL: Zwraca listę dostępnych ruchów na planszy.                                  ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║PARAMETRY:                                                                      ║
        ║    Brak                                                                        ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║ZWRACA:                                                                         ║
        ║    Lista kratek z koordynatami dostępnych ruchów.                              ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║EN: Returns a list of available moves on the board.                             ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║PARAMETERS:                                                                     ║
        ║    None                                                                        ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║RETURNS:                                                                        ║
        ║    A list of tuples with coordinates of available moves.                       ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║                                                             ID IN READ ME: 17  ║
        ╚════════════════════════════════════════════════════════════════════════════════╝
        '''
        return [(x, y) for x in range(self.board_size) for y in range(self.board_size) if self.board[x][y] == " "]
    
    def minimax(self, depth, alpha, beta, is_maximizing):
        '''
        ╔════════════════════════════════════════════════════════════════════════════════╗
        ║PL: Funkcja Minimax do wyznaczania najlepszego ruchu w grze.                    ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║PARAMETRY:                                                                      ║
        ║    depth (int):                                                                ║
        ║       Głębokość przeszukiwania                                                 ║
        ║    alpha (float):                                                              ║
        ║       Wartość alfa dla cięcia alfa-beta                                        ║
        ║    beta (float):                                                               ║
        ║       Wartość beta dla cięcia alfa-beta                                        ║
        ║    is_maximizing (bool):                                                       ║
        ║       Flaga określająca, czy to ruch maksymalizujący                           ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║ZWRACA:                                                                         ║
        ║    Najlepszą ocenę ruchu (int).                                                ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║EN: Minimax function to determine the best move in the game.                    ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║PARAMETERS:                                                                     ║
        ║    depth (int):                                                                ║
        ║       Depth of search                                                          ║
        ║    alpha (float):                                                              ║
        ║       Alpha value for alpha-beta pruning                                       ║
        ║    beta (float):                                                               ║
        ║       Beta value for alpha-beta pruning                                        ║
        ║    is_maximizing (bool):                                                       ║
        ║       Flag to determine if it's a maximizing move                              ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║RETURNS:                                                                        ║
        ║    The best score evaluation of the move (int).                                ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║                                                             ID IN READ ME: 18  ║
        ╚════════════════════════════════════════════════════════════════════════════════╝
        '''
        if depth == 0 or self.check_winner():
            return self.evaluate()

        if is_maximizing:
            max_eval = float('-inf')
            for move in self.available_moves():
                self.make_move("X", move)
                eval = self.minimax(depth - 1, alpha, beta, False)
                self.make_move(" ", move)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for move in self.available_moves():
                self.make_move("O", move)
                eval = self.minimax(depth - 1, alpha, beta, True)
                self.make_move(" ", move)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval
    
    def check_winner(self):
        '''
        ╔════════════════════════════════════════════════════════════════════════════════╗
        ║PL: Sprawdza, czy któryś z graczy wygrał grę.                                   ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║PARAMETRY:                                                                      ║
        ║    Brak                                                                        ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║ZWRACA:                                                                         ║
        ║    True, jeśli któryś z graczy wygrał lub gra zakończyła się remisem           ║
        ║    False w przeciwnym przypadku                                                ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║EN: Checks if any of the players has won the game.                              ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║PARAMETERS:                                                                     ║
        ║    None                                                                        ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║RETURNS:                                                                        ║
        ║    True if a player has won or the game ends in a draw                         ║
        ║    False otherwise                                                             ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║                                                             ID IN READ ME: 19  ║
        ╚════════════════════════════════════════════════════════════════════════════════╝
        '''
        for char in ['X', 'O']:
            for row in self.board:
                if all(cell == char for cell in row):
                    self.winner = char
                    return True

            for col in range(self.board_size):
                if all(self.board[row][col] == char for row in range(self.board_size)):
                    self.winner = char
                    return True

            if all(self.board[i][i] == char for i in range(self.board_size)) or \
            all(self.board[i][self.board_size - i - 1] == char for i in range(self.board_size)):
                self.winner = char
                return True

        if not any(" " in row for row in self.board):
            self.winner = "Remis"
            return True 

        return False
    
    def evaluate(self):
        '''
        ╔════════════════════════════════════════════════════════════════════════════════╗
        ║PL: Ocenia stan gry po każdym ruchu.                                            ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║PARAMETRY:                                                                      ║
        ║    Brak                                                                        ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║ZWRACA:                                                                         ║
        ║    Wartość numeryczną: 1 dla wygranej 'X', -1 dla wygranej 'O', 0 w innym      ║
        ║    przypadku.                                                                  ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║EN: Evaluates the state of the game after each move.                            ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║PARAMETERS:                                                                     ║
        ║    None                                                                        ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║RETURNS:                                                                        ║
        ║    A numerical value: 1 for 'X' win, -1 for 'O' win, 0 otherwise.              ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║                                                             ID IN READ ME: 20  ║
        ╚════════════════════════════════════════════════════════════════════════════════╝
        '''
        self.check_winner()
        if self.winner == 'X':
            return 1
        elif self.winner == 'O':
            return -1
        else:
            return 0
        
    def draw_board(self, cursor_pos):
        '''
        ╔════════════════════════════════════════════════════════════════════════════════╗
        ║PL: Rysuje aktualny stan planszy gry na ekranie.                                ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║PARAMETRY:                                                                      ║
        ║    cursor_pos (tuple):                                                         ║
        ║       Pozycja kursora na planszy                                               ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║ZWRACA:                                                                         ║
        ║    Brak                                                                        ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║EN: Draws the current state of the game board on the screen.                    ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║PARAMETERS:                                                                     ║
        ║    cursor_pos (tuple):                                                         ║
        ║       The cursor position on the board                                         ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║RETURNS:                                                                        ║
        ║    None                                                                        ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║                                                             ID IN READ ME: 21  ║
        ╚════════════════════════════════════════════════════════════════════════════════╝
        '''
        self.screen.clear()
        rows, cols = self.screen.getmaxyx() 
        board_width = 4 * self.board_size - 1
        board_height = 2 * self.board_size - 1
        start_y = (rows - board_height) // 2
        start_x = (cols - board_width) // 2

        for i in range(self.board_size):
            for j in range(self.board_size):
                cell = self.board[i][j]
                x = start_x + j * 4
                y = start_y + i * 2
                if (i, j) == cursor_pos:
                    self.screen.attron(curses.A_REVERSE)
                self.screen.addstr(y, x, cell)
                if (i, j) == cursor_pos:
                    self.screen.attroff(curses.A_REVERSE)
                if j < self.board_size - 1:
                    self.screen.addstr(y, x + 1, " │ ")

        for i in range(1, self.board_size):
            y = start_y + i * 2 - 1
            self.screen.addstr(y, start_x, "──┼───┼──"[:(board_width - 1)])

        self.screen.refresh()
        
    def update_cursor(self, key, cursor_pos):
        '''
        ╔════════════════════════════════════════════════════════════════════════════════╗
        ║PL: Aktualizuje pozycję kursora na planszy w zależności od naciśniętego         ║
        ║    klawisza.                                                                   ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║PARAMETRY:                                                                      ║
        ║    key (int):                                                                  ║
        ║       Kod klawisza                                                             ║
        ║    cursor_pos (tuple):                                                         ║
        ║       Obecna pozycja kursora na planszy                                        ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║ZWRACA:                                                                         ║
        ║    Zaktualizowaną pozycję kursora jako krotkę.                                 ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║EN: Updates the cursor position on the board based on the pressed key.          ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║PARAMETERS:                                                                     ║
        ║    key (int):                                                                  ║
        ║       The key code                                                             ║
        ║    cursor_pos (tuple):                                                         ║
        ║       The current cursor position on the board                                 ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║RETURNS:                                                                        ║
        ║    The updated cursor position as a tuple.                                     ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║                                                             ID IN READ ME: 22  ║
        ╚════════════════════════════════════════════════════════════════════════════════╝
        '''
        x, y = cursor_pos
        if key in [curses.KEY_UP, ord('w')] and x > 0:
            x -= 1
        elif key in [curses.KEY_DOWN, ord('s')] and x < self.board_size - 1:
            x += 1
        elif key in [curses.KEY_LEFT, ord('a')] and y > 0:
            y -= 1
        elif key in [curses.KEY_RIGHT, ord('d')] and y < self.board_size - 1:
            y += 1
        return x, y
    
    def player_move(self, cursor_pos):
        '''
        ╔════════════════════════════════════════════════════════════════════════════════╗
        ║PL: Sprawdza, czy ruch gracza jest możliwy na podanej pozycji.                  ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║PARAMETRY:                                                                      ║
        ║    cursor_pos (tuple):                                                         ║
        ║       Pozycja kursora na planszy                                               ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║ZWRACA:                                                                         ║
        ║    True, jeśli ruch jest możliwy, w przeciwnym razie False.                    ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║EN: Checks if the player's move is possible at the given position.              ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║PARAMETERS:                                                                     ║
        ║    cursor_pos (tuple):                                                         ║
        ║       The cursor position on the board                                         ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║RETURNS:                                                                        ║
        ║    True if the move is possible, otherwise False.                              ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║                                                             ID IN READ ME: 23  ║
        ╚════════════════════════════════════════════════════════════════════════════════╝
        '''
        x, y = cursor_pos
        if self.board[x][y] == " ":
            return True
        return False

    def prompt_for_initials(self):
        '''
        ╔════════════════════════════════════════════════════════════════════════════════╗
        ║PL: Prosi gracza o wpisanie inicjałów.                                          ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║PARAMETRY:                                                                      ║
        ║    Brak                                                                        ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║ZWRACA:                                                                         ║
        ║    Inicjały gracza (str).                                                      ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║EN: Asks the player to enter their initials.                                    ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║PARAMETERS:                                                                     ║
        ║    None                                                                        ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║RETURNS:                                                                        ║
        ║    The player's initials (str).                                                ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║                                                             ID IN READ ME: 24  ║
        ╚════════════════════════════════════════════════════════════════════════════════╝
        '''
        self.screen.addstr("\nWpisz swoje inicjały (3 litery): ")
        self.screen.refresh()
        initials = self.screen.getstr(0, len("Wpisz swoje inicjały (3 litery): "), 3).decode('utf-8')
        return initials
    
    def add_score_to_json(self, initials, time_elapsed):
        '''
        ╔════════════════════════════════════════════════════════════════════════════════╗
        ║PL: Dodaje wynik gracza do pliku JSON.                                          ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║PARAMETRY:                                                                      ║
        ║    initials (str):                                                             ║
        ║       Inicjały gracza                                                          ║
        ║    time_elapsed (int):                                                         ║
        ║       Czas gry w sekundach                                                     ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║ZWRACA:                                                                         ║
        ║    Nic, aktualizuje plik JSON z wynikami.                                      ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║EN: Adds the player's score to the JSON file.                                   ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║PARAMETERS:                                                                     ║
        ║    initials (str):                                                             ║
        ║       Player's initials                                                        ║
        ║    time_elapsed (int):                                                         ║
        ║       Game duration in seconds                                                 ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║RETURNS:                                                                        ║
        ║    None, updates the JSON file with scores.                                    ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║                                                             ID IN READ ME: 25  ║
        ╚════════════════════════════════════════════════════════════════════════════════╝
        '''
        level = self.get_difficulty_level_name()
        
        try:
            if os.path.exists(self.SCORES_FILE):
                with open(self.SCORES_FILE, "r") as file:
                    scores = json.load(file)
            else:
                scores = {"nowicjusz": [], "latwy": [], "sredni": [], "trudny": [], "niezwyciezony": []}

            score_data = {"nazwa": initials, "czas": self.format_time(time_elapsed), "char_player": self.current_side}
            scores[level].append(score_data)
            scores[level] = sorted(scores[level], key=lambda x: x['czas']) 

            with open(self.SCORES_FILE, "w") as file:
                json.dump(scores, file, indent=4)
        except IOError as e:
            print("Wystąpił błąd przy zapisie wyniku: ", e)
            
    def format_time(self, seconds):
        '''
        ╔════════════════════════════════════════════════════════════════════════════════╗
        ║PL: Formatuje czas z sekund na format hh:mm:ss.                                 ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║PARAMETRY:                                                                      ║
        ║    seconds (int):                                                              ║
        ║       Liczba sekund do sformatowania                                           ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║ZWRACA:                                                                         ║
        ║    Sformatowany czas jako string (str).                                        ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║EN: Formats time from seconds to hh:mm:ss format.                               ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║PARAMETERS:                                                                     ║
        ║    seconds (int):                                                              ║
        ║       Number of seconds to format                                              ║
        ╟────────────────────────────────────────────────────────────────────────────────╢
        ║RETURNS:                                                                        ║
        ║    Formatted time as a string (str).                                           ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║                                                             ID IN READ ME: 26  ║
        ╚════════════════════════════════════════════════════════════════════════════════╝
        '''
        return time.strftime('%H:%M:%S', time.gmtime(seconds))

if __name__ == "__main__":
    '''
    ╔════════════════════════════════════════════════════════════════════════════════╗
    ║PL: Główna funkcja uruchamiająca grę w kółko i krzyżyk.                         ║
    ╟────────────────────────────────────────────────────────────────────────────────╢
    ║PARAMETRY:                                                                      ║
    ║    stdscr:                                                                     ║
    ║       Standardowy ekran curses                                                 ║
    ╟────────────────────────────────────────────────────────────────────────────────╢
    ║ZWRACA:                                                                         ║
    ║    Brak.                                                                       ║
    ╠════════════════════════════════════════════════════════════════════════════════╣
    ║EN: Main function to run the Tic-Tac-Toe game.                                  ║
    ╟────────────────────────────────────────────────────────────────────────────────╢
    ║PARAMETERS:                                                                     ║
    ║    stdscr:                                                                     ║
    ║       Standard curses screen                                                   ║
    ╟────────────────────────────────────────────────────────────────────────────────╢
    ║RETURNS:                                                                        ║
    ║    None.                                                                       ║
    ╠════════════════════════════════════════════════════════════════════════════════╣
    ║                                                             ID IN READ ME: 01  ║
    ╚════════════════════════════════════════════════════════════════════════════════╝
    '''
    def main(stdscr):
        game = TicTacToe(stdscr)
        game.__main__()
    curses.wrapper(main)
