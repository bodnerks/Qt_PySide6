from PySide6.QtWidgets import QWidget, QFontDialog
from PySide6.QtGui import QFont
from ui_widget import Ui_Widget


class Widget( QWidget, Ui_Widget ):
    def __init__( self ):
        super().__init__()
        self.setupUi( self )
        self.setWindowTitle( "QFontDialog Demo" )
        self.select_font_button.clicked.connect( self.select_font )

    def select_font( self ):
        ok, font = QFontDialog.getFont( QFont( "Helvetica [Cronyx]", 20 ), self )
        if ok:
            self.font_label.setFont( font )
            self.font_label.setText( "Holy diver" )
        else:
            print( "User didn't select any valid font" )

    