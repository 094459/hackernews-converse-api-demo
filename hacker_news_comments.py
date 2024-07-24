import json
import requests
import sys

# Check if a command-line argument is provided
if len(sys.argv) < 2:
    print("Usage: python script.py story_id")
    sys.exit(1)

# Get the story_id from the command-line argument
story_id = sys.argv[1]

# URL to fetch JSON data
url = f"https://hn.algolia.com/api/v1/search_by_date?tags=comment,story_{story_id}&hitsPerPage=900"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Load the JSON data
    data = response.json()

    # Extract the comment_text values
    comment_texts = [hit["comment_text"] for hit in data["hits"]]

    # Open a file for writing
    with open("comments.txt", "w") as file:
        # Write each comment to the file, separated by a new line
        file.write("\n".join(comment_texts))

    print("Comments written to comments.txt")
else:
    print(f"Error: {response.status_code}")
