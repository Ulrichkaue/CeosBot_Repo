# -*- coding: utf-8 -*-
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import numpy as np
import pandas as pd
from os.path import exists
from rasa_sdk.events import AllSlotsReset

class extract_form_data(Action):

    def name(self) -> Text:
        return "action_extract_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        nome = tracker.get_slot("nome_usuario")
        email = tracker.get_slot("email_de_contato")
        pergunta = tracker.get_slot("pergunta_nova")

        form_slots = nome + "," + email + "," + pergunta + "\n"

        print(form_slots)
        
        path = "C:/Users/ulric/Desktop/Files/Courses/Udemy/Rasa/CeosBot-v35/PerguntasNovas.txt"
        file_exists = exists(path)

        if file_exists == False:
            names = ['Nome']
            emails = ['Email']
            quest = ['Pergunta']
            np.savetxt('PerguntasNovas.txt', [p for p in zip(names, emails, quest)], delimiter=',', fmt = '%s', encoding = 'utf8')
            f = open("PerguntasNovas.txt", "a", encoding='utf-8')
            f.write(form_slots)
            f.close()
            print("Arquivo não encontrado, portanto foi criado e teve as informações adicionadas com sucesso!")
        elif file_exists == True:
            f = open("PerguntasNovas.txt", "a", encoding='utf-8')
            f.write(form_slots)
            f.close()
            print("Informações adicionadas com sucesso!")
        else:
            print("Erro de caminho do arquivo!")
        return []


class ActionResetarSlots(Action):
    def name(self):
        return "action_resetar_slots"
    
    def run(self, dispatcher, tracker, domain):
        return [AllSlotsReset()]
    
