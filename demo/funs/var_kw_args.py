def wish(*names, **args):
    for n in names:
        print(f"Hello {n}")

    for name, msg in args.items():
        print(f"{msg} {name}")


wish("Scott", "Rudy", Anders="Hi", Joe="Hello")
