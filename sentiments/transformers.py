#!/usr/bin/env python3
from transformers import pipeline


# Load a pre-trained sentiment-analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

def transformers_sentiment(message):
    result = sentiment_pipeline(message)
    print(f"Transformer -> {result[0]['label']}, Confidence: {result[0]['score']:.2f}")