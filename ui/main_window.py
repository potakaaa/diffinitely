# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(684, 523)
        MainWindow.setMinimumSize(QSize(684, 523))
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionZoom_In = QAction(MainWindow)
        self.actionZoom_In.setObjectName(u"actionZoom_In")
        self.actionZoom_Out = QAction(MainWindow)
        self.actionZoom_Out.setObjectName(u"actionZoom_Out")
        self.actionReset = QAction(MainWindow)
        self.actionReset.setObjectName(u"actionReset")
        self.actionTheme = QAction(MainWindow)
        self.actionTheme.setObjectName(u"actionTheme")
        self.actionShow_Hide = QAction(MainWindow)
        self.actionShow_Hide.setObjectName(u"actionShow_Hide")
        self.actionUndo = QAction(MainWindow)
        self.actionUndo.setObjectName(u"actionUndo")
        self.actionRedo = QAction(MainWindow)
        self.actionRedo.setObjectName(u"actionRedo")
        self.actionClear = QAction(MainWindow)
        self.actionClear.setObjectName(u"actionClear")
        self.actionGithub_Link = QAction(MainWindow)
        self.actionGithub_Link.setObjectName(u"actionGithub_Link")
        self.mainWidget = QWidget(MainWindow)
        self.mainWidget.setObjectName(u"mainWidget")
        self.gridLayout = QGridLayout(self.mainWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.mainWidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_widget = QWidget(self.widget)
        self.left_widget.setObjectName(u"left_widget")
        self.verticalLayout_7 = QVBoxLayout(self.left_widget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.input_label = QLabel(self.left_widget)
        self.input_label.setObjectName(u"input_label")

        self.verticalLayout_2.addWidget(self.input_label)

        self.input_edit = QLineEdit(self.left_widget)
        self.input_edit.setObjectName(u"input_edit")

        self.verticalLayout_2.addWidget(self.input_edit)


        self.verticalLayout_7.addLayout(self.verticalLayout_2)

        self.graph_widget = QWidget(self.left_widget)
        self.graph_widget.setObjectName(u"graph_widget")

        self.verticalLayout_7.addWidget(self.graph_widget)


        self.horizontalLayout.addWidget(self.left_widget)

        self.right_widget = QWidget(self.widget)
        self.right_widget.setObjectName(u"right_widget")
        self.verticalLayout_6 = QVBoxLayout(self.right_widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self._1st_derivative_label = QLabel(self.right_widget)
        self._1st_derivative_label.setObjectName(u"_1st_derivative_label")

        self.verticalLayout_5.addWidget(self._1st_derivative_label)

        self._1st_derivative_edit = QLineEdit(self.right_widget)
        self._1st_derivative_edit.setObjectName(u"_1st_derivative_edit")

        self.verticalLayout_5.addWidget(self._1st_derivative_edit)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self._2nd_derivative_label = QLabel(self.right_widget)
        self._2nd_derivative_label.setObjectName(u"_2nd_derivative_label")

        self.verticalLayout_4.addWidget(self._2nd_derivative_label)

        self._2nd_derivative_edit = QLineEdit(self.right_widget)
        self._2nd_derivative_edit.setObjectName(u"_2nd_derivative_edit")

        self.verticalLayout_4.addWidget(self._2nd_derivative_edit)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.nth_derivative_label = QLabel(self.right_widget)
        self.nth_derivative_label.setObjectName(u"nth_derivative_label")

        self.verticalLayout_3.addWidget(self.nth_derivative_label)

        self.nth_derivative_edit = QLineEdit(self.right_widget)
        self.nth_derivative_edit.setObjectName(u"nth_derivative_edit")

        self.verticalLayout_3.addWidget(self.nth_derivative_edit)


        self.verticalLayout_6.addLayout(self.verticalLayout_3)

        self.integral_label = QLabel(self.right_widget)
        self.integral_label.setObjectName(u"integral_label")

        self.verticalLayout_6.addWidget(self.integral_label)

        self.integral_edit = QLineEdit(self.right_widget)
        self.integral_edit.setObjectName(u"integral_edit")

        self.verticalLayout_6.addWidget(self.integral_edit)


        self.horizontalLayout.addWidget(self.right_widget)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.widget)

        self.bottom_widget = QWidget(self.mainWidget)
        self.bottom_widget.setObjectName(u"bottom_widget")
        self.horizontalLayout_3 = QHBoxLayout(self.bottom_widget)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton = QPushButton(self.bottom_widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 40))
        self.pushButton.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_2 = QPushButton(self.bottom_widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 40))
        self.pushButton_2.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.bottom_widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 40))
        self.pushButton_3.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.bottom_widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 40))
        self.pushButton_4.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.pushButton_4, 0, 3, 1, 1)

        self.pushButton_7 = QPushButton(self.bottom_widget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(0, 40))
        self.pushButton_7.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.pushButton_7, 1, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.bottom_widget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 40))
        self.pushButton_6.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.pushButton_6, 1, 1, 1, 1)

        self.pushButton_5 = QPushButton(self.bottom_widget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(0, 40))
        self.pushButton_5.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.pushButton_5, 1, 2, 1, 1)

        self.pushButton_8 = QPushButton(self.bottom_widget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(0, 40))
        self.pushButton_8.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.pushButton_8, 1, 3, 1, 1)

        self.pushButton_9 = QPushButton(self.bottom_widget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(0, 40))
        self.pushButton_9.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.pushButton_9, 2, 0, 1, 1)

        self.pushButton_12 = QPushButton(self.bottom_widget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(0, 40))
        self.pushButton_12.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.pushButton_12, 2, 1, 1, 1)

        self.pushButton_10 = QPushButton(self.bottom_widget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(0, 40))
        self.pushButton_10.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.pushButton_10, 2, 2, 1, 1)

        self.pushButton_11 = QPushButton(self.bottom_widget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(0, 40))
        self.pushButton_11.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.pushButton_11, 2, 3, 1, 1)

        self.pushButton_15 = QPushButton(self.bottom_widget)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(0, 40))
        self.pushButton_15.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.pushButton_15, 3, 0, 1, 1)

        self.pushButton_14 = QPushButton(self.bottom_widget)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(0, 40))
        self.pushButton_14.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.pushButton_14, 3, 1, 1, 1)

        self.pushButton_16 = QPushButton(self.bottom_widget)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMinimumSize(QSize(0, 40))
        self.pushButton_16.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.pushButton_16, 3, 2, 1, 1)

        self.pushButton_13 = QPushButton(self.bottom_widget)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(0, 40))
        self.pushButton_13.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.pushButton_13, 3, 3, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout_2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.pushButton_29 = QPushButton(self.bottom_widget)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setMinimumSize(QSize(0, 40))
        self.pushButton_29.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.pushButton_29, 3, 0, 1, 1)

        self.pushButton_19 = QPushButton(self.bottom_widget)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setMinimumSize(QSize(0, 40))
        self.pushButton_19.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.pushButton_19, 0, 2, 1, 1)

        self.pushButton_28 = QPushButton(self.bottom_widget)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setMinimumSize(QSize(0, 40))
        self.pushButton_28.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.pushButton_28, 2, 3, 1, 1)

        self.pushButton_17 = QPushButton(self.bottom_widget)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setMinimumSize(QSize(0, 40))
        self.pushButton_17.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.pushButton_17, 0, 0, 1, 1)

        self.pushButton_21 = QPushButton(self.bottom_widget)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setMinimumSize(QSize(0, 40))
        self.pushButton_21.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.pushButton_21, 1, 0, 1, 1)

        self.pushButton_25 = QPushButton(self.bottom_widget)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setMinimumSize(QSize(0, 40))
        self.pushButton_25.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.pushButton_25, 2, 0, 1, 1)

        self.pushButton_26 = QPushButton(self.bottom_widget)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setMinimumSize(QSize(0, 40))
        self.pushButton_26.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.pushButton_26, 2, 1, 1, 1)

        self.pushButton_20 = QPushButton(self.bottom_widget)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setMinimumSize(QSize(0, 40))
        self.pushButton_20.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.pushButton_20, 0, 3, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_23 = QPushButton(self.bottom_widget)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setMinimumSize(QSize(0, 40))
        self.pushButton_23.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.pushButton_23, 1, 2, 1, 1)

        self.pushButton_22 = QPushButton(self.bottom_widget)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setMinimumSize(QSize(0, 40))
        self.pushButton_22.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.pushButton_22, 1, 1, 1, 1)

        self.pushButton_18 = QPushButton(self.bottom_widget)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setMinimumSize(QSize(0, 40))
        self.pushButton_18.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.pushButton_18, 0, 1, 1, 1)

        self.pushButton_24 = QPushButton(self.bottom_widget)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setMinimumSize(QSize(0, 40))
        self.pushButton_24.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.pushButton_24, 1, 3, 1, 1)

        self.pushButton_32 = QPushButton(self.bottom_widget)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setMinimumSize(QSize(0, 40))
        self.pushButton_32.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.pushButton_32, 3, 3, 1, 1)

        self.pushButton_27 = QPushButton(self.bottom_widget)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setMinimumSize(QSize(0, 40))
        self.pushButton_27.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.pushButton_27, 2, 2, 1, 1)

        self.pushButton_31 = QPushButton(self.bottom_widget)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setMinimumSize(QSize(0, 40))
        self.pushButton_31.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.pushButton_31, 3, 1, 1, 2)


        self.horizontalLayout_3.addLayout(self.gridLayout_3)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.pushButton_33 = QPushButton(self.bottom_widget)
        self.pushButton_33.setObjectName(u"pushButton_33")
        self.pushButton_33.setMinimumSize(QSize(0, 40))

        self.verticalLayout_8.addWidget(self.pushButton_33)

        self.pushButton_34 = QPushButton(self.bottom_widget)
        self.pushButton_34.setObjectName(u"pushButton_34")
        self.pushButton_34.setMinimumSize(QSize(0, 40))

        self.verticalLayout_8.addWidget(self.pushButton_34)

        self.pushButton_35 = QPushButton(self.bottom_widget)
        self.pushButton_35.setObjectName(u"pushButton_35")
        self.pushButton_35.setMinimumSize(QSize(0, 40))

        self.verticalLayout_8.addWidget(self.pushButton_35)

        self.pushButton_36 = QPushButton(self.bottom_widget)
        self.pushButton_36.setObjectName(u"pushButton_36")
        self.pushButton_36.setMinimumSize(QSize(0, 40))

        self.verticalLayout_8.addWidget(self.pushButton_36)


        self.horizontalLayout_3.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, -1, -1, 7)
        self.label_6 = QLabel(self.bottom_widget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_9.addWidget(self.label_6)

        self.listWidget = QListWidget(self.bottom_widget)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_9.addWidget(self.listWidget)


        self.horizontalLayout_3.addLayout(self.verticalLayout_9)


        self.verticalLayout.addWidget(self.bottom_widget)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.mainWidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 684, 33))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menuBar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuEdit_2 = QMenu(self.menuBar)
        self.menuEdit_2.setObjectName(u"menuEdit_2")
        self.menuAbout = QMenu(self.menuBar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuEdit_2.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionZoom_In)
        self.menuEdit.addAction(self.actionZoom_Out)
        self.menuEdit.addAction(self.actionReset)
        self.menuEdit.addAction(self.actionTheme)
        self.menuEdit.addAction(self.actionShow_Hide)
        self.menuEdit_2.addAction(self.actionUndo)
        self.menuEdit_2.addAction(self.actionRedo)
        self.menuEdit_2.addAction(self.actionClear)
        self.menuAbout.addAction(self.actionGithub_Link)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionZoom_In.setText(QCoreApplication.translate("MainWindow", u"Zoom In", None))
        self.actionZoom_Out.setText(QCoreApplication.translate("MainWindow", u"Zoom Out", None))
        self.actionReset.setText(QCoreApplication.translate("MainWindow", u"Reset ", None))
        self.actionTheme.setText(QCoreApplication.translate("MainWindow", u"Dark Mode", None))
        self.actionShow_Hide.setText(QCoreApplication.translate("MainWindow", u"Show/Hide", None))
        self.actionUndo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
        self.actionRedo.setText(QCoreApplication.translate("MainWindow", u"Redo", None))
        self.actionClear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.actionGithub_Link.setText(QCoreApplication.translate("MainWindow", u"Github Link", None))
        self.input_label.setText(QCoreApplication.translate("MainWindow", u"Input", None))
        self.input_edit.setText("")
        self._1st_derivative_label.setText(QCoreApplication.translate("MainWindow", u"1st Derivative", None))
        self._2nd_derivative_label.setText(QCoreApplication.translate("MainWindow", u"2nd Derivative", None))
        self.nth_derivative_label.setText(QCoreApplication.translate("MainWindow", u"Nth Derivative", None))
        self.integral_label.setText(QCoreApplication.translate("MainWindow", u"Integral", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"y", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"a\u00b2", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"a\u1d47", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"!", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"'", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u2264", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"\u2265", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"x!", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"\u221a", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"\u03c0", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"\u2212", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
        self.pushButton_32.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"more", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"delete", None))
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"clear", None))
        self.pushButton_36.setText(QCoreApplication.translate("MainWindow", u"trigo", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuEdit_2.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

