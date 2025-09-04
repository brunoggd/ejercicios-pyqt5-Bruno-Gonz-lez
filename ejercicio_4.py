

# Práctico PyQt5: Editor de Texto con Menús y Diálogos
# ------------------------------------------------
#
# Objetivo: Crear un editor de texto completo integrando todos los conceptos aprendidos:
# menús, diálogos, gestión de archivos, barras de estado y shortcuts de teclado.
#
# Este ejercicio te guiará para construir una aplicación profesional paso a paso.
#
# -----------------------------------------------------------------------------
# Ejercicio 1: Ventana principal con área de texto
# -----------------------------------------------------------------------------
# Teoría:
# - QMainWindow es la base para aplicaciones con menús y barras de herramientas.
# - QTextEdit permite editar texto con formato básico.
# - setCentralWidget() define el widget principal de la ventana.
#
# Consigna:
# - Crear ventana principal (QMainWindow) de 800x600, título "Editor de Texto".
# - Agregar QTextEdit como widget central.
# - Configurar texto inicial: "Escribe aquí tu texto..."

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit, QMenuBar, 
                             QAction, QFileDialog, QMessageBox, QStatusBar,
                             QVBoxLayout, QWidget,QFontDialog,QLabel,QHBoxLayout,QDockWidget,QPushButton,QScrollArea)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence, QFont

