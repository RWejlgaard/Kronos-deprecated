import win32serviceutil
import win32service
import win32event
import servicemanager
import socket
import time
import logging
import kronos

__log_path__ = "C:\\Users\\z6zrw\\Kronos\\kronos.log"

logging.basicConfig(
    filename=__log_path__,
    level=logging.DEBUG,
    format='[kronos-service] %(levelname)-7.7s %(message)s'
)


class KronosSvc(win32serviceutil.ServiceFramework):
    _svc_name_ = "Kronos-Service"
    _svc_display_name_ = "Kronos Service"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.stop_event = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)
        self.stop_requested = False

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.stop_event)
        logging.info('Stopping service ...')
        self.stop_requested = True

    def SvcDoRun(self):
        servicemanager.LogMsg(
            servicemanager.EVENTLOG_INFORMATION_TYPE,
            servicemanager.PYS_SERVICE_STARTED,
            (self._svc_name_, '')
        )
        self.main()

    def main(self):
        kronos.main()
        return


def start():
    win32serviceutil.HandleCommandLine(KronosSvc)

