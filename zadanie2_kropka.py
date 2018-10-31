from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QGridLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
from math import sqrt


class Kalkulator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.interfejs()

    def interfejs(self):

        etykieta1 = QLabel("Liczba 1:", self)
        etykieta2 = QLabel("Liczba 2:", self)
        etykieta3 = QLabel("Wynik:", self)

        ukladT = QGridLayout()
        ukladT.addWidget(etykieta1, 0, 0)
        ukladT.addWidget(etykieta2, 0, 1)
        ukladT.addWidget(etykieta3, 0, 2)

        self.liczba1Edt = QLineEdit()
        self.liczba2Edt = QLineEdit()
        self.wynikEdt = QLineEdit()

        self.wynikEdt.readonly = True
        self.wynikEdt.setToolTip('Wpisz <b>liczby</b> i wybierz działanie...')

        ukladT.addWidget(self.liczba1Edt, 1, 0)
        ukladT.addWidget(self.liczba2Edt, 1, 1)
        ukladT.addWidget(self.wynikEdt, 1, 2)

        dodajBtn = QPushButton("&Dodaj", self)
        odejmijBtn = QPushButton("&Odejmij", self)
        dzielBtn = QPushButton("&Mnóż", self)
        mnozBtn = QPushButton("D&ziel", self)
        kwadBtn = QPushButton("D&o Kwadratu", self)
        pierwBtn = QPushButton("&Pierwiastkuj", self)
        odwBtn = QPushButton("O&dwróć")
        procBtn = QPushButton("&Procent")
        koniecBtn = QPushButton("&Koniec", self)
        koniecBtn.resize(koniecBtn.sizeHint())

        ukladH = QHBoxLayout()
        ukladH.addWidget(dodajBtn)
        ukladH.addWidget(odejmijBtn)
        ukladH.addWidget(dzielBtn)
        ukladH.addWidget(mnozBtn)

        ukladD = QHBoxLayout()
        ukladD.addWidget(kwadBtn)
        ukladD.addWidget(pierwBtn)
        ukladD.addWidget(odwBtn)
        ukladD.addWidget(procBtn)

        ukladT.addLayout(ukladH, 2, 0, 1, 3)
        ukladT.addLayout(ukladD, 3, 0, 1, 3)
        ukladT.addWidget(koniecBtn, 4, 0, 1, 3)

        self.setLayout(ukladT)

        koniecBtn.clicked.connect(self.koniec)
        dodajBtn.clicked.connect(self.dzialanie)
        odejmijBtn.clicked.connect(self.dzialanie)
        mnozBtn.clicked.connect(self.dzialanie)
        dzielBtn.clicked.connect(self.dzialanie)
        kwadBtn.clicked.connect(self.dzialanie)
        pierwBtn.clicked.connect(self.dzialanie)
        odwBtn.clicked.connect(self.dzialanie)
        procBtn.clicked.connect(self.dzialanie)

        self.liczba1Edt.setFocus()
        self.setGeometry(20, 20, 300, 100)
        self.setWindowIcon(QIcon('kalkulator.png'))
        self.setWindowTitle("Prosty kalkulator")
        self.show()

    def koniec(self):
        self.close()

    def closeEvent(self, event):

        odp = QMessageBox.question(
            self, 'Komunikat',
            "Czy na pewno koniec?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if odp == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def dzialanie(self):

        nadawca = self.sender()

        try:
            liczba1 = float(self.liczba1Edt.text())
            liczba2 = self.liczba2Edt.text()
            wynik = ""

            if nadawca.text() == "&Dodaj":
                wynik = liczba1 + float(liczba2)
            elif nadawca.text() == "&Odejmij":
                wynik = liczba1 - float(liczba2)
            elif nadawca.text() == "&Mnóż":
                wynik = liczba1 * float(liczba2)
            elif nadawca.text() == "D&ziel":
                try:
                    wynik = round(liczba1 / float(liczba2), 9)
                except ZeroDivisionError:
                    QMessageBox.critical(
                        self, "Błąd", "Nie można dzielić przez zero!")
                    return
            elif nadawca.text() == "D&o Kwadratu":
                wynik = liczba1 * liczba1
            elif nadawca.text() == "&Pierwiastkuj":
                try:
                    if liczba1 < 0:
                        raise ValueError
                    wynik = round(sqrt(liczba1),9)
                except ValueError:
                    QMessageBox.critical(
                        self, "Błąd", "Nie można obliczyć pierwiastka z liczby ujemnej!")
                    return
            elif nadawca.text() == "O&dwróć":
                try:
                    wynik = round(1/liczba1, 9)
                except ZeroDivisionError:
                    QMessageBox.critical(
                        self, "Błąd", "Nie można dzielić przez zero!")
                    return
            elif nadawca.text() == "&Procent":
                wynik = liczba1 * (float(liczba2)/100)


            self.wynikEdt.setText(str(wynik))

        except ValueError:
            QMessageBox.warning(self, "Błąd", "Błędne dane", QMessageBox.Ok)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = Kalkulator()
    sys.exit(app.exec_())