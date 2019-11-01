import time
import socket
import argparse

from multiprocessing import Process
from configs import bases
from tests import run_test


def get_sock(host, port):
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.set_inheritable(True)
    return sock


def get_args():
    parser = argparse.ArgumentParser(description='aiohttp server')
    parser.add_argument('--run', action='store_true', default=False)
    parser.add_argument('--ip', type=str, default='127.0.0.1', dest='ip', help='server ip. (default: 127.0.0.1)')
    parser.add_argument('--port', type=int, default=8000, dest='port', help='server port. (default: 8000)')
    parser.add_argument('--process-cnt', type=int, default=1, dest='process_cnt', help='process count. (default: 1)')
    parser.add_argument('--server-name', type=str, dest='server_name',
                        choices=['app01'],
                        default='app1', help='server name, default server is app1')
    parser.add_argument('--test', action='store_true', default=False)
    parser.add_argument('--test-module', type=str, dest='test_module', choices=bases.MODULES, default='all',
                        help='test module name, default test all')

    argv = parser.parse_args()
    if not argv.run and not argv.test:
        parser.print_help()
    return argv


def manage_process(argv):
    bases.SERVICE_TYPE = argv.server_name

    from apps import run_server

    process_dict = {}
    sock = get_sock(argv.ip, argv.port)
    process_cnt = argv.process_cnt
    if process_cnt < 1:
        process_cnt = 1
    while True:
        start_process_cnt = process_cnt - len(process_dict)

        for _ in range(start_process_cnt):
            p = Process(target=run_server, args=(argv.server_name, sock))
            p.daemon = True
            p.start()
            process_dict[p.pid] = p
            print('start service pid:', p.pid)

        pids = list(process_dict.keys())
        for pid in pids:
            if not process_dict[pid].is_alive():
                process_dict.pop(pid)
        time.sleep(5)

    for (_, p) in process_dict.items():
        p.join()

    for (_, p) in process_dict.items():
        p.terminate()


def main():
    argv = get_args()

    if not argv.run and not argv.test:
        return 0

    if argv.test:
        run_test(argv.test_module)
        return 0

    print('run {} server at: http://{}:{}'.format(argv.server_name, argv.ip, argv.port))
    manage_process(argv)


if __name__ == "__main__":
    main()
