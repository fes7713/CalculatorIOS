# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(413, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius: 20px;")
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.title_bar_frame = QtWidgets.QFrame(self.main_frame)
        self.title_bar_frame.setMaximumSize(QtCore.QSize(16777215, 30))
        self.title_bar_frame.setStyleSheet("background-color: transparent;")
        self.title_bar_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title_bar_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_bar_frame.setObjectName("title_bar_frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.title_bar_frame)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.title_bar_container = QtWidgets.QFrame(self.title_bar_frame)
        self.title_bar_container.setMaximumSize(QtCore.QSize(16777215, 70))
        self.title_bar_container.setStyleSheet("background-color: transparent;")
        self.title_bar_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title_bar_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_bar_container.setObjectName("title_bar_container")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.title_bar_container)
        self.horizontalLayout_8.setContentsMargins(30, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.title_bar = QtWidgets.QLabel(self.title_bar_container)
        self.title_bar.setStyleSheet("font: bold 20px;\n"
"color: rgb(250, 250, 250);")
        self.title_bar.setObjectName("title_bar")
        self.horizontalLayout_8.addWidget(self.title_bar)
        self.horizontalLayout_6.addWidget(self.title_bar_container)
        self.tool_box = QtWidgets.QFrame(self.title_bar_frame)
        self.tool_box.setMaximumSize(QtCore.QSize(150, 150))
        self.tool_box.setStyleSheet("background-color: transparent;")
        self.tool_box.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tool_box.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tool_box.setObjectName("tool_box")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.tool_box)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.minimizeButton = QtWidgets.QPushButton(self.tool_box)
        self.minimizeButton.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"\n"
"    font: 35px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(85, 85, 255);\n"
"    border-color: rgb(180, 180, 180);\n"
"}")
        self.minimizeButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/Assets/minimize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimizeButton.setIcon(icon)
        self.minimizeButton.setObjectName("minimizeButton")
        self.horizontalLayout_9.addWidget(self.minimizeButton)
        self.restoreButton = QtWidgets.QPushButton(self.tool_box)
        self.restoreButton.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"\n"
"    font: 35px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(170, 255, 127);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(0, 170, 127);\n"
"    border-color: rgb(180, 180, 180);\n"
"}")
        self.restoreButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/Assets/fullscreen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.restoreButton.setIcon(icon1)
        self.restoreButton.setObjectName("restoreButton")
        self.horizontalLayout_9.addWidget(self.restoreButton)
        self.closeButton = QtWidgets.QPushButton(self.tool_box)
        self.closeButton.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"\n"
