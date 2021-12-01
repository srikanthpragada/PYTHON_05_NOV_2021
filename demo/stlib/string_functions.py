import sys


def samechars(st1, st2):
    return sorted(set(st1)) == sorted(set(st2))


if __name__ == '__main__':
    print(samechars(sys.argv[1], sys.argv[2]))
