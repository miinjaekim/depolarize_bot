import os
import telebot
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)


# Load the GODEL model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("microsoft/GODEL-v1_1-large-seq2seq")
model = AutoModelForSeq2SeqLM.from_pretrained("microsoft/GODEL-v1_1-large-seq2seq")

# Store user data
user_data = {}


# Function to generate a response using GODEL
def generate_response(instruction, knowledge, dialog):
    if knowledge:
        knowledge = "[KNOWLEDGE] " + knowledge
    dialog_context = " EOS ".join(dialog)
    prompt = f"{instruction} [CONTEXT] {dialog_context} {knowledge}"

    input_ids = tokenizer(prompt, return_tensors="pt").input_ids
    outputs = model.generate(
        input_ids, max_length=128, min_length=8, top_p=0.9, do_sample=True
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response


# Start message asking for a topic and stance
@bot.message_handler(commands=["start", "hello"])
def send_welcome(message):
    bot.reply_to(
        message,
        "Hello! I'm a bot that will practice having a polarizing conversation with you. Please provide a topic and your stance.",
    )
    # Register the next step to capture the user's response
    bot.register_next_step_handler(message, capture_topic_and_stance)


# Update model instructions with this message
# Function to capture the user's topic and stance
def capture_topic_and_stance(message):
    user_id = message.from_user.id
    user_input = message.text

    # Store user's topic and stance in user_data dictionary
    user_data[user_id] = {
        "instruction": f"Instruction: Have a polarizing conversation with the user. The user chose this topic and stance: '{user_input}'. Take an opposing stance.",
        "dialog": [],
    }

    # Reply to confirm the topic and stance and ask for the first argument or message
    bot.reply_to(
        message,
        "Got it! Let's start the conversation. Please share your first argument or question.",
    )

    # Register the next step to continue the conversation
    bot.register_next_step_handler(message, handle_conversation)


# Function to handle conversation with GODEL
def handle_conversation(message):
    user_id = message.from_user.id
    user_input = message.text

    # Retrieve user data (instruction and dialog)
    instruction = user_data[user_id]["instruction"]
    dialog = user_data[user_id]["dialog"]

    # Append user message to dialog
    dialog.append(user_input)

    # Generate response with GODEL
    response = generate_response(instruction, "", dialog)

    # Send GODEL's response back to the user
    bot.reply_to(message, response)

    # Append bot response to dialog for context
    dialog.append(response)

    # Register next step to keep the conversation going
    bot.register_next_step_handler(message, handle_conversation)


# Run the bot

# Run infinite loop to build conversation


# End conversation and provide feedback on the conversation

bot.infinity_polling()
