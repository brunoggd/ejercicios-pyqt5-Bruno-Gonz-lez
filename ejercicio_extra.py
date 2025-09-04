import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt,QDate

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Validación Fecha de nacimiento")
        self.setGeometry(100, 100, 400, 300)
        layout = QGridLayout()
        self.setLayout(layout)

        label_1=QLabel("Fecha de nacimiento:")
        label_1.setAlignment(Qt.AlignLeft)
        label_1.setWordWrap(True)
        layout.addWidget(label_1,1,0)

        self.fecha_seleccionada=QDateEdit()
        self.fecha_seleccionada.setCalendarPopup(True)
        layout.addWidget(self.fecha_seleccionada,1,1)

        boton_registrarse=QPushButton("Registrarse")
        boton_registrarse.clicked.connect(self.registrar)
        layout.addWidget(boton_registrarse,2,0)

    def registrar(self):
        fecha_nacimiento=self.fecha_seleccionada.date()
        fecha_actual=QDate.currentDate()
        edad=fecha_nacimiento.daysTo(fecha_actual) // 365
        if fecha_nacimiento > fecha_actual:
            QMessageBox.warning(self,"Fecha Invalida","La fecha ingresada es posterior a la actual")
            return        
        if edad < 13:
            QMessageBox.warning(self,"Edad No Suficiente","Tienes menos de 13 años")
        else:
            QMessageBox.information(self,"Registro Correcto","Validación Exitosa")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())