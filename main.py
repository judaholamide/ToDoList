from PyQt5.QtWidgets import QApplication
from ui import ToDoApp  # Import the main UI class

import sys
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec_())
