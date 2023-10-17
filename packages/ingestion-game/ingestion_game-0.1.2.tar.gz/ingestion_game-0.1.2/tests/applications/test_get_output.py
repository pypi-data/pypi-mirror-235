from ingestion_game.application import get_output
from ingestion_game.domain import Rules


def test_get_output(
        new_rules: Rules,
) -> None:
    results = [
        {"food": "pizza", "id": 3, "name": "levy", "type": "A"},
        {"food": "fish", "id": 1, "more_noise": "bye", "name": "lima", "noise": "hello", "type": "B"},
        {"food": "sushi", "id": 10000, "name": "my_name", "type": "C"}
    ]
    expected = "id,name,food,type\n3,levy,pizza,A\n1,lima,fish,B\n10000,my_name,sushi,C\n"
    assert get_output(rules=new_rules, results=results) == expected
