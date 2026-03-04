class MediaPlayer:
    def play(self, audioType: str, fileName: str): ...
    
class AdvancedMediaPlayer:
    def playVLC(self, fileName: str):...
    def playMP4(self, fileName: str):...

class VLCPlayer(AdvancedMediaPlayer):
    def playVLC(self, filename):
        print('Playing VLC', fileName) # type: ignore
        
    def playMP4(self, filename): ...
    
class MP4Player(AdvancedMediaPlayer):
    def playVLC(self, filename): ...
    def playMP4(self, filename):
        print('playing MP4', filename)
        
class MediaAdapter(MediaPlayer):
    advancedMusicPlayer: AdvancedMediaPlayer
    def __init__(self, audioType):
        if audioType == "vlc": self.advancedMusicPlayer = VLCPlayer()
        elif audioType == "mp4": self.advancedMusicPlayer = MP4Player()
        
    def play(self, audioType: str, filename: str):
        if audioType == "vlc": self.advancedMusicPlayer.playVLC(filename)
        if audioType == 'mp4': self.advancedMusicPlayer.playMP4(filename)
        
class AudioPlayer(MediaPlayer):
    mediaAdapter: MediaAdapter
    def play(self, audioType, filename):
        if audioType == 'mp3': print('playing mp3', filename)
        elif audioType == 'vlc' or audioType  == 'mp4':
            mediaAdapter = MediaAdapter(audioType)
            mediaAdapter.play(audioType, filename)
        else:
            print('Not supported')
            
audioPlayer = AudioPlayer()
audioPlayer.play("mp4", 'test.mp4')