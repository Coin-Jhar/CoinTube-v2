def progress_hook(d):
    """Progress hook for yt-dlp to display detailed download status."""
    if d['status'] == 'downloading':
        total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate')
        downloaded_bytes = d.get('downloaded_bytes')
        speed = d.get('_speed_str')
        eta = d.get('_eta_str')

        progress = f"\rDownloading... {d.get('_percent_str', '0%')}"
        if total_bytes:
            progress += f" of {total_bytes_str(total_bytes)}"
        if speed:
            progress += f" at {speed}"
        if eta:
            progress += f" ETA {eta}"

        print(progress, end="")

    elif d['status'] == 'finished':
        print("\nDownload complete!")

    elif d['status'] == 'error':
        print("\nDownload failed!")

def total_bytes_str(total_bytes):
    """Converts bytes to a human-readable string."""
    if total_bytes < 1024:
        return f"{total_bytes}B"
    elif total_bytes < 1024 * 1024:
        return f"{total_bytes / 1024:.2f}KB"
    elif total_bytes < 1024 * 1024 * 1024:
        return f"{total_bytes / (1024 * 1024):.2f}MB"
    else:
        return f"{total_bytes / (1024 * 1024 * 1024):.2f}GB"
