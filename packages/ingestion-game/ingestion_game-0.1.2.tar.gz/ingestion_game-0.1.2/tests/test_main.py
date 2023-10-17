import pytest
from click.testing import CliRunner

from ingestion_game.main import main


def test_main_example(
        new_important_keys: str,
        new_hierarchy: str,
        path_input_txt: str,
) -> None:
    runner = CliRunner()
    result = runner.invoke(main, args=[new_important_keys, new_hierarchy, path_input_txt])
    assert result.exit_code == 0
    expected = "id,name,food,type\n3,levy,pizza,A\n1,lima,fish,B\n10000,my_name,sushi,C\n"
    assert result.output == expected


@pytest.mark.parametrize(
    "important_keys, hierarchy, expected",
    [
        (
                "id:int,name:str",
                "A,B,C",
                "id,name\n3,levy\n1,lima\n10000,my_name\n"
        ),
        (
                "id:int,name:str,food:str,type:str",
                "A",
                "id,name,food,type\n3,levy,pizza,A\n1,name,vegetables,A\n10,lemon,lemonade,A\n"
        ),
        (
                "id:int,name:str,food:str,type:str",
                "A,D",
                "id,name,food,type\n3,levy,pizza,A\n1,name,vegetables,A\n10,lemon,lemonade,A\n"
        ),
        (
                "id:int,name:str,food:str,type:str",
                "B,A",
                "id,name,food,type\n3,levy,pizza,A\n1,name,vegetables,A\n10,lemon,lemonade,A\n"
        ),
        (
                "id:int,name:str,food:str,type:str",
                "B,A,C",
                "id,name,food,type\n3,levy,pizza,A\n1,name,vegetables,A\n10000,my_name,sushi,C\n"
        ),
    ]
)
def test_main_1(
        important_keys: str,
        hierarchy: str,
        expected: str,
        path_input_txt: str,
) -> None:
    runner = CliRunner()
    result = runner.invoke(main, args=[important_keys, hierarchy, path_input_txt])
    assert result.exit_code == 0
    assert result.output == expected
