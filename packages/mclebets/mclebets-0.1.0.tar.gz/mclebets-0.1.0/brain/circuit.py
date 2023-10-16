from .neurons import GPT4
from .stymulus import Stymulus
import nltk
import functools
import multiprocessing
import time
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')


def analyze_neuron(neuron, stymulus):
    stymulus = Stymulus()
    data, prompt = stymulus.activate()
    output = neuron.predict(data, prompt)
    output = self.transmissers.polarity_scores(output)
    return output['compound']

class Circuit:
    def __init__(self, n):
        self.n = n
        self.neurons = [GPT4() for i in range(0,n)]
        self.transmissers = SentimentIntensityAnalyzer()

    def train_models(self, data, prompt):
        for neuron in self.neurons:
            neuron.train(data, prompt)
            return neuron 



    # def analyze(self):
  
       
    #     if __name__ == '__main__':
    #         optimistic_count = 0
    #         pool = multiprocessing.Pool(processes=4)
    #         outputs = pool.map(analyze_neuron, self.neurons)
    #         pool.close()
    #         pool.join()
       
    #         for output in outputs:
    #             optimistic_count += output
       
    #         optimism_percentage = (optimistic_count / len(self.neurons)) * 2 - 1
    #     time.sleep(30)
    #     return optimism_percentage
    
    def analyze(self, stymulus, team1, team2):
        prompt = stymulus.activate(team1, team2)
        optimistic_count = 0
        transmissers = SentimentIntensityAnalyzer()
        for neuron in self.neurons:
            output = neuron.predict(prompt)
            output = transmissers.polarity_scores(output)
            output = output['compound']
            optimistic_count += output

        optimism_percentage = optimistic_count / len(self.neurons)
        return optimism_percentage