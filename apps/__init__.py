from .app01 import server as app01_server


def run_server(name, sock):
    if name == 'app01':
        app01_server.run(sock)
    else:
        raise ImportError('Don\'t found server name: {}'.format(name))