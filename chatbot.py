#importaciones
from cgitb import text
from ctypes import alignment
import re
import random
import json

#Elementos de interfaz grafica
from tkinter import *
import tkinter
from tkinter import font
from turtle import left

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 8"
FONT_BOLD = "Helvetica 10 bold"

bot_name = "Hermes Bot"

#cargamos las respuestas del archivo JSON

with open('respuestas.JSON') as archivo:
    respuestas = json.load(archivo)

  
#definiciones de métodos utilizados
def get_response(user_input):
    #eliminamos de la entrada caracteres especiales
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty +=1

    percentage = float(message_certainty) / float(len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    highest_prob = {}

    def response(bot_response, list_of_words, single_response = False, required_words = []):
        nonlocal highest_prob
        highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    response(respuestas['saludo'][random.randint(0,2)]['respuesta'], ['que','onda', 'hola'], single_response = True)
    response(respuestas['saludo'][random.randint(0,2)]['respuesta'], ['que','onda', 'hola'], required_words=['hola'])
    response(respuestas['estado'][random.randint(0,2)]['respuesta'], ['como','estas'], required_words=['como', 'estas'])
    response(respuestas['regresoestado'][random.randint(0,1)]['respuesta'], ['bien','gracias'], required_words=['bien', 'gracias'])
    response(respuestas['informes'][random.randint(0,1)]['respuesta'], ['reglamento','transito'], required_words=['reglamento', 'transito'])
    response(respuestas['comedia'][random.randint(0,2)]['respuesta'], ['cuenta','chiste'], required_words=['cuenta', 'chiste'])
    response(respuestas['curiosidades'][random.randint(0,2)]['respuesta'], ['dato','curioso'], required_words=['dato', 'curioso'])
    response(respuestas['musica'][random.randint(0,2)]['respuesta'], ['escuchas','musica'], required_words=['musica', 'escuchas'])
    
    response(respuestas['articulo1'][0]['respuesta'], ['articulo', 'uno'], required_words=['articulo', 'uno'])
    response(respuestas['articulo2'][0]['respuesta'], ['articulo', 'dos'], required_words=['articulo', 'dos'])
    response(respuestas['articulo3'][0]['respuesta'], ['articulo', 'tres'], required_words=['articulo', 'tres'])
    response(respuestas['articulo4'][0]['respuestaPrincipal'], ['articulo', 'cuatro'], required_words=['articulo', 'cuatro'])
    response(respuestas['articulo5'][0]['respuesta'], ['articulo', 'cinco'], required_words=['articulo', 'cinco'])
    response(respuestas['articulo6'][0]['respuesta'], ['articulo', 'seis'], required_words=['articulo', 'seis'])
    response(respuestas['articulo7'][0]['respuesta'], ['articulo', 'siete'], required_words=['articulo', 'siete'])
    response(respuestas['articulo8'][0]['respuesta'], ['articulo', 'ocho'], required_words=['articulo', 'ocho'])
    response(respuestas['articulo9'][0]['respuesta'], ['articulo', 'nueve'], required_words=['articulo', 'nueve'])
    response(respuestas['articulo10'][0]['respuesta'], ['articulo', 'diez'], required_words=['articulo', 'diez'])
    response(respuestas['articulo11'][0]['respuesta'], ['articulo', 'once'], required_words=['articulo', 'once'])
    response(respuestas['articulo12'][0]['respuesta'], ['articulo', 'doce'], required_words=['articulo', 'doce'])
    response(respuestas['articulo13'][0]['respuesta'], ['articulo', 'trece'], required_words=['articulo', 'trece'])
    response(respuestas['articulo14'][0]['respuesta'], ['articulo', 'catorce'], required_words=['articulo', 'catorce'])
    response(respuestas['articulo15'][0]['respuesta'], ['articulo', 'quince'], required_words=['articulo', 'quince'])
    response(respuestas['articulo16'][0]['respuesta'], ['articulo', 'dieciseis'], required_words=['articulo', 'dieciseis'])
    response(respuestas['articulo17'][0]['respuesta'], ['articulo', 'diecisiete'], required_words=['articulo', 'diecisiete'])
    response(respuestas['articulo18'][0]['respuesta'], ['articulo', 'dieciocho'], required_words=['articulo', 'dieciocho'])
    response(respuestas['articulo19'][0]['respuesta'], ['articulo', 'diecinueve'], required_words=['articulo', 'diecinueve'])
    response(respuestas['articulo20'][0]['respuesta'], ['articulo', 'veinte'], required_words=['articulo', 'veinte'])
    response(respuestas['articulo21'][0]['respuesta'], ['articulo', 'veintiuno'], required_words=['articulo', 'veintiuno'])
    response(respuestas['articulo22'][0]['respuesta'], ['articulo', 'veintidos'], required_words=['articulo', 'veintidos'])
    response(respuestas['articulo23'][0]['respuesta'], ['articulo', 'veintitres'], required_words=['articulo', 'veintitres'])
    response(respuestas['articulo24'][0]['respuesta'], ['articulo', 'veinticuatro'], required_words=['articulo', 'veinticuatro'])
    response(respuestas['articulo25'][0]['respuesta'], ['articulo', 'veinticinco'], required_words=['articulo', 'veinticinco'])
    response(respuestas['articulo26'][0]['respuesta'], ['articulo', 'veintiseis'], required_words=['articulo', 'veintiseis'])
    response(respuestas['articulo27'][0]['respuesta'], ['articulo', 'veintisiete'], required_words=['articulo', 'veintisiete'])
    response(respuestas['articulo28'][0]['respuesta'], ['articulo', 'veintiocho'], required_words=['articulo', 'veintiocho'])
    response(respuestas['articulo29'][0]['respuesta'], ['articulo', 'veintinueve'], required_words=['articulo', 'veintinueve'])
    response(respuestas['articulo30'][0]['respuesta'], ['articulo', 'treinta'], required_words=['articulo', 'treinta'])
    response(respuestas['articulo31'][0]['respuesta'], ['articulo', 'treinta y uno'], required_words=['articulo', 'treinta','y', 'uno'])
    response(respuestas['articulo32'][0]['respuesta'], ['articulo', 'treinta y dos'], required_words=['articulo', 'treinta', 'y', 'dos'])
    response(respuestas['articulo33'][0]['respuesta'], ['articulo', 'treinta y tres'], required_words=['articulo', 'treinta', 'y', 'tres'])
    response(respuestas['articulo34'][0]['respuesta'], ['articulo', 'treinta y cuatro'], required_words=['articulo', 'treinta', 'y', 'cuatro'])
    response(respuestas['articulo35'][0]['respuesta'], ['articulo', 'treinta y cinco'], required_words=['articulo', 'treinta', 'y', 'cinco'])
    response(respuestas['articulo36'][0]['respuesta'], ['articulo', 'treinta y seis'], required_words=['articulo', 'treinta', 'y', 'seis'])
    response(respuestas['articulo37'][0]['respuesta'], ['articulo', 'treinta y siete'], required_words=['articulo', 'treinta', 'y', 'siete'])
    response(respuestas['articulo38'][0]['respuesta'], ['articulo', 'treinta y ocho'], required_words=['articulo', 'treinta', 'y', 'ocho'])
    response(respuestas['articulo39'][0]['respuesta'], ['articulo', 'treinta y nueve'], required_words=['articulo', 'treinta', 'y', 'nueve'])
    response(respuestas['articulo40'][0]['respuesta'], ['articulo', 'cuarenta'], required_words=['articulo', 'cuarenta'])
    response(respuestas['articulo41'][0]['respuesta'], ['articulo', 'cuarenta y uno'], required_words=['articulo', 'cuarenta', 'y', 'uno'])
    response(respuestas['articulo42'][0]['respuesta'], ['articulo', 'cuarenta y dos'], required_words=['articulo', 'cuarenta', 'y', 'dos'])
    response(respuestas['articulo43'][0]['respuesta'], ['articulo', 'cuarenta y tres'], required_words=['articulo', 'cuarenta', 'y', 'tres'])
    response(respuestas['articulo44'][0]['respuesta'], ['articulo', 'cuarenta y cuatro'], required_words=['articulo', 'cuarenta', 'y', 'cuatro'])
    response(respuestas['articulo45'][0]['respuesta'], ['articulo', 'cuarenta y cinco'], required_words=['articulo', 'cuarenta', 'y', 'cinco'])
    response(respuestas['articulo46'][0]['respuesta'], ['articulo', 'cuarenta y seis'], required_words=['articulo', 'cuarenta', 'y', 'seis'])
    response(respuestas['articulo47'][0]['respuesta'], ['articulo', 'cuarenta y siete'], required_words=['articulo', 'cuarenta', 'y', 'siete'])
    response(respuestas['articulo48'][0]['respuesta'], ['articulo', 'cuarenta y ocho'], required_words=['articulo', 'cuarenta', 'y', 'ocho'])
    response(respuestas['articulo49'][0]['respuesta'], ['articulo', 'cuarenta y nueve'], required_words=['articulo', 'cuarenta', 'y', 'nueve'])
    response(respuestas['articulo50'][0]['respuesta'], ['articulo', 'cincuenta'], required_words=['articulo', 'cincuenta'])
    response(respuestas['articulo51'][0]['respuesta'], ['articulo', 'cincuenta y uno'], required_words=['articulo', 'cincuenta', 'y', 'uno'])
    response(respuestas['articulo52'][0]['respuesta'], ['articulo', 'cincuenta y dos'], required_words=['articulo', 'cincuenta', 'y', 'dos'])
    response(respuestas['articulo53'][0]['respuesta'], ['articulo', 'cincuenta y tres'], required_words=['articulo', 'cincuenta', 'y', 'tres'])
    response(respuestas['articulo54'][0]['respuesta'], ['articulo', 'cincuenta  y cuatro'], required_words=['articulo', 'cincuenta', 'y', 'cuatro'])
    response(respuestas['articulo55'][0]['respuesta'], ['articulo', 'cincuenta y cinco'], required_words=['articulo', 'cincuenta', 'y', 'cinco'])
    response(respuestas['articulo56'][0]['respuesta'], ['articulo', 'cincuenta y seis'], required_words=['articulo', 'cincuenta', 'y', 'seis'])
    response(respuestas['articulo57'][0]['respuesta'], ['articulo', 'cincuenta y siete'], required_words=['articulo', 'cincuenta', 'y', 'siete'])
    response(respuestas['articulo58'][0]['respuesta'], ['articulo', 'cincuenta y ocho'], required_words=['articulo', 'cincuenta', 'y', 'ocho'])
    response(respuestas['articulo59'][0]['respuesta'], ['articulo', 'cincuenta y nueve'], required_words=['articulo', 'cincuenta', 'y', 'nueve'])
    response(respuestas['articulo60'][0]['respuesta'], ['articulo', 'sesenta'], required_words=['articulo', 'sesenta'])
    response(respuestas['articulo61'][0]['respuesta'], ['articulo', 'sesenta y uno'], required_words=['articulo', 'sesenta', 'y', 'uno'])
    response(respuestas['articulo62'][0]['respuesta'], ['articulo', 'sesenta y dos'], required_words=['articulo', 'sesenta', 'y', 'dos'])
    response(respuestas['articulo63'][0]['respuesta'], ['articulo', 'sesenta y tres'], required_words=['articulo', 'sesenta', 'y', 'tres'])
    response(respuestas['articulo64'][0]['respuesta'], ['articulo', 'sesenta y cuatro'], required_words=['articulo', 'sesenta', 'y', 'cuatro'])
    response(respuestas['articulo65'][0]['respuesta'], ['articulo', 'sesenta y cinco'], required_words=['articulo', 'sesenta', 'y', 'cinco'])
    response(respuestas['articulo66'][0]['respuesta'], ['articulo', 'sesenta y seis'], required_words=['articulo', 'sesenta', 'y', 'seis'])
    response(respuestas['articulo67'][0]['respuesta'], ['articulo', 'sesenta y siete'], required_words=['articulo', 'sesenta', 'y', 'siete'])
    response(respuestas['articulo68'][0]['respuesta'], ['articulo', 'sesenta y ocho'], required_words=['articulo', 'sesenta', 'y', 'ocho'])
    response(respuestas['articulo69'][0]['respuesta'], ['articulo', 'sesenta y nueve'], required_words=['articulo', 'sesenta', 'y', 'nueve'])
    response(respuestas['articulo70'][0]['respuesta'], ['articulo', 'setenta'], required_words=['articulo', 'setenta'])

    best_match = max(highest_prob, key=highest_prob.get)
    #print(highest_prob)

    return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
    response = ['Puedes ser mas específico', 'no entendí', 'puedes repetirlo'][random.randrange(3)]
    return response
#comenzaremos creando un bucle para que el bot siempre esté a la espera de las preguntas

while True:
    class ChatApplication:
    
        def __init__(self):
            self.window = Tk()
            self._setup_main_window()
            
        def run(self):
            self.window.mainloop()
            
        def _setup_main_window(self):
            self.window.title("Chat")
            self.window.resizable(width=True, height=True)
            self.window.configure(width=1000, height=550, bg=BG_COLOR)
            
            # head label
            head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                            text="Bienvenido", font=FONT_BOLD, pady=10)
            head_label.place(relwidth=1)
            
            # tiny divider
            line = Label(self.window, width=450, bg=BG_GRAY)
            line.place(relwidth=1, rely=0.07, relheight=0.012)
            
            # text widget
            self.text_widget = Text(self.window, width=20, height=1, bg=BG_COLOR, fg=TEXT_COLOR,
                                    font=FONT, padx=3, pady=5)
            self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
            self.text_widget.configure(cursor="arrow", state=DISABLED)
            
            # scroll bar
            scrollbar = Scrollbar(self.text_widget)
            scrollbar.place(relheight=1, relx=0.974)
            scrollbar.configure(command=self.text_widget.yview)
            
            # bottom label
            bottom_label = Label(self.window, bg=BG_GRAY, height=30)
            bottom_label.place(relwidth=1, rely=0.925)
            
            # message entry box
            self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
            self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
            self.msg_entry.focus()
            self.msg_entry.bind("<Return>", self._on_enter_pressed)
            
            # send button
            send_button = Button(bottom_label, text="Enviar", font=FONT_BOLD, width=20, bg=BG_GRAY,
                                command=lambda: self._on_enter_pressed(None))
            send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
        
        def _on_enter_pressed(self, event):
            msg = self.msg_entry.get()
            self._insert_message(msg, "Usuario")
            
        def _insert_message(self, msg, sender):
            if not msg:
                return
            
            self.msg_entry.delete(0, END)
            msg1 = f" {sender}: {msg}\n\n".format(font)
            self.text_widget.configure(state=NORMAL)
            self.text_widget.insert(END, msg1)
            self.text_widget.configure(state=DISABLED)
            
            msg2 = f"{bot_name}: {get_response(msg)}\n\n"
            self.text_widget.configure(state=NORMAL)
            self.text_widget.insert(END, msg2)
            self.text_widget.configure(state=DISABLED)
            
            self.text_widget.see(END)
             
        
    if __name__ == "__main__":
        app = ChatApplication()
        app.run()



