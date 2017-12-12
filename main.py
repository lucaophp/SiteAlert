# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created: Tue Dec 12 14:26:25 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import sys
import os.path
import time
import re

class Ui_Dialog(QtGui.QMainWindow):
    
    def setupUi(self, Dialog):
        try:
            os.remove('start.ps')
        except: pass
        try:

            os.remove('yes.ps')
            os.remove('com.ps')

        except: pass
        self.setObjectName("Dialog")
        self.resize(386, 288)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.txtURL = QtGui.QLineEdit(self)
        self.txtURL.setGeometry(QtCore.QRect(10, 40, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setWeight(50)
        font.setBold(False)
        self.txtURL.setFont(font)
        self.txtURL.setObjectName("txtURL")
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 20, 101, 16))
        self.label.setObjectName("label")
        self.txtTime = QtGui.QLineEdit(self)
        self.txtTime.setGeometry(QtCore.QRect(10, 140, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setWeight(50)
        font.setBold(False)
        self.txtTime.setFont(font)
        self.txtTime.setObjectName("txtTime")
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 171, 16))
        self.label_2.setObjectName("label_2")
        self.btnStop = QtGui.QPushButton(self)
        self.btnStop.setGeometry(QtCore.QRect(80, 250, 75, 23))
        self.btnStop.setObjectName("btnStop")
        self.btnStart = QtGui.QPushButton(self)
        self.btnStart.setGeometry(QtCore.QRect(220, 250, 75, 23))
        self.btnStart.setObjectName("btnStart")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.events()

    def init(self):
        try:
            os.remove('yes.ps')
        except:
            pass
        with open('com.ps','w') as fp:
            fp.write('Are you Alive?')
        timeInit = time.time()
        while not(os.path.isfile('yes.ps')) and time.time()-timeInit<5: pass
        if not(os.path.isfile('yes.ps')):
            try:
                os.remove('com.ps')
            except: pass
            import subprocess
            print('Nao foi possivel iniciar o processo')
            str_cmd = sys.executable+' ppg.py' if not re.match("win{1}.*", os.sys.platform) is None else 'python ppg.py' 
            
            independent_process = subprocess.Popen(
                str_cmd,
                creationflags=subprocess.CREATE_NEW_PROCESS_GROUP
            )
        try:
            os.remove('yes.ps')
        except: pass

        with open("start.ps",'w') as fp:
            fp.write(self.txtURL.text()+"\n")
            fp.write(self.txtTime.text()+"\n")
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Information)
        msg.setText(u"O serviço iniciado!!!")
        msg.setInformativeText(u"O monitoramento do site %s, foi iniciado!!!"%self.txtURL.text())
        msg.setWindowTitle("Sucesso")
        msg.exec_()


    def stop(self):
        with open('start.ps','w') as fp:
            fp.write("PARAR")
        timeInit = time.time()
        while os.path.isfile('start.ps') and time.time()-timeInit<5: pass
        if os.path.isfile('start.ps'):
            try:
                os.remove('start.ps')
                print('Nao possui nenhum processo ativo!!!')
                msg = QtGui.QMessageBox()
                msg.setIcon(QtGui.QMessageBox.Information)
                msg.setText("Nenhum processo ativo!!!")
                msg.setInformativeText("Nenhum site está sendo monitorado, no memento!!!")
                msg.setWindowTitle("Processos Ativos")
                
                msg.exec_()

            except: pass
        else:
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Information)
            msg.setText("O serviço foi encerrado!!!")
            msg.setInformativeText("O monitoramento de site, foi encerrado!!!")
            msg.setWindowTitle("Sucesso")
            msg.exec_()
            



    def events(self):
        self.btnStart.clicked.connect(self.init)
        self.btnStop.clicked.connect(self.stop)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "SiteAlarm", None, QtGui.QApplication.UnicodeUTF8))
        self.txtURL.setText(QtGui.QApplication.translate("Dialog", "http://", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Site monitorado:", None, QtGui.QApplication.UnicodeUTF8))
        self.txtTime.setText(QtGui.QApplication.translate("Dialog", "60", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Tempo de espera(em segundos):", None, QtGui.QApplication.UnicodeUTF8))
        self.btnStop.setText(QtGui.QApplication.translate("Dialog", "Parar", None, QtGui.QApplication.UnicodeUTF8))
        self.btnStart.setText(QtGui.QApplication.translate("Dialog", "Iniciar", None, QtGui.QApplication.UnicodeUTF8))

app = QtGui.QApplication(sys.argv)
my_win = Ui_Dialog()
my_win.setWindowIcon(QtGui.QIcon('icon.ico'))
my_win.setupUi(None)
my_win.show()
sys.exit(app.exec_())

