import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QTextEdit, QComboBox, QCheckBox, QSpinBox, QSlider, QMessageBox
from PyQt5.QtCore import Qt


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Aplikasi Pendaftaran Pelanggan')
        self.setGeometry(100, 100, 500, 400)

        # Label dan input untuk nama
        self.label_name = QLabel('Nama:', self)
        self.textbox_name = QLineEdit(self)

        # Label dan combobox untuk jenis kelamin
        self.label_gender = QLabel('Jenis Kelamin:', self)
        self.combobox_gender = QComboBox(self)
        self.combobox_gender.addItem('Pria')
        self.combobox_gender.addItem('Wanita')
        self.combobox_gender.addItem('Lainnya')

        # Label dan textedit untuk alamat
        self.label_address = QLabel('Alamat:', self)
        self.textedit_address = QTextEdit(self)

        # Check box untuk status pengiriman
        self.checkbox_delivery = QCheckBox('Pengiriman Ekspres', self)

        # Spin box untuk jumlah barang
        self.label_quantity = QLabel('Jumlah Barang:', self)
        self.spinbox_quantity = QSpinBox(self)
        self.spinbox_quantity.setMinimum(1)
        self.spinbox_quantity.setMaximum(100)

        # Slider untuk rating
        self.label_rating = QLabel('Rating (1-10):', self)
        self.slider_rating = QSlider(Qt.Horizontal, self)
        self.slider_rating.setMinimum(1)
        self.slider_rating.setMaximum(10)
        self.slider_rating.setTickInterval(1)
        self.slider_rating.setSingleStep(1)

        # Tombol Submit
        self.submit_button = QPushButton('Submit', self)
        self.submit_button.clicked.connect(self.submitForm)

        # Membuat layout vertikal
        vbox = QVBoxLayout()
        vbox.addWidget(self.label_name)
        vbox.addWidget(self.textbox_name)
        vbox.addWidget(self.label_gender)
        vbox.addWidget(self.combobox_gender)
        vbox.addWidget(self.label_address)
        vbox.addWidget(self.textedit_address)
        vbox.addWidget(self.checkbox_delivery)
        vbox.addWidget(self.label_quantity)
        vbox.addWidget(self.spinbox_quantity)
        vbox.addWidget(self.label_rating)
        vbox.addWidget(self.slider_rating)
        vbox.addWidget(self.submit_button)
        vbox.addStretch()

        # Membuat layout horizontal untuk memposisikan vertikal di tengah
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addLayout(vbox)
        hbox.addStretch(1)

        self.setLayout(hbox)
        self.show()

    def submitForm(self):
        nama = self.textbox_name.text()
        jenis_kelamin = self.combobox_gender.currentText()
        alamat = self.textedit_address.toPlainText()
        pengiriman_ekspres = self.checkbox_delivery.isChecked()
        jumlah_barang = self.spinbox_quantity.value()
        rating = self.slider_rating.value()

        # Menampilkan hasil form di konsol (bisa diarahkan ke database atau file)
        print(f'Nama: {nama}')
        print(f'Jenis Kelamin: {jenis_kelamin}')
        print(f'Alamat:\n{alamat}')
        print(f'Pengiriman Ekspres: {pengiriman_ekspres}')
        print(f'Jumlah Barang: {jumlah_barang}')
        print(f'Rating: {rating}')

        # Menampilkan pesan berhasil
        QMessageBox.information(self, 'Info', 'Form berhasil disubmit!')

        # Mengosongkan input setelah submit
        self.textbox_name.clear()
        self.combobox_gender.setCurrentIndex(0)
        self.textedit_address.clear()
        self.checkbox_delivery.setChecked(False)
        self.spinbox_quantity.setValue(1)
        self.slider_rating.setValue(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
