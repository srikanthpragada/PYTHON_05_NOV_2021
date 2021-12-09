a = 100  # Global variable


def f1():
    global a
    a = a + 1
    b = 200  # Enclosing variable
    print('In f1')
    print(a)

    # local function
    def f2():
        nonlocal b
        b = 300  # Local variable
        print('In f2')
        print(a, b)

    f2()
    print(b)


f1()
