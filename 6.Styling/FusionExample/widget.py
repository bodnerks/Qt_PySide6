from PySide6.QtWidgets import QWidget

from ui_widget import Ui_Widget

class Widget( QWidget, Ui_Widget ):
    def __init__( self ):
        super().__init__()
        self.setupUi( self )
        self.setWindowTitle( "Fusion Style Demo" )

        # connect signals to slots
        self.get_input_button.clicked.connect( self.get_input )

    def get_input( self ):
        print( "Hello" )