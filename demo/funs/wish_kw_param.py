def wish(name, message):
    print(f"{message} {name}")


wish(message='Hi', name="Anders")  # Keyword params
wish("Scott", "Good Morning")  # positional params
wish("Mark", message='Hello')
