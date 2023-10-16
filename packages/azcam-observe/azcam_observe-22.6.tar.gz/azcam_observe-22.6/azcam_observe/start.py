"""
Contains the Observe class for Qt usage.
"""

import sys
import os

from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QApplication

import azcam
import azcam_console
from azcam_console.tools import create_console_tools
from azcam_observe.observe_qt.observe_qt import ObserveQt


def start():
    """
    Start observe for installed command "observe".
    """

    # app setup
    azcam.db.systemname = "observe"
    azcam.db.systemfolder = f"{os.path.dirname(__file__)}"

    try:
        i = sys.argv.index("-datafolder")
        datafolder = sys.argv[i + 1]
    except ValueError:
        datafolder = None

    if datafolder is None:
        droot = os.environ.get("AZCAM_DATAROOT")
        if droot is None:
            droot = "/data"
        azcam.db.datafolder = os.path.join(droot, azcam.db.systemname)
    else:
        azcam.db.datafolder = datafolder
    azcam.db.datafolder = azcam.utils.fix_path(azcam.db.datafolder)

    parfile = os.path.join(
        azcam.db.datafolder, "parameters", f"parameters_{azcam.db.systemname}.ini"
    )
    azcam.db.tools["parameters"].read_parfile(parfile)
    # azcam.db.tools["parameters"].update_pars( "observe")

    create_console_tools()
    server = azcam.db.tools["server"]
    port = 2442
    server.connect(port=port)

    logfile = os.path.join(azcam.db.datafolder, "logs", "console.log")
    azcam.db.logger.start_logging(logfile=logfile)

    if azcam.db.get("qtapp") is None:
        app = QCoreApplication.instance()
        if app is None:
            app = QApplication(sys.argv)
        azcam.db.qtapp = app

    observe = ObserveQt()
    observe.start()

    sys.exit(azcam.db.qtapp.exec())


if __name__ == "__main__":
    start()
