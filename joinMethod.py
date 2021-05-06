import threading
# very rudimentary multithreading concept 


def hello(n):
    print("Random words, blah blah blah, you deserve to get paid:", n)


T1 = threading.Thread(target=hello, args=(0,))
T1.start()
T1.join()

print("Successful code")
