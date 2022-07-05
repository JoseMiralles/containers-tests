# Thread synchronization

Python uses thread synchronization to avoid issues. Blocks of code are marked as critical sections.

```
x = 0
my_lock = Lock()

def thread_1():
    with my_lock:
        a = x
        b = a + 1
        a = a + b
        x = a
        print(x)

def thread_2():
    with my_lock: // Will wait if thred_1 hasn't released the lock.
        a = x
        a = a + 1
        x = a
        print(x)
```

# Multi threading example

The following code would print different numbers seemingly randomly:

```
def func(_num: int) -> None:
        for _ in range(100):
            print(f"Thread {_num}")

for _i in range(9):
    threading.Thread(target=lambda:func(_i)).start()
```
Output:
```
...
Thread 3
Thread 6
Thread 2
Thread 3
Thread 6
Thread 2
Thread 3
Thread 6
Thread 2
Thread 3
Thread 6
Thread 8
...
```

To force them to print linearly, use a lock:

```
import threading

lock = threading.Lock()

def func(_num: int) -> None:
    with lock:
        for _ in range(100):
            print(f"Thread {_num}")

for _i in range(9):
    threading.Thread(target=lambda:func(_i)).start()
```

# Runing all threads as daemon

This will cause the threads to be ran in the background. But it will also interput them if the program is finished running before the threads are finished.

```
import threading

def func(_num: int) -> None:
        for _ in range(100):
            print(f"Thread {_num}")

for _i in range(9):
    threading.Thread(target=lambda:func(_i), daemon=True).start()
```

Use `thread.join()` to avoid daemon threads to be interrupted when the program finishes.

```
import threading

def func(_num: int) -> None:
        for _ in range(100):
            print(f"Thread {_num}")

for _i in range(9):
    thread = threading.Thread(target=lambda:func(_i), daemon=True)
    thread.start()
    thread.join()   #   <-------
```

# Using `lock.aquire()` and `lock.release()`

This is an alternative to `with lock:`

```
def func(_num: int) -> None:
    lock.acquire()  # <<<
    for _ in range(100):
        print(f"Thread {_num}")
    lock.release()  # <<<
```
Remember to release the lock.

