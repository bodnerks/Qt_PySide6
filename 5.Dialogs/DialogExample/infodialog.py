from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog
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
        self.ok_button.clicked.connect( self.ok )
        self.cancel_button.clicked.connect( self.cancel )


    # slots
    def ok( self ):
        if ( not( self.position_line_edit.text() == '' ) ):
            self.position = self.position_line_edit.text()
        self.favorite_os = self.favorite_os_combo_box.currentText()
        self.accept() # user accepted info
    
    def cancel( self ):
        self.reject() # rekect dialog