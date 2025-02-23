import sys
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice

loader = QUiLoader() #Set up a loader object

app = QtWidgets.QApplication(sys.argv)
# ui_file_name = "/home/softspoke/GitHubCode/Qt_PySide6/4.QtDesigner/4.QDesigner_QUiLoader/widget.ui"
ui_file_name = "4.QtDesigner/4.QDesigner_QUiLoader/widget.ui"
ui_file = QFile( ui_file_name )
res = ui_file.open( QIODevice.ReadOnly )
print( f"file open result: {res}" )
# window = loader.load("widget.ui", None) #Load the ui - happens at run time!
window = loader.load(ui_file, None)
ui_file.close()

if not window:
    print( loader.errorString() )
    sys.exit( -1 )

def do_something() :
    print(window.full_name_line_edit.text(),"is a ", window.occupation_line_edit.text())

#Changing the properties in the form
window.setWindowTitle("User data")

#Accessing widgets in the form
window.submit_button.clicked.connect(do_something)
window.show()

sys.exit( app.exec() )