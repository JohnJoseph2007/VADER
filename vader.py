from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class Vader:
    def __init__(self, sentence):
        self.sentence = sentence
    
    def analyze(self):
        sia = SentimentIntensityAnalyzer()
        score = sia.polarity_scores(self.sentence)
        print("Overall sentiment scores are:\n{0}".format(score))
        print("Sentence Rating (positive): ", score['pos']*100, "%")
        print("Sentence Rating (neutral): ", score['neu']*100, "%")
        print("Sentence Rating (negative): ", score['neg']*100, "%")