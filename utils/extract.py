from keybert import KeyBERT
from nltk.stem import PorterStemmer

kw_model = KeyBERT()

# Extract the core research topic from a simplified user query to improve paper search relevance
def extract_core_term(sentence):
    keywords = kw_model.extract_keywords(sentence, top_n=3)

    if not keywords:
        return None

    stemmer = PorterStemmer()
    seen_stems = set()
    result = []

    for word, _ in keywords:
        stemmed = stemmer.stem(word)
        if stemmed not in seen_stems:
            seen_stems.add(stemmed)
            result.append(word)

    return " / ".join(result)