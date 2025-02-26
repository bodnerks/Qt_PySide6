# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'infodialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_infoDialog(object):
    def setupUi(self, infoDialog):
        if not infoDialog.objectName():
            infoDialog.setObjectName(u"infoDialog")
        infoDialog.resize(332, 165)
        self.verticalLayout = QVBoxLayout(infoDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(infoDialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.position_line_edit = QLineEdit(infoDialog)
        self.position_line_edit.setObjectName(u"position_line_edit")

        self.horizontalLayout.addWidget(self.position_line_edit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(infoDialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.favorite_os_combo_box = QComboBox(infoDialog)
        self.favorite_os_combo_box.addItem("")
        self.favorite_os_combo_box.addItem("")
        self.favorite_os_combo_box.addItem("")
        self.favorite_os_combo_box.setObjectName(u"favorite_os_combo_box")

        self.horizontalLayout_2.addWidget(self.favorite_os_combo_box)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.ok_button = QPushButton(infoDialog)
        self.ok_button.setObjectName(u"ok_button")

        self.horizontalLayout_3.addWidget(self.ok_button)

        self.cancel_button = QPushButton(infoDialog)
        self.cancel_button.setObjectName(u"cancel_button")

        self.horizontalLayout_3.addWidget(self.cancel_button)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(infoDialog)

        QMetaObject.connectSlotsByName(infoDialog)
    # setupUi

    def retranslateUi(self, infoDialog):
        infoDialog.setWindowTitle(QCoreApplication.translate("infoDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("infoDialog", u"Position", None))
        self.label_2.setText(QCoreApplication.translate("infoDialog", u"Favorite OS", None))
        self.favorite_os_combo_box.setItemText(0, QCoreApplication.translate("infoDialog", u"Windows", None))
        self.favorite_os_combo_box.setItemText(1, QCoreApplication.translate("infoDialog", u"LInux", None))
        self.favorite_os_combo_box.setItemText(2, QCoreApplication.translate("infoDialog", u"Mac", None))

        self.ok_button.setText(QCoreApplication.translate("infoDialog", u"OK", None))
        self.cancel_button.setText(QCoreApplication.translate("infoDialog", u"Cancel", None))
    # retranslateUi

