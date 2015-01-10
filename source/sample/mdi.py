from PySide.QtGui import *
from PySide.QtCore import *


def main():
    def on_open():
        print("open")
        widget = QMainWindow()
        pane = QWidget()
        widget.setCentralWidget(pane)

        file = widget.menuBar().addMenu("&File")
        file.addAction("hoge")
        layout = QHBoxLayout(pane)
        layout.addWidget(QPushButton("OK"))

        subwindow = mdi.addSubWindow(widget)
        subwindow.show()

    import sys
    app = QApplication(sys.argv)

    window = QMainWindow()

    mdi = QMdiArea()
    window.setCentralWidget(mdi)

    menubar = window.menuBar()
    filemenu = menubar.addMenu("&File")
    open = filemenu.addAction("&Open")
    open.triggered.connect(on_open)
    window.show()
    app.exec_()

main()
