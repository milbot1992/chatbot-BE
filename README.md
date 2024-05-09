# AI Fitness Chatbot

## Overview
This Chatbot is an AI-driven fitness chatbot that provides personalised advice on fitness and wellness. Leveraging OpenAI's natural language processing capabilities, the Chatbot interacts with users to deliver tailored fitness recommendations. The backend is implemented using Flask.

## Project Structure
- `app.py`: The main Flask application file that defines the API endpoints and initialises the chatbot.
- `utility.py`: Contains helper functions to interact with OpenAI API and manage chat contexts.

## Frontend
You can find the frontend that visualises the chatbot here: https://millie-ellis.com/chatbot
Repo is linked in the Key Information at the bottom

## Prerequisites
- Python 3.x
- Flask
- Flask-CORS
- Flask-RESTful
- Python-dotenv
- OpenAI

## Setup and Installation
1. **Clone the Repository**:
    ```
    git clone https://github.com/milbot1992/chatbot-BE
    cd chatbot-BE
    ```

2. **Install Dependencies**:
    - Create and activate a virtual environment:
        ```
        python -m venv env
        source env/bin/activate  # On Windows use `env\Scripts\activate`
        ```
    - Install required Python packages:
        ```
        pip install -r requirements.txt
        ```

3. **Set Up Environment Variables**:
    - Create a `.env` file in the project root directory.
    - Add your OpenAI API key:
        ```
        GPT_API_KEY='Your-OpenAI-API-Key-Here'
        ```

4. **Run the Backend**:
    ```
    python app.py
    ```
    This will start the Flask server on `http://localhost:5000/`.

5. **Setup and Run the Frontend**:
    - Navigate to the `frontend` directory.
    - Install npm packages and start the React app:
        ```
        npm install
        npm start
        ```
    This will serve the frontend on `http://localhost:3000/`.

## API Endpoints
- **GET /**: Fetches the current chat context.
- **POST /**: Receives a user's message and returns the chatbot's response.

## Using the Chatbot
- Access the chat interface through the frontend served at `http://localhost:3000/`.
- Interact with the Chatbot by sending messages through the chat interface.

## Training the Chatbot
The backend uses a data management system that continually updates the training data for the Chatbot, ensuring it delivers relevant and personalised responses based on the latest fitness trends and user interactions.

## Integration
The Flask-based backend and React-based frontend are integrated to provide a responsive and interactive user experience. CORS is configured to allow seamless communication between the two.

## Contributing
Contributions are welcome! Please follow the standard fork and pull request workflow to propose changes.

## License
N/A
