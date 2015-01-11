QMainWindow -- メインウィンドウ
###############################

メニューの作成
--------------

.. code-block:: python

   # self: QMainWindow 

   menubar = self.menuBar()                     # menubar     : QMenuBar
   filemenu = menubar.addMenu("&File")          # filemenu    : QMenu
   open_action = filemenu.addAction("&Open")    # open_action : QAction

   def on_open():
       print("open")

   open_action.triggered.connect(on_open)
