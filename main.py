from modules.vision import Vision
from modules.speech import Speech
from modules.nlp import NLP
from modules.memory import Memory

def main():
    print("Welcome to Persona!")
    vision = Vision()
    speech = Speech()
    nlp = NLP()
    memory = Memory()

    while True:
        print("\nOptions:")
        print("1. Face Detection")
        print("2. Exit")
        choice = input("Select an option: ")
        if choice == "1":
            vision.detect_face()
        elif choice == "2":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()