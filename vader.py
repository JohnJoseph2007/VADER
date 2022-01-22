from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def score(sentence):
    sia = SentimentIntensityAnalyzer()
    sentimentscore = sia.polarity_scores(sentence)

    print("Overall sentiment scores are:\n{0}".format(sentimentscore))
    print("Sentence Rating (positive): ", sentimentscore['pos']*100, "%")
    print("Sentence Rating (neutral): ", sentimentscore['neu']*100, "%")
    print("Sentence Rating (negative): ", sentimentscore['neg']*100, "%")

n = input("Enter a sentence: ")
score(n)