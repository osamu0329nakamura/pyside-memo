Qt アプリケーションの作成
##########################

QApplication
===============

Qt アプリケーションを作成するには、まず `QApplication` のインスタンスを作成し、
GUI 部品を初期化してから、 QApplication.exec_() を呼び出します。

.. literalinclude:: sample/app0.py
   :linenos:

Qt アプリケーションの終了
--------------------------

OK ボタンを押下した際にアプリケーションを終了するように修正します。

.. code-block:: python

    # ボタンを押下した際に、アプリケーションを終了する
    widget.clicked.connect(app.quit)

上記のコードでは、Qt のシグナルとスロットを使用しています。


シグナル と スロット
------------------------

QPushButton には clicked シグナルが定義されています。
（正確には QPushButton の親クラスの QAbstractButton に clicked シグナルが定義されています）

このシグナルを、QApplication の quit スロットに接続することで、
QPushButton が押下されたときに、QApplication の quit スロットが起動し、
アプリケーションが終了します。


Qt のオブジェクトは、イベント発生時にトリガされる「シグナル」と、
トリガされたシグナルを受信して処理を行う「スロット」を持ちます。
シグナルとスロットは、それぞれ引数を持ち、同じ引数をもつシグナルとスロットを接続することができます。

オブジェクトがどのようなシグナルとスロットを持つかどうかはドキュメントに記載されています。

シグナル signal とスロット slot を接続するには、

``sender.signal.connect(receiver.slot)`` のように記載します。

メインウィンドウの作成
=======================

次は、メニューをもつウィンドウを表示してみましょう。

メニューの追加
--------------

.. literalinclude:: sample/menu.py
   :linenos:


メニューを持つウィンドウを作成するには、QMainWindow を使用します。

::

   window = QMainWindow()

メニューを追加するには、 

   1. QMainWindow.menuBar() を呼び出し、QMenuBar のインスタンスを取得する
   2. QMenuBar.addMenu(string) を呼び出し、メニューを追加する。
   3. 追加したメニューの QMenu.addAction(string) を呼び出し、メニュー項目を追加する。
   4. QAction オブジェクトのシグナルを接続し、メニュー押下時の動作を指定する。


QApplication の取得
====================

QCoreApplication.instance() を呼び出すと、アプリケーションのインスタンスを取得できます。


アプリケーションの終了
======================

QCoreApplication.quit() スロットを呼び出すことで、アプリケーションを終了できます。


アプリケーションの補足
=======================

QCoreApplication.aboutToQuit シグナルを補足することで、アプリケーション終了時の
処理を記述することができます。

