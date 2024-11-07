import os
import telebot
import requests

BOT_TOKEN = os.environ.get('BOT_TOKEN')
HUGGINGFACE_API_KEY = os.environ.get('HUGGINGFACE_API_KEY')

bot = telebot.TeleBot(BOT_TOKEN)

# Set up the Hugging Face API URL and headers
API_URL = (
    "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"
)
headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}


def query_huggingface(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


# Step 1: Set up instructions
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    instructions = (
        """Welcome to the conversation practice bot!
        Here’s how you can use it:\n
        1. Type a controversial topic or question to start a conversation.\n
        2. I’ll respond with an opposing perspective.\n
        3. After the conversation,
        I'll provide feedback on how the conversation went."""
    )
    bot.reply_to(message, instructions)


# Step 2: Conversation handling with an opposing viewpoint
@bot.message_handler(func=lambda msg: True)
def handle_conversation(message):
    # Define the payload for the Hugging Face API
    prompt = (
        f"Respond as someone with an opposing viewpoint on:\n"
        f"User: {message.text}\nAI:"
    )
    payload = {
        "inputs": prompt,
    }

    # Get response from Hugging Face's DialoGPT
    try:
        response = query_huggingface(payload)
        bot_reply = response.get("generated_text",
                                 "I'm sorry, I couldn't generate a response.")
    except Exception:
        bot_reply = """Error connecting to the language model.
        Please try again later."""

    bot.reply_to(message, bot_reply)


# Step 3: Feedback generation (simplified)
@bot.message_handler(commands=['feedback'])
def provide_feedback(message):
    feedback_text = (
        "Here's some feedback:\n"
        "1. Keep the tone respectful.\n"
        "2. Ask clarifying questions to understand the opposing view better.\n"
        "3. Avoid personal attacks and focus on discussing ideas."
    )
    bot.reply_to(message, feedback_text)


bot.infinity_polling()
