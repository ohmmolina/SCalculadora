#Calculadora semantica con GUI en tkinter
from tkinter import *
import tkinter.font as tkf
#Operaciones
def suma(a,b):
   return a+b
def res(a,b):
   return a-b
def mult(a,b):
   return a*b
def div(a,b):
   return a/b
def mod(a,b):
   return a%b
def mcm(a,b): #Minimo comun multiplo.
   m = a if a>b else b
   while m <= a+b:
      if m%a == 0 and m%b == 0:
         return m
      m+=1
def mcd(a,b): #Maximo comun divisor
   M = a if a<b else b
   while M >= 1:
      if a%M == 0 and b%M ==0:
         return M
      M -= 1


def extraer(text):
   l = []
   for t in text.split(' '):
      try:
         l.append(float(t))
      except ValueError:
         if t in numeros.keys():
            try:
               l.append(numeros[t])
            except ValueError: pass
         else: pass
   return l

def calcular():
   text = entrada.get()
   r = ''
   for p in text.split(' '):
      if p.lower() in operacion.keys():
         try:
            if r == '':
               l = extraer(text)
            r = operacion[p.lower()](l[0], l[1])
            l.pop(0)
            l.pop(0)
            l.insert(0,r)
            if len(l) == 1:
               res.set(r)
               break
         except:
            res.set('Algo no entendí bien. Lo siento.')
      elif p.lower() not in operacion.keys():
         res.set('Algo no entendí bien. Lo siento.')

def borrar():
   entrada.delete(0, END)
   res.set('...')

numeros = {'uno':1,'dos':2,'tres':3,'cuatro':4,'cinco':5, 'seis':6, 'siete':7, 'ocho':8, 'nueve':9, 'cero':0}
operacion = {'+':suma, 'suma':suma, 'adicion':suma, 'adición':suma, 'mas':suma, 'más':suma,
   '-':res, 'resta':res, 'sustraccion':res, 'sustracción':res, 'diferencia':res, 'menos':res,
   '*':mult, 'multiplicacion':mult, 'multiplicación':mult, 'multiplicar':mult, 'producto':mult, 'por':mult,
   '%':mod, 'modulo':mod, 'residuo':mod,
   'mcm':mcm, 'minimo comun multiplo':mcm, 'mínimo común múltiplo':mcm,
   'mcd':mcd, 'maximo comun divisor':mcd, 'máximo común divisor':mcd
}



root = Tk()
root.title('CALCULADORA')
root.geometry("400x300")
root.configure(bg='#333')

f_titulo = tkf.Font(family='Verdana', size=15)
f_medium = tkf.Font(family='Verdana', size=12)
f_regular = tkf.Font(family='Verdana', size=8)


titulo = Label(root, text='CALCULADORA SEMANTICA', bg='#222', fg='#eee', font=f_titulo, width=30,  padx=3)
titulo.place(x=0, y=2, height=40)
etiqueta = Label(root, text='Hola! Ingresa debajo que operacion quieres que haga!', bg='#333', fg='#eee', font=f_regular, width=45)
etiqueta.place(x=40, y=45)

texto = StringVar(root)
texto.set('Ej. 5 por ocho')
entrada = Entry(root, bg='#555', fg='#ddd', textvariable= texto, width=52)
entrada.place(x=40, y=70, height=30)

calcular = Button(root, text='Calcular', width=10, command=calcular)
calcular.place(x=80, y=110)
borrar = Button(root, text='Borrar', width=10, command=borrar)
borrar.place(x=240, y=110)

etiqueta_res = Label(root, bg='#333', fg='#eee', font=f_regular, text='Resultado:')
etiqueta_res.place(x=168, y=180)

res=StringVar(root)
res.set('Sin resultado aún')
resultado = Label(root, bg='#333', fg='#aaf', font=f_medium, textvariable=res, width=39)
resultado.place(x=0, y=220)


root.mainloop()