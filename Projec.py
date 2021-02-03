# import json, requests, sys
# 
# 
# 
# url = "https://na1.api.riotgames.com/lol/league/v3/challengerleagues/by-queue/RANKED_SOLO_5x5?api_key=RGAPI-01dd190a-612c-4c89-801d-ffc2ae0d9114"
# response = requests.get(url)
# response.raise_for_status()
# 
# Data = json.loads(response.text)
# 
# print(Data)


from ChampionList import ChampList
import random


def QuestionAnswer(ChampionList, qType, answer):
    if answer == "yes":
        for Champ in ChampionList:
            Champ.Score += getattr(Champ, qType)
    else:
        for Champ in ChampionList:
            Champ.Score += 3 - getattr(Champ, qType)
            

def MeleeAnswer(ChampionList, answer):
    if answer == "melee":
        for Champ in ChampionList:
            if Champ.Melee == True:
                Champ.Score += 100
    else:
        for Champ in ChampionList:
            if Champ.Melee == False:
                Champ.Score += 100
                
def DamageTypeAnswer(ChampionList, answer):
    if answer == "easy":
        for Champ in ChampionList:
            if Champ.Difficulty == 1:
                Champ.Score += 100
    elif answer == "medium":
        for Champ in ChampionList:
            if Champ.Difficulty == 2:
                Champ.Score += 100
    elif answer == "hard":
        for Champ in ChampionList:
            if Champ.Difficulty == 3:
                Champ.Score += 100
                

        # Name, Melee, Damage, Toughness, Control, Mobility, Utility, Difficulty
        
        
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

while (True):
    QuestionType = ["Damage", "Utility", "Mobility", "Control", "Toughness"]
    random.shuffle(QuestionType)
    for question in QuestionType:
        if question == "Damage":
            QuestionAnswer(ChampList, question, input("Do you like dealing massive damage?\n"))
        elif question == "Utility":
            QuestionAnswer(ChampList, question, input("Do you like supporting the team?\n"))
        elif question == "Mobility":
            QuestionAnswer(ChampList, question, input("Do you like being mobile?\n"))
        elif question == "Control":
            QuestionAnswer(ChampList, question, input("Do you like being able to disrupt fights?\n"))
        elif question == "Toughness":
            QuestionAnswer(ChampList, question, input("Do you like being the frontline in fights?\n"))
            
    MeleeAnswer(ChampList, input("Do you like being melee or ranged?\n"))
    DamageTypeAnswer(ChampList, input("Level of difficulty?\n"))
            
    newList = sorted(ChampList, key=lambda x: x.Score, reverse=True)
    for Champ in range(15):
        print(newList[Champ].Name, "  ", newList[Champ].Score)
    break
    

