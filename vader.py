from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class Vader:
    def __init__(self, sentence):
        self.sentence = sentence
    
    positive = 0
    negative = 0
    neutral = 0
    
    def analyze(self):
        sia = SentimentIntensityAnalyzer()
        score = sia.polarity_scores(self.sentence)
        # print("Overall sentiment scores are:\n{0}".format(score))
        # print("Sentence Rating (positive): ", score['pos']*100, "%")
        # print("Sentence Rating (neutral): ", score['neu']*100, "%")
        # print("Sentence Rating (negative): ", score['neg']*100, "%")
        self.positive = score['pos']
        self.negative = score['neg']
        self.neutral = score['neu']