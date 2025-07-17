import json
from sentence_transformers import SentenceTransformer, util

# Load city descriptions
with open("city_descriptions.json") as f:
    city_descriptions = json.load(f)

cities = list(city_descriptions.keys())
descriptions = list(city_descriptions.values())

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")  # Fast, small, free

# Encode all city descriptions
city_embeddings = model.encode(descriptions, convert_to_tensor=True)

# --- City guessing function ---
def guess_city(user_input, threshold=0.4):
    query_embedding = model.encode(user_input, convert_to_tensor=True)
    similarities = util.pytorch_cos_sim(query_embedding, city_embeddings)[0]
    best_idx = similarities.argmax().item()
    best_score = similarities[best_idx].item()
    best_city = cities[best_idx]

    if best_score < threshold:
        return f"🤔 Not sure which city, but it might be in **{guess_country(best_city)}**"
    else:
        return f"🧭 My guess: **{best_city}** (confidence: {best_score:.2f})"

# Optional: map city to country
def guess_country(city):
    city_to_country = {
        "Paris": "France", "New York City": "USA", "Tokyo": "Japan", "London": "UK", "Beijing": "China",
        "Rome": "Italy", "Berlin": "Germany", "Los Angeles": "USA", "Moscow": "Russia", "Toronto": "Canada",
        "Mumbai": "India", "Istanbul": "Turkey", "Chicago": "USA", "Bangkok": "Thailand", "Barcelona": "Spain",
        "Amsterdam": "Netherlands", "Seoul": "South Korea", "Dubai": "UAE", "San Francisco": "USA", "Buenos Aires": "Argentina",
        "Mexico City": "Mexico", "Lisbon": "Portugal", "Cairo": "Egypt", "Singapore": "Singapore", "Delhi": "India",
        "Jakarta": "Indonesia", "Sydney": "Australia", "Lagos": "Nigeria", "Nairobi": "Kenya", "Hanoi": "Vietnam",
        "Copenhagen": "Denmark", "Vienna": "Austria", "Cape Town": "South Africa", "Santiago": "Chile", "Stockholm": "Sweden",
        "Kuala Lumpur": "Malaysia", "Warsaw": "Poland", "Doha": "Qatar", "Tehran": "Iran", "Budapest": "Hungary",
        "Manila": "Philippines", "Melbourne": "Australia", "Athens": "Greece", "Prague": "Czech Republic",
        "Bogotá": "Colombia", "Brussels": "Belgium", "Zurich": "Switzerland", "Tel Aviv": "Israel", "Helsinki": "Finland", "Oslo": "Norway"
    }
    return city_to_country.get(city, "somewhere")

# Example usage
if __name__ == "__main__":
    while True:
        query = input("\nDescribe a city: ")
        if query.strip().lower() in ["q", "quit", "exit"]:
            break
        print(guess_city(query))
