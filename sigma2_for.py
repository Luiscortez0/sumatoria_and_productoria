#ejercicio 2:  (for)    
# n
# Π  i= 1*2*3*4...n
# i=1

from guizero import App, Text, TextBox, PushButton
import pyttsx3
engine=pyttsx3.init()
prod=1
def resultado():
    global prod
    if int(n.value)>0:
        for i in range(1,(int(n.value)+1),1):
            prod=prod*i

        result.value=f"la productoria es: {str(prod)}"
    else:
        result.value="nummero invalido"

    n.value=""

def mensaje():
    cadena="ingresa el valor de n para resolver la productoria"
    engine.say(cadena)
    engine.runAndWait()

def nuevo():
    global prod
    prod=1
    n.value=""
    result.value=""


app=App(title="ICI app")

button=PushButton(app,text="instruciones", command=mensaje)
titulo= Text(app, text="(for)\n")
formula= Text(app, text="n\n  Π i= 1*2*3*4...n \n i=1 ")
message2 = Text(app, text="ingresa el valor de n:")
n= TextBox(app, width=20,)
button2=PushButton(app,text="Resolver", command=resultado)
button3=PushButton(app,text="Nuevo", command=nuevo)
result= Text(app,text="")
app.display()