import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Double Click Example")
        self.resize(400, 300)

        # Tạo QTableWidget
        self.table_widget = QTableWidget()
        self.table_widget.setRowCount(5)
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(["Column 1", "Column 2", "Column 3"])

        # Đặt các giá trị vào bảng
        for row in range(5):
            for col in range(3):
                item = QTableWidgetItem(f"Row {row}, Col {col}")
                self.table_widget.setItem(row, col, item)

        # Kết nối sự kiện double click
        self.table_widget.cellDoubleClicked.connect(self.on_double_click)

        self.setCentralWidget(self.table_widget)

    def on_double_click(self, row, col):
        print(f"Double clicked on row {row} and column {col}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
