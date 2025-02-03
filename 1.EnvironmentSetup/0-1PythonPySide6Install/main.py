from PySide6.QtWidgets import QApplication, QWidget

import sys # for command line options

app = QApplication(sys.argv)

window = QWidget()
window.show()

app.exec()