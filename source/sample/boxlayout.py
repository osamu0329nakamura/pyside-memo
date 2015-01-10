from PySide.QtGui import *
from PySide.QtCore import *

def main():
    import sys

    app = QApplication(sys.argv)

    # GUI オブジェクトの生成
    widget = QWidget()

    hbox = QHBoxLayout(widget)

    hbox.setContentsMargins(0, 0, 0, 0)
    hbox.setSpacing(1)
    hbox.addWidget(QPushButton("left"))
    hbox.addStretch(1)
    hbox.addWidget(QPushButton("center"))
    hbox.addStretch(2)
    hbox.addWidget(QPushButton("right"))

    widget.show()

    # メイン イベントループを開始する
    app.exec_()

if __name__ == '__main__':
    main()

