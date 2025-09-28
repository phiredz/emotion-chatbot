from transformers import pipeline

class EmotionModel:
    def __init__(self):
        # Load a transformer model for emotion/sentiment detection
        self.model = pipeline("sentiment-analysis", model="j-hartmann/emotion-english-distilroberta-base")

    def predict_emotion(self, text):
        """
        Predict emotion of the input text.
        Returns: emotion label (e.g., 'joy', 'sadness', 'anger', etc.)
        """
        result = self.model(text)
        return result[0]['label']
