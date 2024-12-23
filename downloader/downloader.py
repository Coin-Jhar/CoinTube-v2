import logging
import os
import urllib.error
from yt_dlp import YoutubeDL
from downloader.format_selector import get_format_selector
from downloader.progress import progress_hook


def download_video(url: str, output_dir: str, quality: str, format: str, is_playlist: bool, download_subs: bool, playlist_options: dict):
    """Downloads the YouTube video/playlist with the specified quality and format."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    ydl_opts = {
        'noplaylist': not is_playlist,  # Disable noplaylist if it's a playlist
        'nocheckcertificate': True,
        'format': get_format_selector(quality, format),
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'progress_hooks': [progress_hook],
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'quiet': True,  # Suppress unnecessary terminal output
        'no_warnings': True,  # Suppress warnings
        'logtostderr': False,  # Disable error logging to stderr
        'writesubtitles': download_subs,  # Add the option to download subtitles
        'sub_lang': 'en',  # You can make this user-configurable later
        'sub_format': 'srt'  # You can make this user-configurable later
    }

    # Add playlist options if provided
    ydl_opts.update(playlist_options)

    try:
        with YoutubeDL(ydl_opts) as ytdl:
            ytdl.download([url])

    except urllib.error.URLError as e:
        logging.error(f"Network error: {e}")
        print(f"Network error: {e}. Please check your internet connection.")
    except yt_dlp.utils.DownloadError as e:
        logging.error(f"Download error: {e}")
        print(f"Download error: {e}. Please check the URL or try again later.")
    except yt_dlp.utils.PlaylistDownloadError as e:  # Handle playlist errors
        logging.error(f"Playlist download error: {e}")
        print(f"Playlist download error: {e}. Please check the playlist URL and video indices.")
    except FileNotFoundError as e:
        logging.error(f"File error: {e}")
        print(f"File error: {e}. Please check the output directory.")
    except Exception as e:
        logging.exception(f"An unexpected error occurred: {e}")
        print(f"An unexpected error occurred: {e}")
