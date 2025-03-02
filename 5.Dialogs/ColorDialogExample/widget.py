from PySide6.QtWidgets import QWidget, QFontDialog, QColorDialog
from PySide6.QtGui import QFont, QPalette
from ui_widget import Ui_Widget

class Widget( QWidget, Ui_Widget ):
    def __init__( self ):
        super().__init__()
        self.setupUi( self )
        self.setWindowTitle( "QFontDialog Demo" )
        self.text_label.setAutoFillBackground( True ) # important for the colors to show up

        # connect signals to slots
        self.text_color_button.clicked.connect( self.text_color_button_clicked )
        self.background_color_button.clicked.connect( self.background_color_button_clicked )
        self.font_button.clicked.connect( self.set_font )

    def text_color_button_clicked( self ):
        palette = self.text_label.palette() # get palette of label
        color = palette.color( QPalette.WindowText ) # use color of text as default color in ColorDialog 
        chosenColor = QColorDialog.getColor( color, self, "Choose text color" )

        if chosenColor.isValid():
            palette.setColor( QPalette.WindowText, chosenColor )
            self.text_label.setPalette( palette )
        else:
            print( "User chose a bad text color" )


    def background_color_button_clicked( self ):
        palette = self.text_label.palette() # get palette of label
        color = palette.color( QPalette.Window ) # use color of text as default color in ColorDialog 
        chosenColor = QColorDialog.getColor( color, self, "Choose background color" )

        if chosenColor.isValid():
            palette.setColor( QPalette.Window, chosenColor )
            self.text_label.setPalette( palette )
        else:
            print( "User chose a bad text color" )


    def set_font( self ):
        ok, font = QFontDialog.getFont( QFont( "Helvetica [Cronyx]", 20 ), self )
        if ok:
            self.text_label.setFont( font )
        else:
            print( "User didn't select any valid font" )


