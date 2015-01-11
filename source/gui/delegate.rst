QStyledItemDelegate -- QTableView のセルの表示をカスタマイズする
#################################################################

QStyledItemDelegate のサブクラスを作成する。

以下は、int 値を エポック秒とみなして表示するカスタムデリゲートの例

.. code-block:: python

   from PySide.QtGui import QStyledItemDelegate
   from datetime import datetime
   
   class DateTimeItemDelegate(QStyledItemDelegate):
       def __init__(self, format, parent=None):
           u"""int値 を format 文字列でフォーマットし表示する。
           """
           super(DateTimeItemDelegate, self).__init__(parent)
           self.format = format
   
       def displayText(self, value, locale):
           if isinstance(value, int):
               if value > 0:
                   return datetime.fromtimestamp(value).strftime(self.format)
               else:
                   return ""
           else:
               return str(value)
