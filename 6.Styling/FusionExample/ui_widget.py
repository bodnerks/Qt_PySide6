# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(420, 501)
        self.verticalLayout_3 = QVBoxLayout(Widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.get_input_button = QPushButton(Widget)
        self.get_input_button.setObjectName(u"get_input_button")

        self.verticalLayout_3.addWidget(self.get_input_button)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.value_label = QLabel(Widget)
        self.value_label.setObjectName(u"value_label")

        self.horizontalLayout_2.addWidget(self.value_label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setChecked(True)

        self.verticalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.groupBox)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.verticalLayout.addWidget(self.radioButton_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.combo_box = QComboBox(Widget)
        self.combo_box.setObjectName(u"combo_box")

        self.horizontalLayout.addWidget(self.combo_box)

        self.line_edit = QLineEdit(Widget)
        self.line_edit.setObjectName(u"line_edit")

        self.horizontalLayout.addWidget(self.line_edit)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.textEdit = QTextEdit(Widget)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_3.addWidget(self.textEdit)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.get_input_button.setText(QCoreApplication.translate("Widget", u"Get Input", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Value:", None))
        self.value_label.setText(QCoreApplication.translate("Widget", u"[Value]", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"GroupBox", None))
        self.radioButton.setText(QCoreApplication.translate("Widget", u"RadioButton", None))
        self.radioButton_2.setText(QCoreApplication.translate("Widget", u"RadioButton", None))
        self.radioButton_3.setText(QCoreApplication.translate("Widget", u"RadioButton", None))
    # retranslateUi

