from PySide.QtGui import *
from PySide.QtCore import *

def main():
    import sys

    app = QApplication(sys.argv)

    # GUI オブジェクトの生成
    widget = QPushButton("OK")
    widget.show()

    # ボタンを押下した際に、アプリケーションを終了する
    widget.clicked.connect(app.quit)

    # メイン イベントループを開始する
    app.exec_()

if __name__ == '__main__':
    main()

