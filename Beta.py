import sys
import os
from PyQt5.QtCore import QUrl, Qt, QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget, QHBoxLayout, QPushButton, QProgressBar
from PyQt5.QtGui import QIcon, QFont, QPalette, QColor
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.Window | Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint | Qt.WindowCloseButtonHint)
        self.setAttribute(Qt.WA_StyledBackground, True)

        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.layout = QVBoxLayout(self.main_widget)

        self.default_background_color = QColor("#202020")
        palette = self.main_widget.palette()
        palette.setColor(QPalette.Window, self.default_background_color)
        self.main_widget.setPalette(palette)
        self.main_widget.setAutoFillBackground(True)

        self.web_view = QWebEngineView()
        self.layout.addWidget(self.web_view)

        self.url_bar_layout = QHBoxLayout()
        self.layout.addLayout(self.url_bar_layout)

        self.back_button = QPushButton()
        self.back_button.setFixedSize(32, 32)
        self.back_button.setFont(QFont("Segoe MDL2 Assets", 16))
        self.back_button.setText("")
        self.back_button.clicked.connect(self.web_view.back)
        self.url_bar_layout.addWidget(self.back_button)

        self.forward_button = QPushButton()
        self.forward_button.setFixedSize(32, 32)
        self.forward_button.setFont(QFont("Segoe MDL2 Assets", 16))
        self.forward_button.setText("")
        self.forward_button.clicked.connect(self.web_view.forward)
        self.url_bar_layout.addWidget(self.forward_button)

        self.refresh_button = QPushButton()
        self.refresh_button.setFixedSize(32, 32)
        self.refresh_button.setFont(QFont("Segoe MDL2 Assets", 16))
        self.refresh_button.setText("")
        self.refresh_button.clicked.connect(self.web_view.reload)
        self.url_bar_layout.addWidget(self.refresh_button)

        self.url_text_box = QLineEdit()
        self.url_text_box.setPlaceholderText("Enter URL")
        self.url_text_box.setFixedHeight(32)
        self.url_text_box.setFont(QFont("Arial", 14))
        self.url_text_box.returnPressed.connect(self.load_url)
        self.url_bar_layout.addWidget(self.url_text_box)

        self.progress_bar = QProgressBar()
        self.progress_bar.setFixedHeight(8)
        self.progress_bar.setValue(0)
        self.progress_bar.setVisible(False)
        self.layout.addWidget(self.progress_bar)

        self.setWindowTitle("NuggyNet (UI Refresh Beta)")
        self.setMinimumSize(320, 240)

        icon_path = os.path.join(os.path.dirname(__file__), "icon.ico")
        self.setWindowIcon(QIcon(icon_path))

        self.web_view.setUrl(QUrl("https://awethebird.neocities.org/nuggethome"))

        self.web_view.loadStarted.connect(self.on_load_started)
        self.web_view.loadProgress.connect(self.on_load_progress)
        self.web_view.loadFinished.connect(self.on_load_finished)
        self.web_view.urlChanged.connect(self.update_background_and_title)

        self.is_resizing = False
        self.resize_start_pos = None
        self.setMouseTracking(True)

    def load_url(self):
        url = self.url_text_box.text()
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "https://www." + url
        self.web_view.setUrl(QUrl(url))

    def on_load_started(self):
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)

    def on_load_progress(self, progress):
        self.progress_bar.setValue(progress)

    def on_load_finished(self):
        self.progress_bar.setVisible(False)
        self.update_background_and_title()

    def update_background_and_title(self):

        title = self.web_view.page().title()
        if title:
            self.setWindowTitle(f"{title} - NuggyNet (UI Refresh Beta)")
        else:
            self.setWindowTitle("NuggyNet (UI Refresh Beta)")

        self.web_view.page().runJavaScript(
            "getComputedStyle(document.body).backgroundColor;",
            self.set_background_color
        )

    def set_background_color(self, color):
        
        if color and color != "rgba(0, 0, 0, 0)":
            rgb_values = color[4:-1].split(',')
            new_color = QColor(int(rgb_values[0]), int(rgb_values[1]), int(rgb_values[2]))
            palette = self.main_widget.palette()
            palette.setColor(QPalette.Window, new_color)
            self.main_widget.setPalette(palette)
        else:
            
            palette = self.main_widget.palette()
            palette.setColor(QPalette.Window, self.default_background_color)
            self.main_widget.setPalette(palette)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.is_resizing = True
            self.resize_start_pos = event.globalPos()
            self.window_start_size = self.size()

    def mouseMoveEvent(self, event):
        if self.is_resizing and self.resize_start_pos:
            delta = event.globalPos() - self.resize_start_pos
            new_size = self.window_start_size + QSize(delta.x(), delta.y())
            self.resize(new_size)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.is_resizing = False
            self.resize_start_pos = None

app = QApplication(sys.argv)
window = Browser()
window.show()
sys.exit(app.exec_())
