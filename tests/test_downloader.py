import unittest
from downloader.downloader import download_video

class TestDownloader(unittest.TestCase):
    def test_download_video(self):
        # Test with mock data (use actual mock libraries like unittest.mock for real tests)
        video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # example URL
        output_dir = "test_downloads"
        quality = "best"
        format = "mp4"
        is_playlist = False
        download_subs = False
        playlist_options = {}

        try:
            download_video(video_url, output_dir, quality, format, is_playlist, download_subs, playlist_options)
            self.assertTrue(True)  # If no exception is raised, the test passes
        except Exception as e:
            self.fail(f"Download failed with error: {e}")

if __name__ == "__main__":
    unittest.main()
