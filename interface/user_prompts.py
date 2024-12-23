import os
from validation.url_validation import valid_youtube_link

def get_user_input(use_template=False, template=None):
    """Gets the YouTube URL, output directory, quality, and format from the user."""
    url = input("Enter the YouTube video/playlist URL: ").strip()

    while not valid_youtube_link(url):
        print("Invalid YouTube URL. Please try again.")
        url = input("Enter the YouTube video/playlist URL: ").strip()

    default_dir = "downloads"
    os.makedirs(default_dir, exist_ok=True)

    output_dir = (
        template.get("output_dir", default_dir)
        if use_template and template
        else input(f"Enter the output directory (default: {default_dir}): ").strip() or default_dir
    )

    # Other user input handling code...
