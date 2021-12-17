from threading import Thread
import threading


def print_numbers():
    for n in range(1, 11):
        print(f"Child --> {n}")


print(threading.current_thread())

ct = Thread(target=print_numbers)
ct.start()

for n in range(1, 11):
    print(f"Main -> {n}")
