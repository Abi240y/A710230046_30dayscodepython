import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QLabel, QFileDialog, QMessageBox

class NotesApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Aplikasi Catatan PyQt5')
        
        self.label = QLabel('Catatan:', self)
        self.text_edit = QTextEdit(self)
        self.button_save = QPushButton('Simpan', self)
        self.button_load = QPushButton('Muat', self)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.text_edit)
        
        hbox = QHBoxLayout()
        hbox.addWidget(self.button_save)
        hbox.addWidget(self.button_load)
        
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        
        self.button_save.clicked.connect(self.save_notes)
        self.button_load.clicked.connect(self.load_notes)
        
        self.show()

    def save_notes(self):
        filename, _ = QFileDialog.getSaveFileName(self, 'Simpan Catatan', '', 'Text Files (*.txt);;All Files (*)')
        if filename:
            try:
                with open(filename, 'w') as f:
                    f.write(self.text_edit.toPlainText())
                QMessageBox.information(self, 'Informasi', 'Catatan berhasil disimpan.')
            except Exception as e:
                QMessageBox.warning(self, 'Peringatan', f'Gagal menyimpan catatan:\n{str(e)}')

    def load_notes(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Muat Catatan', '', 'Text Files (*.txt);;All Files (*)')
        if filename:
            try:
                with open(filename, 'r') as f:
                    self.text_edit.setPlainText(f.read())
                QMessageBox.information(self, 'Informasi', 'Catatan berhasil dimuat.')
            except Exception as e:
                QMessageBox.warning(self, 'Peringatan', f'Gagal memuat catatan:\n{str(e)}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NotesApp()
    sys.exit(app.exec_())
