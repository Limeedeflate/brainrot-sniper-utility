import requests
import time
from colorama import Fore, Style, init

init(autoreset=True)

class Sniper:
    def __init__(self, game_id, interval=1.0):
        self.game_id = game_id
        self.interval = interval
        self.running = False

    def _fetch_players(self):
        try:
            resp = requests.get(
                f"https://games.roblox.com/v1/games/{self.game_id}/servers/Public",
                params={"limit": 100},
                timeout=5
            )
            resp.raise_for_status()
            data = resp.json()
            total = sum(srv.get("playing", 0) for srv in data.get("data", []))
            return total
        except Exception:
            return -1

    def start(self, target_count=50):
        self.running = True
        print(f"{Fore.CYAN}[*] Sniping game {self.game_id} | Target: {target_count} players")
        while self.running:
            players = self._fetch_players()
            if players >= 0:
                bar = "#" * min(players, 100) + "-" * max(0, 100 - players)
                print(f"\r{Fore.YELLOW}[{players:>4}] |{bar}| ", end="", flush=True)
                if players >= target_count:
                    print(f"\n{Fore.GREEN}[!] Target reached! {players} players online.")
                    self.running = False
            time.sleep(self.interval)

    def stop(self):
        self.running = False