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
        MainWindow.resize(684, 900)
        MainWindow.setMinimumSize(QSize(684, 900))
        MainWindow.setMaximumSize(QSize(896, 900))
        font = QFont()
        font.setFamilies([u"Poppins"])
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"#mainWidget {\n"
"	background-color: rgb(220, 220, 220);\n"
"}\n"
"\n"
"#statusBar {\n"
"	background-color: rgb(54, 69, 79);\n"
"}\n"
"\n"
"#menuBar {\n"
"	background-color: rgb(54, 69, 79);\n"
"}\n"
"\n"
"#top_widget {\n"
"	background-color: rgb(54, 69, 79);\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"#bottom_widget {\n"
"	background-color: rgb(169, 178, 178);\n"
"	border-radius: 0px;\n"
"}\n"
"")
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentNew))
        self.actionNew.setIcon(icon)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentOpen))
        self.actionOpen.setIcon(icon1)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSave))
        self.actionSave.setIcon(icon2)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.WindowClose))
        self.actionExit.setIcon(icon3)
        self.actionZoom_In = QAction(MainWindow)
        self.actionZoom_In.setObjectName(u"actionZoom_In")
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ZoomIn))
        self.actionZoom_In.setIcon(icon4)
        self.actionZoom_Out = QAction(MainWindow)
        self.actionZoom_Out.setObjectName(u"actionZoom_Out")
        icon5 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ZoomOut))
        self.actionZoom_Out.setIcon(icon5)
        self.actionReset = QAction(MainWindow)
        self.actionReset.setObjectName(u"actionReset")
        icon6 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.SystemReboot))
        self.actionReset.setIcon(icon6)
        self.actionTheme = QAction(MainWindow)
        self.actionTheme.setObjectName(u"actionTheme")
        self.actionTheme.setCheckable(True)
        self.actionTheme.setChecked(False)
        icon7 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.WeatherClear))
        self.actionTheme.setIcon(icon7)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        icon8 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.WindowNew))
        self.action.setIcon(icon8)
        self.actionUndo = QAction(MainWindow)
        self.actionUndo.setObjectName(u"actionUndo")
        icon9 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditUndo))
        self.actionUndo.setIcon(icon9)
        self.actionRedo = QAction(MainWindow)
        self.actionRedo.setObjectName(u"actionRedo")
        icon10 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditRedo))
        self.actionRedo.setIcon(icon10)
        self.actionClear = QAction(MainWindow)
        self.actionClear.setObjectName(u"actionClear")
        icon11 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditClear))
        self.actionClear.setIcon(icon11)
        self.actionGithub_Link = QAction(MainWindow)
        self.actionGithub_Link.setObjectName(u"actionGithub_Link")
        icon12 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DialogInformation))
        self.actionGithub_Link.setIcon(icon12)
        self.mainWidget = QWidget(MainWindow)
        self.mainWidget.setObjectName(u"mainWidget")
        font1 = QFont()
        font1.setFamilies([u"Poppins"])
        font1.setPointSize(11)
        self.mainWidget.setFont(font1)
        self.mainWidget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.mainWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_widget = QWidget(self.mainWidget)
        self.top_widget.setObjectName(u"top_widget")
        self.top_widget.setFont(font1)
        self.top_widget.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(78, 94, 104)\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.top_widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_widget = QWidget(self.top_widget)
        self.left_widget.setObjectName(u"left_widget")
        self.left_widget.setMaximumSize(QSize(16777215, 16777215))
        self.left_widget.setFont(font1)
        self.verticalLayout_7 = QVBoxLayout(self.left_widget)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 5, -1, -1)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.input_label = QLabel(self.left_widget)
        self.input_label.setObjectName(u"input_label")
        self.input_label.setMaximumSize(QSize(16777215, 20))
        self.input_label.setFont(font1)

        self.verticalLayout_12.addWidget(self.input_label, 0, Qt.AlignmentFlag.AlignBottom)

        self.input_edit = QLineEdit(self.left_widget)
        self.input_edit.setObjectName(u"input_edit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_edit.sizePolicy().hasHeightForWidth())
        self.input_edit.setSizePolicy(sizePolicy)
        self.input_edit.setMinimumSize(QSize(0, 35))
        self.input_edit.setMaximumSize(QSize(16777215, 44))
        self.input_edit.setFont(font1)

        self.verticalLayout_12.addWidget(self.input_edit)


        self.verticalLayout_2.addLayout(self.verticalLayout_12)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.n_value_label = QLabel(self.left_widget)
        self.n_value_label.setObjectName(u"n_value_label")
        self.n_value_label.setMaximumSize(QSize(16777215, 20))
        self.n_value_label.setFont(font1)

        self.verticalLayout_13.addWidget(self.n_value_label, 0, Qt.AlignmentFlag.AlignBottom)

        self.n_value_edit = QLineEdit(self.left_widget)
        self.n_value_edit.setObjectName(u"n_value_edit")
        sizePolicy.setHeightForWidth(self.n_value_edit.sizePolicy().hasHeightForWidth())
        self.n_value_edit.setSizePolicy(sizePolicy)
        self.n_value_edit.setMinimumSize(QSize(0, 35))
        self.n_value_edit.setMaximumSize(QSize(16777215, 44))
        self.n_value_edit.setFont(font1)

        self.verticalLayout_13.addWidget(self.n_value_edit)


        self.verticalLayout_2.addLayout(self.verticalLayout_13)


        self.verticalLayout_7.addLayout(self.verticalLayout_2)

        self.graph_widget = QWidget(self.left_widget)
        self.graph_widget.setObjectName(u"graph_widget")
        self.graph_widget.setMaximumSize(QSize(16777215, 350))
        self.graph_widget.setFont(font1)
        self.verticalLayout_11 = QVBoxLayout(self.graph_widget)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 6, -1, -1)
        self.label = QLabel(self.graph_widget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 350))
        self.label.setFont(font1)

        self.verticalLayout_11.addWidget(self.label)


        self.verticalLayout_7.addWidget(self.graph_widget)


        self.horizontalLayout.addWidget(self.left_widget)

        self.right_widget = QWidget(self.top_widget)
        self.right_widget.setObjectName(u"right_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.right_widget.sizePolicy().hasHeightForWidth())
        self.right_widget.setSizePolicy(sizePolicy1)
        self.right_widget.setMinimumSize(QSize(0, 0))
        self.right_widget.setMaximumSize(QSize(16777215, 600))
        self.right_widget.setFont(font1)
        self.verticalLayout_14 = QVBoxLayout(self.right_widget)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(-1, 0, -1, 35)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.derivative_1st_label = QLabel(self.right_widget)
        self.derivative_1st_label.setObjectName(u"derivative_1st_label")
        self.derivative_1st_label.setMaximumSize(QSize(432, 20))
        self.derivative_1st_label.setFont(font1)

        self.verticalLayout_5.addWidget(self.derivative_1st_label, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom)

        self.derivative_1st_edit = QLineEdit(self.right_widget)
        self.derivative_1st_edit.setObjectName(u"derivative_1st_edit")
        sizePolicy.setHeightForWidth(self.derivative_1st_edit.sizePolicy().hasHeightForWidth())
        self.derivative_1st_edit.setSizePolicy(sizePolicy)
        self.derivative_1st_edit.setMinimumSize(QSize(0, 35))
        self.derivative_1st_edit.setMaximumSize(QSize(16777215, 44))
        self.derivative_1st_edit.setFont(font1)
        self.derivative_1st_edit.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.derivative_1st_edit)


        self.verticalLayout_14.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.derivative_2nd_label = QLabel(self.right_widget)
        self.derivative_2nd_label.setObjectName(u"derivative_2nd_label")
        self.derivative_2nd_label.setMaximumSize(QSize(16777215, 20))
        self.derivative_2nd_label.setFont(font1)

        self.verticalLayout_4.addWidget(self.derivative_2nd_label, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom)

        self.derivative_2nd_edit = QLineEdit(self.right_widget)
        self.derivative_2nd_edit.setObjectName(u"derivative_2nd_edit")
        sizePolicy.setHeightForWidth(self.derivative_2nd_edit.sizePolicy().hasHeightForWidth())
        self.derivative_2nd_edit.setSizePolicy(sizePolicy)
        self.derivative_2nd_edit.setMinimumSize(QSize(0, 35))
        self.derivative_2nd_edit.setMaximumSize(QSize(16777215, 44))
        self.derivative_2nd_edit.setFont(font1)
        self.derivative_2nd_edit.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.derivative_2nd_edit)


        self.verticalLayout_14.addLayout(self.verticalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.nth_derivative_label = QLabel(self.right_widget)
        self.nth_derivative_label.setObjectName(u"nth_derivative_label")
        self.nth_derivative_label.setMaximumSize(QSize(16777215, 20))
        self.nth_derivative_label.setFont(font1)

        self.verticalLayout_3.addWidget(self.nth_derivative_label, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom)

        self.nth_derivative_edit = QLineEdit(self.right_widget)
        self.nth_derivative_edit.setObjectName(u"nth_derivative_edit")
        sizePolicy.setHeightForWidth(self.nth_derivative_edit.sizePolicy().hasHeightForWidth())
        self.nth_derivative_edit.setSizePolicy(sizePolicy)
        self.nth_derivative_edit.setMinimumSize(QSize(0, 35))
        self.nth_derivative_edit.setMaximumSize(QSize(16777215, 44))
        self.nth_derivative_edit.setFont(font1)
        self.nth_derivative_edit.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.nth_derivative_edit)


        self.verticalLayout_14.addLayout(self.verticalLayout_3)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.integral_label = QLabel(self.right_widget)
        self.integral_label.setObjectName(u"integral_label")
        self.integral_label.setMaximumSize(QSize(16777215, 20))
        self.integral_label.setFont(font1)

        self.verticalLayout_10.addWidget(self.integral_label, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom)

        self.integral_edit = QLineEdit(self.right_widget)
        self.integral_edit.setObjectName(u"integral_edit")
        sizePolicy.setHeightForWidth(self.integral_edit.sizePolicy().hasHeightForWidth())
        self.integral_edit.setSizePolicy(sizePolicy)
        self.integral_edit.setMinimumSize(QSize(0, 35))
        self.integral_edit.setMaximumSize(QSize(16777215, 44))
        self.integral_edit.setFont(font1)
        self.integral_edit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.integral_edit)


        self.verticalLayout_14.addLayout(self.verticalLayout_10)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.definite_integral_label = QLabel(self.right_widget)
        self.definite_integral_label.setObjectName(u"definite_integral_label")
        self.definite_integral_label.setFont(font1)

        self.verticalLayout_6.addWidget(self.definite_integral_label)

        self.definite_integral_edit = QLineEdit(self.right_widget)
        self.definite_integral_edit.setObjectName(u"definite_integral_edit")
        self.definite_integral_edit.setMinimumSize(QSize(0, 35))
        self.definite_integral_edit.setMaximumSize(QSize(16777215, 44))

        self.verticalLayout_6.addWidget(self.definite_integral_edit)


        self.verticalLayout_14.addLayout(self.verticalLayout_6)


        self.horizontalLayout.addWidget(self.right_widget)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.top_widget)

        self.bottom_widget = QWidget(self.mainWidget)
        self.bottom_widget.setObjectName(u"bottom_widget")
        self.bottom_widget.setMaximumSize(QSize(16777215, 250))
        font2 = QFont()
        font2.setFamilies([u"Poppins"])
        font2.setPointSize(14)
        font2.setBold(False)
        self.bottom_widget.setFont(font2)
        self.bottom_widget.setStyleSheet(u"QPushButton {\n"
"	font-size: 18px;\n"
"	font-weight: 500;\n"
"}\n"
"\n"
"QLabel {\n"
"	font-size: 13px;\n"
"	font-weight: 500;\n"
"}\n"
"\n"
"#add_button, #minus_button, #mul_button, #div_button, #equal_button {\n"
"	background-color: rgb(0, 128, 128);\n"
"}\n"
"\n"
"#more_button, #del_button, #clear_button, #empty_button {\n"
"	background-color: rgb(208, 133, 29)\n"
"}\n"
"\n"
"#history_label {\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.horizontalLayout_3 = QHBoxLayout(self.bottom_widget)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.x_button = QPushButton(self.bottom_widget)
        self.x_button.setObjectName(u"x_button")
        self.x_button.setMinimumSize(QSize(0, 40))
        self.x_button.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Poppins"])
        font3.setWeight(QFont.Medium)
        self.x_button.setFont(font3)

        self.gridLayout_2.addWidget(self.x_button, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.a_2_button = QPushButton(self.bottom_widget)
        self.a_2_button.setObjectName(u"a_2_button")
        self.a_2_button.setMinimumSize(QSize(0, 40))
        self.a_2_button.setMaximumSize(QSize(16777215, 16777215))
        self.a_2_button.setFont(font3)

        self.gridLayout_2.addWidget(self.a_2_button, 0, 2, 1, 1)

        self.pi_button = QPushButton(self.bottom_widget)
        self.pi_button.setObjectName(u"pi_button")
        self.pi_button.setMinimumSize(QSize(0, 40))
        self.pi_button.setMaximumSize(QSize(16777215, 16777215))
        self.pi_button.setFont(font3)

        self.gridLayout_2.addWidget(self.pi_button, 3, 3, 1, 1)

        self.a_b_button = QPushButton(self.bottom_widget)
        self.a_b_button.setObjectName(u"a_b_button")
        self.a_b_button.setMinimumSize(QSize(0, 40))
        self.a_b_button.setMaximumSize(QSize(16777215, 16777215))
        self.a_b_button.setFont(font3)

        self.gridLayout_2.addWidget(self.a_b_button, 0, 3, 1, 1)

        self.open_parenthesis_button = QPushButton(self.bottom_widget)
        self.open_parenthesis_button.setObjectName(u"open_parenthesis_button")
        self.open_parenthesis_button.setMinimumSize(QSize(0, 40))
        self.open_parenthesis_button.setMaximumSize(QSize(16777215, 16777215))
        self.open_parenthesis_button.setFont(font3)

        self.gridLayout_2.addWidget(self.open_parenthesis_button, 1, 0, 1, 1)

        self.x_fact_button = QPushButton(self.bottom_widget)
        self.x_fact_button.setObjectName(u"x_fact_button")
        self.x_fact_button.setMinimumSize(QSize(0, 40))
        self.x_fact_button.setMaximumSize(QSize(16777215, 16777215))
        self.x_fact_button.setFont(font3)

        self.gridLayout_2.addWidget(self.x_fact_button, 3, 0, 1, 1)

        self.close_parenthesis_button = QPushButton(self.bottom_widget)
        self.close_parenthesis_button.setObjectName(u"close_parenthesis_button")
        self.close_parenthesis_button.setMinimumSize(QSize(0, 40))
        self.close_parenthesis_button.setMaximumSize(QSize(16777215, 16777215))
        self.close_parenthesis_button.setFont(font3)

        self.gridLayout_2.addWidget(self.close_parenthesis_button, 1, 1, 1, 1)

        self.sqrt_button = QPushButton(self.bottom_widget)
        self.sqrt_button.setObjectName(u"sqrt_button")
        self.sqrt_button.setMinimumSize(QSize(0, 40))
        self.sqrt_button.setMaximumSize(QSize(16777215, 16777215))
        self.sqrt_button.setFont(font3)

        self.gridLayout_2.addWidget(self.sqrt_button, 3, 2, 1, 1)

        self.fact_button = QPushButton(self.bottom_widget)
        self.fact_button.setObjectName(u"fact_button")
        self.fact_button.setMinimumSize(QSize(0, 40))
        self.fact_button.setMaximumSize(QSize(16777215, 16777215))
        self.fact_button.setFont(font3)

        self.gridLayout_2.addWidget(self.fact_button, 2, 0, 1, 1)

        self.y_button = QPushButton(self.bottom_widget)
        self.y_button.setObjectName(u"y_button")
        self.y_button.setMinimumSize(QSize(0, 40))
        self.y_button.setMaximumSize(QSize(16777215, 16777215))
        self.y_button.setFont(font3)

        self.gridLayout_2.addWidget(self.y_button, 0, 1, 1, 1)

        self.percent_button = QPushButton(self.bottom_widget)
        self.percent_button.setObjectName(u"percent_button")
        self.percent_button.setMinimumSize(QSize(0, 40))
        self.percent_button.setMaximumSize(QSize(16777215, 16777215))
        self.percent_button.setFont(font3)

        self.gridLayout_2.addWidget(self.percent_button, 3, 1, 1, 1)

        self.apos_button = QPushButton(self.bottom_widget)
        self.apos_button.setObjectName(u"apos_button")
        self.apos_button.setMinimumSize(QSize(0, 40))
        self.apos_button.setMaximumSize(QSize(16777215, 16777215))
        self.apos_button.setFont(font3)

        self.gridLayout_2.addWidget(self.apos_button, 2, 1, 1, 1)

        self.less_than_button = QPushButton(self.bottom_widget)
        self.less_than_button.setObjectName(u"less_than_button")
        self.less_than_button.setMinimumSize(QSize(0, 40))
        self.less_than_button.setFont(font3)

        self.gridLayout_2.addWidget(self.less_than_button, 2, 2, 1, 1)

        self.greater_than_button = QPushButton(self.bottom_widget)
        self.greater_than_button.setObjectName(u"greater_than_button")
        self.greater_than_button.setMinimumSize(QSize(0, 40))
        self.greater_than_button.setFont(font3)

        self.gridLayout_2.addWidget(self.greater_than_button, 2, 3, 1, 1)

        self.definite_integral_button = QPushButton(self.bottom_widget)
        self.definite_integral_button.setObjectName(u"definite_integral_button")
        self.definite_integral_button.setMinimumSize(QSize(0, 40))
        self.definite_integral_button.setFont(font3)

        self.gridLayout_2.addWidget(self.definite_integral_button, 1, 2, 1, 2)


        self.horizontalLayout_3.addLayout(self.gridLayout_2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.eight_button = QPushButton(self.bottom_widget)
        self.eight_button.setObjectName(u"eight_button")
        self.eight_button.setMinimumSize(QSize(0, 40))
        self.eight_button.setMaximumSize(QSize(16777215, 16777215))
        self.eight_button.setFont(font3)

        self.gridLayout_3.addWidget(self.eight_button, 0, 1, 1, 1)

        self.nine_button = QPushButton(self.bottom_widget)
        self.nine_button.setObjectName(u"nine_button")
        self.nine_button.setMinimumSize(QSize(0, 40))
        self.nine_button.setMaximumSize(QSize(16777215, 16777215))
        self.nine_button.setFont(font3)

        self.gridLayout_3.addWidget(self.nine_button, 0, 2, 1, 1)

        self.six_button = QPushButton(self.bottom_widget)
        self.six_button.setObjectName(u"six_button")
        self.six_button.setMinimumSize(QSize(0, 40))
        self.six_button.setMaximumSize(QSize(16777215, 16777215))
        self.six_button.setFont(font3)

        self.gridLayout_3.addWidget(self.six_button, 1, 2, 1, 1)

        self.add_button = QPushButton(self.bottom_widget)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setMinimumSize(QSize(0, 40))
        self.add_button.setMaximumSize(QSize(16777215, 16777215))
        self.add_button.setFont(font3)

        self.gridLayout_3.addWidget(self.add_button, 3, 3, 1, 1)

        self.one_button = QPushButton(self.bottom_widget)
        self.one_button.setObjectName(u"one_button")
        self.one_button.setMinimumSize(QSize(0, 40))
        self.one_button.setMaximumSize(QSize(16777215, 16777215))
        self.one_button.setFont(font3)

        self.gridLayout_3.addWidget(self.one_button, 2, 0, 1, 1)

        self.minus_button = QPushButton(self.bottom_widget)
        self.minus_button.setObjectName(u"minus_button")
        self.minus_button.setMinimumSize(QSize(0, 40))
        self.minus_button.setMaximumSize(QSize(16777215, 16777215))
        self.minus_button.setFont(font3)

        self.gridLayout_3.addWidget(self.minus_button, 2, 3, 1, 1)

        self.mul_button = QPushButton(self.bottom_widget)
        self.mul_button.setObjectName(u"mul_button")
        self.mul_button.setMinimumSize(QSize(0, 40))
        self.mul_button.setMaximumSize(QSize(16777215, 16777215))
        self.mul_button.setFont(font3)

        self.gridLayout_3.addWidget(self.mul_button, 1, 3, 1, 1)

        self.three_button = QPushButton(self.bottom_widget)
        self.three_button.setObjectName(u"three_button")
        self.three_button.setMinimumSize(QSize(0, 40))
        self.three_button.setMaximumSize(QSize(16777215, 16777215))
        self.three_button.setFont(font3)

        self.gridLayout_3.addWidget(self.three_button, 2, 2, 1, 1)

        self.seven_button = QPushButton(self.bottom_widget)
        self.seven_button.setObjectName(u"seven_button")
        self.seven_button.setMinimumSize(QSize(0, 40))
        self.seven_button.setMaximumSize(QSize(16777215, 16777215))
        self.seven_button.setFont(font3)

        self.gridLayout_3.addWidget(self.seven_button, 0, 0, 1, 1)

        self.two_button = QPushButton(self.bottom_widget)
        self.two_button.setObjectName(u"two_button")
        self.two_button.setMinimumSize(QSize(0, 40))
        self.two_button.setMaximumSize(QSize(16777215, 16777215))
        self.two_button.setFont(font3)

        self.gridLayout_3.addWidget(self.two_button, 2, 1, 1, 1)

        self.equal_button = QPushButton(self.bottom_widget)
        self.equal_button.setObjectName(u"equal_button")
        self.equal_button.setMinimumSize(QSize(0, 40))
        self.equal_button.setMaximumSize(QSize(16777215, 16777215))
        self.equal_button.setFont(font3)

        self.gridLayout_3.addWidget(self.equal_button, 3, 1, 1, 2)

        self.five_button = QPushButton(self.bottom_widget)
        self.five_button.setObjectName(u"five_button")
        self.five_button.setMinimumSize(QSize(0, 40))
        self.five_button.setMaximumSize(QSize(16777215, 16777215))
        self.five_button.setFont(font3)

        self.gridLayout_3.addWidget(self.five_button, 1, 1, 1, 1)

        self.div_button = QPushButton(self.bottom_widget)
        self.div_button.setObjectName(u"div_button")
        self.div_button.setMinimumSize(QSize(0, 40))
        self.div_button.setMaximumSize(QSize(16777215, 16777215))
        self.div_button.setFont(font3)

        self.gridLayout_3.addWidget(self.div_button, 0, 3, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.zero_button = QPushButton(self.bottom_widget)
        self.zero_button.setObjectName(u"zero_button")
        self.zero_button.setMinimumSize(QSize(0, 40))
        self.zero_button.setMaximumSize(QSize(16777215, 16777215))
        self.zero_button.setFont(font3)

        self.gridLayout_3.addWidget(self.zero_button, 3, 0, 1, 1)

        self.four_button = QPushButton(self.bottom_widget)
        self.four_button.setObjectName(u"four_button")
        self.four_button.setMinimumSize(QSize(0, 40))
        self.four_button.setMaximumSize(QSize(16777215, 16777215))
        self.four_button.setFont(font3)

        self.gridLayout_3.addWidget(self.four_button, 1, 0, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout_3)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.more_button = QPushButton(self.bottom_widget)
        self.more_button.setObjectName(u"more_button")
        self.more_button.setMinimumSize(QSize(0, 40))
        self.more_button.setFont(font3)

        self.verticalLayout_8.addWidget(self.more_button)

        self.del_button = QPushButton(self.bottom_widget)
        self.del_button.setObjectName(u"del_button")
        self.del_button.setMinimumSize(QSize(0, 40))
        self.del_button.setFont(font3)

        self.verticalLayout_8.addWidget(self.del_button)

        self.clear_button = QPushButton(self.bottom_widget)
        self.clear_button.setObjectName(u"clear_button")
        self.clear_button.setMinimumSize(QSize(0, 40))
        self.clear_button.setFont(font3)

        self.verticalLayout_8.addWidget(self.clear_button)

        self.empty_button = QPushButton(self.bottom_widget)
        self.empty_button.setObjectName(u"empty_button")
        self.empty_button.setEnabled(False)
        self.empty_button.setMinimumSize(QSize(0, 40))
        self.empty_button.setFont(font3)

        self.verticalLayout_8.addWidget(self.empty_button)


        self.horizontalLayout_3.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, -1, -1, 5)
        self.history_label = QLabel(self.bottom_widget)
        self.history_label.setObjectName(u"history_label")
        self.history_label.setFont(font3)

        self.verticalLayout_9.addWidget(self.history_label)

        self.history_list = QListWidget(self.bottom_widget)
        self.history_list.setObjectName(u"history_list")
        font4 = QFont()
        font4.setFamilies([u"Poppins"])
        font4.setPointSize(11)
        font4.setBold(False)
        self.history_list.setFont(font4)

        self.verticalLayout_9.addWidget(self.history_list)


        self.horizontalLayout_3.addLayout(self.verticalLayout_9)


        self.verticalLayout.addWidget(self.bottom_widget)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.mainWidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 684, 33))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuFile.setMinimumSize(QSize(160, 0))
        self.menuView = QMenu(self.menuBar)
        self.menuView.setObjectName(u"menuView")
        self.menuView.setGeometry(QRect(358, 151, 160, 150))
        self.menuView.setMinimumSize(QSize(160, 0))
        self.menuEdit = QMenu(self.menuBar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuEdit.setMinimumSize(QSize(160, 0))
        self.menuAbout = QMenu(self.menuBar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuAbout.setGeometry(QRect(671, 228, 160, 78))
        self.menuAbout.setMinimumSize(QSize(160, 0))
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menuView.addAction(self.actionZoom_In)
        self.menuView.addAction(self.actionZoom_Out)
        self.menuView.addAction(self.actionReset)
        self.menuView.addAction(self.actionTheme)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addAction(self.actionClear)
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
        self.action.setText(QCoreApplication.translate("MainWindow", u"Show/Hide", None))
        self.actionUndo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
        self.actionRedo.setText(QCoreApplication.translate("MainWindow", u"Redo", None))
        self.actionClear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.actionGithub_Link.setText(QCoreApplication.translate("MainWindow", u"Github Link", None))
        self.input_label.setText(QCoreApplication.translate("MainWindow", u"Input", None))
        self.input_edit.setText("")
        self.n_value_label.setText(QCoreApplication.translate("MainWindow", u"N-value", None))
        self.n_value_edit.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Graph", None))
        self.derivative_1st_label.setText(QCoreApplication.translate("MainWindow", u"1st Derivative", None))
        self.derivative_2nd_label.setText(QCoreApplication.translate("MainWindow", u"2nd Derivative", None))
        self.nth_derivative_label.setText(QCoreApplication.translate("MainWindow", u"Nth Derivative", None))
        self.integral_label.setText(QCoreApplication.translate("MainWindow", u"Integral", None))
        self.definite_integral_label.setText(QCoreApplication.translate("MainWindow", u"Definite Integral", None))
        self.x_button.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.a_2_button.setText(QCoreApplication.translate("MainWindow", u"a\u00b2", None))
        self.pi_button.setText(QCoreApplication.translate("MainWindow", u"\u03c0", None))
        self.a_b_button.setText(QCoreApplication.translate("MainWindow", u"a\u1d47", None))
        self.open_parenthesis_button.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.x_fact_button.setText(QCoreApplication.translate("MainWindow", u"x!", None))
        self.close_parenthesis_button.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.sqrt_button.setText(QCoreApplication.translate("MainWindow", u"\u221a", None))
        self.fact_button.setText(QCoreApplication.translate("MainWindow", u"!", None))
        self.y_button.setText(QCoreApplication.translate("MainWindow", u"y", None))
        self.percent_button.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.apos_button.setText(QCoreApplication.translate("MainWindow", u"'", None))
        self.less_than_button.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.greater_than_button.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.definite_integral_button.setText(QCoreApplication.translate("MainWindow", u"\u2090\u222b\u1d47", None))
        self.eight_button.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.nine_button.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.six_button.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.add_button.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.one_button.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.minus_button.setText(QCoreApplication.translate("MainWindow", u"\u2212", None))
        self.mul_button.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
        self.three_button.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.seven_button.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.two_button.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.equal_button.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.five_button.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.div_button.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.zero_button.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.four_button.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.more_button.setText(QCoreApplication.translate("MainWindow", u"more", None))
        self.del_button.setText(QCoreApplication.translate("MainWindow", u"del", None))
        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"clear", None))
        self.empty_button.setText("")
        self.history_label.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

