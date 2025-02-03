from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QPalette, QColor
from widget import Widget
import sys

app = QApplication(sys.argv)
app.setPalette( QPalette( QColor( "#444444" ) ) )

widget = Widget()
widget.show()

app.exec()