from PySide.QtGui import *
from PySide.QtCore import *

def main():
    import sys

    app = QApplication(sys.argv)

    window = QMainWindow()

    # メニューの追加
    #   メニューバーを取得する
    menubar = window.menuBar()

    # File メニューを追加する
    filemenu = menubar.addMenu("&File")

    # File メニューに、Exit メニュー項目を追加する

    exit_action = filemenu.addAction("&Exit")
    exit_action.triggered.connect(app.quit)

    window.show()

    # メイン イベントループを開始する
    app.exec_()

if __name__ == '__main__':
    main()

