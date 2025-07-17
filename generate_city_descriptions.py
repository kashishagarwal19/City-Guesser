import wikipedia
import json
import time

# List of major cities
cities = [
    "Paris", "New York City", "Tokyo", "London", "Beijing", "Rome", "Berlin", "Los Angeles", "Moscow", "Toronto",
    "Mumbai", "Istanbul", "Chicago", "Bangkok", "Barcelona", "Amsterdam", "Seoul", "Dubai", "San Francisco", "Buenos Aires",
    "Mexico City", "Lisbon", "Cairo", "Singapore", "Delhi", "Jakarta", "Sydney", "Lagos", "Nairobi", "Hanoi",
    "Copenhagen", "Vienna", "Cape Town", "Santiago", "Stockholm", "Kuala Lumpur", "Warsaw", "Doha", "Tehran", "Budapest",
    "Manila", "Melbourne", "Athens", "Prague", "Bogotá", "Brussels", "Zurich", "Tel Aviv", "Helsinki", "Oslo"
]

city_descriptions = {}

for city in cities:
    try:
        # Search for a valid Wikipedia page title
        search_results = wikipedia.search(city)
        if not search_results:
            raise Exception("No search results")
        page_title = search_results[0]

        # Get full content from page
        content = wikipedia.page(page_title).content
        city_descriptions[city] = content

        print(f"✅ {city} -> {page_title}")
        time.sleep(0.5)  # Be polite to Wikipedia servers

    except Exception as e:
        print(f"❌ {city}: {e}")

# Save to JSON file
with open("city_descriptions.json", "w") as f:
    json.dump(city_descriptions, f, indent=2)

print("\n🎉 Done! Saved descriptions to 'city_descriptions.json'")
