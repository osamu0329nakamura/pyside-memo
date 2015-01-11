from PySide.QtCore import (Qt,)
from PySide.QtGui import (QAbstractTableModel,)


class TableModel(QAbstractTableModel):

    def __init__(self, parent=None):
        super(TableModel, self).__init__(parent)

    def rowCount(self, index):
        return self._data

    def columnCount(self, index):
        return 2

    def data(self, index, role):
        if role == Qt.DisplayRole:
            col = index.column()

            data = self._data[index.row()]

            return ""

