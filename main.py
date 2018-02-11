import sys

import comm
import config

import signal
from PyQt5.QtWidgets import QApplication
from gui.GUI import MainWindow
from gui.threadgui import ThreadGui

signal.signal(signal.SIGINT, signal.SIG_DFL)

if __name__ == '__main__':
    cfg = config.load(sys.argv[1])

    # starting comm
    jdrc = comm.init(cfg, "compare3d")


    pose_real = jdrc.getPose3dClient("compare3d.Pose3DReal")
    pose_sim = jdrc.getPose3dClient("compare3d.Pose3DEstimated")

    app = QApplication(sys.argv)
    frame = MainWindow(map="markers.txt")
    frame.setPose3Dsim(pose_sim)
    frame.setPose3dreal(pose_real)
    frame.show()

    t2 = ThreadGui(frame)
    t2.daemon = True
    t2.start()

    sys.exit(app.exec_())


