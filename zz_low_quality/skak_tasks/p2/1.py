from PySide6 import QtCore, QtGui, QtWidgets

def generate_pixmap():
    width = 300
    height = 200

    pixmap = QtGui.QPixmap(width, height)
    painter = QtGui.QPainter(pixmap)

    matrix = QtGui.QTransform()
    # Set the transformation matrix values
    painter.setTransform(matrix)

    pen = QtGui.QPen()
    pen.setWidth(1)
    pen.setColor(QtGui.QColor("green"))
    painter.setPen(pen)
    
    font = QtGui.QFont()
    font.setFamily("Times")
    font.setPointSize((40))
    painter.setFont(font)
    
    painter.drawText(50, 100, "Hello World")
    
    painter.end()
    return pixmap

# Example usage in a PyQt6 application
app = QtWidgets.QApplication([])
window = QtWidgets.QMainWindow()
label = QtWidgets.QLabel(window)
pixmap = generate_pixmap()
label.setPixmap(pixmap)
window.setCentralWidget(label)
window.show()
app.exec()
