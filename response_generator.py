class ResponseGenerator:
    def __init__(self):
        # Define simple responses for each emotion
        self.responses = {
            'joy': [
                "I'm glad you're feeling happy! 😄",
                "Yay! That sounds great!"
            ],
            'sadness': [
                "I'm sorry to hear that. 😢",
                "I hope things get better soon."
            ],
            'anger': [
                "Take a deep breath. 😡",
                "I understand your frustration."
            ],
            'fear': [
                "It's okay to feel scared sometimes. 😨",
                "Try to stay calm. Everything will be fine."
            ],
            'surprise': [
                "Wow, that sounds surprising! 😲",
                "I didn't see that coming either!"
            ],
            'love': [
                "Aww, that's so sweet! ❤️",
                "Love is wonderful, isn't it?"
            ],
            'neutral': [
                "I see. Tell me more.",
                "Interesting!"
            ]
        }

    def generate_response(self, emotion):
        """
        Pick a response based on detected emotion.
        """
        import random
        if emotion in self.responses:
            return random.choice(self.responses[emotion])
        else:
            return "Hmm, I see. Can you tell me more?"
