# positional-only args
def wish(name='Guest', message='Hello', /):
    print(f"{message} {name}")


# wish(message='Hi', name="Anders")  # Keyword params
wish("Scott")
wish()
wish("Scott", "Hi")
