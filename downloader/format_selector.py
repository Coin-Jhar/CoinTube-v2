def get_format_selector(quality: str, format: str) -> str:
    """Returns the yt-dlp format selector string based on quality and format."""
    if quality == "best":
        quality_selector = "bv*+ba/b"
    elif quality == "high":
        quality_selector = "bv[height<=720]+ba/b"
    elif quality == "medium":
        quality_selector = "bv[height<=480]+ba/b"
    elif quality == "low":
        quality_selector = "bv[height<=360]+ba/b"
    else:
        quality_selector = "bv*+ba/b"  # Default to best

    if format == "mp3":
        return "ba"
    elif format in ("mp4", "webm"):
        return f"{quality_selector}[ext={format}]"
    else:
        return quality_selector  # Default to best
