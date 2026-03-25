from unittest.mock import patch

import janken


def test_judge_draw():
    assert janken.judge("グー", "グー") == "あいこ"


def test_judge_win_patterns():
    assert janken.judge("グー", "チョキ") == "勝ち"
    assert janken.judge("チョキ", "パー") == "勝ち"
    assert janken.judge("パー", "グー") == "勝ち"


def test_judge_lose_patterns():
    assert janken.judge("グー", "パー") == "負け"
    assert janken.judge("チョキ", "グー") == "負け"
    assert janken.judge("パー", "チョキ") == "負け"


def test_get_player_choice_retries_until_valid(capsys):
    with patch("builtins.input", side_effect=["ほげ", "チョキ"]):
        choice = janken.get_player_choice()

    captured = capsys.readouterr()
    assert choice == "チョキ"
    assert "無効な入力です。もう一度入力してください。" in captured.out
