# Autor: Jonathan Hernández
# Fecha: 11 Septiembre 2024
# Descripción: Código para procesamiento de imagenes con Sobel.
# GitHub: https://github.com/Jona163

## importaciones a requerir 
import turtle
import pygame
import time
import numpy as np
import matplotlib.pyplot as plt

# Parte 1: Gráfico de una función seno (con matplotlib)
def graficar_seno():
    x = np.linspace(-10, 10, 100)
    y = np.sin(x)
    
    plt.plot(x, y, label='Seno')
    plt.title('Gráfico de la función seno')
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.legend()
    plt.show()
    
# Parte 2: Reloj analógico con turtle
def reloj_turtle():
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.bgcolor("black")
    t.pensize(3)
    t.shape("turtle")
    screen.tracer(0)
    
def draw_hand(length, angle):
        t.penup()
        t.goto(0, 0)
        t.setheading(90)
        t.right(angle)
        t.pendown()
        t.forward(length)


def draw_clock():
        for i in range(12):
            t.penup()
            t.goto(0, 0)
            t.setheading(90)
            t.right(i * 30)
            t.forward(150)
            t.pendown()
            t.forward(10)
            t.penup()
            t.forward(20)
            t.write(str(i + 1), align="center", font=("Arial", 12, "normal"))
            t.goto(0, 0)
            
draw_clock()



    while True:
        t.clear()
        draw_clock()
        h = time.localtime().tm_hour
        m = time.localtime().tm_min
        s = time.localtime().tm_sec
        
        
        


        draw_hand(100, (h % 12) * 30 + m / 2)  # Hora
        draw_hand(120, m * 6)  # Minuto
        draw_hand(140, s * 6)  # Segundo
        screen.update()
        time.sleep(1)