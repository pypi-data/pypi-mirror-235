import subprocess
import json
import os


def convert_rich_text_to_markdown(rich_text):
    # Get the directory of the current Python script
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to your Node.js file
    file_path = os.path.join(current_directory, "adapter.bundle.js")

    # Convert rich_text to JSON
    json_rich_text = json.dumps(rich_text)

    try:
        # Execute Node.js script and capture output
        result = subprocess.run(
            ["node", file_path, json_rich_text],
            capture_output=True,
            check=True,
            text=True,  # Automatically decode bytes to text
        )

        # No need to decode if you use text=True
        markdown = result.stdout
        return markdown

    except subprocess.CalledProcessError as e:
        print(f"Command failed with error {e.returncode}")
        print(f"Standard Error: {e.stderr}")
