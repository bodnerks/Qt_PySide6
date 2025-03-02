from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt
from ui_widget import Ui_Widget


class Widget( QWidget, Ui_Widget ):
    def __init__( self ):
        super().__init__()
        self.setupUi( self )
        self.setWindowTitle( "Palette Demo" )

        # retrieve global palette; can also call palette on the application object
        palette = QPalette() # palette is a copy

        # modify the palette with changes
        palette.setColor( QPalette.Window, Qt.blue )
        palette.setColor( QPalette.WindowText, Qt.red )

        self.sky_label.setAutoFillBackground( True )
        # apply palette
        self.sky_label.setPalette( palette )

        # grab palette from another label and use it
        self.blue_label.setAutoFillBackground( True )
        self.blue_label.setPalette( self.sky_label.palette() )