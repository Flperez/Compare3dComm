from matplotlib import pyplot as plt
from operator import attrgetter
from math import sqrt
import argparse
import os, time
import sys
import numpy as np




if __name__=="__main__":

    #### Load data ####
    path_to_result = sys.argv[1]

    path_pose3dreal_list = os.path.join(path_to_result,"pose3dreal_list.npy")
    path_pose3sim_list = os.path.join(path_to_result,"pose3dreal_list.npy")
    path_pose3Error_list = os.path.join(path_to_result, "pose3dError_list.npy")

    print "Print the season: ",time.ctime(os.path.getctime(path_pose3Error_list))
    Pose_real = np.load(path_pose3dreal_list)
    Pose_estimated = np.load(path_pose3sim_list)
    Error = np.load(path_pose3Error_list)



    ### Split data
    PosRealx = list(map(attrgetter('x'), Pose_real))
    PosRealy = list(map(attrgetter('y'), Pose_real))
    PosRealz = list(map(attrgetter('z'), Pose_real))

    PosRealR = list(map(attrgetter('roll'), Pose_real))
    PosRealY = list(map(attrgetter('yaw'), Pose_real))
    PosRealP = list(map(attrgetter('pitch'), Pose_real))

    PosEstx = list(map(attrgetter('x'), Pose_estimated))
    PosEsty = list(map(attrgetter('y'), Pose_estimated))
    PosEstz = list(map(attrgetter('z'), Pose_estimated))

    PosEstR = list(map(attrgetter('roll'), Pose_estimated))
    PosEstY = list(map(attrgetter('yaw'), Pose_estimated))
    PosEstP = list(map(attrgetter('pitch'), Pose_estimated))

    Errorx = list(map(attrgetter('x'), Error))
    Errory = list(map(attrgetter('y'), Error))
    Errorz = list(map(attrgetter('z'), Error))

    ErrorR = list(map(attrgetter('roll'), Error))
    ErrorY = list(map(attrgetter('yaw'), Error))
    ErrorP = list(map(attrgetter('pitch'), Error))


    ErrornormXYZ=[sqrt(Errorx[i]**2+Errory[i]**2+Errorz[i]**2) for i in range(0,len(Errorx))]
    ErrornormRYP=[sqrt(ErrorR[i]**2+ErrorY[i]**2+ErrorP[i]**2) for i in range(0,len(Errorx))]

    ######### Figure 1 #####################

    #### XYZ real y estimado
    plt.plot(PosRealx,PosRealy,PosEstx,PosEsty),\
    plt.title("Real vs estimated")
    plt.xlabel("x(m)")
    plt.ylabel("y(m)")
    plt.grid()

    plt.show()

    # # ######### Figure 2 #####################
    fig2, axarr = plt.subplots(3, sharex=True)

    # ### Angulo RPY
    t = np.linspace(0,len(PosRealR),len(PosRealR))
    axarr[0].plot(t,PosRealR,label="PosReal"),axarr[0].plot(t,PosEstR,label="PosEst"),axarr[0].set_title("Roll")
    axarr[0].legend(loc='upper left'),axarr[0].grid()
    axarr[1].plot(t,PosRealY,label="PosReal"),axarr[1].plot(t,PosEstY,label="PosEst"),axarr[1].set_title("Yaw")
    axarr[1].legend(loc='upper left'),axarr[1].grid()
    axarr[2].plot(t,PosRealP,label="PosReal"),axarr[2].plot(t,PosEstP,label="PosEst"),axarr[2].set_title("Pitch")
    axarr[2].legend(loc='upper left'),axarr[2].grid()

    plt.show()
    # ######### Figure 3 #####################
    fig3, axarr = plt.subplots(3, sharex=True)

    #### XYZ real y estimado
    axarr[0].plot(t, Errorx),axarr[0].set_title("Error x"),axarr[0].grid()
    axarr[1].plot(t, Errory),axarr[1].set_title("Error y"),axarr[1].grid()
    axarr[2].plot(t, Errorz),axarr[2].set_title("Error z"),axarr[2].grid()
    # #
    plt.show()
    ######### Figure 4 #####################
    fig4, axarr = plt.subplots(3, sharex=True)

    ### Angulo RPY
    axarr[0].plot(t, ErrorR),axarr[0].set_title("Error Roll"),axarr[0].grid()
    axarr[1].plot(t, ErrorP),axarr[1].set_title("Error Pitch"),axarr[1].grid()
    axarr[2].plot(t, ErrorY),axarr[2].set_title("Error yaw"),axarr[2].grid()

    plt.show()
    # ######### Figure 5 #####################
    fig5, axarr = plt.subplots(2, sharex=True)

    ### Angulo RPY
    axarr[0].plot(t, ErrornormXYZ),axarr[0].set_title("Error cuadratico medio XYZ"),axarr[0].grid()
    axarr[1].plot(t, ErrornormRYP),axarr[1].set_title("Error cuadratico medio RPY"),axarr[1].grid()

    plt.show()