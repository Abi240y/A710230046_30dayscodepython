import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Aplikasi Input dan Tombol')
        self.setGeometry(100, 100, 300, 200)

        # Label dan Input Teks
        self.label = QLabel('Masukkan Nama Anda:', self)
        self.inputText = QLineEdit(self)

        # Tombol untuk menampilkan pesan
        self.button = QPushButton('Klik Saya!', self)
        self.button.clicked.connect(self.show_message)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.inputText)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def show_message(self):
        nama = self.inputText.text()
        if nama:
            QMessageBox.information(self, 'Informasi', f'Halo, {nama}!')
        else:
            QMessageBox.warning(self, 'Peringatan', 'Masukkan nama Anda terlebih dahulu.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
