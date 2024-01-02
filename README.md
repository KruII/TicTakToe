# LANGUAGES:
<details>
<summary style="font-size: 24px">POLISH</summary>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
## Spis treści:
- [**<h3>Opis</h3>**](#opis)
- [**<h3>Klasy i Metody:</h3>**](#klasy-i-metody)
    - [**ID 01: Blok `if __name__ == "__main__"` w Grze w Kółko i Krzyżyk**](#id-01-blok-if-__name__--__main__-w-grze-w-kółko-i-krzyżyk)
    - [**ID 02: Klasa `TicTacToe`**](#id-02-klasa-tictactoe)
    - [**ID 03: Stałe Plików Konfiguracyjnych**](#id-03-stałe-plików-konfiguracyjnych)
    - [**ID 04: Mapowanie Poziomów Trudności**](#id-04-mapowanie-poziomów-trudności)
    - [**ID 05: Metoda `__init__(self, screen)`**](#id-05-metoda-__init__self-screen)
    - [**ID 06: Metoda `init_board(self)`**](#id-06-metoda-init_boardself)
    - [**ID 07: Metoda `load_settings(self)`**](#id-07-metoda-load_settingsself)
    - [**ID 08: Metoda `__main__(self)`**](#id-08-metoda-__main__self)
    - [**ID 09: Metoda `settings_menu(self)`**](#id-09-metoda-settings_menuself)
    - [**ID 10: Metoda `get_difficulty_level_name(self)`**](#id-10-metoda-get_difficulty_level_nameself)
    - [**ID 11: Metoda `save_settings(self)`**](#id-11-metoda-save_settingsself)
    - [**ID 12: Metoda `display_scores`**](#id-12-metoda-display_scores)
    - [**ID 13: Metoda `load_scores`**](#id-13-metoda-load_scores)
    - [**ID 14: Metoda `play_game`**](#id-14-metoda-play_game)
    - [**ID 15: Metoda `make_move`**](#id-15-metoda-make_move)
    - [**ID 16: Metoda `self.best_move`**](#id-16-metoda-best_move)
    - [**ID 17: Metoda `available_moves`**](#id-17-metoda-available_moves)
    - [**ID 18: Metoda `minimax`**](#id-18-metoda-minimax)
    - [**ID 19: Metoda `check_winner`**](#id-19-metoda-check_winner)
    - [**ID 20: Metoda `evaluate`**](#id-20-metoda-evaluate)
    - [**ID 21: Metoda `draw_board`**](#id-21-metoda-draw_board)
    - [**ID 22: Metoda `update_cursor`**](#id-22-metoda-update_cursor)
    - [**ID 23: Metoda `player_move`**](#id-23-metoda-player_move)
    - [**ID 24: Metoda `prompt_for_initials`**](#id-24-metoda-prompt_for_initials)
    - [**ID 25: Metoda `add_score_to_json`**](#id-25-metoda-add_score_to_json)
    - [**ID 26: Metoda `format_time`**](#id-26-metoda-format_time)

## Opis
Ten dokument zawiera szczegółowy opis wybranych elementów skryptu gry w kółko i krzyżyk, z naciskiem na ich funkcjonalności i rolę w kodzie.

## Klasy i Metody

### ID 01: Blok [`if __name__ == "__main__"` w Grze w Kółko i Krzyżyk](#id-01-blok-if-__name__--__main__-w-grze-w-kółko-i-krzyżyk-1)
```python
if __name__ == "__main__":
    # Sprawdza, czy skrypt jest uruchamiany bezpośrednio, a nie importowany jako moduł.

    def main(stdscr):
        # Definiuje funkcję 'main', która przyjmuje argument 'stdscr'.
        # 'stdscr' to standardowy ekran dostarczany przez bibliotekę 'curses',
        # służący jako główny punkt interakcji z interfejsem tekstowym.

        game = TicTacToe(stdscr)
        # Tworzy instancję klasy 'TicTacToe', przekazując 'stdscr' jako argument.
        # 'TicTacToe' to klasa gry, która zarządza logiką i wyświetlaniem gry.

        game.__main__()
        # Wywołuje główną metodę klasy 'TicTacToe', która uruchamia grę.

    curses.wrapper(main)
    # Wywołuje funkcję 'wrapper' z modułu 'curses', przekazując do niej funkcję 'main'.
    # Funkcja 'wrapper' zajmuje się inicjalizacją i kończeniem pracy z 'curses',
    # oraz przekazuje standardowy ekran 'stdscr' jako argument do funkcji 'main'.
```
- **Opis**: Ten fragment kodu jest typowym wzorcem używanym w języku Python, który pozwala na uruchomienie kodu tylko wtedy, gdy skrypt jest wykonywany jako program główny, a nie importowany jako moduł. W tym przypadku, uruchamia grę w kółko i krzyżyk.

- **Funkcje**:
    1. **Definicja funkcji `main`**: Funkcja `main(stdscr)` jest zdefiniowana wewnątrz bloku. Przyjmuje ona jeden argument `stdscr`, który jest standardowym ekranem dostarczonym przez bibliotekę `curses`.
    2. **Inicjalizacja gry**: Tworzy instancję klasy [`TicTacToe`](#id-02-klasa-tictactoe), przekazując `stdscr` jako argument. To pozwala na wykorzystanie funkcji biblioteki `curses` w obrębie klasy.
    3. **Uruchomienie głównej pętli gry**: Wywołuje metodę [`__main__`](#id-08-metoda-__main__self) na obiekcie `game`, co uruchamia główną pętlę gry.

- **Wykorzystanie `curses.wrapper`**:
    - `curses.wrapper(main)`: Funkcja `wrapper` z modułu `curses` jest używana do automatycznego zarządzania zasobami i poprawnego inicjowania/kończenia pracy z biblioteką `curses`. Zapewnia to, że wszystkie zasoby są poprawnie zwalniane, nawet jeśli w programie wystąpi błąd lub wyjątek.
    - Przekazuje standardowy ekran `stdscr` do funkcji `main`.

- **Zachowanie**: Ten blok kodu jest punktem wejścia do gry. Gwarantuje, że gra zostanie uruchomiona tylko wtedy, gdy skrypt jest bezpośrednio wykonywany, a nie importowany jako moduł w innym skrypcie.

- **Jak to działa**: Działa jak instrukcja startowa dla gry, inicjując środowisko `curses` i przechodząc do głównej logiki gry.

- **Proste podsumowanie - metafora**: Można to porównać do włączania konsoli do gier: ten fragment kodu "włącza" grę, ustawiając wszystkie niezbędne parametry i uruchamiając główny proces gry.


### ID 02: Klasa [`TicTacToe`](#id-02-klasa-tictactoe)
```python
class TicTacToe:
```
- **Opis**: Klasa [`TicTacToe`](#id-02-klasa-tictactoe) reprezentuje grę w kółko i krzyżyk. Jest to główna klasa, która zarządza logiką gry, w tym inicjalizacją planszy, rozgrywką oraz interakcją z użytkownikiem.

- **Funkcje**:
    1. [`__init__(self, screen)`](#id-05-metoda-__init__self-screen): Konstruktor klasy, który inicjuje nową grę. Ustawia ekran gry, inicjuje planszę do gry, wczytuje ustawienia i przygotowuje grę do rozpoczęcia.
    2. [`init_board(self)`](#id-06-metoda-init_boardself): Tworzy początkowy stan pustej planszy gry.
    3. [`load_settings(self)`](#id-07-metoda-load_settingsself): Wczytuje ustawienia gry z pliku konfiguracyjnego. Ustawia domyślne wartości, jeśli plik konfiguracyjny nie istnieje.
    4. [`__main__(self)`](#id-08-metoda-__main__self): Główna pętla gry, wyświetlająca menu i obsługująca akcje użytkownika.
    5. Inne metody: Kluczowe metody do obsługi rozgrywki, interakcji z użytkownikiem oraz zarządzania stanem gry.

- **Zachowanie**: Klasa [`TicTacToe`](#id-02-klasa-tictactoe) działa jako centrum zarządzania grą, integrując różne aspekty rozgrywki w kółko i krzyżyk. Zapewnia płynną i spójną rozgrywkę poprzez zarządzanie stanem gry i reagowanie na działania użytkownika.

- **Jak to działa**: Klasa [`TicTacToe`](#id-02-klasa-tictactoe) jest jak dyrygent orkiestry, który kieruje różnymi elementami gry - od interfejsu użytkownika, przez logikę gry, aż po wyświetlanie stanu gry na ekranie. Każdy aspekt gry jest skoordynowany, aby zapewnić harmonijną i angażującą rozgrywkę.

- **Proste podsumowanie - metafora**: Można porównać klasę [`TicTacToe`](#id-02-klasa-tictactoe) do kapitana statku, który nawiguje po skomplikowanych wodach gry w kółko i krzyżyk, prowadząc gracza przez różne etapy rozgrywki, od początku do końca.

### ID 03: Stałe Plików Konfiguracyjnych
```python
SCORES_FILE = "wyniki_kolko_i_krzyzyk.json"
SETTINGS_FILE = "ustawienia_kolko_i_krzyzyk.json"
```
- **Opis**: W klasie [`TicTacToe`](#id-02-klasa-tictactoe) zdefiniowane są stałe, które odnoszą się do nazw plików konfiguracyjnych używanych w grze. Te stałe ułatwiają zarządzanie i dostęp do kluczowych plików, takich jak plik zapisu wyników gry i plik ustawień.

- **Funkcje**:
    1. `SCORES_FILE = "wyniki_kolko_i_krzyzyk.json"`: Nazwa pliku, w którym zapisywane są wyniki gry. Używany do przechowywania wyników gry, takich jak nazwe użytkownika, czas i symbol jakim grał,
    2. `SETTINGS_FILE = "ustawienia_kolko_i_krzyzyk.json"`: Nazwa pliku konfiguracyjnego, w którym przechowywane są ustawienia gry. Zawiera informacje takie jak poziom trudności i preferowany symbol gracza (X lub O).

- **Zachowanie**: Te stałe zapewniają spójny i centralny dostęp do ważnych plików konfiguracyjnych, co ułatwia zarządzanie stanem gry i ustawieniami. Zamiast twardo zakodowywać nazwy plików w różnych miejscach kodu, te stałe pozwalają na łatwe modyfikacje i dostosowania.

- **Jak to działa**: Stałe `SCORES_FILE` i `SETTINGS_FILE` działają jak etykiety na słoikach, pozwalając programowi łatwo znaleźć i używać odpowiednich plików konfiguracyjnych. Gdy gra potrzebuje zapisać wynik lub wczytać ustawienia, odwołuje się do tych stałych, aby uzyskać odpowiednie nazwy plików.

- **Proste podsumowanie - metafora**: Można myśleć o tych stałych jako o skrótach na pulpicie komputera, które prowadzą do ważnych dokumentów. Zamiast szukać dokumentów w całym systemie, wystarczy kliknąć na skrót, aby szybko i sprawnie uzyskać dostęp do potrzebnych informacji.

### ID 04: Mapowanie Poziomów Trudności
```python
LEVELS = {
           1: "nowicjusz",          
           2: "latwy",              
           3: "sredni",             
           4: "trudny",             
           5: "niezwyciezony"       
         }
```
- **Opis**: W klasie [`TicTacToe`](#id-02-klasa-tictactoe) zdefiniowane jest mapowanie poziomów trudności gry. Ta funkcjonalność umożliwia łatwe odniesienie się do różnych poziomów trudności przy pomocy nazw, zamiast korzystać z mniej intuicyjnych wartości numerycznych.

- **Funkcje**:
    1. `LEVELS = {1: "nowicjusz", 2: "latwy", 3: "sredni", 4: "trudny", 5: "niezwyciezony"}`: Słownik w Pythonie, który przypisuje każdemu poziomowi trudności (reprezentowanemu przez liczbę) odpowiadającą mu nazwę. Ułatwia to zrozumienie i obsługę różnych poziomów trudności w kodzie gry.
   
- **Zachowanie**: Dzięki temu mapowaniu, kod gry staje się bardziej zrozumiały i łatwiejszy w utrzymaniu. Zamiast wielokrotnego odwoływania się do wartości numerycznych, programiści mogą używać czytelnych nazw, co sprawia, że kod jest bardziej przystępny.

- **Jak to działa**: Gdy gra wymaga określenia poziomu trudności (np. przy wyborze ustawień przez użytkownika lub podczas inicjalizacji nowej gry), używa słownika `LEVELS` do przypisania lub odczytu odpowiedniej nazwy poziomu trudności. Na przykład, `LEVELS[3]` zwróci `"sredni"`, co jest bardziej zrozumiałe niż sama liczba `3`.

- **Proste podsumowanie - metafora**: Można porównać ten słownik do przewodnika turystycznego, który tłumaczy lokalne nazwy miejsc na język zrozumiały dla turystów. Zamiast zastanawiać się, co oznacza każda liczba, użytkownicy i programiści otrzymują klarowne i opisowe nazwy, które od razu informują o poziomie trudności.

### ID 05: Metoda [`__init__(self, screen)`](#id-05-metoda-__init__self-screen)
```python
def __init__(self, screen):
    # Przypisanie przekazanego argumentu 'screen' do zmiennej instancji 'self.screen'.
    # 'screen' odnosi się do obiektu interfejsu użytkownika, okna terminala.
    self.screen = screen

    # Ustawienie rozmiaru planszy gry na 3 (np. 3x3 dla gry w kółko i krzyżyk).
    self.board_size = 3

    # Inicjalizacja planszy gry poprzez wywołanie metody 'self.init_board()'.
    # Ta metoda tworzy początkowy układ planszy.
    self.board = self.init_board()

    # Wczytanie ustawień gry (np. z pliku konfiguracyjnego) i ustawienie bieżącego poziomu.
    # Jeśli ustawienie 'level' nie zostanie znalezione, domyślnie ustawia poziom na 1.
    self.current_level = self.load_settings().get("level", 1)

    # Wczytanie ustawień gry i ustawienie bieżącej strony (np. 'X' lub 'O' w grze w kółko i krzyżyk).
    # Jeśli ustawienie 'side' nie zostanie znalezione, domyślnie ustawia stronę na 'X'.
    self.current_side = self.load_settings().get("side", "X")

    # Ustawienie gracza AI na przeciwną stronę niż bieżąca strona użytkownika.
    # Jeśli użytkownik gra jako 'X', AI będzie grać jako 'O', i odwrotnie.
    self.ai_player = 'O' if self.current_side == 'X' else 'X'

    # Ustawienie zmiennej 'self.winner' na wartość "Remis".
    # Ta zmienna jest używana do przechowywania informacji o zwycięzcy gry.
    self.winner = "Remis"
```
- **Opis**: Metoda [`__init__`](#id-05-metoda-__init__self-screen) to konstruktor klasy [`TicTacToe`](#id-02-klasa-tictactoe), odpowiedzialny za inicjalizację podstawowych elementów gry, takich jak plansza, poziom trudności, strona gracza i inne ustawienia.

- **Parametry**:
    - `screen`: Obiekt ekranu, pochodzący z biblioteki `curses`, który służy do wyświetlania treści gry w terminalu. Jest to główny interfejs do interakcji z użytkownikiem.

- **Funkcje**:
    1. `self.screen = screen`: Przypisanie obiektu ekranu do zmiennej instancji klasy.
    2. `self.board_size = 3`: Ustawienie rozmiaru planszy na 3x3.
    3. `self.board = self.init_board()`: Inicjalizacja pustej planszy gry.
    4. `self.current_level` i `self.current_side`: Wczytanie lub ustawienie domyślnych wartości poziomu trudności i strony gracza.
    5. `self.ai_player`: Określenie znaku reprezentującego sztuczną inteligencję w grze.
    6. `self.winner`: Inicjalizacja zmiennej do przechowywania informacji o zwycięzcy gry.

- **Zachowanie**: Metoda [`__init__`](#id-05-metoda-__init__self-screen) przygotowuje wszystkie niezbędne elementy do rozpoczęcia gry, zapewniając łatwą konfigurację i gotowość do uruchomienia rozgrywki.

- **Jak to działa**: Ta metoda działa jak proces "rozpakowywania i ustawiania" nowej gry planszowej, gdzie wszystkie komponenty są przygotowywane do pierwszej rozgrywki.

- **Proste podsumowanie - metafora**: Można porównać metodę [`__init__`](#id-05-metoda-__init__self-screen) do scenarzysty filmowego, który przygotowuje scenę, ustawia aktorów i planuje scenariusz przed rozpoczęciem kręcenia filmu. Podobnie, [`__init__`](#id-05-metoda-__init__self-screen) ustawia wszystkie elementy gry, zanim rozpocznie się właściwa akcja.

### ID 06: Metoda [`init_board(self)`](#id-06-metoda-init_boardself)
```python
def init_board(self):
    # Zwraca nową planszę gry jako dwuwymiarową listę (listę list).

    return [[" " for _ in range(self.board_size)] for _ in range(self.board_size)]
```
- **Opis**: Metoda [`init_board`](#id-06-metoda-init_boardself) w klasie [`TicTacToe`](#id-02-klasa-tictactoe) służy do inicjalizacji początkowej planszy gry w kółko i krzyżyk. Metoda ta jest elastyczna i pozwala na tworzenie planszy o różnych rozmiarach, zależnie od potrzeb gry.

- **Zwraca**: Dwuwymiarowa lista, reprezentująca planszę gry. Rozmiar planszy jest określony przez zmienną [`self.board_size`](#id-05-metoda-__init__self-screen), co pozwala na elastyczne dostosowanie jej rozmiarów.

- **Funkcje**:
    1. **Tworzenie elastycznej planszy**: Metoda wykorzystuje wartość [`self.board_size`](#id-05-metoda-__init__self-screen) do utworzenia planszy o odpowiednim rozmiarze. Wykorzystuje do tego list comprehension w Pythonie, tworząc listę list, gdzie każda podlista reprezentuje jeden rząd planszy.
    2. **Inicjalizacja pustych pól**: Niezależnie od rozmiaru, każde pole na planszy jest inicjalizowane jako puste (reprezentowane przez pusty ciąg znaków), co oznacza gotowość do rozpoczęcia gry.

- **Zachowanie**: Metoda ta jest wywoływana na początku każdej gry, zapewniając, że plansza jest odpowiednio przygotowana i czysta. Jest to kluczowe dla rozpoczęcia każdej nowej rozgrywki.

- **Jak to działa**: Metoda [`init_board`](#id-06-metoda-init_boardself) działa jak przygotowanie pola do gry. Niezależnie od wybranego rozmiaru, tworzy ona pustą przestrzeń, która jest niezbędna do rozpoczęcia i prowadzenia gry.

- **Proste podsumowanie - metafora**: Można porównać [`init_board`](#id-06-metoda-init_boardself) do przygotowania płótna malarskiego przez artystę. Tak jak artysta wybiera płótno o odpowiednim rozmiarze dla swojego dzieła, [`init_board`](#id-06-metoda-init_boardself) przygotowuje "płótno gry" o wymiarach dopasowanych do preferencji graczy lub wymagań gry.

### ID 07: Metoda [`load_settings(self)`](#id-07-metoda-load_settingsself)
```python
def load_settings(self):
    try:
        # Blok 'try' służy do obsługi wyjątków, które mogą wystąpić podczas otwierania i czytania pliku.

        with open(self.SETTINGS_FILE, "r") as file:
            # Używając 'with', otwieramy plik określony w 'self.SETTINGS_FILE' w trybie czytania ('r').
            # 'with' zapewnia, że plik zostanie prawidłowo zamknięty po zakończeniu bloku kodu.

            settings = json.load(file)
            # Za pomocą funkcji 'json.load' wczytujemy dane JSON z pliku.
            # Dane są konwertowane na słownik Pythona i przypisywane do zmiennej 'settings'.

            return settings
            # Zwracamy wczytane ustawienia.

    except (FileNotFoundError, json.JSONDecodeError):
        # Obsługa wyjątków: Jeśli plik nie zostanie znaleziony (FileNotFoundError)
        # lub jeśli zawiera niepoprawny format JSON (JSONDecodeError),

        return {"level": 1, "side": "X"}
        # zwracamy domyślne ustawienia gry.
```
- **Opis**: Metoda [`load_settings`](#id-07-metoda-load_settingsself) w klasie [`TicTacToe`](#id-02-klasa-tictactoe) jest odpowiedzialna za wczytywanie ustawień gry z pliku konfiguracyjnego. Zapewnia ona personalizację rozgrywki, umożliwiając graczowi zapis wybór poziomu trudności i strony (X lub O).

- **Zwraca**: Słownik z ustawieniami gry. W przypadku problemów z odczytem pliku, metoda zwraca domyślne ustawienia.

- **Funkcje**:
    1. **Otwarcie pliku konfiguracyjnego**: Metoda próbuje otworzyć plik konfiguracyjny określony w [`self.SETTINGS_FILE`](#id-03-stałe-plików-konfiguracyjnych), korzystając z modułu `json`.
    2. **Wczytywanie ustawień**: Jeśli odczyt się powiedzie, zwraca słownik zawierający ustawienia gry.
    3. **Obsługa błędów**: W przypadku błędów, takich jak `FileNotFoundError` (plik nie istnieje) lub `json.JSONDecodeError` (plik nie jest poprawnym dokumentem JSON), metoda zwraca domyślny słownik ustawień.
    4. **Ustawienia domyślne**: W przypadku wystąpienia wyjątku, zwracane są domyślne ustawienia: `{"level": 1, "side": "X"}`, co oznacza początkowy poziom trudności "nowicjusz" i grę jako "X".

- **Zachowanie**: Metoda [`load_settings`](#id-07-metoda-load_settingsself) zapewnia, że gra zawsze rozpocznie się z aktualnymi ustawieniami, niezależnie od tego, czy są one wczytane z pliku, czy ustawione na wartości domyślne. Jest to kluczowe dla spójności doświadczenia użytkownika.

- **Jak to działa**: Metoda [`load_settings`](#id-07-metoda-load_settingsself) funkcjonuje jak mechanizm wczytywania preferencji użytkownika przed rozpoczęciem gry. Podobna do wczytywania zapisanych ustawień w aplikacji, zapewnia kontynuację z poprzednio wybranymi opcjami.

- **Proste podsumowanie - metafora**: Można porównać metodę [`load_settings`](#id-07-metoda-load_settingsself) do ustawiania preferencji w telewizorze. Tak jak wybieramy ulubiony kanał czy regulujemy jasność ekranu, tak [`load_settings`](#id-07-metoda-load_settingsself) wczytuje preferowane ustawienia gry, aby dostosować doświadczenie do oczekiwań gracza.

### ID 08: Metoda [`__main__(self)`](#id-08-metoda-__main__self)
```python
def __main__(self):
    curses.curs_set(0)
    # Wyłącza widoczność kursora w terminalu, co jest przydatne dla estetyki interfejsu użytkownika.

    self.screen.clear()
    # Czyści ekran, usuwając wszelkie wcześniej wyświetlane treści.

    self.screen.refresh()
    # Odświeża ekran, aby zastosować czyszczenie i wyświetlić pusty ekran.

    menu_items = ["Graj", "Tablica wyników", "Ustawienia", "Wyjdź z gry"]
    # Definiuje listę opcji, które będą wyświetlane w menu.

    current_selection = 0
    # Ustawia początkowy wybór w menu na pierwszą opcję ("Graj").

    # Główna pęgla
    while True:
        self.screen.clear()
        # Ponownie czyści ekran na początku każdej iteracji pętli, aby zapobiec nakładaniu się treści.

        height, width = self.screen.getmaxyx()
        # Pobiera aktualne wymiary ekranu, aby odpowiednio wyśrodkować elementy menu.

        for index, item in enumerate(menu_items):
            x = width // 2 - len(item) // 2
            y = height // 2 - len(menu_items) // 2 + index
            # Oblicza pozycję, w której powinna być wyświetlona każda opcja menu.

            if index == current_selection:
                self.screen.attron(curses.A_REVERSE)
            # Podświetla aktualnie wybraną opcję (odwraca kolory).

            self.screen.addstr(y, x, item)
            # Wyświetla opcję menu na ekranie.

            if index == current_selection:
                self.screen.attroff(curses.A_REVERSE)
            # Wyłącza podświetlenie po wyświetleniu opcji.

        key = self.screen.getch()
        # Oczekuje na naciśnięcie klawisza przez użytkownika.

        # Logika nawigacji w menu:
        if key in [curses.KEY_UP, ord('w')] and current_selection > 0:
            current_selection -= 1
            # Przesuwa wybór w górę, jeśli naciśnięto klawisz w górę lub 'w'.

        elif key in [curses.KEY_DOWN, ord('s')] and current_selection < len(menu_items) - 1:
            current_selection += 1
            # Przesuwa wybór w dół, jeśli naciśnięto klawisz w dół lub 's'.

        elif key == curses.KEY_ENTER or key in [10, 13]:
            choice = menu_items[current_selection]
            # Pobiera aktualnie wybraną opcję menu, jeśli naciśnięto Enter.

            # Wykonuje akcję związaną z wybraną opcją:
            if choice == "Wyjdź z gry":
                break
                # Kończy pętlę, zamykając program.

            elif choice == "Ustawienia":
                self.settings_menu()
                # Wywołuje metodę odpowiedzialną za wyświetlenie menu ustawień.

            elif choice == "Tablica wyników":
                self.display_scores()
                # Wyświetla tablicę wyników.

            elif choice == "Graj":
                self.play_game()
                # Rozpoczyna nową grę.

        self.screen.refresh()
        # Odświeża ekran na końcu każdej iteracji, aby wyświetlić zmiany.
```

- **Opis**: Metoda [`__main__`](#id-08-metoda-__main__self) jest centrum zarządzania interfejsem użytkownika gry w kółko i krzyżyk. Odpowiada za wyświetlanie menu głównego, reagowanie na wybory użytkownika i uruchamianie odpowiednich funkcji gry.

- **Funkcje**:
    1. `curses.curs_set(0)`: Ukrywa kursor w terminalu dla lepszej estetyki.
    2. `self.screen.clear()`: Czyści ekran terminala, przygotowując go do wyświetlenia nowych informacji.
    3. `self.screen.refresh()`: Odświeża ekran, aby aktualne informacje były widoczne.
    4. `menu_items`: Lista zawierająca opcje menu.
    5. `current_selection`: Zmienna śledząca, która opcja menu jest aktualnie wybrana.
    6. Pętla `while True`: Główna pętla programu, która działa do momentu zakończenia gry przez użytkownika.
    7. `self.screen.getch()`: Oczekuje na naciśnięcie klawisza przez użytkownika i zwraca jego kod.
    8. Logika decyzyjna: Wybiera odpowiednią akcję w zależności od wyboru użytkownika w menu.

- **Zachowanie**: Podczas działania metody [`__main__`](#id-08-metoda-__main__self), użytkownik jest prezentowany z czystym, intuicyjnym interfejsem, gdzie może nawigować po menu i wybierać opcje. Program dynamicznie reaguje na każde działanie użytkownika, zapewniając płynność i responsywność interakcji.

- **Jak to działa**: Metoda [`__main__`](#id-08-metoda-__main__self) działa jak interaktywny przewodnik po grze. Na początku przygotowuje "scenę" poprzez wyczyszczenie ekranu i ukrycie kursora. Następnie prezentuje użytkownikowi szereg opcji do wyboru, z których każda prowadzi do innej ścieżki działania - od rozpoczęcia nowej gry, przez przeglądanie wyników, po zmianę ustawień i wyjście z gry. Wybory użytkownika są nieustannie monitorowane, a reakcje programu są szybkie i zgodne z oczekiwaniami.

- **Proste podsumowanie - metafora**: Można sobie wyobrazić metodę [`__main__`](#id-08-metoda-__main__self) jako kontrolera telewizyjnego, gdzie każdy przycisk to inna opcja menu, a naciśnięcie go przekierowuje nas do nowego "kanału" rozrywki. Tak jak w przypadku pilota, użytkownik ma pełną kontrolę nad tym, co chce zobaczyć i robić, a zmiany następują natychmiastowo po jego decyzji.


### ID 09: Metoda [`settings_menu(self)`](#id-09-metoda-settings_menuself)
```python
def settings_menu(self):
    levels = ["nowicjusz", "latwy", "sredni", "trudny", "niezwyciezony"]
    sides = ['X', 'O']
    # Definiuje listy możliwych poziomów trudności i stron do wyboru przez użytkownika.

    level_index = levels.index(self.get_difficulty_level_name())
    side_index = sides.index(self.current_side)
    # Ustawia początkowe indeksy na podstawie aktualnych ustawień gry.

    # Pętla menu ustawień
    while True:
        self.screen.clear()
        # Czyści ekran w celu przygotowania do wyświetlenia opcji ustawień.

        self.screen.addstr(0, 0, "Ustawienia:\n")
        self.screen.addstr(2, 0, "Wybierz poziom trudności:\n")
        # Wyświetla tytuł i opcje poziomu trudności.

        for idx, level in enumerate(levels):
            if idx == level_index:
                self.screen.attron(curses.A_REVERSE)
            # Podświetla aktualnie wybrany poziom trudności.

            self.screen.addstr(f"{level}\n")
            # Wyświetla każdy poziom trudności.

            if idx == level_index:
                self.screen.attroff(curses.A_REVERSE)
            # Wyłącza podświetlenie po wyświetleniu opcji.

        self.screen.addstr(10, 0, "Wybierz stronę:\n")
        # Wyświetla opcje wyboru strony.

        for idx, side in enumerate(sides):
            if idx == side_index:
                self.screen.attron(curses.A_REVERSE)
            self.screen.addstr(f"{side}\n")
            # Podobnie, wyświetla i podświetla opcje strony.

            if idx == side_index:
                self.screen.attroff(curses.A_REVERSE)

        self.screen.refresh()
        # Odświeża ekran, aby wyświetlić wszystkie opcje.

        key = self.screen.getch()
        # Oczekuje na wejście użytkownika.

        # Logika nawigacji i wyboru w menu:
        if key in [curses.KEY_UP, ord('w')]:
            # Poruszanie się w górę po menu
            if level_index > 0:
                level_index -= 1
            else:
                side_index = (side_index - 1) % len(sides)
        elif key in [curses.KEY_DOWN, ord('s')]:
            # Poruszanie się w dół po menu
            if level_index < len(levels) - 1:
                level_index += 1
            else:
                side_index = (side_index + 1) % len(sides)
        elif key in [curses.KEY_LEFT, ord('a')]:
            # Zmiana strony na poprzednią
            side_index = (side_index - 1) % len(sides)
        elif key in [curses.KEY_RIGHT, ord('d')]:
            # Zmiana strony na następną
            side_index = (side_index + 1) % len(sides)
        elif key == curses.KEY_ENTER or key in [10, 13]:
            # Zapisanie ustawień po naciśnięciu Enter
            break

    self.current_level, self.current_side = level_index + 1, sides[side_index]
    # Aktualizuje ustawienia gry na podstawie wybranych opcji.

    self.save_settings()
    # Zapisuje zaktualizowane ustawienia do pliku konfiguracyjnego.
```
- **Opis**: Metoda [`settings_menu`](#id-09-metoda-settings_menuself) jest odpowiedzialna za prezentowanie i obsługę menu ustawień gry. Pozwala użytkownikowi wybrać poziom trudności oraz decydować, czy chce grać jako "X" czy "O".

- **Funkcje**:
    1. `levels` i `sides`: Listy zawierające opcje dla poziomu trudności i wyboru strony.
    2. `level_index` i `side_index`: Zmienne śledzące, które opcje są obecnie wybrane.
    3. Pętla `while True`: Główna pętla menu ustawień, pozwalająca na interaktywne nawigowanie i wybieranie opcji.
    4. `self.screen.clear()`: Czyści ekran przed każdym wyświetleniem opcji.
    5. `self.screen.addstr()`: Wyświetla tekst na ekranie, używane do prezentacji opcji ustawień.
    6. `self.screen.attron()` i `self.screen.attroff()`: Podświetlenie aktualnie wybranej opcji.
    7. `self.screen.getch()`: Oczekuje na wejście użytkownika.
    8. Logika nawigacyjna: Reaguje na naciśnięcia klawiszy, umożliwiając zmianę wyborów.
    9. [`self.save_settings()`](#id-11-metoda-save_settingsself): Zapisuje nowe ustawienia po wybraniu.

- **Zachowanie**: Interfejs ustawień jest prosty i intuicyjny, oferując użytkownikowi wyraźne opcje do wyboru. Program reaguje na każdą akcję użytkownika, zapewniając płynne doświadczenie podczas konfiguracji ustawień gry.

- **Jak to działa**: Metoda [`settings_menu`](#id-09-metoda-settings_menuself) funkcjonuje jak interaktywny panel sterowania. Użytkownik jest prowadzony przez różne opcje, które może modyfikować według własnych preferencji. Wybór każdej opcji jest natychmiastowo odzwierciedlany w interfejsie, dając użytkownikowi pełną kontrolę nad ustawieniami gry.

- **Proste podsumowanie - metafora**: Można porównać metodę [`settings_menu`](#id-09-metoda-settings_menuself) do obsługi zdalnego sterowania klimatyzacją - użytkownik ma możliwość zmiany temperatury (poziomu trudności) i kierunku nawiewu (strony gry), aby dostosować otoczenie do własnych potrzeb.

### ID 10: Metoda [`get_difficulty_level_name(self)`](#id-10-metoda-get_difficulty_level_nameself)
```python
def get_difficulty_level_name(self):
    # Zwraca nazwę poziomu trudności opartą na aktualnej wartości 'self.current_level'.

    return self.LEVELS.get(self.current_level, "nieznany")
    # Używa metody słownikowej 'get' do pobrania nazwy poziomu trudności z 'self.LEVELS',
    # gdzie 'self.current_level' jest kluczem.
    # Jeśli 'self.current_level' nie znajduje się w słowniku 'self.LEVELS', 
    # zwraca domyślną wartość "nieznany".
```
- **Opis**: Metoda [`get_difficulty_level_name`](#id-10-metoda-get_difficulty_level_nameself) w klasie [`TicTacToe`](#id-02-klasa-tictactoe) służy do przekształcania numerycznego poziomu trudności gry na zrozumiałą nazwę. Ułatwia to interakcję z użytkownikiem, prezentując poziomy trudności w bardziej przystępnej formie.

- **Zwraca**: Nazwę poziomu trudności jako ciąg znaków (string). Jeśli aktualny poziom trudności nie istnieje w zdefiniowanym słowniku, zwraca `"nieznany"`.

- **Funkcje**:
    1. **Mapowanie poziomu trudności**: Metoda korzysta ze słownika [`self.LEVELS`](#id-04-mapowanie-poziomów-trudności), który przypisuje każdej liczbie reprezentującej poziom trudności jego nazwę.
    2. **Bezpieczne odwołanie**: Używa metody `get` na słowniku, co zapewnia, że nawet jeśli dany poziom trudności nie jest zdefiniowany, metoda nie spowoduje błędu, lecz zwróci wartość domyślną `"nieznany"`.

- **Zachowanie**: Metoda [`get_difficulty_level_name`](#id-10-metoda-get_difficulty_level_nameself) zapewnia czytelność i użyteczność interfejsu użytkownika, prezentując poziomy trudności w sposób zrozumiały, zamiast opierać się na surowych wartościach numerycznych.

- **Jak to działa**: Działa to podobnie do tłumacza, który przekłada kod lub numer na język zrozumiały dla ludzi. Zamiast pokazywać użytkownikowi niejasne liczby, metoda prezentuje klarowne i zrozumiałe etykiety.

- **Proste podsumowanie - metafora**: Można porównać tę metodę do przewodnika turystycznego, który tłumaczy lokalne nazwy na język zrozumiały dla turystów. Zamiast kazać turystom zgadywać, co oznaczają poszczególne słowa, przewodnik dostarcza łatwych do zrozumienia tłumaczeń.

### ID 11: Metoda [`save_settings(self)`](#id-11-metoda-save_settingsself)
```python
def save_settings(self):
    # Używając 'with', otwieramy plik określony w 'self.SETTINGS_FILE' w trybie zapisu ('w'). 
    # 'with' zapewnia, że plik zostanie prawidłowo zamknięty po zakończeniu bloku kodu.
    with open(self.SETTINGS_FILE, "w") as file:

        # Używając funkcji 'json.dump', zapisujemy słownik z aktualnymi ustawieniami gry do pliku.
        # Słownik zawiera klucze 'level' i 'side', które odnoszą się do atrybutów obiektu (np. self.current_level, self.current_side).
        # Argument 'indent=4' powoduje sformatowanie zapisanych danych JSON w bardziej czytelny, sformatowany sposób.
        json.dump({"level": self.current_level, "side": self.current_side}, file, indent=4)
```
- **Opis**: Metoda [`save_settings(self)`](#id-11-metoda-save_settingsself) jest odpowiedzialna za zapisywanie bieżących ustawień gry do pliku konfiguracyjnego. Dzięki temu użytkownicy mogą zachować swoje preferencje dotyczące poziomu trudności i wybranej strony na przyszłe sesje gry.

- **Zwraca**: Metoda nie zwraca wartości, jej głównym zadaniem jest zapis ustawień do pliku.

- **Funkcje**:
    1. **Otwarcie pliku konfiguracyjnego**: Metoda używa ścieżki pliku określonej w [`self.SETTINGS_FILE`](#id-03-stałe-plików-konfiguracyjnych) do otwarcia pliku konfiguracyjnego.
    2. **Zapis ustawień do pliku**: Aktualne ustawienia gry są konwertowane na format JSON i zapisywane w pliku. Dzięki temu ustawienia mogą być łatwo wczytane przy kolejnym uruchomieniu gry.
    3. **Aktualizacja pliku konfiguracyjnego**: Jeśli plik już istnieje, jest nadpisywany nowymi ustawieniami. W przeciwnym razie tworzony jest nowy plik.

- **Zachowanie**: Metoda [`save_settings(self)`](#id-11-metoda-save_settingsself) zapewnia, że wszystkie zmiany dokonane przez użytkownika w ustawieniach gry zostaną zachowane do przyszłego użycia, co umożliwia personalizację doświadczenia gry.

- **Jak to działa**: Funkcjonuje podobnie do opcji "Zapisz ustawienia" w wielu aplikacjach, gdzie użytkownik może dostosować preferencje, a aplikacja pamięta te wybory na przyszłość.

- **Proste podsumowanie - metafora**: Można to porównać do zapisywania ważnych notatek w dzienniku. Tak jak notatki pomagają pamiętać kluczowe informacje na później, tak [`save_settings(self)`](#id-11-metoda-save_settingsself) przechowuje ustawienia gry dla przyszłych sesji.

### ID 12: Metoda [`display_scores`](#id-12-metoda-display_scores)
```python
def display_scores(self):
    scores = self.load_scores()
    # Wczytuje wyniki gry z pliku.
    self.screen.clear()
    # Czyści ekran, przygotowując go do wyświetlenia nowych informacji.

    self.screen.addstr(0, 0, "Tablica wyników:\n")
    # Dodaje nagłówek "Tablica wyników" na początku ekranu.

    for level, level_scores in scores.items():
        # Iteruje przez wszystkie poziomy trudności i ich wyniki w słowniku wyników.

        self.screen.addstr(f"Poziom {level.capitalize()}:\n")
        # Wyświetla nazwę poziomu trudności z pierwszą literą zamienioną na wielką.

        top_scores = sorted(level_scores, key=lambda x: x['czas'])[:5]
        # Sortuje wyniki na danym poziomie trudności według czasu, biorąc 5 najlepszych.

        for idx, score in enumerate(top_scores, start=1):
            # Iteruje przez 5 najlepszych wyników, numerując je od 1.

            self.screen.addstr(f"{idx}. {score['nazwa']} - {score['czas']} - {score['char_player']}\n")
            # Wyświetla każdy wynik w formacie "numer. nazwa gracza - czas - znak gracza".

        self.screen.addstr("\n")
        # Dodaje pustą linię po każdym poziomie trudności dla lepszej czytelności.

    self.screen.refresh()
    # Odświeża ekran, aby wyświetlić wszystkie dodane informacje.

    self.screen.getch()
    # Oczekuje na naciśnięcie klawisza przez użytkownika, zanim powróci do poprzedniego menu.
```
- **Opis**: Metoda [`display_scores`](#id-12-metoda-display_scores) w grze w kółko i krzyżyk jest odpowiedzialna za wyświetlanie tablicy wyników na ekranie. Dzięki niej gracze mogą zobaczyć dotychczasowe wyniki, co dodaje element rywalizacji i śledzenia postępów w grze.

- **Zwraca**: Metoda nie zwraca żadnej wartości, ale efektem jej działania jest wyświetlenie wyników gry na ekranie użytkownika.

- **Funkcje**:
    1. **Wczytywanie wyników**: Metoda używa funkcji [`load_scores`](#id-13-metoda-load_scores) do wczytania wyników gry z pliku konfiguracyjnego.
    2. **Prezentacja wyników**: Wyniki są formatowane i wyświetlane w przystępny sposób na ekranie, zazwyczaj w postaci listy.
    3. **Interakcja z użytkownikiem**: Użytkownik może przeglądać wyniki.

- **Zachowanie**: Metoda [`display_scores`](#id-12-metoda-display_scores) służy jako narzędzie do prezentacji wyników, dodając do gry aspekt rywalizacji i umożliwiając graczom śledzenie swoich osiągnięć.

- **Jak to działa**: Podobnie do tablicy wyników w sportach czy na platformach gier, [`display_scores`](#id-12-metoda-display_scores) prezentuje zestawienie osiągnięć graczy, umożliwiając łatwe śledzenie postępów i porównywanie wyników.

- **Proste podsumowanie - metafora**: Można porównać tę metodę do billboardu z najlepszymi wynikami w grze arcade, gdzie gracze mogą zobaczyć, kto osiągnął najwyższe wyniki, co motywuje do dalszej gry i poprawiania swoich rezultatów.

### ID 13: Metoda [`load_scores`](#id-13-metoda-load_scores)
```python
def load_scores(self):
    # Sprawdza, czy plik z wynikami istnieje w systemie plików.
    if os.path.exists(self.SCORES_FILE):
        # Jeśli plik istnieje, otwiera go w trybie do czytania ('r').

        with open(self.SCORES_FILE, "r") as file:
            # Używając 'with', otwiera plik i zapewnia, że zostanie on prawidłowo zamknięty po zakończeniu bloku kodu.

            scores = json.load(file)
            # Wczytuje wyniki z pliku i konwertuje je z formatu JSON na strukturę danych Pythona (prawdopodobnie słownik).

    else:
        # Jeśli plik z wynikami nie istnieje, tworzy domyślny słownik wyników.
        scores = {"nowicjusz": [], "latwy": [], "sredni": [], "trudny": [], "niezwyciezony": []}
        # Słownik zawiera klucze odpowiadające różnym poziomom trudności,
        # a każdy z nich ma przypisaną pustą listę, oznaczającą brak wyników.

    return scores
    # Zwraca słownik wyników.
```
- **Opis**: Metoda [`load_scores`](#id-13-metoda-load_scores) jest odpowiedzialna za wczytywanie wyników gry z pliku konfiguracyjnego. Umożliwia to śledzenie postępów i wyników graczy na różnych poziomach trudności.

- **Zwraca**: Słownik z wynikami gry, podzielonymi na poszczególne poziomy trudności.

- **Funkcje**:
    1. **Sprawdzenie istnienia pliku**: Metoda najpierw sprawdza, czy plik wyników ([`self.SCORES_FILE`](#id-03-stałe-plików-konfiguracyjnych)) istnieje w systemie plików.
    2. **Wczytywanie wyników**: Jeśli plik istnieje, wyniki są wczytywane do słownika za pomocą modułu `json`.
    3. **Obsługa braku pliku**: W przypadku braku pliku, metoda zwraca słownik z pustymi listami dla każdego poziomu trudności, co reprezentuje brak zapisanych wyników.
    4. **Zwracanie wyników**: Niezależnie od tego, czy wyniki pochodzą z pliku, czy są inicjalizowane jako puste, metoda zawsze zwraca strukturę danych reprezentującą wyniki.

- **Zachowanie**: Metoda [`load_scores`](#id-13-metoda-load_scores) zapewnia, że gra zawsze ma dostęp do aktualnych wyników, niezależnie od tego, czy są one wczytane z pliku, czy inicjowane jako puste w przypadku braku danych.

- **Jak to działa**: Działa to podobnie do systemu wczytywania zapisanych danych w grach wideo, gdzie postępy gracza są przechowywane i dostępne podczas kolejnych sesji gry.

- **Proste podsumowanie - metafora**: Można myśleć o metodzie [`load_scores`](#id-13-metoda-load_scores) jako o otwieraniu skrzyni ze skarbami, gdzie skarby to dotychczasowe wyniki graczy. W przypadku nowej gry, skrzynia ta jest pusta, ale z czasem wypełnia się coraz to nowymi osiągnięciami.

### ID 14: Metoda [`play_game`](#id-14-metoda-play_game)
```python
def play_game(self):
    self.board = self.init_board()
    # Inicjalizacja pustej planszy gry.

    cursor_pos = (0, 0)
    # Ustawienie początkowej pozycji kursora na planszy.

    current_player = 'X'
    # Ustawienie aktualnego gracza na 'X'.

    self.ai_player = 'O' if self.current_side == 'X' else 'X'
    # Ustawienie gracza AI na przeciwny znak niż gracz.

    if self.current_side == 'O':
        # Jeśli gracz wybrał 'O', AI (grając jako 'X') wykonuje pierwszy ruch.
        self.make_move(current_player)
        current_player = 'O'

    player_time = 0
    # Inicjalizacja czasu gry gracza.

    while True:
        # Główna pętla gry.

        self.draw_board(None)
        self.screen.refresh()
        # Rysowanie aktualnego stanu planszy i odświeżanie ekranu.

        if self.check_winner():
            # Sprawdzenie, czy jest zwycięzca gry.
            break

        if current_player == self.current_side:
            # Logika ruchu gracza, jeśli to jego kolej.

            player_start_time = time.time()
            # Rozpoczęcie odliczania czasu ruchu gracza.

            while True:
                key = self.screen.getch()
                # Oczekiwanie na wejście klawiatury od gracza.

                if key in [curses.KEY_UP, ord('w'), curses.KEY_DOWN, ord('s'),
                           curses.KEY_LEFT, ord('a'), curses.KEY_RIGHT, ord('d')]:
                    cursor_pos = self.update_cursor(key, cursor_pos)
                    self.draw_board(cursor_pos)
                    self.screen.refresh()
                    # Logika poruszania kursora na planszy i odświeżania widoku.

                elif key == 10:
                    # Jeśli gracz naciśnie Enter (klawisz o kodzie 10).
                    if self.player_move(cursor_pos):
                        # Jeśli ruch gracza jest dozwolony.
                        self.make_move(current_player, cursor_pos)
                        current_player = self.ai_player
                        # Zmiana tury na AI.
                        break

            player_end_time = time.time()
            player_time += player_end_time - player_start_time
            # Dodanie czasu ruchu do całkowitego czasu gracza.

        else:
            # Logika ruchu AI, jeśli to jego kolej.
            self.make_move(current_player)
            current_player = self.current_side
            # Zmiana tury na gracza.

    # Po zakończeniu gry.
    if self.winner == self.current_side:
        # Jeśli gracz wygrał.
        initials = self.prompt_for_initials()
        self.add_score_to_json(initials, player_time)
        # Zapisanie wyniku gracza.

    self.draw_board(None)
    rows, cols = self.screen.getmaxyx()
    message = f"Zwycięzca: {self.winner}" if self.winner != "Remis" else "Remis"
    self.screen.addstr(rows // 2 + self.board_size + 2, (cols - len(message)) // 2, message)
    self.screen.refresh()
    # Wyświetlenie wiadomości końcowej i odświeżenie ekranu.

    self.screen.getch()
    # Oczekiwanie na naciśnięcie klawisza, aby zakończyć.
```
- **Opis**: Metoda [`play_game`](#id-14-metoda-play_game) zarządza głównym przebiegiem rozgrywki w kółko i krzyżyk. Odpowiada za cykl gry, od początkowego ustawienia planszy, przez interakcję z graczem, aż po zakończenie gry i ogłoszenie wyników.

- **Funkcje**:
    1. **Inicjalizacja planszy**: Rozpoczyna grę od pustej planszy, tworzonej przez [`self.init_board()`](#id-06-metoda-init_boardself).
    2. **Ustawienie początkowego gracza**: Określa, który gracz (lub AI) rozpoczyna grę, bazując na aktualnych ustawieniach gry.
    3. **Obsługa ruchów graczy**: W pętli `while True` gra czeka na ruchy gracza, które są rejestrowane za pomocą klawiatury. Wykorzystuje [`self.update_cursor`](#id-22-metoda-update_cursor) do aktualizacji pozycji kursora na planszy i [`self.make_move`](#id-15-metoda-make_move) do wykonania ruchu.
    4. **Sprawdzanie warunków zwycięstwa**: Po każdym ruchu [`self.check_winner`](#id-19-metoda-check_winner) jest wywoływana, aby sprawdzić, czy któryś z graczy wygrał grę.
    5. **Zarządzanie zmianą graczy**: Alternuje pomiędzy graczami po każdym wykonanym ruchu, umożliwiając każdemu z nich wykonanie swojej tury.
    6. **Pomiar czasu gry**: Dla gracza rejestrowany jest czas trwania gry, który może być używany do celów rankingowych.
    7. **Wyświetlanie planszy**: Gra regularnie aktualizuje i wyświetla stan planszy na ekranie, informując graczy o bieżącym stanie gry.
    8. **Zakończenie gry i ogłoszenie wyników**: Po zakończeniu gry wyświetlany jest komunikat z informacją o zwycięzcy lub remisie, a wyniki gry są zapisywane.

- **Zachowanie**: [`play_game`](#id-14-metoda-play_game) jest dynamicznym środowiskiem, gdzie gracze angażują się w rywalizację, podejmują decyzje i obserwują rozwój gry. Zapewnia płynne przejście pomiędzy różnymi etapami gry i utrzymuje graczy w stałym zaangażowaniu.

- **Jak to działa**: Metoda działa jak koordynator gry, zarządzając różnymi aspektami rozgrywki. Od rejestrowania ruchów, przez aktualizację stanu gry, po ogłoszenie zwycięzcy, [`play_game`](#id-14-metoda-play_game) jest centralnym punktem, gdzie wszystkie te działania są integrowane.

- **Proste podsumowanie - metafora**: Można myśleć o [`play_game`](#id-14-metoda-play_game) jako o mistrzu ceremonii w grze planszowej. Tak jak mistrz ceremonii prowadzi graczy przez różne etapy gry, podobnie [`play_game`](#id-14-metoda-play_game) prowadzi graczy przez sekwencje rozgrywki, od rozpoczęcia do zakończenia.

### ID 15: Metoda [`make_move`](#id-15-metoda-make_move)
```python
def make_move(self, player, move = None):
    # Metoda ta jest wywoływana, aby umieścić znak gracza na planszy.

    x, y = move if move is not None else self.best_move()
    # Określa współrzędne ruchu. Jeśli ruch ('move') jest podany, używa go.
    # Jeśli 'move' jest None, wywołuje metodę 'self.best_move()', aby obliczyć najlepszy ruch.

    self.board[x][y] = player
    # Umieszcza znak gracza ('player') na planszy w wybranym miejscu (współrzędne x, y).
```
- **Opis**: Metoda [`make_move`](#id-15-metoda-make_move) jest kluczową częścią mechaniki gry w kółko i krzyżyk. Odpowiada za wykonanie ruchu na planszy, umieszczając symbol gracza (X lub O) w wybranym miejscu.

- **Parametry**:
    - `player`: Symbol gracza, który wykonuje ruch (X lub O).
    - `move` (opcjonalny): Krotka (tuple) zawierająca współrzędne (x, y) miejsca na planszy, gdzie gracz chce wykonać ruch. Jeśli `move` nie jest podane, ruch jest dobierany automatycznie przez metodę [`self.best_move`](#id-16-metoda-best_move).

- **Funkcje**:
    1. **Wybór miejsca na ruch**: Jeśli `move` jest podane, metoda używa tych współrzędnych. W przeciwnym wypadku, wywołuje [`self.best_move`](#id-16-metoda-best_move) do automatycznego wyboru najlepszego ruchu, zazwyczaj używanego przez AI.
    2. **Aktualizacja planszy**: Umieszcza symbol gracza (`player`) w wybranym miejscu na planszy.

- **Zachowanie**: [`make_move`](#id-15-metoda-make_move) jest podstawową metodą, która pozwala graczom na interakcję z planszą. Zapewnia, że ruchy są wykonane zgodnie z zasadami gry i odzwierciedla je na planszy.

- **Jak to działa**: Podobnie do umieszczania pionka na planszy w tradycyjnych grach, [`make_move`](#id-15-metoda-make_move) umożliwia graczom "postawienie" swojego symbolu w wybranym miejscu na wirtualnej planszy gry.

- **Proste podsumowanie - metafora**: Można porównać [`make_move`](#id-15-metoda-make_move) do ruchu pędzlem na płótnie malarskim. Tak jak artysta dokonuje świadomego wyboru, gdzie umieścić pociągnięcie pędzla, aby stworzyć obraz, gracze wybierają, gdzie umieścić swój symbol na planszy, aby osiągnąć zwycięstwo.

### ID 16: Metoda [`self.best_move`](#id-16-metoda-best_move)
```python
def best_move(self):
    if not self.available_moves():
        # Sprawdza, czy są dostępne ruchy.
        return None
        # Jeśli nie ma dostępnych ruchów, zwraca None.

    if self.current_level == 1: 
        # Jeśli poziom trudności gry to 1 (najniższy).
        return random.choice(self.available_moves())
        # Wybiera losowy dostępny ruch.

    else:
        # Dla poziomów trudności wyższych niż 1.
        if self.current_level == 5:
            # Jeśli poziom trudności to 5 (najwyższy).
            difficulty = len(self.available_moves())
            # Ustawia poziom trudności na liczbę dostępnych ruchów.
        else:
            difficulty = self.current_level
            # Ustawia poziom trudności na bieżący poziom gry.

        best_score = float('-inf') if self.ai_player == "X" else float('inf')
        # Ustawia początkowy najlepszy wynik na minus nieskończoność, jeśli AI gra jako "X",
        # lub na plus nieskończoność, jeśli AI gra jako "O".

        moves = self.available_moves()
        # Pobiera listę dostępnych ruchów.

        best_moves = []
        # Inicjalizuje listę najlepszych ruchów.

        for move in moves:
            # Iteruje przez wszystkie dostępne ruchy.

            self.make_move(self.ai_player, move)
            # Wykonuje tymczasowy ruch dla AI.

            if self.ai_player == "X":
                # Jeśli AI gra jako "X".
                score = self.minimax(difficulty, float('-inf'), float('inf'), False)
                # Oblicza wynik ruchu za pomocą algorytmu minimax.

                # Aktualizuje listę najlepszych ruchów w zależności od wyniku.
                if score > best_score:
                    best_score = score
                    best_moves = [move]
                elif score == best_score:
                    best_moves.append(move)

            else:
                # Analogicznie, jeśli AI gra jako "O".
                score = self.minimax(difficulty, float('-inf'), float('inf'), True)
                if score < best_score:
                    best_score = score
                    best_moves = [move]
                elif score == best_score:
                    best_moves.append(move)

            self.make_move(" ", move)
            # Cofa tymczasowy ruch, przywracając pierwotny stan planszy.

        return random.choice(best_moves) if best_moves else None
        # Zwraca losowy ruch z listy najlepszych ruchów, jeśli taka lista nie jest pusta.
```
- **Opis**: Metoda [`self.best_move`](#id-16-metoda-best_move) w grze w kółko i krzyżyk jest kluczową częścią algorytmu sztucznej inteligencji (AI). Jej zadaniem jest wybór najlepszego możliwego ruchu na planszy, w zależności od poziomu trudności gry.

- **Zwraca**: Najlepszy ruch jako krotkę (tuple) zawierającą współrzędne (x, y), lub `None`, jeśli nie ma dostępnych ruchów.

- **Funkcje**:
    1. **Sprawdzenie dostępnych ruchów**: Najpierw metoda sprawdza, czy są dostępne ruchy na planszy.
    2. **Wybór ruchu dla różnych poziomów trudności**:
        - Na poziomie "nowicjusz" (`level == 1`), wybiera losowy dostępny ruch.
        - Na wyższych poziomach, wykorzystuje algorytm Minimax do oceny najlepszego ruchu.
    3. **Ocena ruchów**:
        - Dla każdego możliwego ruchu, metoda symuluje wykonanie tego ruchu, a następnie używa algorytmu Minimax do oceny jego wartości.
        - Przechowuje ruchy o najwyższej wartości w liście [`self.best_move`](#id-16-metoda-best_move).
    4. **Wybór najlepszego ruchu**: Ostatecznie, jeśli istnieje więcej niż jeden "najlepszy" ruch, metoda wybiera jeden z nich losowo.

- **Zachowanie**: [`self.best_move`](#id-16-metoda-best_move) jest kluczowa dla działania AI w grze. Zapewnia, że komputerowy przeciwnik podejmuje inteligentne decyzje, dostosowane do wybranego poziomu trudności.

- **Jak to działa**: Podobnie do szachisty analizującego szachownicę,[`self.best_move`](#id-16-metoda-best_move) rozważa różne możliwości i wybiera ruch, który najbardziej przyczyni się do potencjalnego zwycięstwa.

- **Proste podsumowanie - metafora**: Można myśleć o metodzie [`self.best_move`](#id-16-metoda-best_move) jako o strategu wojskowym, który analizuje pole bitwy i decyduje o najlepszym kursie działania. Każdy ruch jest dokładnie przemyślany, aby zwiększyć szanse na zwycięstwo.

### ID 17: Metoda [`available_moves`](#id-17-metoda-available_moves)
```python
def available_moves(self):
    # Metoda ta zwraca listę wszystkich pustych pól (dostępnych ruchów) na planszy gry.

    return [(x, y) for x in range(self.board_size) for y in range(self.board_size) if self.board[x][y] == " "]
    # Używa składni list comprehension w Pythonie do iteracji przez wszystkie pola planszy.

    # 'range(self.board_size)' to zakres od 0 do rozmiaru planszy minus jeden.
    # 'for x in range(self.board_size)' i 'for y in range(self.board_size)' tworzą dwie pętle,
    # które przechodzą przez każdą komórkę na planszy.

    # 'if self.board[x][y] == " "' sprawdza, czy dane pole (komórka) jest puste.
    # Jeśli pole jest puste, jego współrzędne (x, y) są dodawane do listy zwracanej przez metodę.
```
- **Opis**: Metoda [`available_moves`](#id-17-metoda-available_moves) w grze w kółko i krzyżyk służy do identyfikacji wszystkich dostępnych ruchów na planszy. Jest to kluczowy element algorytmu gry, pozwalający na określenie możliwych miejsc, w które gracz lub AI mogą postawić swój znak.

- **Zwraca**: Listę krotek (tuple) zawierających współrzędne (x, y) pustych miejsc na planszy, gdzie gracze mogą wykonać ruch.

- **Funkcje**:
    1. **Generowanie listy dostępnych ruchów**: Metoda przeszukuje planszę gry, aby znaleźć wszystkie puste pola.
    2. **Wykorzystanie składni list comprehension**: Używa składni list comprehension w Pythonie do efektywnego przeszukiwania planszy i tworzenia listy dostępnych ruchów.
    3. **Sprawdzanie pustych miejsc**: Dla każdego pola na planszy metoda sprawdza, czy jest ono puste (oznaczone jako `" "`), i jeśli tak, dodaje jego współrzędne do listy dostępnych ruchów.

- **Zachowanie**: [`available_moves`](#id-17-metoda-available_moves) jest niezbędna do zrozumienia aktualnego stanu gry, informując gracza lub AI o wszystkich możliwych ruchach, które mogą być wykonane w danym momencie gry.

- **Jak to działa**: Metoda ta działa jak eksplorator mapy, szukający wszystkich niezajętych miejsc, gdzie można by coś umieścić. W kontekście gry, przeszukuje planszę w poszukiwaniu pustych pól, które są potencjalnymi miejscami na ruch.

- **Proste podsumowanie - metafora**: Można porównać [`available_moves`](#id-17-metoda-available_moves) do roli detektywa, który bada scenę i wskazuje wszystkie możliwe ślady. W grze, metoda wskazuje wszystkie pola, na których gracze mogą "zostawić swój ślad", czyli wykonać ruch.

### ID 18: Metoda [`minimax`](#id-18-metoda-minimax)
```python
def minimax(self, depth, alpha, beta, is_maximizing):
    # Algorytm analizuje przyszłe ruchy do określonej głębokości ('depth').

    if depth == 0 or self.check_winner():
        # Warunek bazowy: jeśli osiągnięto maksymalną głębokość lub jest zwycięzca.
        return self.evaluate()
        # Zwraca ocenę aktualnego stanu planszy.

    if is_maximizing:
        # Jeśli jest to ruch maksymalizujący (ruch gracza 'X').
        max_eval = float('-inf')
        # Ustawia początkową maksymalną ocenę na minus nieskończoność.

        for move in self.available_moves():
            # Iteruje przez wszystkie dostępne ruchy.

            self.make_move("X", move)
            # Wykonuje tymczasowy ruch na planszy.

            eval = self.minimax(depth - 1, alpha, beta, False)
            # Rekurencyjne wywołanie funkcji minimax, zmniejszając głębokość i zmieniając gracza.

            self.make_move(" ", move)
            # Cofa tymczasowy ruch, przywracając stan planszy.

            max_eval = max(max_eval, eval)
            # Aktualizuje maksymalną ocenę.

            alpha = max(alpha, eval)
            # Aktualizuje wartość alfa.

            if beta <= alpha:
                # Przerywa pętlę, jeśli wartość beta jest mniejsza lub równa alfa (cięcie alfa-beta).
                break

        return max_eval
        # Zwraca najlepszą ocenę dla ruchu maksymalizującego.

    else:
        # Analogicznie, dla ruchu minimalizującego (gracz 'O').
        min_eval = float('inf')
        # Ustawia początkową minimalną ocenę na plus nieskończoność.

        for move in self.available_moves():
            # Iteruje przez dostępne ruchy.

            self.make_move("O", move)
            # Wykonuje tymczasowy ruch.

            eval = self.minimax(depth - 1, alpha, beta, True)
            # Rekurencyjne wywołanie funkcji minimax.

            self.make_move(" ", move)
            # Cofa tymczasowy ruch.

            min_eval = min(min_eval, eval)
            # Aktualizuje minimalną ocenę.

            beta = min(beta, eval)
            # Aktualizuje wartość beta.

            if beta <= alpha:
                # Przerywa pętlę dla cięcia alfa-beta.
                break

        return min_eval
        # Zwraca najlepszą ocenę dla ruchu minimalizującego.
```
- **Opis**: Metoda [`minimax`](#id-18-metoda-minimax) jest implementacją algorytmu MiniMax, który jest szeroko stosowany w grach takich jak kółko i krzyżyk. Służy do znalezienia najlepszego możliwego ruchu, analizując przyszłe możliwości i ich wyniki.

- **Parametry**:
    - `depth`: Głębokość rekurencyjnego przeszukiwania, określająca, jak daleko algorytm ma analizować możliwe ruchy.
    - `alpha` i `beta`: Parametry używane w optymalizacji cięć alfa-beta, które pomagają zredukować liczbę przeszukiwanych węzłów.
    - `is_maximizing`: Boolowska wartość wskazująca, czy obecny ruch jest wykonywany przez gracza maksymalizującego wynik (zazwyczaj AI).

- **Funkcje**:
    1. **Ocena warunków końcowych**: Jeśli osiągnięto maksymalną głębokość przeszukiwania lub gra została rozstrzygnięta, metoda zwraca ocenę bieżącego stanu planszy.
    2. **Maksymalizacja lub minimalizacja**: W zależności od tego, czy ruch jest wykonywany przez gracza maksymalizującego czy minimalizującego, algorytm próbuje znaleźć ruch o najwyższej (dla maksymalizującego) lub najniższej (dla minimalizującego) wartości oceny.
    3. **Rekurencyjne przeszukiwanie**: Algorytm rekurencyjnie analizuje możliwe ruchy, przewidując przyszłe stany gry i oceniając je.
    4. **Optymalizacja cięć alfa-beta**: Zastosowanie cięć alfa-beta pozwala na redukcję liczby węzłów do analizy, co zwiększa efektywność algorytmu.

- **Zachowanie**: [`minimax`](#id-18-metoda-minimax) jest fundamentem inteligentnego zachowania AI w grze. Umożliwia dokonywanie wyważonych decyzji, które są kluczowe w strategii gry.

- **Jak to działa**: Podobnie do gracza szachowego, który przewiduje możliwe ruchy przeciwnika i planuje swoje, [`minimax`](#id-18-metoda-minimax) analizuje potencjalne przyszłe ruchy i ich konsekwencje, wybierając optymalny ruch.

- **Proste podsumowanie - metafora**: Można myśleć o [`minimax`](#id-18-metoda-minimax) jako o wytrawnym strategu, który przewiduje kilka ruchów do przodu, starając się znaleźć najlepszy możliwy plan działania w złożonej grze taktycznej.

### ID 19: Metoda [`check_winner`](#id-19-metoda-check_winner)
```python
def check_winner(self):
    for char in ['X', 'O']:
        # Sprawdza dla obu graczy ('X' i 'O').

        for row in self.board:
            # Sprawdza każdy rząd na planszy.
            if all(cell == char for cell in row):
                # Jeśli wszystkie komórki w rzędzie są zajęte przez tego samego gracza.
                self.winner = char
                # Ustawia zwycięzcę.
                return True
                # Zwraca True, wskazując, że jest zwycięzca.

        for col in range(self.board_size):
            # Sprawdza każdą kolumnę na planszy.
            if all(self.board[row][col] == char for row in range(self.board_size)):
                # Jeśli wszystkie komórki w kolumnie są zajęte przez tego samego gracza.
                self.winner = char
                return True

        # Sprawdza obie przekątne.
        if all(self.board[i][i] == char for i in range(self.board_size)) or \
           all(self.board[i][self.board_size - i - 1] == char for i in range(self.board_size)):
            # Jeśli wszystkie komórki na którejkolwiek przekątnej są zajęte przez tego samego gracza.
            self.winner = char
            return True

    # Sprawdza, czy zostały wolne komórki na planszy.
    if not any(" " in row for row in self.board):
        # Jeśli nie ma żadnych wolnych komórek, oznacza to remis.
        self.winner = "Remis"
        return True 

    return False
    # Jeśli nie ma zwycięzcy i nie ma remisu, zwraca False.
```
- **Opis**: Metoda [`check_winner`](#id-19-metoda-check_winner) w grze w kółko i krzyżyk służy do sprawdzania, czy któryś z graczy wygrał grę lub czy gra zakończyła się remisem. Jest kluczowa dla określenia wyniku rozgrywki.

- **Zwraca**: Boolowską wartość `True`, jeśli gra została rozstrzygnięta (czyli jest zwycięzca lub remis), lub `False`, jeśli gra jest nadal nierozstrzygnięta.

- **Funkcje**:
    1. **Sprawdzanie wierszy**: Przechodzi przez każdy wiersz planszy, aby sprawdzić, czy wszystkie pola w wierszu są zajęte przez ten sam znak (X lub O), co oznacza wygraną jednego z graczy.
    2. **Sprawdzanie kolumn**: Analogicznie, sprawdza każdą kolumnę pod kątem wygranej.
    3. **Sprawdzanie przekątnych**: Sprawdza obie przekątne planszy, aby zobaczyć, czy któryś gracz zajął wszystkie pola wzdłuż przekątnej.
    4. **Określenie remisu**: Jeśli na planszy nie ma już wolnych miejsc i żaden z graczy nie wygrał, oznacza to remis.
    5. **Aktualizacja zwycięzcy**: Ustawia zmienną [`self.winner`](#id-05-metoda-__init__self-screen) na znak zwycięzcy ('X' lub 'O') lub na "Remis", jeśli taka jest sytuacja.

- **Zachowanie**: [`check_winner`](#id-19-metoda-check_winner) jest wywoływana po każdym ruchu, aby natychmiast określić, czy rozgrywka została rozstrzygnięta. Jest to niezbędne dla prawidłowego przebiegu gry.

- **Jak to działa**: Metoda działa jak sędzia w grze, który po każdym ruchu sprawdza, czy nie nastąpiło rozstrzygnięcie, zgodnie z zasadami gry.

- **Proste podsumowanie - metafora**: Można porównać [`check_winner`](#id-19-metoda-check_winner) do sędziego w sporcie, który po każdej akcji graczy sprawdza, czy nie zostały spełnione warunki zwycięstwa, i ogłasza wynik gry.

### ID 20: Metoda [`evaluate`](#id-20-metoda-evaluate)
```python
def evaluate(self):
    # Ta metoda ocenia planszę gry.

    self.check_winner()
    # Najpierw wywołuje metodę 'check_winner', aby sprawdzić, czy jest zwycięzca.

    if self.winner == 'X':
        # Jeśli zwycięzcą jest gracz 'X'.
        return 1
        # Zwraca wartość 1, co oznacza korzystny wynik dla 'X'.

    elif self.winner == 'O':
        # Jeśli zwycięzcą jest gracz 'O'.
        return -1
        # Zwraca wartość -1, co oznacza korzystny wynik dla 'O'.

    else:
        # Jeśli nie ma zwycięzcy (czyli jest remis lub gra nadal trwa).
        return 0
        # Zwraca 0, co oznacza neutralny wynik.
```
- **Opis**: Metoda [`evaluate`](#id-20-metoda-evaluate) służy do oceny bieżącego stanu planszy w grze w kółko i krzyżyk. Jest wykorzystywana głównie przez algorytm [`minimax`](#id-18-metoda-minimax) do określenia wartości danego stanu planszy z perspektywy AI.

- **Zwraca**: Liczbę całkowitą reprezentującą ocenę stanu planszy: `1` dla wygranej 'X', `-1` dla wygranej 'O', i `0` w przypadku remisu lub nierozstrzygniętej gry.

- **Funkcje**:
    1. **Sprawdzenie wyniku gry**: Najpierw wywołuje [`self.check_winner`](#id-19-metoda-check_winner) do sprawdzenia, czy gra została rozstrzygnięta.
    2. **Ocena stanu gry**:
        - Zwraca `1`, jeśli zwycięzcą jest 'X' – oznacza to pozytywny wynik dla 'X'.
        - Zwraca `-1`, jeśli zwycięzcą jest 'O' – oznacza to negatywny wynik dla 'X' i pozytywny dla 'O'.
        - Zwraca `0`, jeśli gra jest remisem lub jeszcze się nie zakończyła.

- **Zachowanie**: [`evaluate`](#id-20-metoda-evaluate) jest kluczowa dla algorytmu decyzyjnego AI. Pozwala AI ocenić, czy dany ruch prowadzi do wygranej, przegranej czy remisu.

- **Jak to działa**: Metoda działa jak system oceniania w grach, gdzie każdy możliwy wynik (wygrana, przegrana, remis) jest przyporządkowany do określonej wartości, ułatwiając algorytmowi podejmowanie decyzji.

- **Proste podsumowanie - metafora**: Można myśleć o [`evaluate`](#id-20-metoda-evaluate) jako o sędzi punktowym w zawodach sportowych, który przyznaje punkty na podstawie wyniku. W tym przypadku, punkty są przyznawane za wygraną, przegraną lub remis w grze.

### ID 21: Metoda [`draw_board`](#id-21-metoda-draw_board)
```python
def draw_board(self, cursor_pos):
    self.screen.clear()
    # Czyści ekran, aby narysować aktualny stan planszy.

    rows, cols = self.screen.getmaxyx()
    # Pobiera wymiary dostępnego okna ekranu.

    board_width = 4 * self.board_size - 1
    board_height = 2 * self.board_size - 1
    # Oblicza szerokość i wysokość planszy w znakach.

    start_y = (rows - board_height) // 2
    start_x = (cols - board_width) // 2
    # Oblicza początkowe pozycje (x, y) dla rysowania planszy, aby była ona wyśrodkowana.

    for i in range(self.board_size):
        for j in range(self.board_size):
            # Iteruje przez wszystkie komórki planszy.

            cell = self.board[i][j]
            # Pobiera zawartość komórki (znak 'X', 'O' lub puste).

            x = start_x + j * 4
            y = start_y + i * 2
            # Oblicza pozycję każdej komórki na ekranie.

            if (i, j) == cursor_pos:
                self.screen.attron(curses.A_REVERSE)
                # Jeśli pozycja komórki pokrywa się z pozycją kursora, aktywuje odwrócenie kolorów.

            self.screen.addstr(y, x, cell)
            # Wyświetla zawartość komórki na ekranie.

            if (i, j) == cursor_pos:
                self.screen.attroff(curses.A_REVERSE)
                # Deaktywuje odwrócenie kolorów po wyświetleniu komórki.

            if j < self.board_size - 1:
                self.screen.addstr(y, x + 1, " │ ")
                # Dodaje separator pionowy między komórkami.

    for i in range(1, self.board_size):
        y = start_y + i * 2 - 1
        self.screen.addstr(y, start_x, "──┼───┼──"[:(board_width - 1)])
        # Rysuje separatory poziome między rzędami komórek.

    self.screen.refresh()
    # Odświeża ekran, aby wyświetlić zaktualizowany stan planszy.
```
- **Opis**: Metoda [`draw_board`](#id-21-metoda-draw_board) odpowiada za graficzne przedstawienie planszy gry w kółko i krzyżyk na ekranie. Używa biblioteki `curses` do rysowania planszy w terminalu.

- **Parametry**:
    - `cursor_pos`: Krotka (tuple) zawierająca współrzędne (x, y) kursora na planszy, co umożliwia wizualne wyróżnienie aktualnego miejsca wyboru na planszy.

- **Funkcje**:
    1. **Czyszczenie ekranu**: Usuwa wszelką poprzednią zawartość ekranu.
    2. **Obliczanie wymiarów planszy**: Wylicza rozmiary potrzebne do centrowania planszy na ekranie.
    3. **Rysowanie komórek planszy**: Iteruje przez komórki planszy, rysując symbol każdego gracza i linie oddzielające komórki.
    4. **Wyróżnienie kursora**: Używa odwróconego koloru (funkcje `attron` i `attroff` z `curses`) do wizualnego wyróżnienia komórki, na której znajduje się kursor.
    5. **Rysowanie linii oddzielających**: Dodaje linie pionowe i poziome, aby oddzielić komórki planszy od siebie.
    6. **Odświeżenie ekranu**: Aktualizuje wyświetlaną zawartość ekranu.

- **Zachowanie**: [`draw_board`](#id-21-metoda-draw_board) jest kluczowa dla interaktywnego aspektu gry, ponieważ zapewnia wizualną reprezentację planszy, na której gracz wykonuje ruchy.

- **Jak to działa**: Podobnie do rysowania na fizycznej planszy, [`draw_board`](#id-21-metoda-draw_board) tworzy wizualną reprezentację planszy w konsoli, umożliwiając graczom łatwe śledzenie gry.

- **Proste podsumowanie - metafora**: Można myśleć o [`draw_board`](#id-21-metoda-draw_board) jako o malarzu, który tworzy obraz gry na płótnie ekranu komputera. Każdy ruch gracza jest jak pociągnięcie pędzla, które zmienia wygląd obrazu.

### ID 22: Metoda [`update_cursor`](#id-22-metoda-update_cursor)
```python
def update_cursor(self, key, cursor_pos):
    x, y = cursor_pos
    # Rozpakowuje bieżącą pozycję kursora na współrzędne x i y.

    if key in [curses.KEY_UP, ord('w')] and x > 0:
        # Jeśli naciśnięto klawisz 'w' lub strzałkę w górę i kursor nie jest na górnej krawędzi planszy.
        x -= 1
        # Przesuwa kursor o jedno pole w górę (zmniejsza wartość x).

    elif key in [curses.KEY_DOWN, ord('s')] and x < self.board_size - 1:
        # Jeśli naciśnięto klawisz 's' lub strzałkę w dół i kursor nie jest na dolnej krawędzi planszy.
        x += 1
        # Przesuwa kursor o jedno pole w dół (zwiększa wartość x).

    elif key in [curses.KEY_LEFT, ord('a')] and y > 0:
        # Jeśli naciśnięto klawisz 'a' lub strzałkę w lewo i kursor nie jest na lewej krawędzi planszy.
        y -= 1
        # Przesuwa kursor o jedno pole w lewo (zmniejsza wartość y).

    elif key in [curses.KEY_RIGHT, ord('d')] and y < self.board_size - 1:
        # Jeśli naciśnięto klawisz 'd' lub strzałkę w prawo i kursor nie jest na prawej krawędzi planszy.
        y += 1
        # Przesuwa kursor o jedno pole w prawo (zwiększa wartość y).

    return x, y
    # Zwraca nową pozycję kursora jako krotkę (x, y).
```
- **Opis**: Metoda [`update_cursor`](#id-22-metoda-update_cursor) jest używana do aktualizacji pozycji kursora na planszy w grze w kółko i krzyżyk. Umożliwia ona graczom nawigację po planszy za pomocą klawiatury, aby wybrać miejsce, w którym chcą wykonać ruch.

- **Parametry**:
    - `key`: Klucz reprezentujący naciśnięcie klawisza przez użytkownika.
    - `cursor_pos`: Aktualna pozycja kursora jako krotka (x, y).

- **Zwraca**: Nową pozycję kursora jako krotkę (x, y) po zastosowaniu naciśnięć klawiszy.

- **Funkcje**:
    1. **Obsługa klawiszy kierunkowych**: Reaguje na naciśnięcia klawiszy strzałek lub odpowiednich klawiszy ('w', 'a', 's', 'd') do poruszania kursora.
    2. **Aktualizacja pozycji kursora**: Zmienia pozycję kursora (x, y) w odpowiedzi na naciśnięcie klawisza, z zachowaniem ograniczeń planszy.
    3. **Zapobieganie wyjściu poza planszę**: Sprawdza, czy nowa pozycja kursora nie wykracza poza granice planszy, i w razie potrzeby zatrzymuje kursor na krawędzi.

- **Zachowanie**: [`update_cursor`](#id-22-metoda-update_cursor) pozwala na płynne i intuicyjne nawigowanie po planszy, co jest kluczowe dla wygody użytkowania i interakcji z grą.

- **Jak to działa**: Podobnie do używania pilota do nawigacji w menu telewizora, [`update_cursor`](#id-22-metoda-update_cursor) pozwala graczom na poruszanie się po wirtualnej planszy za pomocą klawiatury.

- **Proste podsumowanie - metafora**: Można porównać [`update_cursor`](#id-22-metoda-update_cursor) do sterowania zdalnie sterowanym pojazdem, gdzie naciśnięcia klawiszy kierują ruchem pojazdu (tutaj kursora) w obrębie określonej przestrzeni (planszy gry).

### ID 23: Metoda [`player_move`](#id-23-metoda-player_move)
```python
def player_move(self, cursor_pos):
    x, y = cursor_pos
    # Rozpakowuje pozycję kursora na współrzędne x i y.

    if self.board[x][y] == " ":
        # Sprawdza, czy wybrane pole na planszy jest puste.

        return True
        # Jeśli pole jest puste, zwraca True, oznaczając, że ruch na tej pozycji jest dozwolony.

    return False
    # Jeśli pole nie jest puste, zwraca False, co oznacza, że ruch na tej pozycji nie jest dozwolony.
```
- **Opis**: Metoda [`player_move`](#id-23-metoda-player_move) jest używana do sprawdzenia, czy gracz może wykonać ruch w wybranym miejscu na planszy w grze w kółko i krzyżyk. Jest to mechanizm kontroli, który zapobiega wykonaniu ruchu na zajętym polu.

- **Parametry**:
    - `cursor_pos`: Pozycja kursora jako krotka (x, y), określająca miejsce na planszy, gdzie gracz chce wykonać ruch.

- **Zwraca**: Boolowską wartość `True`, jeśli wybrane miejsce na planszy jest puste i gracz może tam wykonać ruch, lub `False`, jeśli miejsce jest już zajęte.

- **Funkcje**:
    1. **Sprawdzenie dostępności miejsca**: Metoda sprawdza, czy wybrane pole na planszy (określone przez `cursor_pos`) jest puste (oznaczone jako " ").
    2. **Decyzja o możliwości ruchu**: Jeśli pole jest puste, zwraca `True`, co oznacza, że gracz może tam wykonać ruch. W przeciwnym razie zwraca `False`.

- **Zachowanie**: [`player_move`](#id-23-metoda-player_move) jest niezbędna do zapewnienia, że ruchy są wykonywane zgodnie z zasadami gry. Zapobiega sytuacjom, w których gracz próbuje wykonać ruch na zajętym polu.

- **Jak to działa**: Metoda działa jak rodzaj "strażnika", który sprawdza, czy proponowany ruch jest legalny i zgodny z zasadami gry.

- **Proste podsumowanie - metafora**: Można porównać [`player_move`](#id-23-metoda-player_move) do sędziego w sporcie, który decyduje, czy ruch zawodnika jest zgodny z zasadami. Tak jak sędzia zapobiega nieprzepisowym ruchom, tak [`player_move`](#id-23-metoda-player_move) zapewnia, że ruchy na planszy są wykonywane zgodnie z regułami gry w kółko i krzyżyk.

### ID 24: Metoda [`prompt_for_initials`](#id-24-metoda-prompt_for_initials)
```python
def prompt_for_initials(self):
    self.screen.addstr("\nWpisz swoje inicjały (3 litery): ")
    # Wyświetla monit o wpisanie inicjałów gracza.

    self.screen.refresh()
    # Odświeża ekran, aby wyświetlić monit.

    initials = self.screen.getstr(0, len("Wpisz swoje inicjały (3 litery): "), 3).decode('utf-8')
    # Pobiera ciąg znaków wprowadzony przez gracza. Argumenty '0' i 'len(...)' określają
    # pozycję na ekranie, gdzie ma zostać umieszczony kursor, a '3' określa maksymalną długość ciągu.
    # Metoda 'decode('utf-8')' konwertuje wprowadzone dane z formatu bajtów na ciąg znaków.

    return initials
    # Zwraca wprowadzone inicjały.
```
- **Opis**: Metoda [`prompt_for_initials`](#id-24-metoda-prompt_for_initials) służy do pobierania inicjałów gracza po zakończeniu gry w kółko i krzyżyk. Inicjały te mogą być używane do identyfikacji gracza w tabeli wyników lub do innych celów personalizacji.

- **Zwraca**: Ciąg znaków (string) zawierający inicjały gracza, ograniczone do 3 liter.

- **Funkcje**:
    1. **Wyświetlanie monitu**: Wyświetla na ekranie komunikat zachęcający gracza do wpisania swoich inicjałów.
    2. **Odświeżenie ekranu**: Aktualizuje zawartość ekranu, aby wyświetlić monit.
    3. **Pobieranie inicjałów**: Umożliwia graczowi wpisanie swoich inicjałów, ograniczając wprowadzenie do 3 liter.
    4. **Dekodowanie ciągu znaków**: Konwertuje pobrane dane z formatu bajtowego na ciąg znaków UTF-8, co umożliwia ich poprawne wyświetlenie i przetwarzanie.

- **Zachowanie**: [`prompt_for_initials`](#id-24-metoda-prompt_for_initials) jest prosta i intuicyjna w użyciu, umożliwiając graczowi szybkie wpisanie i zatwierdzenie swoich inicjałów.

- **Jak to działa**: Metoda działa jak elektroniczny formularz, w którym użytkownik wpisuje swoje dane identyfikacyjne. Jest to standardowa praktyka w grach, gdzie gracze mogą zostawić swój ślad, np. w tabeli wyników.

- **Proste podsumowanie - metafora**: Można porównać [`prompt_for_initials`](#id-24-metoda-prompt_for_initials) do podpisania swojego nazwiska na liście gości podczas wydarzenia. Tak jak goście zapisują swoje imiona, aby zaznaczyć swoją obecność, gracze wpisują swoje inicjały, aby zarejestrować swoje osiągnięcia w grze.

### ID 25: Metoda [`add_score_to_json`](#id-25-metoda-add_score_to_json)
```python
def add_score_to_json(self, initials, time_elapsed):
    level = self.get_difficulty_level_name()
    # Pobiera nazwę bieżącego poziomu trudności gry.

    try:
        if os.path.exists(self.SCORES_FILE):
            # Sprawdza, czy plik z wynikami już istnieje.
            with open(self.SCORES_FILE, "r") as file:
                # Otwiera istniejący plik z wynikami w trybie czytania.
                scores = json.load(file)
                # Wczytuje istniejące wyniki z pliku JSON do zmiennej 'scores'.

        else:
            # Jeśli plik z wynikami nie istnieje, tworzy nowy słownik wyników.
            scores = {"nowicjusz": [], "latwy": [], "sredni": [], "trudny": [], "niezwyciezony": []}

        score_data = {"nazwa": initials, "czas": self.format_time(time_elapsed), "char_player": self.current_side}
        # Tworzy słownik z danymi wyniku, zawierającymi inicjały gracza, czas gry oraz znak gracza.

        scores[level].append(score_data)
        # Dodaje wynik do odpowiedniej listy na podstawie poziomu trudności.

        scores[level] = sorted(scores[level], key=lambda x: x['czas'])
        # Sortuje wyniki na danym poziomie trudności według czasu.

        with open(self.SCORES_FILE, "w") as file:
            # Otwiera plik z wynikami w trybie zapisu.
            json.dump(scores, file, indent=4)
            # Zapisuje zaktualizowane wyniki do pliku JSON.

    except IOError as e:
        # Obsługuje błędy związane z operacjami na plikach.
        print("Wystąpił błąd przy zapisie wyniku: ", e)
```
- **Opis**: Metoda [`add_score_to_json`](#id-25-metoda-add_score_to_json) służy do zapisywania wyniku gracza w pliku JSON po zakończeniu gry w kółko i krzyżyk. Pozwala na przechowywanie informacji o wynikach graczy, w tym ich inicjałów, czasu gry oraz strony, którą grali.

- **Parametry**:
    - `initials`: Inicjały gracza.
    - `time_elapsed`: Czas, w jakim gracz ukończył grę.

- **Funkcje**:
    1. **Określenie poziomu trudności**: Pobiera nazwę obecnego poziomu trudności gry.
    2. **Sprawdzenie i wczytywanie istniejących wyników**: Sprawdza, czy plik z wynikami ([`self.SCORES_FILE`](#id-03-stałe-plików-konfiguracyjnych)) już istnieje. Jeśli tak, wczytuje istniejące wyniki, w przeciwnym razie tworzy pusty szablon wyników.
    3. **Przygotowanie danych wyniku**: Tworzy słownik z danymi wyniku, w tym inicjałami gracza, sformatowanym czasem gry i oznaczeniem strony.
    4. **Dodawanie i sortowanie wyników**: Dodaje nowy wynik do odpowiedniej listy w słowniku wyników i sortuje listę według czasu gry.
    5. **Zapis do pliku JSON**: Zapisuje zaktualizowany słownik wyników do pliku JSON, formatując go dla lepszej czytelności.
    6. **Obsługa błędów wejścia/wyjścia**: Zabezpiecza przed błędami związanymi z operacjami na pliku, takimi jak brak uprawnień do zapisu.

- **Zachowanie**: [`add_score_to_json`](#id-25-metoda-add_score_to_json) zapewnia stałe śledzenie i zapisywanie osiągnięć graczy, co pozwala na tworzenie historii wyników i rywalizację.

- **Jak to działa**: Metoda działa jak rejestrator wyników, zbierający i zapisujący informacje o wynikach gry, podobnie do tablicy wyników w grach elektronicznych czy sportowych.

- **Proste podsumowanie - metafora**: Można myśleć o [`add_score_to_json`](#id-25-metoda-add_score_to_json) jako o tworzeniu i aktualizacji sportowej tablicy wyników, gdzie każdy nowy wynik jest dodawany, a tablica jest regularnie aktualizowana i utrzymywana w porządku.

### ID 26: Metoda [`format_time`](#id-26-metoda-format_time)
```python
def format_time(self, seconds):
    # Metoda przyjmuje czas wyrażony w sekundach.

    return time.strftime('%H:%M:%S', time.gmtime(seconds))
    # Używa funkcji 'strftime' z modułu 'time', aby sformatować czas.

    # '%H:%M:%S' to format, w którym czas będzie wyświetlany. Oznacza to, że czas będzie
    # prezentowany w formacie godzin, minut i sekund.

    # 'time.gmtime(seconds)' konwertuje liczbę sekund na format godzinowy (UTC).
    # Funkcja 'gmtime' przekształca sekundy na krotkę reprezentującą czas (rok, miesiąc, dzień,
    # godzina, minuta, sekunda). 'strftime' następnie formatuje tę krotkę do postaci stringu.
```
- **Opis**: Metoda [`format_time`](#id-26-metoda-format_time) służy do formatowania czasu gry z sekund na bardziej czytelny format godzin:minut:sekund. Jest używana do prezentacji czasu gry w tabeli wyników lub w innych częściach gry, gdzie czas jest ważnym elementem.

- **Parametry**:
    - `seconds`: Czas gry podany w sekundach.

- **Zwraca**: Sformatowany ciąg znaków (string) reprezentujący czas w formacie HH:MM:SS (godziny:minuty:sekundy).

- **Funkcje**:
    1. **Konwersja sekund na formatowalny czas**: Używa funkcji `time.gmtime` z modułu `time` do przekształcenia liczby sekund na strukturę czasu w formacie UTC.
    2. **Formatowanie czasu**: Wykorzystuje funkcję `time.strftime` do przekształcenia struktury czasu na sformatowany ciąg znaków zgodnie z formatem HH:MM:SS.

- **Zachowanie**: [`format_time`](#id-26-metoda-format_time) zapewnia czytelne i zrozumiałe przedstawienie czasu gry, co jest przydatne zarówno dla graczy, jak i dla celów prezentacji wyników.

- **Jak to działa**: Metoda przekształca surowe dane liczbowe (czas w sekundach) na format łatwy do odczytania i zrozumienia dla ludzi, podobnie do zegara cyfrowego wyświetlającego czas.

- **Proste podsumowanie - metafora**: Można porównać [`format_time`](#id-26-metoda-format_time) do pracy tłumacza, który przekłada techniczne dane (liczba sekund) na język zrozumiały dla wszystkich (sformatowany czas).
</details>
