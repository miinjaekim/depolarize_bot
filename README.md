# Depolarize Bot

## Overview

This project is an MVP (Minimum Viable Product) and a work in progress. It was primarily developed as a learning exercise rather than a fully completed project.

The Depolarize Bot is a Telegram bot designed to help users practice conversations on various topics and receive feedback on the polarity of their language. The aim is to promote balanced discussions and reduce polarized communication.

## Features

- **Topic Selection:** Users can choose from a list of predefined topics to practice conversations.
- **Conversation Practice:** Engages users in simulated discussions on the selected topic.
- **Polarity Analysis:** Analyzes user input to detect polarized language and provides constructive feedback.

## Installation

To set up the Depolarize Bot locally, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/miinjaekim/depolarize_bot.git
   cd depolarize_bot
   ```

2. **Create a Virtual Environment (Optional but Recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **Telegram Bot Token:** Obtain a bot token by creating a new bot through the [BotFather](https://core.telegram.org/bots#botfather) on Telegram.

2. **Environment Variables:** Create a `.env` file in the project root directory and add your Telegram bot token:

   ```
   TELEGRAM_BOT_TOKEN=your_bot_token_here
   ```

   *Note: The `python-dotenv` package can be used to load environment variables from the `.env` file.*

## Usage

To run the bot:

```bash
python main.py
```

*Note: Ensure that your Telegram bot token is correctly configured before running the bot.*

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

## License

This project is not currently licensed. If you intend to use or distribute this code, please contact the repository owner for permission.

## Contact

For questions or collaboration opportunities, feel free to reach out to [Minjae Kim](https://github.com/miinjaekim).
