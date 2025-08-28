
# AgriBot 🌾🤖

This repository contains the complete source code, assets, and implementation of **AgriBot**, an AI-powered assistant for farmers. AgriBot provides real-time weather updates, latest agriculture news, farming tips, and resource links to help farmers make informed decisions quickly and effectively.

---

## 📚 Table of Contents
- Project Overview
- 🎥 Demo Video
- Getting Started
- APIs
- Usage
- Technologies used
- Requirements
- Contributing
- License


---

## Project Overview

AgriBot is a smart web application designed to assist farmers. By leveraging AI (Google Gemini AI) and external APIs (OpenWeatherMap, NewsAPI), it provides:

- **AI Chat Assistant**: Answer farming-related questions in under 100 words.
- **Weather Updates**: Real-time weather conditions with dynamic background animations.
- **Agriculture News**: Latest news articles about agriculture.
- **Farming Tips & Facts**: Useful insights and guidance for better crop management.
- **Resources & Schemes**: Access to government and agricultural organization websites, including PMFBY, PKVY, and Soil Health Card.

The project is built with **Flask** for the backend and **HTML, Tailwind CSS, and JavaScript** for the frontend.

---
🎥 **Demo Video**  
[Watch the Demo Video](https://drive.google.com/file/d/1i_YmzdvRPKm8faCIoioh5CLwuYBNVJ9e/view?usp=drivesdk)



---

## Getting Started

### Prerequisites
- Python 3.10+
- pip
- Git
- Virtual Environment (recommended)

### Installation Steps
1. Clone the repository:
```bash
git clone https://github.com/PoojaReddy44/AgriBot.git
cd AgriBot

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
3. Install required packages

If you haven’t already, install Flask, requests, python-dotenv, and google-generativeai:
```bash
pip install flask requests python-dotenv google-generativeai
  ```
4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Create a `.env` file and add your API keys:

   ```
   GEMINI_API_KEY=<your-gemini-key>
   WEATHER_API_KEY=<your-openweather-key>
   NEWS_API_KEY=<your-newsapi-key>
   ```

6. Run the Flask app:

   ```bash
   python app.py
   ```

7. Open your browser and go to `http://127.0.0.1:5000/`

## APIs Used

Google Gemini AI – Provides AI chat assistant functionality.

OpenWeatherMap API – Fetches current weather based on location.

NewsAPI – Fetches latest agriculture-related news.

## Usage

Home Page: Displays rotating quotes, current weather, and quick module access.

Chat Module: AI-powered assistant answers farming questions.

News Module: Latest agriculture news and updates.

Resources Module: Government websites, schemes, and other useful links.

## Technologies Used

* **Frontend**: HTML, CSS, Tailwind CSS, JavaScript
* **Backend**: Python, Flask
* **APIs**: Google Gemini AI, OpenWeatherMap, NewsAPI


## Requirements

Before running the project, make sure the following Python packages are installed.  

Make sure your virtual environment is activated, then run:

```bash
pip install -r requirements.txt
```
Sample requirements.txt file content:
```bash
Flask==3.0.0
tensorflow==2.14.0
Pillow==10.0.0
numpy==1.24.3
```
## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## 📜 License
This project is licensed under the MIT License.

You are free to use, modify, and distribute this project with attribution.




