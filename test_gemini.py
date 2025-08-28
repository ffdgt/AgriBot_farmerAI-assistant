import os
import google.generativeai as genai

# Configure API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model instance
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-latest",
    system_instruction="You are AgriBot, a helpful assistant for farmers."
)

# Start a chat session
chat_session = model.start_chat(history=[])

# Send a user message
response = chat_session.send_message("Tell me about paddy crop.")

# Print the response
print(response.text)
