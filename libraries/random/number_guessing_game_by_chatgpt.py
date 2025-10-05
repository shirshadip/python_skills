
# Number Guessing Game (CLI)
# Features:
# - Difficulty levels (Easy/Medium/Hard or custom)
# - Limited attempts with higher/lower hints and "close" indicator
# - Input validation (integers only) and 'q' to quit mid-game
# - Replay loop
# - Simple high score tracking per difficulty saved to highscores.json
#
# Run: python number_guessing_game.py

import random
import json
from pathlib import Path

HIGHSCORE_FILE = Path(__file__).with_name("highscores.json")

DIFFICULTIES = {
    "1": {"name": "Easy", "low": 1, "high": 50, "attempts": 10},
    "2": {"name": "Medium", "low": 1, "high": 100, "attempts": 7},
    "3": {"name": "Hard", "low": 1, "high": 200, "attempts": 5},
    "4": {"name": "Custom", "low": None, "high": None, "attempts": None},
}


def load_highscores():
    if HIGHSCORE_FILE.exists():
        try:
            with open(HIGHSCORE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def save_highscores(scores):
    try:
        with open(HIGHSCORE_FILE, "w", encoding="utf-8") as f:
            json.dump(scores, f, indent=2)
    except Exception as e:
        print(f"[!] Could not save highscores: {e}")


def pick_difficulty():
    print("\nChoose difficulty:")
    for key, cfg in DIFFICULTIES.items():
        if cfg["name"] == "Custom":
            print(f"  {key}. {cfg['name']} (you choose range & attempts)")
        else:
            print(f"  {key}. {cfg['name']} ({cfg['low']}-{cfg['high']}, {cfg['attempts']} attempts)")

    while True:
        choice = input("Enter 1/2/3/4: ").strip()
        if choice in DIFFICULTIES:
            cfg = DIFFICULTIES[choice].copy()
            if cfg["name"] == "Custom":
                cfg["low"] = ask_int("  Lowest number? ", minimum=None)
                cfg["high"] = ask_int(f"  Highest number (>{cfg['low']})? ", minimum=cfg["low"] + 1)
                cfg["attempts"] = ask_int("  How many attempts? ", minimum=1)
            return cfg
        print("Invalid choice. Try again.")


def ask_int(prompt, minimum=None, maximum=None):
    while True:
        raw = input(prompt).strip()
        if raw.lower() == "q":
            raise KeyboardInterrupt
        try:
            val = int(raw)
            if minimum is not None and val < minimum:
                print(f"Enter a value \u2265 {minimum}.")
                continue
            if maximum is not None and val > maximum:
                print(f"Enter a value \u2264 {maximum}.")
                continue
            return val
        except ValueError:
            print("Please enter a valid integer (or 'q' to quit).")


def feedback(secret, guess):
    diff = abs(secret - guess)
    if guess < secret:
        relation = "Too low"
    elif guess > secret:
        relation = "Too high"
    else:
        return "Correct!"

    if diff <= 3:
        hint = "🔥 Very close!"
    elif diff <= 10:
        hint = "✨ Close."
    else:
        hint = ""
    return f"{relation}. {hint}".strip()


def play_round(cfg, scores):
    low, high, attempts = cfg["low"], cfg["high"], cfg["attempts"]
    secret = random.randint(low, high)

    print(f"\nI'm thinking of a number between {low} and {high}.")
    print(f"You have {attempts} attempts. Type 'q' anytime to quit. Good luck!\n")

    for turn in range(1, attempts + 1):
        try:
            guess = ask_int(f"Attempt {turn}/{attempts} - Your guess: ", minimum=low, maximum=high)
        except KeyboardInterrupt:
            print("\nYou quit the round. The number was:", secret)
            return None  # no score
        result = feedback(secret, guess)
        if result == "Correct!":
            print("🎉 Correct! You guessed it in", turn, "attempt(s).")
            # Update highscores
            key = f"{cfg['name']}:{low}-{high}:{attempts}"
            best = scores.get(key)
            if best is None or turn < best:
                scores[key] = turn
                print("🏆 New high score for this difficulty!")
            return turn
        else:
            print(result)

    print(f"\nOut of attempts! The number was: {secret}")
    return None  # didn’t guess


def show_highscores(scores):
    if not scores:
        print("No highscores yet. Be the first!\n")
        return
    print("\n=== Highscores ===")
    # Sort by attempts then key
    for key, val in sorted(scores.items(), key=lambda kv: (kv[1], kv[0])):
        name, rng, tries = key.split(":")
        print(f"{name:6} | Range {rng:>9} | Attempts {tries:>3} | Best: {val}")
    print()


def main():
    print("=== Number Guessing Game ===")
    scores = load_highscores()
    show_highscores(scores)

    while True:
        cfg = pick_difficulty()
        try:
            play_round(cfg, scores)
        except KeyboardInterrupt:
            print("\nExiting... Bye!")
            break

        save_highscores(scores)

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break

    save_highscores(scores)


if __name__ == "__main__":
    main()
