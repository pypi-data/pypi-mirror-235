from main import say_hello

def test1():
    assert say_hello() == 'Hello, World!'

def test2():
    assert say_hello("Nits") == 'Hello, Nits!'