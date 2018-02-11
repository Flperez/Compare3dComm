from PyQt5.QtWidgets import QWidget,QCheckBox,QPushButton,QLineEdit,QVBoxLayout
from PyQt5.QtCore import Qt,pyqtSignal
import jderobot
import numpy as np
import sys,os
from OpenGL.GL import *
from OpenGL.GLU import *
import threading
from widgetplot import MyplotXYZ,MyplotRPY,MyDynamicMplCanvas



class MainWindow(QWidget):
    updGUI = pyqtSignal()
    def __init__(self,map):

        super(MainWindow, self).__init__()
        self.updGUI.connect(self.updateGUI)

        self.pose3dsim_list = []
        self.pose3dreal_list = []


        self.initUI(map=map)
        self.myplot()


    def initUI(self,map):
        ### initialize
        self.filename = map



        self.loadpathXYZ()


        ### Text out
        self.textbox = QLineEdit(self)
        self.textbox.move(20,480+10)
        self.textbox.resize(640,80)



        ### To select a different graph
        self.showNow = "showXYZ"
        
        ## XYZ
        self.cbxyz = QCheckBox('Show XYZ', self)
        self.cbxyz.move(640+40, 100)
        self.cbxyz.toggle()
        self.cbxyz.setChecked(True)
        self.cbxyz.stateChanged.connect(self.showXYZ)

        ## RPY
        self.cbRPY = QCheckBox('Show RPY', self)
        self.cbRPY.move(640+40, 200)
        self.cbRPY.toggle()
        self.cbRPY.setChecked(False)
        self.cbRPY.stateChanged.connect(self.showRPY)

        ## Error
        self.cbError = QCheckBox('Show Error', self)
        self.cbError.move(640+40, 300)
        self.cbError.toggle()
        self.cbError.setChecked(False)
        self.cbError.stateChanged.connect(self.showError)



        ### Saving results
        ButtonSave = QPushButton('Save results', self)
        ButtonSave.setCheckable(True)
        ButtonSave.move(640+50, 480+30)
        ButtonSave.clicked[bool].connect(self.savingResult)




        self.setGeometry(600, 600, 250, 150)
        self.setWindowTitle('Compare')
        self.setFixedSize(10+640+20+150,600)

    def myplot(self):
        self.main_widget = QWidget(self)
        l = QVBoxLayout(self.main_widget)
        self.dc = MyDynamicMplCanvas(parent=self.main_widget, option=self.showNow,
                                     map=self.map,
                                     poseEst=self.pose3dsim_list,poseReal=self.pose3dreal_list)
        l.addWidget(self.dc)

    def showXYZ(self,state):
        if state == Qt.Checked:
            self.textbox.setText("You have selected show XYZ graph")
            self.showNow = "showXYZ"
            self.dc.setOption(self.showNow)

            self.cbRPY.setChecked(False)
            self.cbError.setChecked(False)

    def showRPY(self, state):
        if state == Qt.Checked:
            self.textbox.setText("You have selected show RPY graph")
            self.showNow = "showRPY"
            self.cbxyz.setChecked(False)
            self.cbError.setChecked(False)
            self.dc.setOption(self.showNow)



            

    def showError(self, state):
        if state == Qt.Checked:
            self.textbox.setText("You have selected show error graph")
            self.showNow = "showError"
            self.dc.setOption(self.showNow)
            self.cbxyz.setChecked(False)
            self.cbRPY.setChecked(False)

            
    def savingResult(self):
        self.textbox.setText("Saving result...")


        self.textbox.setText("Done!")

    def setPose3Dsim(self,pose):
        self.pose3dEstimated_client = pose


    def setPose3dreal(self,pose):
        self.pose3dReal_client = pose


    def updateGUI(self):
        self.pose3dsim=self.pose3dReal_client.getPose3d()
        self.pose3dsim_list.append(self.pose3dsim)
        self.pose3dReal=self.pose3dEstimated_client.getPose3d()
        self.pose3dreal_list.append(self.pose3dReal)





    def loadpathXYZ(self):
        a=[]

        for line in open(self.filename, 'r').readlines():
            line = line.rstrip('\n')
            linelist = line.split()
            if len(linelist)>1:
                pose = jderobot.Pose3DData()
                pose.x = float(linelist[0])
                pose.y = float(linelist[1])
                pose.z = float(linelist[2])
                a.append(pose)

        self.map = list(a)







