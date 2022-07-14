import threading

lock = threading.Lock()

def func(_num: int) -> None:
    lock.acquire()
    for _ in range(100):
        print(f"Thread {_num}")
    lock.release()

for _i in range(9):
    thread = threading.Thread(target=lambda:func(_i), daemon=True)
    thread.start()
    thread.join()
