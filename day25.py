import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Kalkulator Sederhana')
        self.setGeometry(100, 100, 300, 300)
        
        self.expression_line = QLineEdit(self)
        self.expression_line.setPlaceholderText('Masukkan ekspresi matematika')
        self.expression_line.setReadOnly(True)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.expression_line)
        
        grid_layout = QHBoxLayout()
        
        buttons = [
            ('7', self.on_button_click), ('8', self.on_button_click), ('9', self.on_button_click), ('/', self.on_button_click),
            ('4', self.on_button_click), ('5', self.on_button_click), ('6', self.on_button_click), ('*', self.on_button_click),
            ('1', self.on_button_click), ('2', self.on_button_click), ('3', self.on_button_click), ('-', self.on_button_click),
            ('0', self.on_button_click), ('.', self.on_button_click), ('=', self.on_equal_click), ('+', self.on_button_click),
            ('Clear', self.on_clear_click)
        ]
        
        for text, slot in buttons:
            button = QPushButton(text)
            button.clicked.connect(slot)
            grid_layout.addWidget(button)
        
        vbox.addLayout(grid_layout)
        self.setLayout(vbox)
    
    def on_button_click(self):
        button = self.sender()
        current_text = self.expression_line.text()
        new_text = current_text + button.text()
        self.expression_line.setText(new_text)
    
    def on_equal_click(self):
        try:
            result = eval(self.expression_line.text())
            self.expression_line.setText(str(result))
        except Exception as e:
            self.expression_line.setText('Error')
    
    def on_clear_click(self):
        self.expression_line.clear()

def main():
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
