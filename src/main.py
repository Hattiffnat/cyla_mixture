
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtWidgets import QPushButton, QPlainTextEdit, QApplication, QShortcut
from PyQt5.QtGui import QKeySequence


class App(QApplication):
    def __init__(self, argv):
        super().__init__(argv)

        self.cy_alphabet = 'аеёорсухАВЕЁЗКМНОРСТХ'
        self.la_alphabet = 'aeeopcyxABEE3KMHOPCTX'

        self.main_window = uic.loadUi("design.ui")

        self.btn_make_mix = self.main_window.findChild(QPushButton, 'pushButton_gen_translite')
        self.btn_make_mix.clicked.connect(self._make_mix)

        self.shortcut_make_mix = QShortcut(self.btn_make_mix)
        self.shortcut_make_mix.setKey(QKeySequence('Ctrl+Enter'))

        self.text_form_input = self.main_window.findChild(QPlainTextEdit, 'plainTextEdit_input')

        self.text_form_output = self.main_window.findChild(QPlainTextEdit, 'plainTextEdit_output')

    def _make_mix(self):
        text = self.text_form_input.toPlainText()
        text = self._mixture_generating(text)

        self.text_form_output.clear()
        self.text_form_output.appendPlainText(text)
        self.text_form_output.selectAll()

    def _mixture_generating(self, text):
        res = text
        for i, cy_let in enumerate(self.cy_alphabet):
            res = res.replace(cy_let, self.la_alphabet[i])
        return res


if __name__ == "__main__":

    app = App([])

    app.main_window.show()
    app.exec_()
