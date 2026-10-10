from myproject import greet
from myproject.__main__ import main


def test_greet_default():
    assert greet() == "Hello, world!"


def test_greet_name():
    assert greet("Ada") == "Hello, Ada!"


def test_cli(capsys):
    assert main(["Ada"]) == 0
    assert capsys.readouterr().out.strip() == "Hello, Ada!"
