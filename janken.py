import random

CHOICES = ["グー", "チョキ", "パー"]
WIN_RULES = {
    ("グー", "チョキ"),
    ("チョキ", "パー"),
    ("パー", "グー"),
}


def judge(player: str, computer: str) -> str:
    if player == computer:
        return "あいこ"
    if (player, computer) in WIN_RULES:
        return "勝ち"
    return "負け"


def get_player_choice() -> str:
    while True:
        print("手を選んでください: グー / チョキ / パー")
        player = input("> ").strip()
        if player in CHOICES:
            return player
        print("無効な入力です。もう一度入力してください。")


def main() -> None:
    print("じゃんけんゲームへようこそ！")
    player = get_player_choice()
    computer = random.choice(CHOICES)
    result = judge(player, computer)

    print(f"あなた: {player}")
    print(f"コンピューター: {computer}")
    print(f"結果: {result}")


if __name__ == "__main__":
    main()
