'''
Create a system that processes files. 

You have handlers for text files (.txt), audio files (.mp3), and image files (.jpg). 

Each handler should perform a specific action if it recognizes the file type.
'''

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
    # ??? TODO
    def can_handle(self, request):
        return request.type == 'txt'

    def handle_request(self, request):
        if self.can_handle(request):
            print(f"Request {request} handled by TextHandler")
        else:
            super().handle_request(request)

class AudioHandler(Handler):
    # ??? TODO
     def can_handle(self, request):
        return request.type == 'mp3'
     
     def handle_request(self, request):
        if self.can_handle(request):
            print(f"Request {request} handled by AudioHandler")
        else:
            super().handle_request(request)


class ImageHandler(Handler):
    # ??? TODO
     def can_handle(self, request):
        return request.type == 'jpg'
     
     def handle_request(self, request):
        if self.can_handle(request):
            print(f"Request {request} handled by ImageHandler")
        else:
            super().handle_request(request)


class DefaultHandler(Handler):
    # ??? TODO
    """A fallback handler that catches any request passed to it."""
    def can_handle(self, request):
        return True
    
    def handle_request(self, request):
        print(f" Cannot process file. Unknown type: '{request.type}'")


        


if __name__ == "__main__":
    
    text_file = File("document.txt")
    audio_file = File("song.mp3")
    image_file = File("photo.jpg")
    video_file = File("movie.mkv")

    # 2. Build the chain by passing the successor into the constructor.
    # The chain is built "backwards" from the end to the start.
    # The order will be: text -> audio -> image -> default
    default_h = DefaultHandler()
    image_h = ImageHandler(default_h)
    audio_h = AudioHandler(image_h)
    pipeline = TextHandler(audio_h) 

    print("--- Processing Files ---")
    # 3. Process each file by calling the first handler in the chain.
    pipeline.handle_request(text_file)
    pipeline.handle_request(audio_file)
    pipeline.handle_request(image_file)
    pipeline.handle_request(video_file)

    print("\n--- Processing Complete ---")