"    font: 35px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: ;\n"
"    background-color: rgb(255, 85, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(208, 0, 0);\n"
"    border-color: rgb(180, 180, 180);\n"
"}")
        self.closeButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/Assets/X.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeButton.setIcon(icon2)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_9.addWidget(self.closeButton)
        self.horizontalLayout_6.addWidget(self.tool_box)
        self.verticalLayout_2.addWidget(self.title_bar_frame)
        self.display_frame = QtWidgets.QFrame(self.main_frame)
        self.display_frame.setMaximumSize(QtCore.QSize(16777215, 150))
        self.display_frame.setStyleSheet("background-color: transparent;")
        self.display_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.display_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.display_frame.setObjectName("display_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.display_frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.display_textSubLine = QtWidgets.QLineEdit(self.display_frame)
        self.display_textSubLine.setMinimumSize(QtCore.QSize(30, 30))
        self.display_textSubLine.setStyleSheet("QLineEdit {\n"
"    background-color: transparent;\n"
"    color: rgb(132, 132, 132);\n"
"    font: 20px;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    padding: 6px;\n"
"\n"
"}\n"
"\n"
"")
        self.display_textSubLine.setText("")
        self.display_textSubLine.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.display_textSubLine.setReadOnly(True)
        self.display_textSubLine.setObjectName("display_textSubLine")
        self.verticalLayout.addWidget(self.display_textSubLine)
        self.display_textLine = QtWidgets.QLineEdit(self.display_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.display_textLine.sizePolicy().hasHeightForWidth())
        self.display_textLine.setSizePolicy(sizePolicy)
        self.display_textLine.setStyleSheet("QLineEdit {\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 60px;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    padding: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.display_textLine.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.display_textLine.setReadOnly(True)
        self.display_textLine.setObjectName("display_textLine")
        self.verticalLayout.addWidget(self.display_textLine)
        self.verticalLayout_2.addWidget(self.display_frame)
        self.keypad_frame = QtWidgets.QFrame(self.main_frame)
        self.keypad_frame.setStyleSheet("background-color: transparent;")
        self.keypad_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.keypad_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.keypad_frame.setObjectName("keypad_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.keypad_frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(7)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.keypad_row1_frame = QtWidgets.QFrame(self.keypad_frame)
        self.keypad_row1_frame.setStyleSheet("background-color: transparent;")
        self.keypad_row1_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.keypad_row1_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.keypad_row1_frame.setObjectName("keypad_row1_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.keypad_row1_frame)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.AC_buttom = QtWidgets.QPushButton(self.keypad_row1_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AC_buttom.sizePolicy().hasHeightForWidth())
        self.AC_buttom.setSizePolicy(sizePolicy)
        self.AC_buttom.setMinimumSize(QtCore.QSize(80, 80))
        self.AC_buttom.setMaximumSize(QtCore.QSize(80, 80))
        self.AC_buttom.setStyleSheet("QPushButton {\n"
"    background-color: rgb(170, 170, 170);\n"
"    color: rgb(16, 16, 16);\n"
"    border-style: solid;\n"
"    border-radius: 40px;\n"
"    font: 35px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(150, 150, 150);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(120, 120, 120);\n"
"}\n"
"")
        self.AC_buttom.setObjectName("AC_buttom")
        self.horizontalLayout.addWidget(self.AC_buttom)
        self.C_button = QtWidgets.QPushButton(self.keypad_row1_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.C_button.sizePolicy().hasHeightForWidth())
        self.C_button.setSizePolicy(sizePolicy)
        self.C_button.setMinimumSize(QtCore.QSize(80, 80))
        self.C_button.setMaximumSize(QtCore.QSize(80, 80))
        self.C_button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(170, 170, 170);\n"
"    color: rgb(16, 16, 16);\n"
"    border-style: solid;\n"
"    border-radius: 40px;\n"
"    font: 35px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(150, 150, 150);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(120, 120, 120);\n"
"}\n"
"")
        self.C_button.setObjectName("C_button")
        self.horizontalLayout.addWidget(self.C_button)
        self.sign_button = QtWidgets.QPushButton(self.keypad_row1_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sign_button.sizePolicy().hasHeightForWidth())
        self.sign_button.setSizePolicy(sizePolicy)
        self.sign_button.setMinimumSize(QtCore.QSize(80, 80))
        self.sign_button.setMaximumSize(QtCore.QSize(80, 80))
        self.sign_button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(170, 170, 170);\n"
"    color: rgb(16, 16, 16);\n"
"    border-style: solid;\n"
"    border-radius: 40px;\n"
"    font: 35px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(150, 150, 150);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(120, 120, 120);\n"
"}\n"
"")
        self.sign_button.setObjectName("sign_button")
        self.horizontalLayout.addWidget(self.sign_button)
        self.divide_button = QtWidgets.QPushButton(self.keypad_row1_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.divide_button.sizePolicy().hasHeightForWidth())
        self.divide_button.setSizePolicy(sizePolicy)
        self.divide_button.setMinimumSize(QtCore.QSize(80, 80))
        self.divide_button.setMaximumSize(QtCore.QSize(80, 80))
        self.divide_button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 140, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-radius: 40px;\n"
"    font:bold 35px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(236, 126, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(212, 113, 0);\n"
"}")
        self.divide_button.setObjectName("divide_button")
        self.horizontalLayout.addWidget(self.divide_button)
        self.verticalLayout_3.addWidget(self.keypad_row1_frame)
        self.keypad_row2_frame = QtWidgets.QFrame(self.keypad_frame)
        self.keypad_row2_frame.setStyleSheet("background-color: transparent;")
        self.keypad_row2_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.keypad_row2_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.keypad_row2_frame.setObjectName("keypad_row2_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.keypad_row2_frame)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_7 = QtWidgets.QPushButton(self.keypad_row2_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_7.sizePolicy().hasHeightForWidth())
        self.button_7.setSizePolicy(sizePolicy)
        self.button_7.setMinimumSize(QtCore.QSize(80, 80))
        self.button_7.setMaximumSize(QtCore.QSize(80, 80))
        self.button_7.setStyleSheet("QPushButton {\n"
"    background-color: rgb(45, 45, 45);\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-radius: 40px;\n"
"    font: 35px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(35, 35, 35);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(20, 20, 20);\n"
"}")
        self.button_7.setObjectName("button_7")
        self.horizontalLayout_2.addWidget(self.button_7)
        self.button_8 = QtWidgets.QPushButton(self.keypad_row2_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_8.sizePolicy().hasHeightForWidth())
        self.button_8.setSizePolicy(sizePolicy)
        self.button_8.setMinimumSize(QtCore.QSize(80, 80))
        self.button_8.setMaximumSize(QtCore.QSize(80, 80))
        self.button_8.setStyleSheet("QPushButton {\n"
"    background-color: rgb(45, 45, 45);\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-radius: 40px;\n"
"    font: 35px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(35, 35, 35);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(20, 20, 20);\n"
"}")
        self.button_8.setObjectName("button_8")
        self.horizontalLayout_2.addWidget(self.button_8)
        self.button_9 = QtWidgets.QPushButton(self.keypad_row2_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_9.sizePolicy().hasHeightForWidth())
        self.button_9.setSizePolicy(sizePolicy)
        self.button_9.setMinimumSize(QtCore.QSize(80, 80))
        self.button_9.setMaximumSize(QtCore.QSize(80, 80))
        self.button_9.setStyleSheet("QPushButton {\n"
"    background-color: rgb(45, 45, 45);\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-radius: 40px;\n"
"    font: 35px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(35, 35, 35);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(20, 20, 20);\n"
"}")
        self.button_9.setObjectName("button_9")
        self.horizontalLayout_2.addWidget(self.button_9)
        self.multi_button = QtWidgets.QPushButton(self.keypad_row2_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.multi_button.sizePolicy().hasHeightForWidth())
        self.multi_button.setSizePolicy(sizePolicy)
        self.multi_button.setMinimumSize(QtCore.QSize(80, 80))
        self.multi_button.setMaximumSize(QtCore.QSize(80, 80))
        self.multi_button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 140, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-radius: 40px;\n"
"    font:bold 35px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(236, 126, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(212, 113, 0);\n"
"}")
        self.multi_button.setObjectName("multi_button")
        self.horizontalLayout_2.addWidget(self.multi_button)
        self.verticalLayout_3.addWidget(self.keypad_row2_frame)
        self.keypad_row3_frame = QtWidgets.QFrame(self.keypad_frame)
        self.keypad_row3_frame.setStyleSheet("background-color: transparent;")
        self.keypad_row3_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.keypad_row3_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.keypad_row3_frame.setObjectName("keypad_row3_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.keypad_row3_frame)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.button_4 = QtWidgets.QPushButton(self.keypad_row3_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_4.sizePolicy().hasHeightForWidth())
        self.button_4.setSizePolicy(sizePolicy)
        self.button_4.setMinimumSize(QtCore.QSize(80, 80))
        self.button_4.setMaximumSize(QtCore.QSize(80, 80))
        self.button_4.setStyleSheet("QPushButton {\n"
"    background-color: rgb(45, 45, 45);\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-radius: 40px;\n"
"    font: 35px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(35, 35, 35);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(20, 20, 20);\n"
"}")
        self.button_4.setObjectName("button_4")
        self.horizontalLayout_3.addWidget(self.button_4)
        self.button_5 = QtWidgets.QPushButton(self.keypad_row3_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_5.sizePolicy().hasHeightForWidth())
        self.button_5.setSizePolicy(sizePolicy)
        self.button_5.setMinimumSize(QtCore.QSize(80, 80))
        self.button_5.setMaximumSize(QtCore.QSize(80, 80))
        self.button_5.setStyleSheet("QPushButton {\n"
"    background-color: rgb(45, 45, 45);\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-radius: 40px;\n"
"    font: 35px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(35, 35, 35);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(20, 20, 20);\n"
"}")
        self.button_5.setObjectName("button_5")
        self.horizontalLayout_3.addWidget(self.button_5)
        self.button_6 = QtWidgets.QPushButton(self.keypad_row3_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_6.sizePolicy().hasHeightForWidth())
        self.button_6.setSizePolicy(sizePolicy)
        self.button_6.setMinimumSize(QtCore.QSize(80, 80))
        self.button_6.setMaximumSize(QtCore.QSize(80, 80))
        self.button_6.setStyleSheet("QPushButton {\n"
"    background-color: rgb(45, 45, 45);\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-radius: 40px;\n"
"    font: 35px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(35, 35, 35);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(20, 20, 20);\n"
"}")
        self.button_6.setObjectName("button_6")
        self.horizontalLayout_3.addWidget(self.button_6)
        self.subtract_button = QtWidgets.QPushButton(self.keypad_row3_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subtract_button.sizePolicy().hasHeightForWidth())
        self.subtract_button.setSizePolicy(sizePolicy)
        self.subtract_button.setMinimumSize(QtCore.QSize(80, 80))
        self.subtract_button.setMaximumSize(QtCore.QSize(80, 80))
        self.subtract_button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 140, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-radius: 40px;\n"
"    font:bold 35px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(236, 126, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(212, 113, 0);\n"
"}")
        self.subtract_button.setObjectName("subtract_button")
        self.horizontalLayout_3.addWidget(self.subtract_button)
        self.verticalLayout_3.addWidget(self.keypad_row3_frame)
        self.keypad_row4_frame = QtWidgets.QFrame(self.keypad_frame)
        self.keypad_row4_frame.setStyleSheet("background-color: transparent;")
        self.keypad_row4_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.keypad_row4_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.keypad_row4_frame.setObjectName("keypad_row4_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.keypad_row4_frame)
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.button_1 = QtWidgets.QPushButton(self.keypad_row4_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_1.sizePolicy().hasHeightForWidth())
        self.button_1.setSizePolicy(sizePolicy)
        self.button_1.setMinimumSize(QtCore.QSize(80, 80))
        self.button_1.setMaximumSize(QtCore.QSize(80, 80))
        self.button_1.setStyleSheet("QPushButton {\n"
"    background-color: rgb(45, 45, 45);\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-radius: 40px;\n"
"    font: 35px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(35, 35, 35);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(20, 20, 20);\n"
"}")
        self.button_1.setObjectName("button_1")
        self.horizontalLayout_4.addWidget(self.button_1)
        self.button_2 = QtWidgets.QPushButton(self.keypad_row4_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_2.sizePolicy().hasHeightForWidth())
        self.button_2.setSizePolicy(sizePolicy)
        self.button_2.setMinimumSize(QtCore.QSize(80, 80))
        self.button_2.setMaximumSize(QtCore.QSize(80, 80))
        self.button_2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(45, 45, 45);\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-radius: 40px;\n"
"    font: 35px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(35, 35, 35);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(20, 20, 20);\n"
"}")
        self.button_2.setObjectName("button_2")
        self.horizontalLayout_4.addWidget(self.button_2)
        self.button_3 = QtWidgets.QPushButton(self.keypad_row4_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_3.sizePolicy().hasHeightForWidth())
        self.button_3.setSizePolicy(sizePolicy)
        self.button_3.setMinimumSize(QtCore.QSize(80, 80))
        self.button_3.setMaximumSize(QtCore.QSize(80, 80))
        self.button_3.setStyleSheet("QPushButton {\n"
"    background-color: rgb(45, 45, 45);\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-radius: 40px;\n"
"    font: 35px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(35, 35, 35);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(20, 20, 20);\n"
"}")
        self.button_3.setObjectName("button_3")
        self.horizontalLayout_4.addWidget(self.button_3)
        self.add_button = QtWidgets.QPushButton(self.keypad_row4_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_button.sizePolicy().hasHeightForWidth())
        self.add_button.setSizePolicy(sizePolicy)
        self.add_button.setMinimumSize(QtCore.QSize(80, 80))
        self.add_button.setMaximumSize(QtCore.QSize(80, 80))
        self.add_button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 140, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-radius: 40px;\n"
"    font:bold 35px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(236, 126, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(212, 113, 0);\n"
"}")
        self.add_button.setObjectName("add_button")
        self.horizontalLayout_4.addWidget(self.add_button)
        self.verticalLayout_3.addWidget(self.keypad_row4_frame)
        self.keypad_row5_frame = QtWidgets.QFrame(self.keypad_frame)
        self.keypad_row5_frame.setStyleSheet("background-color: transparent;")
        self.keypad_row5_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.keypad_row5_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.keypad_row5_frame.setObjectName("keypad_row5_frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.keypad_row5_frame)
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_5.setSpacing(8)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.button_0 = QtWidgets.QPushButton(self.keypad_row5_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_0.sizePolicy().hasHeightForWidth())
        self.button_0.setSizePolicy(sizePolicy)
        self.button_0.setMinimumSize(QtCore.QSize(170, 80))
        self.button_0.setMaximumSize(QtCore.QSize(170, 80))
        self.button_0.setAutoFillBackground(False)
        self.button_0.setStyleSheet("QPushButton {\n"
"        background-color: rgb(45, 45, 45);\n"
"    color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-radius: 40px;\n"
"    font: 35px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(35, 35, 35)\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(20, 20, 20);\n"
"}\n"
"\n"
"QPushButton {\\n    background-color: rgb(45, 45, 45);\\n    \\n    color: rgb(255, 255, 255);\\n    border-style: solid;\\n    border-radius: 40px;\\n    font: 35px;\\n    padding: 6px;\\n}\\n\\n\\nQPushButton:hover {\\nbackground-color: rgb(35, 35, 35);\\n}\\n\\nQPushButton:pressed {\\nbackground-color: rgb(20, 20, 20);\\n}")
        self.button_0.setAutoDefault(False)
        self.button_0.setObjectName("button_0")
        self.horizontalLayout_5.addWidget(self.button_0)
        self.dp_button = QtWidgets.QPushButton(self.keypad_row5_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dp_button.sizePolicy().hasHeightForWidth())
        self.dp_button.setSizePolicy(sizePolicy)
        self.dp_button.setMinimumSize(QtCore.QSize(80, 80))
        self.dp_button.setMaximumSize(QtCore.QSize(80, 80))
        self.dp_button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(45, 45, 45);\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-radius: 40px;\n"
"    font: 35px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(35, 35, 35);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(20, 20, 20);\n"
"}")
        self.dp_button.setObjectName("dp_button")
        self.horizontalLayout_5.addWidget(self.dp_button)
        self.equal_button = QtWidgets.QPushButton(self.keypad_row5_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.equal_button.sizePolicy().hasHeightForWidth())
        self.equal_button.setSizePolicy(sizePolicy)
        self.equal_button.setMinimumSize(QtCore.QSize(80, 80))
        self.equal_button.setMaximumSize(QtCore.QSize(80, 80))
        self.equal_button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 140, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-radius: 40px;\n"
