import sys
from src import Sniper, find_brainrot_games
from colorama import Fore, Style, init

init(autoreset=True)

def main():
    print(f"{Fore.MAGENTA}=== Brainrot Sniper Utility ==={Style.RESET_ALL}")
    print(f"{Fore.CYAN}[1] Find brainrot games")
    print(f"{Fore.CYAN}[2] Snipe a game by ID")
    choice = input(f"{Fore.WHITE}Select option (1/2): ").strip()

    if choice == "1":
        games = find_brainrot_games(max_games=20)
        if not games:
            print(f"{Fore.RED}No brainrot games found.")
            return
        print(f"\n{Fore.GREEN}Found {len(games)} brainrot games:\n")
        for i, g in enumerate(games[:10], 1):
            print(f"{i}. {Fore.YELLOW}{g['name']} {Fore.WHITE}(ID: {g['id']}) - {g['player_count']} players")
        print()
    elif choice == "2":
        game_id = input(f"{Fore.WHITE}Enter game ID: ").strip()
        if not game_id.isdigit():
            print(f"{Fore.RED}Invalid ID.")
            return
        target = input(f"{Fore.WHITE}Target player count (default 50): ").strip()
        target = int(target) if target.isdigit() else 50
        sniper = Sniper(int(game_id))
        try:
            sniper.start(target_count=target)
        except KeyboardInterrupt:
            sniper.stop()
            print(f"\n{Fore.RED}Sniping stopped.")
    else:
        print(f"{Fore.RED}Invalid option.")

if __name__ == "__main__":
    main()