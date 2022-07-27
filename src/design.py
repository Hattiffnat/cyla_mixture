# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_cyla(object):
    def setupUi(self, MainWindow_cyla):
        MainWindow_cyla.setObjectName("MainWindow_cyla")
        MainWindow_cyla.resize(693, 497)
        MainWindow_cyla.setMinimumSize(QtCore.QSize(200, 100))
        self.centralwidget = QtWidgets.QWidget(MainWindow_cyla)
        self.centralwidget.setMinimumSize(QtCore.QSize(100, 100))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.plainTextEdit_input = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Hack")
        self.plainTextEdit_input.setFont(font)
        self.plainTextEdit_input.setObjectName("plainTextEdit_input")
        self.verticalLayout.addWidget(self.plainTextEdit_input)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_gen_translite = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_gen_translite.setObjectName("pushButton_gen_translite")
        self.horizontalLayout.addWidget(self.pushButton_gen_translite)
        self.label_translite_shortcut = QtWidgets.QLabel(self.centralwidget)
        self.label_translite_shortcut.setAlignment(QtCore.Qt.AlignCenter)
        self.label_translite_shortcut.setObjectName("label_translite_shortcut")
        self.horizontalLayout.addWidget(self.label_translite_shortcut)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.plainTextEdit_output = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_output.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Hack")
        self.plainTextEdit_output.setFont(font)
        self.plainTextEdit_output.setReadOnly(True)
        self.plainTextEdit_output.setPlainText("")
        self.plainTextEdit_output.setObjectName("plainTextEdit_output")
        self.verticalLayout.addWidget(self.plainTextEdit_output)
        MainWindow_cyla.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_cyla)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_cyla)

    def retranslateUi(self, MainWindow_cyla):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_cyla.setWindowTitle(_translate("MainWindow_cyla", "Cyla Mixture"))
        self.pushButton_gen_translite.setText(_translate("MainWindow_cyla", "Generate translite"))
        self.pushButton_gen_translite.setShortcut(_translate("MainWindow_cyla", "Ctrl+Enter, Ctrl+Return"))
        self.label_translite_shortcut.setText(_translate("MainWindow_cyla", "Ctrl + Enter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_cyla = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_cyla()
    ui.setupUi(MainWindow_cyla)
    MainWindow_cyla.show()
    sys.exit(app.exec_())