from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QWidget, QListWidget
from PyQt5.QtCore import Qt

class ToDoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List")
        self.setGeometry(100, 100, 600, 400)
        self.setup_ui()

    def setup_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        self.task_list = QListWidget()
        layout.addWidget(self.task_list)

        self.add_task_btn = QPushButton("Add Task")
        self.add_task_btn.clicked.connect(self.add_task)
        layout.addWidget(self.add_task_btn)

        self.delete_task_btn = QPushButton("Delete Task")
        self.delete_task_btn.clicked.connect(self.delete_task)
        layout.addWidget(self.delete_task_btn)

        self.central_widget.setLayout(layout)

    def add_task(self):
        pass

    def delete_task(self):
        pass
