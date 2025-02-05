from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QWidget,  QLabel, QHBoxLayout, QVBoxLayout, QPushButton
from pathlib import Path

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLabel Image Demo")

        img_path = Path( '~/GitHubCode/Qt_PySide6/3.ATourOfQtWidgets/7.QLabel_images/images').expanduser() / 'minions.png'
        print( img_path )
        image_label = QLabel()
        # pixmap = QPixmap( str( img_path) )
        # image_label.setPixmap(QPixmap(str( img_path ) ) )
        image_label.setPixmap(QIcon(str( img_path ) ).pixmap( image_label.size() ) )
        image_label.setPixmap( QPixmap( "images/minionis.png" ))

        button = QPushButton()
        img_path2 = Path( '~/GitHubCode/Qt_PySide6/3.ATourOfQtWidgets/7.QLabel_images/images').expanduser() / 'ButtonTest.png'
        print( img_path2 )
        
        # button.setIcon( QPixmap( str( img_path2 ) ) )
        # button.setIcon( QIcon( str( img_path2 ) ).pixmap( 16, 16 ) )
        button.setIcon( QPixmap( 'images/ButtonTest.png' ) ) 
        button.clicked.connect( self.do_something )

        layout = QVBoxLayout()
        layout.addWidget(image_label)
        layout.addWidget( button )


        self.setLayout(layout)

    def do_something( self ):
        print( f"doing something" )