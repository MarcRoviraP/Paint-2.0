# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/app.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(956, 717)
        MainWindow.setMinimumSize(QtCore.QSize(956, 717))
        MainWindow.setMaximumSize(QtCore.QSize(956, 717))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pintaArea = QtWidgets.QLabel(self.centralwidget)
        self.pintaArea.setGeometry(QtCore.QRect(10, 140, 931, 521))
        self.pintaArea.setStyleSheet("border: 1px solid black")
        self.pintaArea.setText("")
        self.pintaArea.setObjectName("pintaArea")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 10, 921, 78))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.opcions = QtWidgets.QComboBox(self.widget)
        self.opcions.setObjectName("opcions")
        self.opcions.addItem("")
        self.opcions.addItem("")
        self.opcions.addItem("")
        self.opcions.addItem("")
        self.opcions.addItem("")
        self.opcions.addItem("")
        self.opcions.addItem("")
        self.verticalLayout.addWidget(self.opcions)
        self.limpiar = QtWidgets.QPushButton(self.widget)
        self.limpiar.setObjectName("limpiar")
        self.verticalLayout.addWidget(self.limpiar)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 956, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Paint 2.0"))
        self.label.setText(_translate("MainWindow", "Tria una forma per a dibuixar:"))
        self.opcions.setItemText(0, _translate("MainWindow", "Punt"))
        self.opcions.setItemText(1, _translate("MainWindow", "Rectangle"))
        self.opcions.setItemText(2, _translate("MainWindow", "Rectangle arredonit"))
        self.opcions.setItemText(3, _translate("MainWindow", "El·lipsis"))
        self.opcions.setItemText(4, _translate("MainWindow", "Rectangles multiples"))
        self.opcions.setItemText(5, _translate("MainWindow", "Linies"))
        self.opcions.setItemText(6, _translate("MainWindow", "Text"))
        self.limpiar.setText(_translate("MainWindow", "Netejar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
