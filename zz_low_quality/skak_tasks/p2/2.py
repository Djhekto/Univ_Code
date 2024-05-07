from PySide6.QtGui import QPixmap, QPainter
from PySide6.QtCore import Qt

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Example matrix
width = len(matrix[0])
height = len(matrix)
pixmap = QPixmap(width, height)

painter = QPainter(pixmap)

for i in range(height):
    for j in range(width):
        value = matrix[i][j]
        painter.setPen(Qt.black)
        painter.setBrush(Qt.white)
        painter.drawRect(j, i, 1, 1)

painter.end()
pixmap.save("output.png")
