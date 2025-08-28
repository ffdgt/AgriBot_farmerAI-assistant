

````markdown
# AgriBot 🌾🤖

AgriBot is a smart AI-powered web application designed for farmers, providing real-time agricultural assistance. It delivers weather updates, latest agriculture news, farming tips, and resources to help farmers make informed decisions.

## Features

- AI Chat Assistant: Ask AgriBot practical farming questions and get concise guidance.
- Weather Updates: Real-time weather information with location-based conditions.
- Agriculture News: Latest news articles from trusted sources about agriculture.
- Farming Facts & Tips: Useful insights and tips for better crop management.
- Resources: Access to government and agricultural organization websites, and schemes like PMFBY, PKVY, Soil Health Card.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/PoojaReddy44/AgriBot.git
   cd AgriBot
````

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Mac/Linux
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file and add your API keys:

   ```
   GEMINI_API_KEY=<your-gemini-key>
   WEATHER_API_KEY=<your-openweather-key>
   NEWS_API_KEY=<your-newsapi-key>
   ```

5. Run the Flask app:

   ```bash
   python app.py
   ```

6. Open your browser and go to `http://127.0.0.1:5000/`

## Technologies Used

* **Frontend**: HTML, CSS, Tailwind CSS, JavaScript
* **Backend**: Python, Flask
* **APIs**: Google Gemini AI, OpenWeatherMap, NewsAPI

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.


