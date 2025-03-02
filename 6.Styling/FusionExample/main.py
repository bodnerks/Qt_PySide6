import sys

from PySide6 import QtWidgets
from widget import Widget

app = QtWidgets.QApplication( sys.argv )
app.setStyle( 'Fusion' ) # use the Fusion style

window = Widget()
window.show()

app.exec()

