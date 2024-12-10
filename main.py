from PyQt5.QtWidgets import  *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets


from app import Ui_MainWindow


class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
       
        self.colors = {
            "Punt": "#0000ff",
            "Rectangle": "#ff0000",
            "Rectangle arredonit": "#ffa500",
            "El·lipsis": "#00bfff",
            "Rectangles multiples": "#800080",
            "Linies": "#00ff00",
            "Text": "#8b1612"
            
        }
        self.eleccio = "Punt"
        self.opcions.currentIndexChanged.connect(self.cambio)
        
        self.pintaArea.mousePressEvent = self.pintar
        self.canvas = QPixmap(self.pintaArea.size())
        
        self.limpiarCanvas()
        self.limpiar.clicked.connect(self.limpiarCanvas)
    
    def limpiarCanvas(self):
        self.canvas.fill(Qt.white)
        self.pintaArea.setPixmap(self.canvas)
        self.ultimaPosicioLinea = ""
                
        
        
        
        
    def cambio(self):
        self.eleccio = self.opcions.currentText()
        
        
    def pintar(self, event):
        painter = QPainter(self.pintaArea.pixmap())
        pen = QPen(QColor(self.colors[self.eleccio]), 5)
        painter.setPen(pen)   
        x,y = event.pos().x(), event.pos().y()
        
        if self.eleccio == "Punt":
            pen = QPen(Qt.black, 10)
            painter.drawPoint(x, y)
            
        elif self.eleccio == "Rectangle":
            painter.drawRect(x, y, 100, 50)
        elif self.eleccio == "Rectangle arredonit":
            painter.drawRoundedRect(x, y, 100, 50, 20, 20)
        elif self.eleccio == "El·lipsis":
            painter.drawEllipse(x, y, 100, 50)
        elif self.eleccio == "Rectangles multiples":
            size = 50
            for i in range(1,4):
                painter.drawRect(x+(size + 10) * i, y, size, size)
        elif self.eleccio == "Linies":
            if self.ultimaPosicioLinea != "":
                painter.drawLine(self.ultimaPosicioLinea[0], self.ultimaPosicioLinea[1],x,y)
                self.ultimaPosicioLinea = ""
            else:
                self.ultimaPosicioLinea = [x,y]
        elif self.eleccio == "Text":
            painter.drawText(x, y, "Hola, QPainter!")
            
        painter.end()
        self.pintaArea.update()

        
        
        
app =  QApplication([])
window = MainApp()
window.show()


app.exec_()