def wish(*names, message='Hi'):
    for n in names:
        print(f"{message} {n}")


wish("Anders", "Joe")
wish("Jack", "Mark", message="Hello")
