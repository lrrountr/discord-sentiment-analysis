#!/usr/bin/env python3
from textblob import TextBlob

def text_blob_sentiment(message):
    blob = TextBlob(message)
    sentiment = blob.sentiment
    print(f'TextBolb -> Polarity: {sentiment.polarity}, Subjectivity: {sentiment.subjectivity}')
