import threading
import dis

if __name__ == "__main__":
    n = 0

    def foo():
        global n
        n += 1

    threads = []

    for i in range(100):
        t = threading.Thread(target=foo)
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()
    dis.dis(foo)
