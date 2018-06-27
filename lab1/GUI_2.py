import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QFormLayout


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(QFormLayout())
        label = QLabel('kek')
        self.layout().addWidget(label)
        self.resize(500, 500)
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = Widget()

    sys.exit(app.exec_())
