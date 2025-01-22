class Player:
    def __init__(self, name):
        self.name = name
        self.matches_played = 0
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.points = 0

    def update_stats(self, result):
        self.matches_played += 1
        if result == 'win':
            self.wins += 1
            self.points += 3
        elif result == 'loss':
            self.losses += 1
        elif result == 'draw':
            self.draws += 1
            self.points += 1

    def __str__(self):
        return f"{self.name}: {self.points} pts (W: {self.wins}, D: {self.draws}, L: {self.losses}, MP: {self.matches_played})"


class ChessLeague:
    def __init__(self):
        self.players = {}

    def add_player(self, name):
        if name not in self.players:
            self.players[name] = Player(name)
            print(f"Player {name} added to the league.")
        else:
            print(f"Player {name} already exists in the league.")

    def record_match(self, player1_name, player2_name, result):
        if player1_name not in self.players or player2_name not in self.players:
            print("Both players must be registered in the league.")
            return

        player1 = self.players[player1_name]
        player2 = self.players[player2_name]

        if result == player1_name:
            player1.update_stats('win')
            player2.update_stats('loss')
        elif result == player2_name:
            player1.update_stats('loss')
            player2.update_stats('win')
        elif result == 'draw':
            player1.update_stats('draw')
            player2.update_stats('draw')
        else:
            print("Invalid result. Use player1 name, player2 name, or 'draw'.")

    def display_standings(self):
        print("\nLeague Standings:")
        sorted_players = sorted(self.players.values(), key=lambda p: p.points, reverse=True)
        for idx, player in enumerate(sorted_players, 1):
            print(f"{idx}. {player}")

    def menu(self):
        while True:
            print("\nChess League Manager")
            print("1. Add Player")
            print("2. Record Match")
            print("3. Display Standings")
            print("4. Exit")

            choice = input("Choose an option: ")
            if choice == '1':
                name = input("Enter player name: ")
                self.add_player(name)
            elif choice == '2':
                player1 = input("Enter Player 1 name: ")
                player2 = input("Enter Player 2 name: ")
                result = input("Enter result (Player 1 name, Player 2 name, or 'draw'): ")
                self.record_match(player1, player2, result)
            elif choice == '3':
                self.display_standings()
            elif choice == '4':
                print("Exiting Chess League Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    league = ChessLeague()
    league.menu()
