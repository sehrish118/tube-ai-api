from urllib.parse import urlparse, parse_qs


def extract_video_id(youtube_url: str) -> str | None:
    parsed_url = urlparse(youtube_url)

    # https://youtu.be/VIDEO_ID
    if parsed_url.netloc in ("youtu.be", "www.youtu.be"):
        video_id = parsed_url.path.strip("/")
        return video_id or None

    # Youtube URLs
    if parsed_url.netloc in ("youtube.com", "www.youtube.com", "m.youtube.com"):
        # https://youtube.com/watch?v=VIDEO_ID
        if parsed_url.path == "/watch":
            query_params = parse_qs(parsed_url.query)  # parse query parameters
            return query_params.get("v", [None])[0]

        # https://youtube.com/shorts/VIDEO_ID
        if parsed_url.path.startswith("/shorts/"):
            parts = parsed_url.path.split("/")
            return parts[2] if len(parts) > 2 else None

    return None
