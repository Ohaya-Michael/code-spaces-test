import wikipedia
from textblob import TextBlob


def search_wikipedia(name):
    """ Search wikipedia """
    print(f"Searching for {name}")

    return wikipedia.search(name)


def sumarize_wikipedia(name):
    """ Summarize Wikipedia """
    print(f"Getting Summary for {name}")
    return wikipedia.summary(name)


def get_blob(text):
    """Use blob to get insights """
    print(f"")
    blob = TextBlob(text)
    return blob


def get_phrases(name):
    """Get the phrases from wikepedia """

    text = sumarize_wikipedia(name)
    blob = get_blob(text)
    phrases = blob.noun_phrases
    return phrases

