import requests

# Define the base URL for the Rick and Morty API
base_url = "https://rickandmortyapi.com/api/"

# Function to count character appearances
def count_character_appearances(episode_data):
    character_counts = {}
    for episode in episode_data:
        for character_url in episode["characters"]:
            # Make a GET request to retrieve character data
            character_response = requests.get(character_url)
            if character_response.status_code == 200:
                character_data = character_response.json()
                character_name = character_data["name"]
                character_counts[character_name] = character_counts.get(character_name, 0) + 1
    return character_counts

# Make a GET request to the 'episode' endpoint to retrieve episode information
episode_response = requests.get(base_url + "episode")

# Check if the episode request was successful
if episode_response.status_code == 200:
    episode_data = episode_response.json()["results"]

    # Count character appearances
    character_counts = count_character_appearances(episode_data)

    # Get the top 5 characters with the most appearances
    top_characters = sorted(character_counts.items(), key=lambda x: x[1], reverse=True)[:5]

    # Print the top characters and their appearance counts
    for character, appearances in top_characters:
        print(f"{character}: {appearances} appearances in episodes")
else:
    print("Failed to retrieve episode data from the Rick and Morty API")
