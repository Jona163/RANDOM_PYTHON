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