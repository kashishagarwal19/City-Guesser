# City-Guesser

City Guesser from Text Descriptions

This is a simple NLP project that guesses a city based on your natural language description. It uses Wikipedia content and semantic similarity via sentence-transformers to find the best match.

#Features

- Input: A short text description (e.g. "a city with canals and tulips"*)
- Output: Best-matching city (e.g. *Amsterdam*)
- Lightweight (no image models or large data)
- Based on open-source tools and works offline

##Setup Instructions

### 1. Clone the repository
git clone https://github.com/yourusername/city-guesser.git
cd city-guesser

### 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate 

### 3. Install the dependencies
pip install -r requirements.txt

### 4. Create the city descriptions
python generate_city_descriptions.py

### 5. Run the guesser
python city_guesser.py
