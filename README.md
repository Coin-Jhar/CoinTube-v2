# Coin Downloader

This tool allows you to download YouTube videos and playlists, manage configurations, and customize settings for video quality, format, and subtitles.

## Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/yourusername/coin_downloader.git
cd coin_downloader
pip install -r requirements.txt

Usage

Run the main script:

python main.py

Follow the prompts to download videos and manage settings.

### Final Steps:
- **Testing**: Ensure each module works individually. You may need to mock some parts, like the actual video download in unit tests.
- **Error handling**: You might want to improve how errors are handled (e.g., retries or more user-friendly error messages).
- **Logging**: The `logging` setup in `main.py` is important to capture errors and successes, especially when the script is running in a production or long-term environment.
