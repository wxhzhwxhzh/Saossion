import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl  # 导入 QUrl

class WebEngineWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Web Engine Example")
        self.setGeometry(100, 100, 800, 600)

        # 创建一个垂直布局
        layout = QVBoxLayout()

        # 创建一个 QWebEngineView
        webview = QWebEngineView()

        # 加载网页，需要将字符串转换为 QUrl 对象
        webview.setUrl(QUrl("https://www.drissionpage.cn"))

        # 将 QWebEngineView 添加到布局中
        layout.addWidget(webview)

        # 创建一个QWidget作为主窗口的中央部件
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

def main():
    app = QApplication(sys.argv)
    window = WebEngineWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
