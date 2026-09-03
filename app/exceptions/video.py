class InvalidYoutubeURL(Exception):
    def __init__(self, message: str = "Invalid or unsupported URL"):
        self.message = message
        super().__init__(self.message)


# Python Exception
#      ▲
#      │ inherits
#      │
# InvalidYouTubeURL
