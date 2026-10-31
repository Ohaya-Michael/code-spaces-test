from blobproject import corenlp


def test_search_wikipedia():
    phrases = corenlp.get_phrases("Golden State Warriors")
    assert phrases[0:3] == ['golden state', 'warriors', 'american professional basketball team']
