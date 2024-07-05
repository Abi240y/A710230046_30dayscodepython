import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget


class ScheduleApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Jadwal')

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(2)

        self.tableWidget.setHorizontalHeaderLabels(['Hari', 'Kegiatan'])

        self.setCentralWidget(self.tableWidget)

        self.populateData()

    def populateData(self):
        schedule = {
            0: ('Senin', 'manajemen pendidikan'),
            1: ('Selasa', 'praktikum'),
            2: ('Rabu', 'Struktur data, logika, PBO'),
            3: ('Kamis', 'Istirahat'),
            4: ('Jumat', 'AOK, kurikulum pendidikan')
        }

        for day, (day_name, activity) in schedule.items():
            item_day = QTableWidgetItem(day_name)
            item_activity = QTableWidgetItem(activity)

            self.tableWidget.setItem(day, 0, item_day)
            self.tableWidget.setItem(day, 1, item_activity)

        self.tableWidget.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    schedule_app = ScheduleApp()
    schedule_app.show()
    sys.exit(app.exec_())
