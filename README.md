# text-generation-for-SocialMedia

## Overview

This project is a simple web application that leverages the power of transformer models to generate text specifically tailored for social media. It provides an API endpoint to generate text based on a user-provided prompt and desired maximum length. Optionally, it includes a basic web interface for easier interaction.

## Features

* **Text Generation:** Utilizes pre-trained transformer models (defaulting to GPT-2) to generate creative and contextually relevant text.
* **API Endpoint:** Offers a `/generate` endpoint that accepts POST requests with a prompt and maximum length for text generation.
* **JSON Response:** The API returns a JSON response containing the generated text or an error message.
* **Optional Web Interface:** Includes a basic HTML interface (`index.html`) for users to interact with the text generation functionality through a web browser.
* **Customizable Model:** Easily adaptable to use different text generation models from the Hugging Face Transformers library.

## Requirements

* Python 3.x
* pip (Python package installer)

**Python Libraries:**
* flask
* transformers
* torch
* snscrape

## Installation

1.  **Clone the repository (if you haven't already):**
    ```bash
    git clone <your_repository_url>
    cd text-generation-for-SocialMedia
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install the required Python libraries:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running the Application

1.  Ensure you are in the project directory and have activated the virtual environment (if used).
2.  Run the Flask application:
    ```bash
    python app.py
    ```
    This will start the development server (usually at `http://127.0.0.1:5000/`).

### Interacting via API

You can send a POST request to the `/generate` endpoint with a JSON payload containing the `prompt` and optionally `max_length`.

**Example using `curl`:**

```bash
curl -X POST -H "Content-Type: application/json" -d '{"prompt": "Social media is great for...", "max_length": 80}' [http://127.0.0.1:5000/generate](https://www.google.com/search?q=http://127.0.0.1:5000/generate)
