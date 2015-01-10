from PySide.QtGui import *
from PySide.QtCore import *

def main():
    import sys

    app = QApplication(sys.argv)

    window = QMainWindow()

    # メニューの追加
    #   1. メニューバーを取得する
    menubar = window.menuBar()

    #   2. File メニューを追加する
    filemenu = menubar.addMenu("&File")

    #   3. File メニューに、Exit メニュー項目を追加する
    exit_action = filemenu.addAction("&Exit")

    #   4. メニュー項目の動作を指定する
    exit_action.triggered.connect(app.quit)

    window.show()

    # メイン イベントループを開始する
    app.exec_()

if __name__ == '__main__':
    main()


