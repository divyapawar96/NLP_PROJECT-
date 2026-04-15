import json
import os
from utils import preprocess_text

class IntentClassifier:
    def __init__(self, responses_file="responses.json"):
        # Detect absolute filesystem path for safe loading
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        self.responses_path = os.path.join(self.base_path, responses_file)
        
        # Load the responses map
        self.intents = self.load_responses()
        
        # Rule-based intent keyword dictionary using lemmatized terms
        self.keywords = {
            "greeting": ["hello", "hi", "hey", "morning", "evening", "greet"],
            "meeting_request": ["meet", "meeting", "schedule", "call", "zoom", "appointment", "discuss", "book"],
            "question": ["what", "how", "why", "when", "where", "can", "help", "question", "wonder"],
            "apology": ["sorry", "apology", "apologize", "bad", "mistake", "fault"],
            "gratitude": ["thank", "thanks", "appreciate", "grateful"],
            "farewell": ["bye", "goodbye", "cy", "see", "later", "leave"]
        }
        
    def load_responses(self):
        """Load JSON containing mapping of intent to a list of suggestions."""
        with open(self.responses_path, "r", encoding="utf-8") as file:
            return json.load(file)
            
    def detect_intent(self, text):
        """
        Detect the user's intent by preprocessing text and matching keywords.
        Returns highest matching intent, and confidence score.
        """
        cleaned_text = preprocess_text(text)
        words = set(cleaned_text.split())
        
        intent_scores = {intent: 0 for intent in self.keywords}
        
        # Determine keyword overlap
        for intent, kwords in self.keywords.items():
            overlap = len(words.intersection(set(kwords)))
            intent_scores[intent] = overlap
            
        best_intent = max(intent_scores, key=intent_scores.get)
        max_score = intent_scores[best_intent]
        total_score = sum(intent_scores.values())
        
        # Base fallback if no key intents found
        if max_score == 0:
            return "unknown", 0.0
            
        # Optional basic probability rating based on word overlap metric
        confidence = round(max_score / total_score, 2)
        return best_intent, confidence
        
    def get_replies(self, intent):
        """Fetch 3 smart replies mapped to a given intent."""
        # Fallback to unknown if intent not found in json
        replies = self.intents.get(intent, self.intents.get("unknown"))
        return replies[:3]
