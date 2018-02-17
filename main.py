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
    if len(sys.argv)>2:
        file_world = sys.argv[2]
    else:
        file_world = None


    # starting comm
    jdrc = comm.init(cfg, "compare3d")
    x = jdrc.getConfig()

    pose_real = jdrc.getPose3dClient("compare3d.Pose3DReal")
    pose_sim = jdrc.getPose3dClient("compare3d.Pose3DEstimated")

    app = QApplication(sys.argv)
    frame = MainWindow(file_world=file_world)
    frame.setPose3Dsim(pose_sim)
    frame.setPose3dreal(pose_real)
    frame.show()

    t2 = ThreadGui(frame)
    t2.daemon = True
    t2.start()

    sys.exit(app.exec_())