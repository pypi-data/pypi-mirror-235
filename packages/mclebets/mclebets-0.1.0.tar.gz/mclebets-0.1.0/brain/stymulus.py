import requests
from bs4 import BeautifulSoup
import logging

class Scrapper:
    def __init__(self):
        pass

    def scrape(self, url, limit=8192):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.text
        
        return text[:8192]

class StatisticsScrapper:
    def __init__(self):
        pass

class Stymulus:
    def __init__(self):
        pass
        

    def activate(self, team1, team2):
        ids = {'Benfica': 211, 'FC Porto': 212, 'Moreirense': 215, 'Portimonense': 216, 'SC Braga': 217, 'Boavista': 222, 'Chaves': 223,
                'Guimaraes': 224, 'Rio Ave': 226, 'Sporting CP': 228, 'Estoril': 230, 'Farense': 231, 'Arouca': 240, 'Famalicao': 242, 'GIL Vicente': 762, 'Vizela': 810, 'Casa Pia': 4716, 'Estrela': 15130}
        # scrapper = Scrapper()
        # url = "https://www.zerozero.pt/match_preview.php?id=9025419"
        # analysis = scrapper.scrape(url)

        statistics = ""
        headers = {
            "X-RapidAPI-Key": "b6eedd67cfmsh9c81d913114956ap1b47cbjsn778004eabf84",
            "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
        }

        # url = "https://api-football-v1.p.rapidapi.com/v3/leagues/"
        # response = requests.get(url, headers=headers, params={"country": "Portugal"})
        # league_id = response.json()["response"][0]["league"]['id']

        # url = "https://api-football-v1.p.rapidapi.com/v3/teams/"
        # response = requests.get(url, headers=headers, params={"league": league_id, "season":2023})
        # print([f"{team['team']['name']}: {team['team']['id']}" for team in response.json()["response"]])
       
        url = "https://api-football-v1.p.rapidapi.com/v3/fixtures/headtohead"
        querystring = {"h2h":f"{ids[team1]}-{ids[team2]}", "season":2023}
        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()['response'][0]
        
        # team1 = data['teams']['home']['id']
        # team1_name = data['teams']['home']['name']
        # team2 =data['teams']['away']['id']
  
        url = "https://api-football-v1.p.rapidapi.com/v3/predictions"
        params = {
            'fixture': f"{data['fixture']['id']}",  # Modify this to match the correct format
        }

        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code == 200:
            data = response.json()['response'][0]
        
            predictions = data['predictions']

            stats = data['teams']
            logging.info(f'Predictions for {team1} vs {team2}:')
            for prediction in list(predictions.keys()):
                statistics += prediction
                prediction = predictions[prediction]
                if prediction is dict:
                    for item, value in prediction.items():
                        statistics += f"{item}: {value}"
                else:
                    statistics += str(prediction)
            for stat in stats:
                continue

        else:
            logging.warning(f'Failed to retrieve data: {response.status_code}')


        prompt = f'''Based solely on this statistics: {statistics}, 
        and taking nothing else into account,
        how likely do you think is {team1} or {team2} winning the match?
        Answer me in a friendly tone, as if we are buddies.'''
        logging.info(statistics)
        return prompt
