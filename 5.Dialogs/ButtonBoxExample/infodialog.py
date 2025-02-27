from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QDialogButtonBox
from ui_infodialog import Ui_infoDialog

class InfoDialog( QDialog, Ui_infoDialog ):
    def __init__( self ):
        super().__init__()
        self.setupUi( self )
        self.setWindowTitle( "Provide your info" )

        # fields
        self.position = ""
        self.favorite_os = ""

        # connections
        self.button_box.clicked.connect( self.button_box_clicked )

    def button_box_clicked( self, button ): # button that was clicked
        std_button = self.button_box.standardButton( button ) # which button clicked
        if ( std_button == QDialogButtonBox.Ok ):
            if ( not( self.position_line_edit.text() == '' ) ):
                self.position = self.position_line_edit.text()
            self.favorite_os = self.favorite_os_combo_box.currentText()
            self.accept()
        elif( std_button == QDialogButtonBox.Cancel ):
            self.reject()
        elif( std_button == QDialogButtonBox.Save ):
            print( "Save" )
        elif ( std_button == QDialogButtonBox.SaveAll ):
            print( "SaveAll" )
        elif( std_button == QDialogButtonBox.Open ):
            print( "Open" )
        else:
            print( "Some other button" )