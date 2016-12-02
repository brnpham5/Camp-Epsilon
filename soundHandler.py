#Version 2.1
from pygame import mixer    #Module needed for sound playing

class soundHandler():
    music = True        #Flag that music is on
    sfx = True          #Flag that sound effects is on
    musicfile = ""      #Name 
    
    #Constructor where we create mixer to play sounds
    def __init__(self):
        mixer.init()

    #Method to play music. Uses OGG or MP3 files
    def updateMusic(self,musicFile): 
        if(mixer.music.get_busy()):     #check to see if music is already playing.
            mixer.music.stop()          #if so stop music.
        musicfile = musicFile
        if(musicFile != ""):
            mixer.music.load(musicFile)        #Load music file
            mixer.music.play(-1,0.0)       #Play music file. Optons below
        #Current option is infinite loop
        #Options we can do (loops,start time)
        #Loops = 0 for 1 time, add 1 for each loop. us -1 for infinite
        #start time = choose where music starts in song. Position in seconds. Uses floats. Strart is 0.0 but is default

    #Used to play sound effects
    #soundFile is name of sound effect file
    def playSound(self,soundFile):
        se = mixer.Sound(soundFile)            #Create sound object to play sound 
        if(self.sfx):
            print ("playing " + soundFile)
            se.play(0,1900)                         #Play sounds. Options below mthod
        #Current option is now no loops
        #Optons we can do (loops,maxtime,fade_ms)
        #loops = 0 for 1 time, add 1 for each loop. use -1 for infinite
        #maxtime = max time to play sound in milliseconds. Use if we want a specific sound from file
        #fade_ms = sound starts at no volume then builds up to max. use number to change

    #Used to stop audio when program ends
    def endHandler(self):
        mixer.stop()    #stop all playback
        mixer.quit()    #ends all playback

    #Used when music is toggled off and on in options
    def toggleMusic(self):
        if(mixer.music.get_busy()): #if music is playing stop it
            mixer.music.stop()
        if(self.music):
            mixer.music.set_volume(0.0) #set music volume to 0.0(no volume)
            self.music = False               #set flag to false
        else:
            mixer.music.set_volume(1.0) #set music volume to 1.0(max volume)
            if(self.musicfile != ""):
                mixer.music.load(self.musicfile) #load music file again for volume to change
            self.music = True                #set flag to true

    #Used when sfx is toggled on or off in options
    def toggleSFX(self):
        if(self.sfx):
            self.sfx = False #Turn flag to false
        else:
            self.sfx = True  #Turn flag to true
