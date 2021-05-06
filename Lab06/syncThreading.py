import threading
import time

# Code has 2 threads(multithreading) running simultaneously and with a 0,25 second pause in each thread.
# Code also has finds out how long each thread takes to execute
# Code is sync'd that the sum_function starts first then the difference function comes in after the other started


def sum_function(arr):
    print("Calculate the sum for the given numbers\n")
    summ = 0
    for n in arr:
        time.sleep(0.25)  # code waits for 0.25 seconds
        summ += n
    print("Sum is:", summ)


def difference(x, y):
    print("Calculate the difference for the given numbers\n")
    time.sleep(0.25)  # code waits for 0.25 seconds
    answer = x/y
    print("The difference is", answer)


my_array = [2, 3, 4, 5, 6]

T1 = threading.Thread(target=sum_function, args=(my_array,))
T2 = threading.Thread(target=difference, args=(10, 2))
T1.start()
total_time = time.time()  # gets the total execution time
print("Total sum_function execution time is:", total_time)

T2.start()

T1.join()

T2.join()
print("Total difference execution time is:", time.time() - total_time)



