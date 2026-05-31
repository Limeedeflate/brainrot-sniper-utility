import requests

BRAINROT_KEYWORDS = [
    "brainrot", "skibidi", "rizz", "sigma", "fanum", "gyat", "ohio",
    "edging", "mewing", "looksmaxxing", "mogging", "alpha", "beta"
]

def find_brainrot_games(max_games=20):
    try:
        resp = requests.get(
            "https://games.roblox.com/v1/games/list",
            params={"limit": max_games, "sortOrder": "Desc"},
            timeout=5
        )
        resp.raise_for_status()
    except Exception:
        return []

    games = resp.json().get("data", [])
    matches = []
    for game in games:
        name = game.get("name", "").lower()
        desc = game.get("description", "").lower()
        combined = name + " " + desc
        if any(kw in combined for kw in BRAINROT_KEYWORDS):
            matches.append({
                "id": game["id"],
                "name": game["name"],
                "description": game.get("description", ""),
                "player_count": game.get("playing", 0)
            })
    return matches