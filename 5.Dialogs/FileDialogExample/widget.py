from fileinput import filename
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget,QFileDialog
from ui_widget import Ui_Widget

class Widget( QWidget, Ui_Widget ):
    def __init__(self):
        super().__init__()
        self.setupUi( self )
        self.setWindowTitle( "User data" )

        self.click_button.clicked.connect( self.button_clicked )

    def button_clicked( self ):


        '''
        # get existing directory
        dir = QFileDialog.getExistingDirectory( self, "Open directory", "/home", QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks )

        print( f"Chosen dir: {dir}" )
        '''

        '''
        # GetOpenFileName
        file_name, _ = QFileDialog.getOpenFileName( self, "Open File", "/home", "Images (*.png *.xpm *.jpg);;All files(*.*)" )
        print( f"Your chosen filename is: {file_name}" )

        '''

        '''
        #getOpenFileNames
        file_names, _ = QFileDialog.getOpenFileNames( self, "Open Files", "/home", "Images (*.png *.xpm *.jpg);;All files(*.*)" )
        for f in file_names:
            print( f"File: {f}" )
        '''  


        # getSaveFileName
        file_name, _ = QFileDialog.getSaveFileName( self, "Save File", "/home", "Images (*.png *.xpm *.jpg);;All files(*.*)" )
        print( f"Filename: {file_name}" )