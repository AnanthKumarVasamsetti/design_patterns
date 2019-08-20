"""
Command: Command design pattern encapsulates all the requests into a single object and excutes them as a single command.

Application: Assume a home automation system which turns on and off the lights and plays music on just by one click. There will be 
             few operations while playing a music system like loading a cd, setting the song and adjusting the volume. But the command 
             design pattern takes care of all these operations from a single click and call the "excute" method.
"""

import abc

class Command:
    @abc.abstractclassmethod
    def execute(self):
        pass

class Light:
    def __init__(self):
        pass
    
    def on(self):
        print("Light is turned on")
    
    def off(self):
        print("Light is turned off")

class LightOnCommand(Command):
    def __init__(self):
        self.light = Light()
    
    def execute(self):
        self.light.on()

class LightOffCommand(Command):
    def __init__(self):
        self.light = Light()
    
    def execute(self):
        self.light.off()

class Stereo:

    def __init__(self):
        pass
    
    def on(self):
        print("Turning on the stereo")

    def insert_cd(self):
        print("Inserting CD")
    
    def set_volume(self):
        print("Setting volume to 11")
    
    def off(self):
        print("Turning off stereo")

class StereoOnCommand(Command):

    def __init__(self):
        self.stereo = Stereo()
    
    def execute(self):
        self.stereo.on()
        self.stereo.insert_cd()
        self.stereo.set_volume()
    
class StereoOffCommand(Command):

    def __init__(self):
        self.stereo = Stereo()
    
    def execute(self):
        self.stereo.off()
    

class SimpleRemoteController():

    def __init__(self):
        pass
    
    def setCommand(self, obj):
        self.obj = obj

    def clicked(self):
        self.obj.execute()

if __name__ == "__main__":
    remote = SimpleRemoteController()
    remote.setCommand(LightOnCommand())
    remote.clicked()
    remote.setCommand(StereoOnCommand())
    remote.clicked()
    remote.setCommand(LightOffCommand())
    remote.clicked()
    remote.setCommand(StereoOffCommand())
    remote.clicked()