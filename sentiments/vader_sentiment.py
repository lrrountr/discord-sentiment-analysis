#!/usr/bin/env python3
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize the VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

def vader_sentiment(message):
    scores = analyzer.polarity_scores(message)
    print(f'VaderSentiment -> {scores}')