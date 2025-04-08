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
        MainWindow.resize(684, 680)
        MainWindow.setMinimumSize(QSize(684, 680))
        MainWindow.setMaximumSize(QSize(896, 900))
        font = QFont()
        font.setFamilies([u"Poppins"])
        MainWindow.setFont(font)
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
        icon7 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.WeatherClear))
        self.actionTheme.setIcon(icon7)
        self.actionShow_Hide = QAction(MainWindow)
        self.actionShow_Hide.setObjectName(u"actionShow_Hide")
        icon8 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.WindowNew))
        self.actionShow_Hide.setIcon(icon8)
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
        self.mainWidget.setFont(font)
        self.gridLayout = QGridLayout(self.mainWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_widget = QWidget(self.mainWidget)
        self.top_widget.setObjectName(u"top_widget")
        self.horizontalLayout_2 = QHBoxLayout(self.top_widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_widget = QWidget(self.top_widget)
        self.left_widget.setObjectName(u"left_widget")
        self.verticalLayout_7 = QVBoxLayout(self.left_widget)
        self.verticalLayout_7.setSpacing(20)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.input_label = QLabel(self.left_widget)
        self.input_label.setObjectName(u"input_label")
        self.input_label.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_12.addWidget(self.input_label, 0, Qt.AlignmentFlag.AlignBottom)

        self.input_edit = QLineEdit(self.left_widget)
        self.input_edit.setObjectName(u"input_edit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_edit.sizePolicy().hasHeightForWidth())
        self.input_edit.setSizePolicy(sizePolicy)
        self.input_edit.setMinimumSize(QSize(0, 35))

        self.verticalLayout_12.addWidget(self.input_edit)


        self.verticalLayout_2.addLayout(self.verticalLayout_12)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.n_value_label_2 = QLabel(self.left_widget)
        self.n_value_label_2.setObjectName(u"n_value_label_2")
        self.n_value_label_2.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_13.addWidget(self.n_value_label_2, 0, Qt.AlignmentFlag.AlignBottom)

        self.n_value_edit_2 = QLineEdit(self.left_widget)
        self.n_value_edit_2.setObjectName(u"n_value_edit_2")
        sizePolicy.setHeightForWidth(self.n_value_edit_2.sizePolicy().hasHeightForWidth())
        self.n_value_edit_2.setSizePolicy(sizePolicy)
        self.n_value_edit_2.setMinimumSize(QSize(0, 35))

        self.verticalLayout_13.addWidget(self.n_value_edit_2)


        self.verticalLayout_2.addLayout(self.verticalLayout_13)


        self.verticalLayout_7.addLayout(self.verticalLayout_2)

        self.graph_widget = QWidget(self.left_widget)
        self.graph_widget.setObjectName(u"graph_widget")
        self.label = QLabel(self.graph_widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 37, 17))

        self.verticalLayout_7.addWidget(self.graph_widget)


        self.horizontalLayout.addWidget(self.left_widget)

        self.right_widget = QWidget(self.top_widget)
        self.right_widget.setObjectName(u"right_widget")
        self.verticalLayout_6 = QVBoxLayout(self.right_widget)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.derivative_1st_label = QLabel(self.right_widget)
        self.derivative_1st_label.setObjectName(u"derivative_1st_label")
        self.derivative_1st_label.setMaximumSize(QSize(432, 20))

        self.verticalLayout_5.addWidget(self.derivative_1st_label, 0, Qt.AlignmentFlag.AlignBottom)

        self.derivative_1st_edit = QLineEdit(self.right_widget)
        self.derivative_1st_edit.setObjectName(u"derivative_1st_edit")
        sizePolicy.setHeightForWidth(self.derivative_1st_edit.sizePolicy().hasHeightForWidth())
        self.derivative_1st_edit.setSizePolicy(sizePolicy)
        self.derivative_1st_edit.setMinimumSize(QSize(0, 35))

        self.verticalLayout_5.addWidget(self.derivative_1st_edit)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.derivative_2nd_label = QLabel(self.right_widget)
        self.derivative_2nd_label.setObjectName(u"derivative_2nd_label")
        self.derivative_2nd_label.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_4.addWidget(self.derivative_2nd_label, 0, Qt.AlignmentFlag.AlignBottom)

        self.derivative_2nd_edit = QLineEdit(self.right_widget)
        self.derivative_2nd_edit.setObjectName(u"derivative_2nd_edit")
        sizePolicy.setHeightForWidth(self.derivative_2nd_edit.sizePolicy().hasHeightForWidth())
        self.derivative_2nd_edit.setSizePolicy(sizePolicy)
        self.derivative_2nd_edit.setMinimumSize(QSize(0, 35))

        self.verticalLayout_4.addWidget(self.derivative_2nd_edit)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.nth_derivative_label = QLabel(self.right_widget)
        self.nth_derivative_label.setObjectName(u"nth_derivative_label")
        self.nth_derivative_label.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_3.addWidget(self.nth_derivative_label, 0, Qt.AlignmentFlag.AlignBottom)

        self.nth_derivative_edit = QLineEdit(self.right_widget)
        self.nth_derivative_edit.setObjectName(u"nth_derivative_edit")
        sizePolicy.setHeightForWidth(self.nth_derivative_edit.sizePolicy().hasHeightForWidth())
        self.nth_derivative_edit.setSizePolicy(sizePolicy)
        self.nth_derivative_edit.setMinimumSize(QSize(0, 35))

        self.verticalLayout_3.addWidget(self.nth_derivative_edit)


        self.verticalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.integral_label = QLabel(self.right_widget)
        self.integral_label.setObjectName(u"integral_label")
        self.integral_label.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_10.addWidget(self.integral_label, 0, Qt.AlignmentFlag.AlignBottom)

        self.integral_edit = QLineEdit(self.right_widget)
        self.integral_edit.setObjectName(u"integral_edit")
        sizePolicy.setHeightForWidth(self.integral_edit.sizePolicy().hasHeightForWidth())
        self.integral_edit.setSizePolicy(sizePolicy)
        self.integral_edit.setMinimumSize(QSize(0, 35))

        self.verticalLayout_10.addWidget(self.integral_edit)


        self.verticalLayout_6.addLayout(self.verticalLayout_10)


        self.horizontalLayout.addWidget(self.right_widget)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.top_widget)

        self.bottom_widget = QWidget(self.mainWidget)
        self.bottom_widget.setObjectName(u"bottom_widget")
        self.bottom_widget.setMaximumSize(QSize(16777215, 250))
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

        self.gridLayout_2.addWidget(self.x_button, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.y_button = QPushButton(self.bottom_widget)
        self.y_button.setObjectName(u"y_button")
        self.y_button.setMinimumSize(QSize(0, 40))
        self.y_button.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.y_button, 0, 1, 1, 1)

        self.a_2_button = QPushButton(self.bottom_widget)
        self.a_2_button.setObjectName(u"a_2_button")
        self.a_2_button.setMinimumSize(QSize(0, 40))
        self.a_2_button.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.a_2_button, 0, 2, 1, 1)

        self.a_b_button = QPushButton(self.bottom_widget)
        self.a_b_button.setObjectName(u"a_b_button")
        self.a_b_button.setMinimumSize(QSize(0, 40))
        self.a_b_button.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.a_b_button, 0, 3, 1, 1)

        self.open_parenthesis_button = QPushButton(self.bottom_widget)
        self.open_parenthesis_button.setObjectName(u"open_parenthesis_button")
        self.open_parenthesis_button.setMinimumSize(QSize(0, 40))
        self.open_parenthesis_button.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.open_parenthesis_button, 1, 0, 1, 1)

        self.close_parenthesis_button = QPushButton(self.bottom_widget)
        self.close_parenthesis_button.setObjectName(u"close_parenthesis_button")
        self.close_parenthesis_button.setMinimumSize(QSize(0, 40))
        self.close_parenthesis_button.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.close_parenthesis_button, 1, 1, 1, 1)

        self.less_button = QPushButton(self.bottom_widget)
        self.less_button.setObjectName(u"less_button")
        self.less_button.setMinimumSize(QSize(0, 40))
        self.less_button.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.less_button, 1, 2, 1, 1)

        self.great_button = QPushButton(self.bottom_widget)
        self.great_button.setObjectName(u"great_button")
        self.great_button.setMinimumSize(QSize(0, 40))
        self.great_button.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.great_button, 1, 3, 1, 1)

        self.fact_button = QPushButton(self.bottom_widget)
        self.fact_button.setObjectName(u"fact_button")
        self.fact_button.setMinimumSize(QSize(0, 40))
        self.fact_button.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.fact_button, 2, 0, 1, 1)

        self.apos_button = QPushButton(self.bottom_widget)
        self.apos_button.setObjectName(u"apos_button")
        self.apos_button.setMinimumSize(QSize(0, 40))
        self.apos_button.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.apos_button, 2, 1, 1, 1)

        self.less_equal_button = QPushButton(self.bottom_widget)
        self.less_equal_button.setObjectName(u"less_equal_button")
        self.less_equal_button.setMinimumSize(QSize(0, 40))
        self.less_equal_button.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.less_equal_button, 2, 2, 1, 1)

        self.great_equal_button = QPushButton(self.bottom_widget)
        self.great_equal_button.setObjectName(u"great_equal_button")
        self.great_equal_button.setMinimumSize(QSize(0, 40))
        self.great_equal_button.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.great_equal_button, 2, 3, 1, 1)

        self.x_fact_button = QPushButton(self.bottom_widget)
        self.x_fact_button.setObjectName(u"x_fact_button")
        self.x_fact_button.setMinimumSize(QSize(0, 40))
        self.x_fact_button.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.x_fact_button, 3, 0, 1, 1)

        self.percent_button = QPushButton(self.bottom_widget)
        self.percent_button.setObjectName(u"percent_button")
        self.percent_button.setMinimumSize(QSize(0, 40))
        self.percent_button.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.percent_button, 3, 1, 1, 1)

        self.sqrt_button = QPushButton(self.bottom_widget)
        self.sqrt_button.setObjectName(u"sqrt_button")
        self.sqrt_button.setMinimumSize(QSize(0, 40))
        self.sqrt_button.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.sqrt_button, 3, 2, 1, 1)

        self.pi_button = QPushButton(self.bottom_widget)
        self.pi_button.setObjectName(u"pi_button")
        self.pi_button.setMinimumSize(QSize(0, 40))
        self.pi_button.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.pi_button, 3, 3, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout_2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.zero_button = QPushButton(self.bottom_widget)
        self.zero_button.setObjectName(u"zero_button")
        self.zero_button.setMinimumSize(QSize(0, 40))
        self.zero_button.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.zero_button, 3, 0, 1, 1)

        self.nine_button = QPushButton(self.bottom_widget)
        self.nine_button.setObjectName(u"nine_button")
        self.nine_button.setMinimumSize(QSize(0, 40))
        self.nine_button.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.nine_button, 0, 2, 1, 1)

        self.minus_button = QPushButton(self.bottom_widget)
        self.minus_button.setObjectName(u"minus_button")
        self.minus_button.setMinimumSize(QSize(0, 40))
        self.minus_button.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.minus_button, 2, 3, 1, 1)

        self.seven_button = QPushButton(self.bottom_widget)
        self.seven_button.setObjectName(u"seven_button")
        self.seven_button.setMinimumSize(QSize(0, 40))
        self.seven_button.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.seven_button, 0, 0, 1, 1)

        self.four_button = QPushButton(self.bottom_widget)
        self.four_button.setObjectName(u"four_button")
        self.four_button.setMinimumSize(QSize(0, 40))
        self.four_button.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.four_button, 1, 0, 1, 1)

        self.one_button = QPushButton(self.bottom_widget)
        self.one_button.setObjectName(u"one_button")
        self.one_button.setMinimumSize(QSize(0, 40))
        self.one_button.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.one_button, 2, 0, 1, 1)

        self.two_button = QPushButton(self.bottom_widget)
        self.two_button.setObjectName(u"two_button")
        self.two_button.setMinimumSize(QSize(0, 40))
        self.two_button.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.two_button, 2, 1, 1, 1)

        self.div_button = QPushButton(self.bottom_widget)
        self.div_button.setObjectName(u"div_button")
        self.div_button.setMinimumSize(QSize(0, 40))
        self.div_button.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.div_button, 0, 3, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.six_button = QPushButton(self.bottom_widget)
        self.six_button.setObjectName(u"six_button")
        self.six_button.setMinimumSize(QSize(0, 40))
        self.six_button.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.six_button, 1, 2, 1, 1)

        self.five_button = QPushButton(self.bottom_widget)
        self.five_button.setObjectName(u"five_button")
        self.five_button.setMinimumSize(QSize(0, 40))
        self.five_button.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.five_button, 1, 1, 1, 1)

        self.eight_button = QPushButton(self.bottom_widget)
        self.eight_button.setObjectName(u"eight_button")
        self.eight_button.setMinimumSize(QSize(0, 40))
        self.eight_button.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.eight_button, 0, 1, 1, 1)

        self.mul_button = QPushButton(self.bottom_widget)
        self.mul_button.setObjectName(u"mul_button")
        self.mul_button.setMinimumSize(QSize(0, 40))
        self.mul_button.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.mul_button, 1, 3, 1, 1)

        self.add_button = QPushButton(self.bottom_widget)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setMinimumSize(QSize(0, 40))
        self.add_button.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.add_button, 3, 3, 1, 1)

        self.three_button = QPushButton(self.bottom_widget)
        self.three_button.setObjectName(u"three_button")
        self.three_button.setMinimumSize(QSize(0, 40))
        self.three_button.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.three_button, 2, 2, 1, 1)

        self.equal_button = QPushButton(self.bottom_widget)
        self.equal_button.setObjectName(u"equal_button")
        self.equal_button.setMinimumSize(QSize(0, 40))
        self.equal_button.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.equal_button, 3, 1, 1, 2)


        self.horizontalLayout_3.addLayout(self.gridLayout_3)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.more_button = QPushButton(self.bottom_widget)
        self.more_button.setObjectName(u"more_button")
        self.more_button.setMinimumSize(QSize(0, 40))

        self.verticalLayout_8.addWidget(self.more_button)

        self.del_button = QPushButton(self.bottom_widget)
        self.del_button.setObjectName(u"del_button")
        self.del_button.setMinimumSize(QSize(0, 40))

        self.verticalLayout_8.addWidget(self.del_button)

        self.clear_button = QPushButton(self.bottom_widget)
        self.clear_button.setObjectName(u"clear_button")
        self.clear_button.setMinimumSize(QSize(0, 40))

        self.verticalLayout_8.addWidget(self.clear_button)

        self.pushButton_36 = QPushButton(self.bottom_widget)
        self.pushButton_36.setObjectName(u"pushButton_36")
        self.pushButton_36.setMinimumSize(QSize(0, 40))

        self.verticalLayout_8.addWidget(self.pushButton_36)


        self.horizontalLayout_3.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, -1, -1, 5)
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
        self.menuFile.setMinimumSize(QSize(160, 0))
        self.menuView = QMenu(self.menuBar)
        self.menuView.setObjectName(u"menuView")
        self.menuView.setGeometry(QRect(607, 287, 160, 174))
        self.menuView.setMinimumSize(QSize(160, 0))
        self.menuEdit = QMenu(self.menuBar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuEdit.setMinimumSize(QSize(160, 0))
        self.menuAbout = QMenu(self.menuBar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuAbout.setGeometry(QRect(724, 287, 200, 78))
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
        self.menuView.addAction(self.actionShow_Hide)
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
        self.actionShow_Hide.setText(QCoreApplication.translate("MainWindow", u"Show/Hide", None))
        self.actionUndo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
        self.actionRedo.setText(QCoreApplication.translate("MainWindow", u"Redo", None))
        self.actionClear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.actionGithub_Link.setText(QCoreApplication.translate("MainWindow", u"Github Link", None))
        self.input_label.setText(QCoreApplication.translate("MainWindow", u"Input", None))
        self.input_edit.setText("")
        self.n_value_label_2.setText(QCoreApplication.translate("MainWindow", u"N-value", None))
        self.n_value_edit_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Graph", None))
        self.derivative_1st_label.setText(QCoreApplication.translate("MainWindow", u"1st Derivative", None))
        self.derivative_2nd_label.setText(QCoreApplication.translate("MainWindow", u"2nd Derivative", None))
        self.nth_derivative_label.setText(QCoreApplication.translate("MainWindow", u"Nth Derivative", None))
        self.integral_label.setText(QCoreApplication.translate("MainWindow", u"Integral", None))
        self.x_button.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.y_button.setText(QCoreApplication.translate("MainWindow", u"y", None))
        self.a_2_button.setText(QCoreApplication.translate("MainWindow", u"a\u00b2", None))
        self.a_b_button.setText(QCoreApplication.translate("MainWindow", u"a\u1d47", None))
        self.open_parenthesis_button.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.close_parenthesis_button.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.less_button.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.great_button.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.fact_button.setText(QCoreApplication.translate("MainWindow", u"!", None))
        self.apos_button.setText(QCoreApplication.translate("MainWindow", u"'", None))
        self.less_equal_button.setText(QCoreApplication.translate("MainWindow", u"\u2264", None))
        self.great_equal_button.setText(QCoreApplication.translate("MainWindow", u"\u2265", None))
        self.x_fact_button.setText(QCoreApplication.translate("MainWindow", u"x!", None))
        self.percent_button.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.sqrt_button.setText(QCoreApplication.translate("MainWindow", u"\u221a", None))
        self.pi_button.setText(QCoreApplication.translate("MainWindow", u"\u03c0", None))
        self.zero_button.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.nine_button.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.minus_button.setText(QCoreApplication.translate("MainWindow", u"\u2212", None))
        self.seven_button.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.four_button.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.one_button.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.two_button.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.div_button.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.six_button.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.five_button.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.eight_button.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.mul_button.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
        self.add_button.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.three_button.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.equal_button.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.more_button.setText(QCoreApplication.translate("MainWindow", u"more", None))
        self.del_button.setText(QCoreApplication.translate("MainWindow", u"delete", None))
        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"clear", None))
        self.pushButton_36.setText(QCoreApplication.translate("MainWindow", u"trigo", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

