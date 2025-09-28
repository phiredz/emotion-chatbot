from utils import preprocess_text
from emotion_model import EmotionModel
from response_generator import ResponseGenerator

def main():
    print("💬 Emotion-Aware Chatbot")
    print("Type 'quit' to exit.\n")

    emotion_model = EmotionModel()
    response_gen = ResponseGenerator()

    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Chatbot: Goodbye! 👋")
            break

        processed_input = preprocess_text(user_input)
        emotion = emotion_model.predict_emotion(processed_input)
        response = response_gen.generate_response(emotion)

        print(f"Chatbot ({emotion}): {response}\n")

if __name__ == "__main__":
    main()
