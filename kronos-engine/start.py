import api
import sys,os


def start():
    if os.name == 'nt':
        import win_service
        win_service.start()
    else:
        import unix_service
        unix_service.Daemon('/tmp/kronos.pid').start()


if __name__ == '__main__':
    start()