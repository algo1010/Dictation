from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Viewer")

        label = QLabel(self)
        pixmap = QPixmap("../images/mb.jpeg")  # Thay đường dẫn bằng đường dẫn thực tế của hình ảnh
        label.setPixmap(pixmap)
        label.resize(pixmap.width(), pixmap.height())


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
