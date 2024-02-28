#import tkinter
import math
from tkinter import *
from tkinter import ttk

# importando funções de matemática

import math as mt

#cores

cor1 = '#EEE8AA' #Azul
cor2 = '#FF8C00' #DarkOrange
cor3 = '#C0C0C0' #Cinza
cor4 = '#F0FFF0' #VerdeAgua
cor5 = '#000000' #Preto

#Conf botões

font = 'Ivy 10 bold'
relief = RAISED
width = 10
height = 3

#calculadora

calculadora = Tk()
calculadora.title('CALCULADORA')
calculadora.geometry('500x550+500+100')
calculadora.resizable(width=False, height=False)
calculadora.config(bg=cor4)

#Função para entrar o valor no frame.

global todos_valores

todos_valores = ""
texto = StringVar()

def valores_button(evento):
    global todos_valores
    todos_valores = todos_valores + str(evento)
    texto.set(todos_valores)

def valores_button1(evento):
    global todos_valores
    todos_valores = str(evento)
    texto.set(todos_valores)
    # todos_valores = ""


#FUNÇAO_CALCULAR

def calcular ():
    global todos_valores

    resultado = str(eval(todos_valores))
    texto.set(resultado)
    todos_valores = ''

#Limpar tela

def limpar():
    global todos_valores
    todos_valores = ''
    texto.set('')

#limpar ultimo item

def limpar_ultimo_item():
    global todos_valores
    todos_valores = todos_valores[:-1]
    texto.set(todos_valores)

#Entry. Campo que aparecerá os números quando apertar os botões. (Frames)

frame_tela = Frame(calculadora, width=100, height=50, bg=cor1)
frame_tela.grid(row=0, column=0)

label_tela = Label(calculadora, textvariable=texto, width=50, height=4, padx=7, bg=cor4, anchor='e', bd=0, justify=RIGHT, font='Arial 15 bold', fg=cor5)
label_tela.place(x=-170, y=0)
# label_tela1 = Label(label_tela, border=2, bg=cor5)


#Botões números

bt1 = Button(calculadora, command=lambda:valores_button('1'), text='1', font=font, relief=relief, bg=cor3, width=width, height=height)
bt1.place(x=50, y=150)


bt2 = Button(calculadora, command=lambda:valores_button('2'), text='2', font=font, relief=relief, bg=cor3, width=width, height=height)
bt2.place(x=150, y=150)

bt3 = Button(calculadora, command=lambda:valores_button('3'), text='3', font=font, relief=relief, bg=cor3, width=width, height=height)
bt3.place(x=250, y=150)

bt4 = Button(calculadora, command=lambda:valores_button('4'), text='4', font=font, relief=relief, bg=cor3, width=width, height=height)
bt4.place(x=50, y=225)

bt5 = Button(calculadora, command=lambda:valores_button('5'), text='5', font=font, relief=relief, bg=cor3, width=width, height=height)
bt5.place(x=150, y=225)

bt6 = Button(calculadora, command=lambda:valores_button('6'), text='6', font=font, relief=relief, bg=cor3, width=width, height=height)
bt6.place(x=250, y=225)

bt7 = Button(calculadora, command=lambda:valores_button('7'), text='7', font=font, relief=relief, bg=cor3, width=width, height=height)
bt7.place(x=50, y=300)

bt8 = Button(calculadora, command=lambda:valores_button('8'), text='8', font=font, relief=relief, bg=cor3, width=width, height=height)
bt8.place(x=150, y=300)

bt9 = Button(calculadora, command=lambda:valores_button('9'), text='9', font=font, relief=relief, bg=cor3, width=width, height=height)
bt9.place(x=250, y=300)

bt0 = Button(calculadora, command=lambda:valores_button('0'), text='0', font=font, relief=relief, bg=cor3, width=width, height=height)
bt0.place(x=150, y=375)



#Botões calculos

bt_potencia = Button(calculadora, command=lambda:valores_button('**'), text='exp', font=font, relief=relief, bg=cor1, width=width, height=height)
bt_potencia.place(x=50, y=375)

bt_ponto = Button(calculadora, command=lambda:valores_button('.'), text='.', font=font, relief=relief, bg=cor1, width=width, height=height)
bt_ponto.place(x=250, y=375)

bt_divisao = Button(calculadora, command=lambda:valores_button('/'), text='/', font=font, relief=relief, width=width, height=height)
bt_divisao.place(x=350, y=150)

bt_multiplicacao = Button(calculadora, command=lambda:valores_button('*'), text='*', font=font, relief=relief, width=width, height=height)
bt_multiplicacao.place(x=350, y=225)

bt_soma = Button(calculadora, command=lambda:valores_button('+'), text='+', font=font, relief=relief, width=width, height=height)
bt_soma.place(x=350, y=300)

bt_subtracao = Button(calculadora, command=lambda:valores_button('-'), text='-', font=font, relief=relief, width=width, height=height)
bt_subtracao.place(x=350, y=375)

bt_pi = Button(calculadora, command=lambda:valores_button('3.14159'), text='Л', font=font, relief=relief, bg=cor2, width=width, height=height)
bt_pi.place(x=50, y=75)

bt_porcentagem = Button(calculadora, command=lambda:valores_button1(per(todos_valores)), text='%', font=font, relief=relief, bg=cor2, width=width, height=height)
bt_porcentagem.place(x=150, y=75)

bt_c = Button(calculadora, command=limpar, text='C', font=font, relief=relief, bg=cor2, width=width, height=height)
bt_c.place(x=250, y=75)

bt_backspace = Button(calculadora, command=limpar_ultimo_item, text='←', font=font, relief=relief, bg=cor2, width=width, height=height)
bt_backspace.place(x=350, y=75)

bt_raiz = Button(calculadora, command=lambda:valores_button('**(1/2)'), text='√', font=font, relief=relief, bg=cor1, width=width, height=height)
bt_raiz.place(x=50, y=450)

bt_sin = Button(calculadora, command=lambda:valores_button1(sen(todos_valores)), text='SIN', font=font, relief=relief, bg=cor1, width=width, height=height)
bt_sin.place(x=150, y=450)

bt_cos = Button(calculadora, command=lambda:valores_button1(cos(todos_valores)), text='COS', font=font, relief=relief, bg=cor1, width=width, height=height)
bt_cos.place(x=250, y=450)

bt_igual = Button(calculadora, command=calcular, text='=', font=font, relief=relief, bg=cor2, width=width, height=height)
bt_igual.place(x=350, y=450)

#FUNÇÕES

#SOMA

def add (a,b):
    somar = a + b
    print(a, '+', b, '=', somar)

#SUBTRAÇÃO

def sub (a,b):
    subtracao = a - b
    print(a, '-', b, '=', subtracao)

#MULTIPLICAÇÃO

def mult (a, b):
    multiplicacao = a * b
    print(a, '*', b, '=', multiplicacao)

#DIVISÃO

def div (a,b):
    divisao = a / b
    print(a, '/', b, '=', divisao)

#expoente

def expoente (a,b):
    exp = a ** b
    print(a, '**', b, '=', exp)

#seno

def sen (x):
    rai = math.sin(int(x))
    return rai

#cosseno

def cos (x):
    rai = math.cos(int(x))
    return rai

#porcentagem

def per (x):
    res = float(x)/100
    return res

#Não permite que a calculadora feche sozinha. Precisa ser a última linha do código.

calculadora.mainloop()
