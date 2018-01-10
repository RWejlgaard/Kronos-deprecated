import api
import sys,os


def main():
    if os.name == 'nt':
        import win_service
        service = win_service.AppServerSvc()
    else:
        import unix_service
        service = unix_service.Daemon('/tmp/kronos.pid')

    class uni_service(service):
        @classmethod
        def run(cls):
            api.launch()

    service.start()


if __name__ == '__main__':
    main()