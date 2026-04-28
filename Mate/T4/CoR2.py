from abc import ABC, abstractmethod

class File:
    def __init__(self, name):
        self.name = name
        self.type = name.split('.')[-1]

class Handler(ABC):
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, request):
        if self.successor:
            self.successor.handle_request(request)

    @abstractmethod
    def can_handle(self, request):
        pass

class TextHandler(Handler):
    # need a can handle
    def can_handle(self, request):
        return isinstance(request, File) and request.type == "txt"

    def handle_request(self, request):
        if self.can_handle(request):
            print(f"Reading text file {request.name}")
        else:
            super().handle_request(request)

# class AudioHandler(Handler):
#     ??? TODO

# class ImageHandler(Handler):
#     ??? TODO

class DefaultHandler(Handler):
    def can_handle(self, request):
        return True

    def handle_request(self, request):
        print(f"Cannot process file of unknown type {request.type}")
        

if __name__ == "__main__":
    
    text_file = File("document.txt")
    audio_file = File("song.mp3")
    image_file = File("photo.jpg")
    video_file = File("movie.mkv")

    # create starting from the last one to be called
    # Default Handler
    default_h = DefaultHandler()
    image_h = ImageHandler(default_h)
    audio_h = AudioHandler(image_h)
    pipeline = TextHandler(audio_h)