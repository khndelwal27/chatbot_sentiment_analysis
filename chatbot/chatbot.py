from .sentiment_analyzer import SentimentAnalyzer

class ChatBot:
    def __init__(self):
        self.analyzer = SentimentAnalyzer()

    def reply(self, message):
        sentiment = self.analyzer.analyze(message)
        
        if sentiment == "Negative":
            response = "I'm sorry you felt that way. I'll make sure your concern is addressed."
        elif sentiment == "Positive":
            response = "I'm glad to hear that! Let me know if you need anything else."
        else:
            response = "I understand. Let me know how I can assist further."

        return response, sentiment
