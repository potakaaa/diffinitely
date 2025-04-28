# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'definite_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_DefiniteIntegralInput(object):
    def setupUi(self, DefiniteIntegralInput):
        if not DefiniteIntegralInput.objectName():
            DefiniteIntegralInput.setObjectName(u"DefiniteIntegralInput")
        DefiniteIntegralInput.resize(260, 160)
        DefiniteIntegralInput.setMinimumSize(QSize(260, 160))
        DefiniteIntegralInput.setMaximumSize(QSize(260, 160))
        font = QFont()
        font.setFamilies([u"Poppins"])
        DefiniteIntegralInput.setFont(font)
        DefiniteIntegralInput.setStyleSheet(u"\n"
"#DefiniteIntegralInput {\n"
"    background-color: rgb(169, 178, 178);\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 13px;\n"
"    font-weight: 600;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QLineEdit {\n"
"    font-size: 16px;\n"
"}\n"
"   ")
        self.verticalLayout = QVBoxLayout(DefiniteIntegralInput)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.limitsLayout = QVBoxLayout()
        self.limitsLayout.setObjectName(u"limitsLayout")
        self.label_a = QLabel(DefiniteIntegralInput)
        self.label_a.setObjectName(u"label_a")

        self.limitsLayout.addWidget(self.label_a)

        self.a_value_edit = QLineEdit(DefiniteIntegralInput)
        self.a_value_edit.setObjectName(u"a_value_edit")
        self.a_value_edit.setMinimumSize(QSize(0, 35))
        self.a_value_edit.setMaximumSize(QSize(16777215, 44))
        font1 = QFont()
        font1.setFamilies([u"Poppins"])
        font1.setPointSize(11)
        self.a_value_edit.setFont(font1)

        self.limitsLayout.addWidget(self.a_value_edit)

        self.label_b = QLabel(DefiniteIntegralInput)
        self.label_b.setObjectName(u"label_b")

        self.limitsLayout.addWidget(self.label_b)

        self.b_value_edit = QLineEdit(DefiniteIntegralInput)
        self.b_value_edit.setObjectName(u"b_value_edit")
        self.b_value_edit.setMinimumSize(QSize(0, 35))
        self.b_value_edit.setMaximumSize(QSize(16777215, 44))
        self.b_value_edit.setFont(font1)

        self.limitsLayout.addWidget(self.b_value_edit)


        self.verticalLayout.addLayout(self.limitsLayout)


        self.retranslateUi(DefiniteIntegralInput)

        QMetaObject.connectSlotsByName(DefiniteIntegralInput)
    # setupUi

    def retranslateUi(self, DefiniteIntegralInput):
        DefiniteIntegralInput.setWindowTitle(QCoreApplication.translate("DefiniteIntegralInput", u"Definite Integral Limits", None))
        self.label_a.setText(QCoreApplication.translate("DefiniteIntegralInput", u"Lower limit (a):", None))
        self.label_b.setText(QCoreApplication.translate("DefiniteIntegralInput", u"Upper limit (b):", None))
    # retranslateUi

