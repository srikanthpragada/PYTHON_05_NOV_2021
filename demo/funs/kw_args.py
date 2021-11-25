def wish(**args):
    for name, msg in args.items():
        print(f"{msg} {name}")


wish(anders="hi", joe="Hello", bill="Good Morning")
