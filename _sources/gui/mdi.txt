MDI
#############


`QMdiArea` を `QMainWindow` に追加する。

`QMdiArea.addSubWindow(widget)` で `QMdiSubWindow` を作成する。

.. code-block:: python

   mdi_area = QMdiArea()
   self.setCentralWidget(mdi_area)

   subwindow = mdi_area.addSubWindow(widget)
   subwindow.show()
