class A:
    def process(self):
        print("Process in A")


class B:
    def process(self):
        print("Process in B")


class C(B, A):
    pass


obj = C()
obj.process()
