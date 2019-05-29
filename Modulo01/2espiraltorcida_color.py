# 1espiralcuadrada.py - Esto es un comentario. Dibujaremos una espiral cuadrada
import turtle
t= turtle.Pen()
colores=["red","yellow","blue","green"]
for x in range(100):
    t.pencolor(colores[x%4])
    t.forward(x)
    t.left(91)
