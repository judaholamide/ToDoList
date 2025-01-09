from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QListWidget, QHBoxLayout
from PyQt5.QtGui import QPalette, QColor
import sys

class ToDoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List App")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout()
        self.list_layout = QVBoxLayout()
        self.button_layout = QHBoxLayout()

        self.task_list = QListWidget()
        self.main_layout.addLayout(self.list_layout)
        self.list_layout.addWidget(self.task_list)

        self.add_task_button = QPushButton("Add Task")
        self.delete_task_button = QPushButton("Delete Task")
        self.theme_toggle_button = QPushButton("Toggle Theme")

        self.button_layout.addWidget(self.add_task_button)
        self.button_layout.addWidget(self.delete_task_button)
        self.button_layout.addWidget(self.theme_toggle_button)

        self.main_layout.addLayout(self.button_layout)

        self.central_widget.setLayout(self.main_layout)

        self.add_task_button.clicked.connect(self.add_task)
        self.delete_task_button.clicked.connect(self.delete_task)
        self.theme_toggle_button.clicked.connect(self.toggle_theme)

        self.light_theme = True
        self.apply_light_theme()

    def add_task(self):
        self.task_list.addItem("New Task")

    def delete_task(self):
        selected_items = self.task_list.selectedItems()
        for item in selected_items:
            self.task_list.takeItem(self.task_list.row(item))

    def toggle_theme(self):
        if self.light_theme:
            self.apply_dark_theme()
        else:
            self.apply_light_theme()
        self.light_theme = not self.light_theme

    def apply_light_theme(self):
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#ffffff"))
        palette.setColor(QPalette.WindowText, QColor("#000000"))
        palette.setColor(QPalette.Base, QColor("#f5f5f5"))
        palette.setColor(QPalette.AlternateBase, QColor("#e0e0e0"))
        palette.setColor(QPalette.ToolTipBase, QColor("#ffffff"))
        palette.setColor(QPalette.ToolTipText, QColor("#000000"))
        palette.setColor(QPalette.Text, QColor("#000000"))
        palette.setColor(QPalette.Button, QColor("#f5f5f5"))
        palette.setColor(QPalette.ButtonText, QColor("#000000"))
        palette.setColor(QPalette.Highlight, QColor("#4caf50"))
        palette.setColor(QPalette.HighlightedText, QColor("#ffffff"))
        QApplication.setPalette(palette)

    def apply_dark_theme(self):
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#121212"))
        palette.setColor(QPalette.WindowText, QColor("#ffffff"))
        palette.setColor(QPalette.Base, QColor("#333333"))
        palette.setColor(QPalette.AlternateBase, QColor("#3c3c3c"))
        palette.setColor(QPalette.ToolTipBase, QColor("#ffffff"))
        palette.setColor(QPalette.ToolTipText, QColor("#ffffff"))
        palette.setColor(QPalette.Text, QColor("#ffffff"))
        palette.setColor(QPalette.Button, QColor("#3c3c3c"))
        palette.setColor(QPalette.ButtonText, QColor("#ffffff"))
        palette.setColor(QPalette.Highlight, QColor("#6200ea"))
        palette.setColor(QPalette.HighlightedText, QColor("#ffffff"))
        QApplication.setPalette(palette)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    todo_app = ToDoApp()
    todo_app.show()
    sys.exit(app.exec_())
