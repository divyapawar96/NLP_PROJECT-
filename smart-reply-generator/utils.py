import spacy
import re

def load_nlp_model():
    """Load the Spacy model, downloading if not present."""
    try:
        return spacy.load("en_core_web_sm")
    except OSError:
        print("Downloading spaCy model 'en_core_web_sm'...")
        from spacy.cli import download
        download("en_core_web_sm")
        return spacy.load("en_core_web_sm")

nlp = load_nlp_model()

def preprocess_text(text):
    """
    Preprocess user message by lowercasing, removing extra characters,
    tokenizing, and finding the lemmas to match with the intent models.
    """
    text = str(text).lower().strip()
    
    # Remove punctuation & special characters
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    
    # Pass text through spaCy NLP pipeline
    doc = nlp(text)
    
    tokens = []
    for token in doc:
        # Ignore stop words and punctuation and append the basic root word (lemma)
        if not token.is_stop and not token.is_punct and token.text.strip():
            tokens.append(token.lemma_)
            
    return " ".join(tokens)
