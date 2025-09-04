import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de Usuario")
        self.setGeometry(100, 100, 400, 300)
        layout = QGridLayout()
        self.setLayout(layout)
        self.setStyleSheet("background-color: #A5A3D6;")

        label_1=QLabel("Formulario de Registro")
        layout.addWidget(label_1,0,0,1,3)
        label_1.setAlignment(Qt.AlignHCenter)
        label_1.setFont(QFont("Comic Sans", 30, QFont.Bold))
        label_1.setStyleSheet("color: #4943F7")
        label_1.setFont(QFont("Times New Roman", 15, QFont.Bold))
        label_1.setWordWrap(True)

        label_2=QLabel("Nombre:")
        layout.addWidget(label_2,1,0)
        label_2.setAlignment(Qt.AlignLeft)
        label_2.setStyleSheet("color: #4943F7")
        label_2.setFont(QFont("Times New Roman", 15, QFont.Bold))

        self.label_nombre=QLineEdit()
        layout.addWidget(self.label_nombre,1,1,1,2)
        
        label_3=QLabel("Email:")
        layout.addWidget(label_3,2,0)
        label_3.setAlignment(Qt.AlignLeft)
        label_3.setStyleSheet("color: #4943F7")
        label_3.setFont(QFont("Times New Roman", 15, QFont.Bold))

        self.label_email=QLineEdit()
        layout.addWidget(self.label_email,2,1,1,2)

        label_4=QLabel("Contraseña:")
        layout.addWidget(label_4, 3, 0)
        label_4.setAlignment(Qt.AlignLeft)
        label_4.setStyleSheet("color: #4943F7")
        label_4.setFont(QFont("Times New Roman", 15, QFont.Bold))

        self.contraseña_oculta = QLineEdit()
        self.contraseña_oculta.setEchoMode(QLineEdit.Password) 
        layout.addWidget(self.contraseña_oculta, 3,1,1,2)

        label_5=QLabel("Género:")
        layout.addWidget(label_5,4,0)
        label_5.setAlignment(Qt.AlignLeft)
        label_5.setStyleSheet("color: #4943F7")
        label_5.setFont(QFont("Times New Roman", 15, QFont.Bold))

        boton_radio_masculino = QRadioButton("Masculino")
        boton_radio_masculino.setStyleSheet("color: #4943F7")
        boton_radio_masculino.setFont(QFont("Times New Roman", 10, QFont.Bold))
        boton_radio_masculino.setChecked(True)
        boton_radio_masculino.genero = "Masculino"
        layout.addWidget(boton_radio_masculino, 4, 1)

        boton_radio_femenino = QRadioButton("Femenino")
        boton_radio_femenino.setStyleSheet("color: #4943F7")
        boton_radio_femenino.setFont(QFont("Times New Roman", 10, QFont.Bold))
        boton_radio_femenino.setChecked(False)
        boton_radio_femenino.genero = "Fémenino"
        layout.addWidget(boton_radio_femenino, 4, 2)

        grupo_genero=QButtonGroup()
        grupo_genero.addButton(boton_radio_masculino)
        grupo_genero.addButton(boton_radio_femenino)

        label_6=QLabel("País:")
        layout.addWidget(label_6,5,0)
        label_6.setAlignment(Qt.AlignLeft)
        label_6.setStyleSheet("color: #4943F7")
        label_6.setFont(QFont("Times New Roman", 15, QFont.Bold))

        paises=QComboBox()
        paises.addItem("Argentina")
        paises.addItem("Brasil")
        paises.addItem("Alemania")
        paises.addItem("Francia")
        paises.addItem("España")
        layout.addWidget(paises,5,1,1,2)

        self.checkbox_terminos = QCheckBox("Acepto los términos y condiciones")
        layout.addWidget(self.checkbox_terminos, 6, 0, 1, 3)

        boton_registrarse=QPushButton("Registrarse")
        boton_registrarse.clicked.connect(self.registrar)
        layout.addWidget(boton_registrarse,7,0)

    def registrar(self):
        nombre = self.label_nombre.text()
        email = self.label_email.text()
        contraseña = self.contraseña_oculta.text()

        if not nombre or not email or not contraseña:
            QMessageBox.warning(self, "Campos incompletos", "Por favor, completá todos los campos.")
        elif not self.checkbox_terminos.isChecked():
            QMessageBox.warning(self, "Términos no aceptados", "Debés aceptar los términos y condiciones.")
        else:
            QMessageBox.information(self, "Registro exitoso", "¡Te has registrado correctamente!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())