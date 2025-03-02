from PySide6.QtWidgets import QWidget, QInputDialog, QLineEdit
from PySide6.QtCore import QDir
from ui_widget import Ui_Widget

class Widget( QWidget, Ui_Widget ):
    def __init__( self ):
        super().__init__()
        self.setupUi( self )
        self.setWindowTitle( "QInputDialog Demo" )

        # connect signals to slots
        self.get_input_button.clicked.connect( self.get_input )

    def get_input( self ):

        '''
        # get text
        text, ok = QInputDialog.getText( self, "getText", "Enter your name: " )
        if ok and not text == "":
            self.value_label.setText( text )

        '''

        '''
        # get double
        value, ok = QInputDialog.getDouble( self, "Get double", "Select a value: ", 150, 100, 200 )
        if ok:
            self.value_label.setText( f"{value}" )

        '''


        '''
        # get int
        value, ok = QInputDialog.getInt( self, "Get int", "Select a value: ", 150, 100, 200 )
        if ok:
            self.value_label.setText( f"{value}" )

        '''

        # get item
        items = [ "Spring", "Sumer", "Fall", "Winter" ]
        item, ok = QInputDialog.getItem( self, "Get item", "Season: ", items )
        if ok:
            self.value_label.setText( item )