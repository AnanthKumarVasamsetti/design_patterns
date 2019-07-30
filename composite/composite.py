"""
Composite: This is a structural pattern whose main goal is to compose nested structures of objects and to deal with the 
           classes for these objects uniformly.

There are two kinds of classes here 
1. Composite class
2. Leaf class

Composite class: It implements the component interface and allows you to "traverse through" and "potentially manipulate"
                 the component objects that the composite object contains.

Leaf class: It also implements the component interface but it is not composed of other components.

Example: The following example is about an application which has playlists, where each playlist can consist of songs and other playlists also.
"""


import abc

class ComponentInterface:
    @abc.abstractclassmethod
    def play(self):
        pass
    
    @abc.abstractclassmethod
    def setPlayBackSpeed(self, speed):
        pass
    
    @abc.abstractclassmethod
    def getName(self):
        pass

class Playlist(ComponentInterface):
    def __init__(self, name, componentsList=None):
        self.name = name
        self.playlist = componentsList if componentsList and len(componentsList) > 0 else []
    
    def play(self):
        print("======= Started playing playlist: ", self.name)
        for component in self.playlist:
            component.play()
            
    def setPlayBackSpeed(self, speed):
        print("Playing playlist: ", self.name, " at a playback speed: ",speed)
    
    def getName(self):
        return self.name
    
    def add(self, component):
        self.playlist.append(component)
    
    def remove(self, component):
        self.playlist.remove(component)

class Song(ComponentInterface):
    def __init__(self, name, artist=None, speed=None):
        self.songName = name
        self.artist = artist
        self.speed = speed
    
    def play(self):
        print("Playing song: ",self.songName)
    
    def setPlayBackSpeed(self, speed):
        print("Playing song ",self.songName," at a playback speed: ",speed)
    
    def getName(self):
        return self.songName

    def getArtist(self):
        return self.artist

def mainApplication():
    morningPlaylist = Playlist("morningPlaylist")
    songA = Song("songA")
    songB = Song("songB")

    morningPlaylist.add(songA)
    morningPlaylist.add(songB)

    workoutPlaylist = Playlist("workoutPlaylist")
    songC = Song("songC")
    songB = Song("songB")
    songD = Song("songD")

    workoutPlaylist.add(songC)
    workoutPlaylist.add(songB)
    workoutPlaylist.add(songD)

    workoutPlaylist.add(morningPlaylist)

    morningPlaylist.play()

    workoutPlaylist.play()

if __name__ == "__main__":
    mainApplication()