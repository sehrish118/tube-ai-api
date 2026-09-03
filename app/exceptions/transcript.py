class TranscriptNotAvailable(Exception): #transcript does not exist/isn't available
    def __init__(self,message:str="Transcript is not available for this video."):
        self.message = message
        super().__init__(message)


class TranscriptFetchError(Exception): #something went wrong while fetching transcript

    def __init__(self,message:str = "Failed to fetch the video transcript."):
        self.message = message
        super().__init__(message)


