# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'more_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MoreFunctions(object):
    def setupUi(self, MoreFunctions):
        if not MoreFunctions.objectName():
            MoreFunctions.setObjectName(u"MoreFunctions")
        MoreFunctions.resize(257, 220)
        MoreFunctions.setMinimumSize(QSize(257, 220))
        MoreFunctions.setMaximumSize(QSize(259, 220))
        font = QFont()
        font.setFamilies([u"Poppins"])
        MoreFunctions.setFont(font)
        MoreFunctions.setStyleSheet(u"#MoreFunctions {\n"
"	background-color: rgb(169, 178, 178);\n"
"}\n"
"\n"
"QPushButton {\n"
"	font-size: 18px;\n"
"	font-weight: 500;\n"
"}\n"
"\n"
"QLabel {\n"
"	font-size: 13px;\n"
"	font-weight: 600;\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(MoreFunctions)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.others_label = QLabel(MoreFunctions)
        self.others_label.setObjectName(u"others_label")

        self.verticalLayout.addWidget(self.others_label, 0, Qt.AlignmentFlag.AlignBottom)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.log_button = QPushButton(MoreFunctions)
        self.log_button.setObjectName(u"log_button")
        self.log_button.setMinimumSize(QSize(0, 45))

        self.gridLayout_2.addWidget(self.log_button, 0, 1, 1, 1)

        self.ln_button = QPushButton(MoreFunctions)
        self.ln_button.setObjectName(u"ln_button")
        self.ln_button.setMinimumSize(QSize(0, 45))

        self.gridLayout_2.addWidget(self.ln_button, 0, 2, 1, 1)

        self.e_button = QPushButton(MoreFunctions)
        self.e_button.setObjectName(u"e_button")
        self.e_button.setMinimumSize(QSize(0, 45))

        self.gridLayout_2.addWidget(self.e_button, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.trigo_button = QLabel(MoreFunctions)
        self.trigo_button.setObjectName(u"trigo_button")

        self.verticalLayout_2.addWidget(self.trigo_button)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.sin_button = QPushButton(MoreFunctions)
        self.sin_button.setObjectName(u"sin_button")
        self.sin_button.setMinimumSize(QSize(0, 45))

        self.gridLayout.addWidget(self.sin_button, 0, 0, 1, 1)

        self.cos_button = QPushButton(MoreFunctions)
        self.cos_button.setObjectName(u"cos_button")
        self.cos_button.setMinimumSize(QSize(0, 45))

        self.gridLayout.addWidget(self.cos_button, 0, 1, 1, 1)

        self.tan_button = QPushButton(MoreFunctions)
        self.tan_button.setObjectName(u"tan_button")
        self.tan_button.setMinimumSize(QSize(0, 45))

        self.gridLayout.addWidget(self.tan_button, 0, 2, 1, 1)

        self.csc_button = QPushButton(MoreFunctions)
        self.csc_button.setObjectName(u"csc_button")
        self.csc_button.setMinimumSize(QSize(0, 45))

        self.gridLayout.addWidget(self.csc_button, 1, 0, 1, 1)

        self.sec_button = QPushButton(MoreFunctions)
        self.sec_button.setObjectName(u"sec_button")
        self.sec_button.setMinimumSize(QSize(0, 45))

        self.gridLayout.addWidget(self.sec_button, 1, 1, 1, 1)

        self.cot_button = QPushButton(MoreFunctions)
        self.cot_button.setObjectName(u"cot_button")
        self.cot_button.setMinimumSize(QSize(0, 45))

        self.gridLayout.addWidget(self.cot_button, 1, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(MoreFunctions)

        QMetaObject.connectSlotsByName(MoreFunctions)
    # setupUi

    def retranslateUi(self, MoreFunctions):
        MoreFunctions.setWindowTitle(QCoreApplication.translate("MoreFunctions", u"Form", None))
        self.others_label.setText(QCoreApplication.translate("MoreFunctions", u"Others", None))
        self.log_button.setText(QCoreApplication.translate("MoreFunctions", u"log", None))
        self.ln_button.setText(QCoreApplication.translate("MoreFunctions", u"ln", None))
        self.e_button.setText(QCoreApplication.translate("MoreFunctions", u"e", None))
        self.trigo_button.setText(QCoreApplication.translate("MoreFunctions", u"Trigonometric", None))
        self.sin_button.setText(QCoreApplication.translate("MoreFunctions", u"sin", None))
        self.cos_button.setText(QCoreApplication.translate("MoreFunctions", u"cos", None))
        self.tan_button.setText(QCoreApplication.translate("MoreFunctions", u"tan", None))
        self.csc_button.setText(QCoreApplication.translate("MoreFunctions", u"csc", None))
        self.sec_button.setText(QCoreApplication.translate("MoreFunctions", u"sec", None))
        self.cot_button.setText(QCoreApplication.translate("MoreFunctions", u"cot", None))
    # retranslateUi

