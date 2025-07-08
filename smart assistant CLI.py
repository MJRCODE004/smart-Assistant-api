import requests

def get_pokemon_info(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"\n🔴 Pokémon: {data['name'].title()}")
        print(f"Height: {data['height']}")
        print(f"Weight: {data['weight']}")
        print("Abilities:", ", ".join([a['ability']['name'] for a in data['abilities']]))
    else:
        print("Pokémon not found!")

def get_cat_fact():
    url = "https://catfact.ninja/fact"
    response = requests.get(url)
    print(f"\n🐱 Cat Fact: {response.json()['fact']}")

def get_advice():
    url = "https://api.adviceslip.com/advice"
    response = requests.get(url)
    print(f"\n💡 Advice: {response.json()['slip']['advice']}")

def predict_age(name):
    url = f"https://api.agify.io/?name={name}"
    response = requests.get(url)
    print(f"\n🎂 Predicted age for {name.title()}: {response.json()['age']}")

def get_activity():
    url = "https://www.boredapi.com/api/activity"
    response = requests.get(url)
    print(f"\n🕹️ Try this: {response.json()['activity']}")

# --- Menu ---
def main():
    while True:
        print("\n🧠 Smart Assistant")
        print("1. Get Pokémon info")
        print("2. Get a cat fact")
        print("3. Get random advice")
        print("4. Predict age by name")
        print("5. Suggest a fun activity")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter Pokémon name: ")
            get_pokemon_info(name)
        elif choice == '2':
            get_cat_fact()
        elif choice == '3':
            get_advice()
        elif choice == '4':
            name = input("Enter your name: ")
            predict_age(name)
        elif choice == '5':
            get_activity()
        elif choice == '6':
            print("👋 Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