class EditorTexto(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor de Texto")
        self.setGeometry(100, 100, 800, 600)
        self.centrar_ventana()    
        # COMPLETAR: Crear QTextEdit y establecerlo como widget central
        hoja = QWidget()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        self.editor = QTextEdit()
        self.editor.setPlaceholderText("Escribe aquí tu texto...")
        self.editor.setFixedWidth(600)
        self.setStyleSheet("""
                            background: #191A73;
                            color: #4FFFFE;
                            border: 2px inset #009DFF;
                            border-radius: 10px;
                            padding: 8px 8px;
                            font-family: Cascadia Mono;
                            font-size: 15px;
                                """)
        self.editor.setStyleSheet("background: white;color:black")

        etiqueta_titulo_programa=QLabel("Word +")
        etiqueta_titulo_programa.setWordWrap(True)
        etiqueta_titulo_programa.setStyleSheet("""
                                                  background: #001859;
                                                  color: #4FFFFE;""")
        layout.addWidget(etiqueta_titulo_programa,alignment=Qt.AlignCenter)

        self.archivo_actual = None

        layout.addWidget(self.editor)
        hoja.setLayout(layout)
        self.setCentralWidget(hoja)

        boton_de_prueba_1 = QPushButton("Botón de Prueba 1")
        boton_de_prueba_1.clicked.connect(lambda: print("Este es un texto generado por el botón 1"))
        boton_de_prueba_2 = QPushButton("Botón de Prueba 2")
        boton_de_prueba_2.clicked.connect(lambda: print("Este es un texto generado por el botón 2"))
        boton_de_prueba_3 = QPushButton("Botón de Prueba 3")
        boton_de_prueba_3.clicked.connect(lambda: print("Este es un texto generado por el botón 3"))

        informacion_scroll=QLabel("""\nEsto es un ejemplo de información en una scroll area.\n
                                    \n1) Dato 1: Primer dato de la scroll area.\n
                                    \n2) Dato 2: Segundo dato de la scroll area.\n
                                    \n3) Dato 3: Tercer dato de la scroll area.\n
                                    \n4) Dato 4: Cuarto dato de la scroll area.\n
                                    \n5) Dato 5: Quinto dato de la scroll area.\n
                                    \n6) Dato 6: Sexto dato de la scroll area.\n
                                    \n7) Dato 7: Septimo dato de la scroll area.\n
                                    \n8) Dato 8: Octavo dato de la scroll area.\n
                                    \n9) Dato 9: Noveno dato de la scroll area.\n
                                    \n10) Dato 10: Decimo dato de la scroll area.\n""")
        informacion_scroll.setWordWrap(True)


        contenedor = QWidget()
        layout_2 = QVBoxLayout()
        contenedor.setLayout(layout_2)
        layout_2.addWidget(boton_de_prueba_1)
        layout_2.addWidget(boton_de_prueba_2)
        layout_2.addWidget(boton_de_prueba_3)
        layout_2.addWidget(informacion_scroll)

        scroll_area=QScrollArea()
        scroll_area.setMinimumWidth(230)
        scroll_area.setMaximumWidth(300)
        scroll_area.setWidget(contenedor)
        scroll_area.setWidgetResizable(True)

        dockwidget = QDockWidget("Herramientas", self)
        dockwidget.setFeatures(QDockWidget.DockWidgetMovable)
        dockwidget.setWidget(scroll_area)

        self.addDockWidget(Qt.LeftDockWidgetArea, dockwidget)

# -----------------------------------------------------------------------------
# Ejercicio 2: Crear la barra de menús
# -----------------------------------------------------------------------------
# Teoría:
# - menuBar() devuelve la barra de menús de QMainWindow.
# - addMenu() crea un menú nuevo.
# - QAction representa una acción que puede estar en menús o barras de herramientas.
#
# Consigna:
# - Crear menú "Archivo" con opciones: "Nuevo", "Abrir", "Guardar", "Salir".
# - Crear menú "Editar" con opciones: "Cortar", "Copiar", "Pegar".
# - Crear menú "Ayuda" con opción: "Acerca de".
    def centrar_ventana(self):
        pantalla = QApplication.primaryScreen().availableGeometry()
        ventana = self.frameGeometry()
        ventana.moveCenter(pantalla.center())
        self.move(ventana.topLeft())

        """ > availableGeometry(): obtiene el área visible de la pantalla (sin la barra de tareas).
            > frameGeometry(): obtiene el rectángulo de la ventana incluyendo bordes.
            > moveCenter(): centra ese rectángulo en la pantalla.
            > move(): posiciona la ventana en ese punto.
            > primaryscreen(): devuelve la pantalla principal del sistema, por si hay dos monitores.
            > center(): devuelve el punto central de la pantalla, también puede ser de ventanas.
            > topLeft(): devuelve la coordenada de la esquina superior izquierda de la ventana,
                         al igual que center es compatible tanto para ventanas como para pantallas."""

    def crear_menus(self):
        # COMPLETAR: Obtener la barra de menús
        menubar = self.menuBar()
        
        # COMPLETAR: Crear menú Archivo
        menu_archivo = menubar.addMenu('&Archivo')
        menu_archivo.setStyleSheet("""border: 2px inset #009DFF;
                                      border-radius: 10px;
                                      padding: 8px 8px;""")
        
        # COMPLETAR: Crear acciones para el menú Archivo
        accion_nuevo = QAction('&Nuevo', self)
        accion_nuevo.setShortcut(QKeySequence.New)  # Ctrl+N
        accion_nuevo.triggered.connect(self.nuevo_archivo)
        menu_archivo.addAction(accion_nuevo)

        accion_abrir = QAction('&Abrir', self)
        accion_abrir.setShortcut(QKeySequence.Open)  
        accion_abrir.triggered.connect(self.abrir_archivo)
        menu_archivo.addAction(accion_abrir)

        menu_archivo.addSeparator()

        accion_guardar = QAction('&Guardar', self)
        accion_guardar.setShortcut(QKeySequence.Save)  
        accion_guardar.triggered.connect(self.guardar_archivo)
        menu_archivo.addAction(accion_guardar)

        menu_archivo.addSeparator()

        accion_salir = QAction('&Salir', self)
        accion_salir.setShortcut(QKeySequence.Quit)  
        accion_salir.triggered.connect(self.salir)
        menu_archivo.addAction(accion_salir)

        menu_archivo.addSeparator()

        menu_editar = menubar.addMenu('&Editar')
        menu_editar.setStyleSheet("""border: 2px inset #009DFF;
                                      border-radius: 10px;
                                      padding: 8px 8px;""")

        accion_cortar = QAction('&Cortar', self)
        accion_cortar.setShortcut(QKeySequence.Cut)  
        accion_cortar.triggered.connect(self.editor.cut)
        menu_editar.addAction(accion_cortar)

        accion_copiar = QAction('&Copiar', self)
        accion_copiar.setShortcut(QKeySequence.Copy)  
        accion_copiar.triggered.connect(self.editor.copy)
        menu_editar.addAction(accion_copiar)

        accion_pegar = QAction('&Pegar', self)
        accion_pegar.setShortcut(QKeySequence.Paste)  
        accion_pegar.triggered.connect(self.editor.paste)
        menu_editar.addAction(accion_pegar)

        menu_ayuda = menubar.addMenu('A&yuda')
        menu_ayuda.setStyleSheet("""border: 2px inset #009DFF;
                                      border-radius: 10px;
                                      padding: 8px 8px;""")
        
        accion_acerca_de = QAction('&Acerca del editor de texto', self)
        accion_acerca_de.triggered.connect(self.acerca_de)
        menu_ayuda.addAction(accion_acerca_de)

        menu_opciones= menubar.addMenu('&Opciones')
        menu_opciones.setStyleSheet("""border: 2px inset #009DFF;
                                      border-radius: 10px;
                                      padding: 8px 8px;""")

        accion_opciones_fuente = QAction('Seleccionar Fuente', self)
        accion_opciones_fuente.triggered.connect(self.seleccionar_fuente)
        menu_opciones.addAction(accion_opciones_fuente)
        


# -----------------------------------------------------------------------------
# Ejercicio 3: Implementar funciones de archivo
# -----------------------------------------------------------------------------
# Teoría:
# - QFileDialog proporciona diálogos estándar para abrir/guardar archivos.
# - QFileDialog.getOpenFileName() abre diálogo para seleccionar archivo.
# - QFileDialog.getSaveFileName() abre diálogo para guardar archivo.
#
# Consigna:
# - Implementar nuevo_archivo(): limpiar el editor.
# - Implementar abrir_archivo(): usar QFileDialog para cargar archivo.
# - Implementar guardar_archivo(): usar QFileDialog para guardar texto.

    def nuevo_archivo(self):
        if self.editor.document().isModified():
            respuesta = QMessageBox.question(self, 'Nuevo archivo',
                                           '¿Desea guardar los cambios?',
                                           QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if respuesta == QMessageBox.Yes:
                self.guardar_archivo()
            elif respuesta == QMessageBox.Cancel:
                return
        
        self.editor.clear()
        self.archivo_actual = None
        self.setWindowTitle("Editor - Nuevo documento")
        self.statusBar().showMessage("Nuevo documento creado", 2000)
    
    def abrir_archivo(self):
        archivo, _ = QFileDialog.getOpenFileName(self, 'Abrir archivo', '', 'Archivos de texto (*.txt)')
        if archivo:
            try:
                with open(archivo, 'r', encoding='utf-8') as archivo:
                    contenido = archivo.read()
                    self.editor.setPlainText(contenido)
            except Exception as e:
                QMessageBox.warning(self, 'Error', f'No se pudo abrir el archivo:\n{e}')

    def guardar_como(self):
        archivo, _ = QFileDialog.getSaveFileName(
            self,
            'Guardar archivo como',
            '',
            'Archivos de texto (*.txt);;Todos los archivos (*.*)'
        )
        
        if archivo:
            self._escribir_archivo(archivo)

    def _escribir_archivo(self, archivo):
        try:
            with open(archivo, 'w', encoding='utf-8') as f:
                f.write(self.editor.toPlainText())
            
            self.archivo_actual = archivo
            self.setWindowTitle(f"Editor - {archivo}")
            self.statusBar().showMessage(f"Archivo guardado: {archivo}", 3000)
            self.editor.document().setModified(False)
            
        except Exception as e:
            QMessageBox.critical(self, 'Error al guardar',
                               f'No se pudo guardar el archivo:\n{str(e)}')
    
    def guardar_archivo(self):
        if self.archivo_actual:
            self._escribir_archivo(self.archivo_actual)
        else:
            self.guardar_como()

# -----------------------------------------------------------------------------
# Ejercicio 4: Agregar diálogos informativos
# -----------------------------------------------------------------------------
# Teoría:
# - QMessageBox permite mostrar mensajes, advertencias y preguntas al usuario.
# - QMessageBox.information() muestra información.
# - QMessageBox.question() hace preguntas con botones Sí/No.
#
# Consigna:
# - Implementar acerca_de(): mostrar información del programa.
# - Modificar salir(): preguntar si desea guardar antes de cerrar.

    def acerca_de(self):
        QMessageBox.about(self,'Acerca de', 
                                '<h3>Editor de Texto<h3> v1.0\n\nCreado con PyQt5\n\nPara aprender desarrollo de interfaces.\n\nHola profe todo bien? acá haciendo word 2.')
    
    def salir(self):
        # COMPLETAR: Preguntar si desea guardar antes de salir
        respuesta = QMessageBox.question(self, 'Salir', 
                                        '¿Desea guardar los cambios antes de salir?',
                                        QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        if respuesta == QMessageBox.Yes:
            self.guardar_archivo()
        elif respuesta == QMessageBox.No:
            self.close()

    def seleccionar_fuente(self):
        fuente_actual = self.font()
        fuente, ok = QFontDialog.getFont(fuente_actual, self, "Seleccionar fuente")
        if ok:
            QMessageBox.about(self,"Fuente Seleccionada",f"Has seleccionado la fuente [ {fuente.family()} ]")


# -----------------------------------------------------------------------------
# Ejercicio 5: Agregar barra de estado
# -----------------------------------------------------------------------------
# Teoría:
# - QStatusBar muestra información en la parte inferior de la ventana.
# - statusBar() devuelve la barra de estado de QMainWindow.
# - showMessage() muestra un mensaje temporal.
#
# Consigna:
# - Agregar barra de estado que muestre "Listo" al inicio.
# - Actualizar mensaje cuando se realizan acciones (abrir, guardar, etc.).

    def actualizar_cursor(self):
        cursor = self.editor.textCursor()
        linea = cursor.blockNumber() + 1
        columna = cursor.columnNumber() + 1
        self.statusBar().showMessage(f'Línea: {linea}, Columna: {columna}')

    def crear_barra_estado(self):
        self.statusBar().showMessage('Listo')
        self.editor.cursorPositionChanged.connect(self.actualizar_cursor)

# -----------------------------------------------------------------------------
# Ejercicio 6: Integración completa
# -----------------------------------------------------------------------------
# Consigna:
# - Llamar todos los métodos de configuración en __init__.
# - Probar todas las funcionalidades del editor.
# - Personalizar colores, fuentes o agregar más opciones de menú.

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    editor = EditorTexto()
    # COMPLETAR: Llamar métodos de configuración
    editor.crear_menus()
    editor.crear_barra_estado()
    editor.show()
    sys.exit(app.exec_())

# -----------------------------------------------------------------------------
# Ejercicio Extra: Mejoras opcionales
# -----------------------------------------------------------------------------
# - Agregar función "Buscar y reemplazar".
# - Implementar vista previa de impresión.
# - Añadir formato de texto (negrita, cursiva).
# - Crear diálogo de configuración de fuente.
# - Implementar funcionalidad de "Archivos recientes".
