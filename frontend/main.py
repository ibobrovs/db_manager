from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class DatabaseManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DB Manager")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        self.btn_connect = QPushButton("Подключиться к MySQL")
        self.btn_import_excel = QPushButton("Импортировать Excel")

        layout.addWidget(self.btn_connect)
        layout.addWidget(self.btn_import_excel)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

app = QApplication([])
window = DatabaseManager()
window.show()
app.exec()
