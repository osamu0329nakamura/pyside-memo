from PySide.QtGui import *
from PySide.QtCore import *

import sys

app = QApplication(sys.argv)

Item = QTreeWidgetItem
order = Item(['order', 'hoge'])
series = Item(order, ['series', ''])
country = Item(series, ['country', 96])
market = Item(series, ['market', 96])
user = Item(order, ['user', ''])
member = Item(user, ['member', ''])
sign = Item(user, ['sign', ''])
side = Item(order, ['side', "Bid"])
premium = Item(order, ['premium', 100])

tree = QTreeWidget()
tree.addTopLevelItem(order)
tree.setColumnCount(2)
tree.show()

model = tree.model()
print(model.columnCount())
user_index = model.index(1, 0, model.index(0, 0))
sign_index = model.index(1, 0, user_index)
print(model.parent(sign_index))
print(user_index)

app.exec_()

"""
class TreeModel(QAbstractItemModel):

    def __init__(self, parent=None):
        super(TreeModel, self).__init__(parent)

    def data(self, index, role):
        pass

    def rowCount(self, index):
        pass
 """
