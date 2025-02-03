from PySide6.QtWidgets import QMainWindow, QPushButton 


# subclass QMainWindow to customize your application's main windows
class ButtonHolder(QMainWindow):
    def __init__ (self):
        super().__init__() # call parent contructor
        self.setWindowTitle("Button Holder App")
        button = QPushButton("Press Me!")

        #Set up the button as our central widget
        self.setCentralWidget(button)