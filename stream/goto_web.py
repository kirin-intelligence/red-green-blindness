import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView

import os
cwd = os.getcwd()


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('My Browser')
        self.showMaximized()
        self.webview = QWebEngineView()
        print(cwd+os.sep+"index.html")
        self.webview.load(QUrl.fromLocalFile(cwd+os.sep+"index.html"))
        self.setCentralWidget(self.webview)

if __name__ == "__main__":
    # app = QApplication(sys.argv)
    # w = MainWindow()
    # w.show()
    # sys.exit(app.exec_())
    import qtmodern.styles
    import qtmodern.windows


    app = QApplication(sys.argv)
    win = MainWindow()
    mw = qtmodern.windows.ModernWindow(win)
    mw.show()
    sys.exit(app.exec_())