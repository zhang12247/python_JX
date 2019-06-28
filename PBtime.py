import time


class TimeView(object):
    def __init__(self):
        print("-------begin--------")
        start = time.perf_counter()
        end = time.perf_counter()
        print("-------end--------")
        print("wall time:{}", end - start)
