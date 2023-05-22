import openai
from tkinter import *
openai.api_key = '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'

class App:
    
    def __init__(self):
        
        # Ventana raíz
        self.root = Tk()
        self.root.title('ChatGTP')
        self.root.resizable(False, False)
        self.root.config()
        
        # Frame principal
        self.v_principal = Frame(self.root)
        self.v_principal.grid(row=4, column=0)
        
        # Widgets frame principal
        self.r_1 = Label(self.v_principal)
        self.r_1.grid(row=0, column=2, padx=20)
        
        self.l_1 = Label(self.v_principal)
        self.l_1.grid(row=0, column=0, padx=20)
        
        self.encabezado = Label(self.v_principal)
        self.encabezado.config(text='PROYECTO CHATGTP', font='arial 14 bold')
        self.encabezado.grid(row=1, column=1, padx=20, pady=10)
        
        self.salida = Text(self.v_principal)
        self.salida.config(bg='white', padx=25, pady=5)
        self.salida.grid(row=2, column=1)
        
        self.barra = Scrollbar(self.v_principal)
        self.barra.grid(row=2, column=1, sticky='nese')
        self.salida['yscrollcommand'] = self.barra.set
        
        self.r_2 = Label(self.v_principal)
        self.r_2.grid(row=3, column=2, padx=20, pady=20)
        
        self.l_2 = Label(self.v_principal)
        self.l_2.grid(row=3, column=0, padx=20, pady=20)
        
        self.entrada = Entry(self.v_principal)
        self.entrada.config(width=80)
        self.entrada.grid(row=4, column=1)
        
        self.r_3 = Label(self.v_principal)
        self.r_3.grid(row=5, column=2, padx=20, pady=5)
        
        self.l_3 = Label(self.v_principal)
        self.l_3.grid(row=5, column=0, padx=20, pady=5)
        
        self.enviar = Button(self.v_principal)
        self.enviar.config(text='Enviar', bg='#817e7e', font='arial 14 bold', command=self.chat)
        self.enviar.grid(row=6, column=1)
        self.entrada.bind('<Return>', self.pulsar_enter)
        
        self.r_4 = Label(self.v_principal)
        self.r_4.grid(row=7, column=2, padx=20, pady=5)
        
        self.l_4 = Label(self.v_principal)
        self.l_4.grid(row=7, column=0, padx=20, pady=5)
        
        #self.chat()
        self.root.mainloop()   
    
    def chat(self):
        self.salida.delete(1.0, END)
        pregunta = self.entrada.get()
        mensaje = [{"role": "user", "content": pregunta}]
        respuesta = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=mensaje)
        self.salida.insert(INSERT, respuesta.choices[0].message.content)
        self.entrada.delete(0, END)
        
    def pulsar_enter(self, Event):
        self.chat()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        