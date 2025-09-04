import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt,QDate
from PyQt5.QtGui import QFont

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Compra de Pasaje Aéreo")
        self.setGeometry(100, 100, 500, 350)
        layout = QGridLayout()
        self.setLayout(layout)
        self.setStyleSheet("background-color: #CAE3EB;")

        label_1=QLabel("Formulario de Compra")
        label_1.setAlignment(Qt.AlignHCenter)
        label_1.setFont(QFont("Comic Sans", 30, QFont.Bold))
        label_1.setStyleSheet("color: #000000")
        label_1.setFont(QFont("Times New Roman", 15, QFont.Bold))
        label_1.setWordWrap(True)
        layout.addWidget(label_1,0,0,1,3)

        label_2=QLabel("Nombre:")
        layout.addWidget(label_2,1,0)
        label_2.setAlignment(Qt.AlignLeft)
        label_2.setStyleSheet("color: #000000")
        label_2.setFont(QFont("Times New Roman", 15, QFont.Bold))

        self.label_nombre=QLineEdit()
        layout.addWidget(self.label_nombre,1,1,1,1)
        
        label_3=QLabel("Apellido:")
        layout.addWidget(label_3,2,0)
        label_3.setAlignment(Qt.AlignLeft)
        label_3.setStyleSheet("color: #000000")
        label_3.setFont(QFont("Times New Roman", 15, QFont.Bold))

        self.label_apellido=QLineEdit()
        layout.addWidget(self.label_apellido,2,1,1,1)

        label_4=QLabel("DNI:")
        layout.addWidget(label_4, 3, 0)
        label_4.setAlignment(Qt.AlignLeft)
        label_4.setStyleSheet("color: #000000")
        label_4.setFont(QFont("Times New Roman", 15, QFont.Bold))

        self.dni = QLineEdit()
        layout.addWidget(self.dni, 3,1,1,1)

        label_5=QLabel("Origen:")
        layout.addWidget(label_5,4,0)
        label_5.setAlignment(Qt.AlignLeft)
        label_5.setStyleSheet("color: #000000")
        label_5.setFont(QFont("Times New Roman", 15, QFont.Bold))

        origenes=QComboBox()
        origenes.addItem("Buenos Aires")
        origenes.addItem("Barcelona")
        origenes.addItem("Bariloche")
        layout.addWidget(origenes,4,1,1,1)

        label_6=QLabel("Destino:")
        layout.addWidget(label_6,5,0)
        label_6.setAlignment(Qt.AlignLeft)
        label_6.setStyleSheet("color: #000000")
        label_6.setFont(QFont("Times New Roman", 15, QFont.Bold))

        destinos=QComboBox()
        destinos.addItem("Manchester")
        destinos.addItem("Londres")
        destinos.addItem("Rosario")
        layout.addWidget(destinos,5,1,1,1)

        label_7=QLabel("Fecha de vuelo:")
        layout.addWidget(label_7,6,0)
        label_7.setAlignment(Qt.AlignLeft)
        label_7.setStyleSheet("color: #000000")
        label_7.setFont(QFont("Times New Roman", 15, QFont.Bold))

        fecha=QDateEdit()
        fecha.setCalendarPopup(True)
        fecha.setDate(QDate.currentDate())
        layout.addWidget(fecha,6,1,1,1)

        label_8=QLabel("Clase:")
        layout.addWidget(label_8,7,0)
        label_8.setAlignment(Qt.AlignLeft)
        label_8.setStyleSheet("color: #000000")
        label_8.setFont(QFont("Times New Roman", 15, QFont.Bold))

        boton_turista = QRadioButton("Turista")
        boton_turista.setStyleSheet("color: #000000")
        boton_turista.setFont(QFont("Times New Roman", 10, QFont.Bold))
        boton_turista.setChecked(True)
        layout.addWidget(boton_turista, 7, 1)

        boton_ejecutiva = QRadioButton("Ejecutiva")
        boton_ejecutiva.setStyleSheet("color: #000000")
        boton_ejecutiva.setFont(QFont("Times New Roman", 10, QFont.Bold))
        boton_ejecutiva.setChecked(False)
        layout.addWidget(boton_ejecutiva, 7, 2)

        grupo_clase=QButtonGroup()
        grupo_clase.addButton(boton_turista)
        grupo_clase.addButton(boton_ejecutiva)

        label_9=QLabel("Cantidad de pasajeros:")
        layout.addWidget(label_9,8,0)
        label_9.setAlignment(Qt.AlignLeft)
        label_9.setStyleSheet("color: #000000")
        label_9.setFont(QFont("Times New Roman", 15, QFont.Bold))

        spinbox_cantidad_pasajeros= QSpinBox()
        spinbox_cantidad_pasajeros.setMinimum(1)
        spinbox_cantidad_pasajeros.setMaximum(10)
        layout.addWidget(spinbox_cantidad_pasajeros,8,1,1,1)

        boton_comprar=QPushButton("Comprar")
        boton_comprar.clicked.connect(self.comprar)
        layout.addWidget(boton_comprar,9,0)

    def comprar(self):
        nombre = self.label_nombre.text()
        apellido = self.label_apellido.text()
        dni = self.dni.text()
        if not nombre or not apellido or not dni:
            QMessageBox.warning(self, "Campos incompletos", "Por favor, completá todos los campos.")
        else:
            QMessageBox.information(self, "Compra Exitosa", "Se ha realizado la compra correctamente.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())