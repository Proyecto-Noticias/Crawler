# Imports the Google Cloud client library
from google.cloud import language_v1


def analyze_body(text):
    # Instantiates a client
    client = language_v1.LanguageServiceClient()

    # The text to analyze
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment

    return sentiment.score, sentiment.magnitude