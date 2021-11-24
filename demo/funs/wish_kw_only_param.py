# Keyword-only args
def wish(*, message='Hello', name='Guest'):
    print(f"{message} {name}")


wish(message='Hi', name="Anders")  # Keyword params
# wish("Scott")
wish()
wish(message='Good Morning')
