import threading
import time

# Code has 2 threads(multithreading) running simultaneously and with a 0,25 second pause in each thread.
# Code also has finds out how long each thread takes to execute


def sum_function(arr):
    print("Calculate the sum for the given numbers")
    summ = 0
    for n in arr:
        time.sleep(0.25)  # code waits for 0.25 seconds
        summ += n
    print("Sum is:", summ)


def difference(x, y):
    print("Calculate the difference for the given numbers")
    time.sleep(0.25)  # code waits for 0.25 seconds
    answer = x/y
    print("The difference is", answer)


my_array = [2, 3, 4, 5, 6]

T1 = threading.Thread(target=sum_function, args=(my_array,))
T1.start()
T1.join()
totalTime = time.time()  # gets the total execution time
print("Total execution time is:",  totalTime)
print("")
T2 = threading.Thread(target=difference, args=(10, 2))
T2.start()
T2.join()
print("Total execution time is:",  time.time() - totalTime)
