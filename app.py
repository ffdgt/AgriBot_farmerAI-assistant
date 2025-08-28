import os
import requests
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# --- API Key Configuration ---
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# Configure Gemini client
genai.configure(api_key=GEMINI_API_KEY)

# --- AI Model Configuration ---
system_instruction = (
    "You are AgriBot, a helpful AI assistant for farmers. "
    "Provide concise, direct, and practical advice. "
    "Keep your answers under 100 words unless the user explicitly asks for a detailed explanation."
)

model = genai.GenerativeModel(
    model_name='gemini-1.5-flash-latest',
    system_instruction=system_instruction
)

# --- Flask Routes ---
@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/app')
def app_page():
    module = request.args.get('module', 'chat')
    return render_template('app.html', module=module)

@app.route('/chatpage')
def chatpage():
    return render_template('chatpage.html')

# --- News Routes ---
@app.route('/news.html')
@app.route('/newspage')
def news_page():
    articles = []
    if NEWS_API_KEY:
        try:
            news_api_url = f"https://newsapi.org/v2/everything?q=agriculture&language=en&sortBy=publishedAt&apiKey={NEWS_API_KEY}"
            response = requests.get(news_api_url)
            response.raise_for_status()
            news_articles = response.json().get('articles', [])
            articles = [
                {"title": a.get("title"), "url": a.get("url"), "source": a.get("source", {}).get("name")}
                for a in news_articles[:10]
            ]
        except Exception as e:
            print(f"Error fetching news data: {e}")
    return render_template('news.html', articles=articles)

# --- Resources Route ---
@app.route('/resourcespage')
def resources_page():
    resources = {
        "websites": [
            {"name": "ICAR", "url": "https://www.icar.org.in/"},
            {"name": "Ministry of Agriculture", "url": "https://agricoop.nic.in/"},
            {"name": "NABARD", "url": "https://www.nabard.org/"}
        ],
        "schemes": [
            {"name": "PMFBY", "description": "Comprehensive crop insurance."},
            {"name": "PKVY", "description": "Promotes organic farming."},
            {"name": "Soil Health Card", "description": "Provides soil nutrient info."}
        ]
    }
    return render_template('resources.html', resources=resources)

@app.route('/resources')
def resources_page_route():
    """Renders the Resources page."""
    return render_template('resources.html')
@app.route('/facts')
@app.route('/facts.html')
def facts_page():
    """Renders the Facts & Info page."""
    return render_template('facts.html')



# --- Chat API Endpoint ---
@app.route('/chat', methods=['POST'])
def chat():
    user_text = request.form.get('text')
    if not user_text:
        return jsonify({'text': "Please enter a message."})

    try:
        chat_session = model.start_chat(history=[])
        response = chat_session.send_message(user_text)
        return jsonify({'text': response.text})
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        return jsonify({'text': "Sorry, I can't connect to the AI service right now."})

# --- Weather Endpoint ---
@app.route('/weather', methods=['GET'])
def get_weather():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    if not WEATHER_API_KEY:
        return jsonify({'error': 'Weather API key not configured.'}), 500
    try:
        if lat and lon:
            weather_api_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}&units=metric"
        else:
            location = request.args.get('location', 'Hyderabad')
            weather_api_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={WEATHER_API_KEY}&units=metric"
        response = requests.get(weather_api_url)
        response.raise_for_status()
        data = response.json()
        simplified_weather = {
            "location": data.get("name"),
            "temperature": data.get("main", {}).get("temp"),
            "conditions": data.get("weather", [{}])[0].get("description"),
            "humidity": data.get("main", {}).get("humidity"),
        }
        return jsonify(simplified_weather)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return jsonify({'error': 'Could not retrieve weather data.'}), 500

# --- News API Endpoint ---
@app.route('/news', methods=['GET'])
def get_news():
    if not NEWS_API_KEY:
        return jsonify({'error': 'News API key not configured.'}), 500
    try:
        news_api_url = f"https://newsapi.org/v2/everything?q=agriculture&language=en&sortBy=publishedAt&apiKey={NEWS_API_KEY}"
        response = requests.get(news_api_url)
        response.raise_for_status()
        news_articles = response.json().get('articles', [])
        simplified_articles = [
            {"title": a.get("title"), "url": a.get("url"), "source": a.get("source", {}).get("name")}
            for a in news_articles[:10]
        ]
        return jsonify({'articles': simplified_articles})
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news data: {e}")
        return jsonify({'error': 'Could not retrieve news data.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
