import time
import zmq


def run():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.bind('tcp://*:6666')

    cnt = 1

    while True:
        time.sleep(1)
        # socket.send_string('server cnt {}'.format(cnt))
        socket.send_string('server')
        print('send {}'.format(cnt))
        cnt += 1


if __name__ == '__main__':
    run()
