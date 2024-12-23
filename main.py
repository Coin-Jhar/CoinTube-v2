import logging
from config.config_manager import load_config
from downloader.downloader import download_video
from interface.user_prompts import get_user_input
from utils.helpers import create_directory
from validation.url_validation import valid_youtube_link


def main():
    logging.basicConfig(
        filename='downloader.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    # Load the configuration file
    config = load_config("config.json")
    if config is None:
        print("Error: Unable to load or create configuration file.")
        exit(1)

    # Allow the user to select a template and input
    template = config.get("templates", {}).get("default", {})
    user_input = get_user_input(use_template=True, template=template)
    if not user_input:
        print("Error: Failed to get user input. Exiting...")
        exit(1)

    video_url, output_directory, quality, format, is_playlist, download_subs, playlist_options = user_input

    # Validate URL
    if not valid_youtube_link(video_url):
        print("Invalid YouTube URL. Exiting...")
        exit(1)

    # Ensure output directory exists
    create_directory(output_directory)

    try:
        # Download video using the specified options
        download_video(
            video_url,
            output_directory,
            quality,
            format,
            is_playlist,
            download_subs,
            playlist_options
        )
        print("Download complete! Check your output directory.")
    except Exception as e:
        logging.error(f"Failed to download video: {e}")
        print("An error occurred while downloading the video. Check the logs for details.")


if __name__ == "__main__":
    main()
