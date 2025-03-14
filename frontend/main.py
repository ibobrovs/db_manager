import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTextEdit, QLabel

class DBManagerApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("DB Manager")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        self.label = QLabel("Выберите действие")
        layout.addWidget(self.label)

        self.query_input = QTextEdit()
        layout.addWidget(self.query_input)

        self.run_query_btn = QPushButton("Выполнить SQL-запрос")
        layout.addWidget(self.run_query_btn)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DBManagerApp()
    window.show()
    sys.exit(app.exec())
