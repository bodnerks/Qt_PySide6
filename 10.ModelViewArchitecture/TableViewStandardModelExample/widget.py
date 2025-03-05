from PySide6.QtCore import Qt, QModelIndex
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QStandardItemModel, QStandardItem
from ui_widget import Ui_Widget

class Widget( QWidget, Ui_Widget ):
    def __init__( self ):
        super().__init__()
        self.setupUi( self )
        self.setWindowTitle( "QTableView - QStandardItemModel" )

        # set up model
        self.model = QStandardItemModel( 4, 4 )
        for row in range( self.model.rowCount() ):
            for column in range( self.model.columnCount() ):
                item = QStandardItem( f"row: {row}, column: {column}" )
                self.model.setItem( row, column, item )

        # set model to view
        self.tableView.setModel( self.model )

        # connect signal to slot
        self.read_data_button.clicked.connect( self.read_data )

    def read_data( self ):
        for row in range( self.model.rowCount() ):
            for column in range( self.model.columnCount() ):
                index = self.model.index( row, column, QModelIndex() )
                # data = index.data( Qt.DisplayRole ) # call data method on index
                data = self.model.data( index, Qt.DisplayRole ) # or call data method on model
                print( data )
        