"    font:bold 35px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(236, 126, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(212, 113, 0);\n"
"}")
        self.equal_button.setObjectName("equal_button")
        self.horizontalLayout_5.addWidget(self.equal_button)
        self.verticalLayout_3.addWidget(self.keypad_row5_frame)
        self.verticalLayout_2.addWidget(self.keypad_frame)
        self.horizontalLayout_7.addWidget(self.main_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title_bar.setText(_translate("MainWindow", "Calculator"))
        self.display_textLine.setText(_translate("MainWindow", "0"))
        self.AC_buttom.setText(_translate("MainWindow", "AC"))
        self.C_button.setText(_translate("MainWindow", "C"))
        self.sign_button.setText(_translate("MainWindow", "+/-"))
        self.divide_button.setText(_translate("MainWindow", "/"))
        self.button_7.setText(_translate("MainWindow", "7"))
        self.button_8.setText(_translate("MainWindow", "8"))
        self.button_9.setText(_translate("MainWindow", "9"))
        self.multi_button.setText(_translate("MainWindow", "*"))
        self.button_4.setText(_translate("MainWindow", "4"))
        self.button_5.setText(_translate("MainWindow", "5"))
        self.button_6.setText(_translate("MainWindow", "6"))
        self.subtract_button.setText(_translate("MainWindow", "-"))
        self.button_1.setText(_translate("MainWindow", "1"))
        self.button_2.setText(_translate("MainWindow", "2"))
        self.button_3.setText(_translate("MainWindow", "3"))
        self.add_button.setText(_translate("MainWindow", "+"))
        self.button_0.setText(_translate("MainWindow", "0"))
        self.dp_button.setText(_translate("MainWindow", "."))
        self.equal_button.setText(_translate("MainWindow", "="))
import img_rc
