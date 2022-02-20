#importaciones
import re
import random
import json

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
    response(respuestas['estado'][random.randint(0,2)]['respuesta'], ['como','estas'], required_words=['como', 'estas'])
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

    best_match = max(highest_prob, key=highest_prob.get)
    #print(highest_prob)

    return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
    response = ['Puedes ser mas especifico', 'no entendi', 'puedes repetirlo'][random.randrange(3)]
    return response
#comenzaremos creando un bucle para que el bot siempre esté a la espera de las preguntas

while True:
    print("Bot: " + get_response(input('You: ')))