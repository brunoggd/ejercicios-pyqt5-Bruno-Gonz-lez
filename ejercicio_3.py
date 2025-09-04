# Práctico PyQt5: Uso de múltiples ventanas (Herramientas y Contexto)
# -------------------------------------------------------------------
#
# Objetivo: Aprender a crear y manejar dos ventanas simultáneas en PyQt5.
# Una ventana será de herramientas (con botones como Guardar, Abrir, Buscar, etc.)
# y la otra mostrará el contexto: un formulario de afiliados al Club Atlético Chacarita Juniors.
#
# Cada ejercicio suma widgets y lógica, guiando al alumno en el uso de PyQt5, QGridLayout y manejo de ventanas.
#
# -----------------------------------------------------------------------------
# Ejercicio 1: Crear la ventana de contexto (formulario de afiliados)
# -----------------------------------------------------------------------------
# Teoría:
# - QWidget es la base para crear ventanas.
# - QGridLayout organiza los widgets en filas y columnas.
# - QLabel y QLineEdit permiten mostrar e ingresar datos.
#
# Consigna:
# - Crear una ventana principal (QWidget) de 500x350, título "Afiliados - Chacarita Juniors".
# - Agregar QLabel grande y centrado: "Formulario de Afiliación".
# - Agregar QLabel y QLineEdit para Nombre, Apellido, DNI y Fecha de nacimiento.
#
# -----------------------------------------------------------------------------
# Ejercicio 2: Crear la ventana de herramientas
# -----------------------------------------------------------------------------
# Teoría:
# - Otra instancia de QWidget puede funcionar como ventana secundaria.
# - QPushButton permite crear botones de acción.
# - QVBoxLayout organiza widgets en columna.
#
# Consigna:
# - Crear una ventana secundaria de 200x300, título "Herramientas".
# - Agregar botones: "Guardar", "Abrir", "Buscar", "Salir".
#
# -----------------------------------------------------------------------------
# Ejercicio 3: Mostrar ambas ventanas a la vez
# -----------------------------------------------------------------------------
# Teoría:
# - Puedes crear y mostrar varias ventanas instanciando varias clases QWidget.
# - show() en cada ventana las hace visibles simultáneamente.
#
# Consigna:
# - Modifica el script para que ambas ventanas se muestren al ejecutar el programa.
#
# -----------------------------------------------------------------------------
# Ejercicio 4: Conectar botones de herramientas con el formulario
# -----------------------------------------------------------------------------
# Teoría:
# - Los botones pueden ejecutar funciones que interactúan con la otra ventana.
# - Puedes pasar referencias entre ventanas para manipular datos.
#
# Consigna:
# - Haz que el botón "Guardar" muestre un mensaje con los datos ingresados en el formulario.
# - El botón "Salir" debe cerrar ambas ventanas.
#
# -----------------------------------------------------------------------------
# Ejercicio 5: Personalización visual y validaciones
# -----------------------------------------------------------------------------
# Consigna:
# - Cambia colores, fuentes y tamaño de los widgets para una interfaz moderna.
# - Valida que los campos obligatorios estén completos antes de guardar.
#
# -----------------------------------------------------------------------------
# Sugerencia:
# - Usa QDateEdit para la fecha de nacimiento.
# - Usa QMessageBox para mostrar mensajes.
#
# -----------------------------------------------------------------------------
# Esqueleto inicial:

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class VentanaFormulario(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Afiliados - Chacarita Juniors")
        self.setGeometry(100, 100, 500, 350)
        layout = QGridLayout()
        self.setLayout(layout)
        self.setStyleSheet("background-color: #C91700;")

        # COMPLETAR: agregar widgets para el formulario
        etiqueta_1=QLabel("Formulario de Afiliación\nClub Atlético Chacarita Juniors")
        etiqueta_1.setWordWrap(True)
        etiqueta_1.setAlignment(Qt.AlignHCenter)
        etiqueta_1.setFont(QFont("Comic Sans", 20, QFont.Bold))
        layout.addWidget(etiqueta_1,0,0,0,3)
        self.nombre=""
        self.apellido=""
        self.dni=""
        self.fecha_de_nacimiento=""

        etiqueta_nombre=QLabel("Nombre:")
        etiqueta_nombre.setAlignment(Qt.AlignLeft)
        etiqueta_nombre.setFont(QFont("Comic Sans", 10, QFont.Bold))
        layout.addWidget(etiqueta_nombre,1,0)

        self.ingresar_nombre=QLineEdit()
        self.nombre=self.ingresar_nombre
        self.ingresar_nombre.setAlignment(Qt.AlignLeft)
        layout.addWidget(self.ingresar_nombre,1,1,1,2)

        etiqueta_apellido=QLabel("Apellido:")
        etiqueta_apellido.setAlignment(Qt.AlignLeft)
        etiqueta_apellido.setFont(QFont("Comic Sans", 10, QFont.Bold))
        layout.addWidget(etiqueta_apellido,2,0)

        self.ingresar_apellido=QLineEdit()
        self.apellido=self.ingresar_apellido
        self.ingresar_apellido.setAlignment(Qt.AlignLeft)
        layout.addWidget(self.ingresar_apellido,2,1,1,2)

        etiqueta_dni=QLabel("DNI:")
        etiqueta_dni.setAlignment(Qt.AlignLeft)
        etiqueta_dni.setFont(QFont("Comic Sans", 10, QFont.Bold))
        layout.addWidget(etiqueta_dni,3,0)

        self.ingresar_dni=QLineEdit()
        self.dni=self.ingresar_dni
        self.ingresar_dni.setAlignment(Qt.AlignLeft)
        layout.addWidget(self.ingresar_dni,3,1,1,2)

        etiqueta_fecha_de_nacimiento=QLabel("Fecha de nacimiento:")
        etiqueta_fecha_de_nacimiento.setAlignment(Qt.AlignLeft)
        etiqueta_fecha_de_nacimiento.setFont(QFont("Comic Sans", 10, QFont.Bold))
        layout.addWidget(etiqueta_fecha_de_nacimiento,4,0)

        self.fecha_seleccionada=QDateEdit()
        self.fecha_de_nacimiento=self.fecha_seleccionada
        self.fecha_seleccionada.setCalendarPopup(True)
        layout.addWidget(self.fecha_seleccionada,4,1,1,2)


class VentanaHerramientas(QWidget):
    def __init__(self,ventana_formulario):
        super().__init__()
        self.setWindowTitle("Herramientas")
        self.setGeometry(650, 100, 200, 300)
        self.setStyleSheet("background-color: #C91700;") 
        self.ventana_formulario=ventana_formulario
        layout = QVBoxLayout()
        self.setLayout(layout)

        etiqueta_1=QLabel("Herramientas")
        etiqueta_1.setAlignment(Qt.AlignHCenter)
        etiqueta_1.setFont(QFont("Comic Sans", 20, QFont.Bold))
        layout.addWidget(etiqueta_1)
        # COMPLETAR: agregar botones de herramientas
        boton_guardar=QPushButton("Guardar")
        boton_guardar.setFont(QFont("Comic Sans", 10, QFont.Bold))
        boton_guardar.clicked.connect(self.guardar)
        layout.addWidget(boton_guardar)

        boton_abrir=QPushButton("Abrir")
        boton_abrir.setFont(QFont("Comic Sans", 10, QFont.Bold))
        boton_abrir.clicked.connect(self.abrir)
        layout.addWidget(boton_abrir)

        boton_buscar=QPushButton("Buscar")
        boton_buscar.setFont(QFont("Comic Sans", 10, QFont.Bold))
        boton_buscar.clicked.connect(self.buscar)
        layout.addWidget(boton_buscar)
        
        boton_salir=QPushButton("Salir")
        boton_salir.setFont(QFont("Comic Sans", 10, QFont.Bold))
        boton_salir.clicked.connect(lambda: self.close())
        boton_salir.clicked.connect(lambda: self.ventana_formulario.close())
        layout.addWidget(boton_salir)

    def guardar(self):
        nombre = self.ventana_formulario.nombre.text()
        apellido = self.ventana_formulario.apellido.text()
        dni = self.ventana_formulario.dni.text()
        fecha_de_nacimiento = self.ventana_formulario.fecha_de_nacimiento.date().toString()
        if not dni.isdigit() or not (7 <= len(dni) <= 8):
            QMessageBox.warning(self, "DNI inválido", "El DNI debe tener entre 7 y 8 dígitos numéricos.")
            return
        if not nombre or not apellido or not dni or not fecha_de_nacimiento:
            QMessageBox.warning(self,"Error!","Campos incompletos, completa todos los cuadros.")
        else:
            QMessageBox.information(self,"Información Ingresada",f"La información ingresada fue:\nNombre: {nombre}\nApellido: {apellido}\nDNI: {dni}\nFecha de Nacimiento: {fecha_de_nacimiento}")

    def abrir(self):
        print("Si hubiera algo para abrir...")

    def buscar(self):
        print("Qué buscas maestro?")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana_form = VentanaFormulario()
    ventana_herr = VentanaHerramientas(ventana_form)
    ventana_form.show()
    ventana_herr.show()
    # COMPLETAR: mostrar ambas ventanas
    sys.exit(app.exec_())
