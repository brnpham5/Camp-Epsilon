#Version 0.0.8
from Tkinter import *
from soundHandler import soundHandler
#from UserFile_Handler import UserFile_Handler

#Used for testing will delete this class
class Choice:
    answers = []
    results = []
    def setChoice(self,answer,result):
        self.answers.append(answer)
        self.results.append(result)

class GUI_Manager:
    #userFile = UserFile_Handler()  #object for userfile. used for getting save files and creating new saves
    soundPlayer = soundHandler()    #object for soundHandler. used to play music and sound effects
    
    y = 50  #y coordinate to place text on canvas
    def __init__(self,master = None):
        self.startScreen = Frame(master)                    #Create a frame to hold stuff for startScreen
        master.minsize(width = 1000,height = 500)           #Set minimum size to main window
        self.root = master                                  #Save tk object to loal var 
        self.startScreen.config(height = 500, width = 500)  #Set dimensions for start screen
        master.resizable(width = False, height = False)     #Make window not resizable 
        self.startScreen.pack()                             #pack strartscreen into window

    #Method creates the startscreen for the game
    def startMenu(self):
        buttonFont = tkFont.Font(size = 24)                 #Create custom font for buttons
        titleFont = tkFont.Font(size = 30)                  #Create custom font for buttons
        buttonStart = Button(self.startScreen, text = "New Game",command = lambda: self.startGame(),font = buttonFont)  #created button for start screen 
        buttonStart.place(bordermode = OUTSIDE, height = 100, width = 250, relx = 0.30, rely = .20)                     #Set button in place, set dimensions
        buttonCont = Button(self.startScreen, text = "Continue Game",command = lambda: self.loadGame(),font = buttonFont)#create button for load screen
        buttonCont.place(bordermode = OUTSIDE, height = 100, width = 250, relx = 0.30, rely = .45)                      #set button in place, set dimensions
        buttonExit = Button(self.startScreen, text = "Exit Game", font = buttonFont)                                    #create button for game exit
        buttonExit.place(bordermode = OUTSIDE, height = 100, width = 250, relx = 0.30, rely = .70)                      #set button in place, set dimensions 
        title = Label(self.startScreen,text = "Camp Epsilon", font = titleFont)                                         #Create label for title
        title.place(bordermode = OUTSIDE, height = 90, width = 300, relx = 0.20, rely = .007)                           #set label in place and set dimensions
        #soundplayer.updateMusic(placeholder)               #play music on screen

    #Method that creates the load screen for the game. 
    def loadGame(self):
        self.startScreen.pack_forget()                      #Take away frame that holds starts screen stuff from window
        self.loadScreen = Frame(self.root,bg = "black")     #Create new frame that holds stuff for load screen
        self.loadScreen.config(height = 500, width = 500)   #Set dimensions
        self.loadScreen.pack(expand = True,fill = BOTH)     #pack screen into window
        titleFont = tkFont.Font(size = 30)
        buttonFont = tkFont.Font(size = 18)                 #Set font size
        title = Label(self.loadScreen,text = "Save File Menu",font = titleFont,bg = "black",fg = "red")
        title.place(height = 90,width = 300, relx = .35, rely = .007)
        files = []                                          #list that will hold butttons for save files
        counter = 0                                         #used in placing buttons
        ycoord = 100                                        #y coordinate to place buttons
        #saveFiles = userFile.getFileNames()                #Called to get save files 
        names = ["bill","mandy","edd","dora","jimmy"]       #Test list for names. Will delete later
        #names= []
        self.filename =""
        for name in names:                                  #For loop that goes through all file names 
            files.append(Button(self.loadScreen, text = name,font = buttonFont,command = lambda:(self.setfile(name))))#Testing. Will delete later.
            #files.append(Button(self.loadScreen, text = name,font = buttonFont,command = lambda: userFile.loadFile(name)))#Creates buttons that will tell userFile_Handler to load file
            files[counter].place(x = 450, y = ycoord)    #Place button in frame
            counter += 1 #update counter
            ycoord += 60 #update y coordinate
        if(len(files) == 0):
            warning = Label(self.loadScreen,text = "No Saves Availiable",font = titleFont,bg = "black",fg = "red")
            warning.place(height = 90,width  = 500,relx = .25, rely = .30)
        buttonReturn = Button(self.loadScreen, text = "Return to start", command = lambda: self.LoadToStart(),font = buttonFont)#Button to return to start screen
        buttonReturn.place(height = 100, width = 200, x= 400, y = 400)#place button and set dimensions
        buttonLoad = Button(self.loadScreen, text = "Load Game", command = lambda: self.userfile.loadFile(self.filename),font = buttonFont)#Button to load save file 
        buttonLoad.place(height = 100, width = 200, x= 700, y = 400)#place button and set dimensions
        buttonDelete = Button(self.loadScreen, text = "Delete Game", command = lambda: self.userfile.DeleteFile(self.filename),font = buttonFont)#Button to load save file 
        buttonDelete.place(height = 100, width = 200, x= 100, y = 400)#place button and set dimensions

    #Method used to get file name from to pass to user file
    def setfile(self,name):
        self.filename = name    #Set name to variable

    #Method that creates popup window for file name entry. Changes start screen to game screen
    def startGame(self):
        self.startScreen.pack_forget()                                  #Take away frame that holds starts screen stuff from window
        buttonFont = tkFont.Font(size = 15)                             #create custom font for buttons
        self.entry = Toplevel(self.root,height = 250, width = 300)      #Create new window
        self.entry.title("Enter a name")                                #Set title of window. Text thats on top left of window
        self.entry.resizable(height = False, width = False)             #Make window not resizable
        instruct = Label(self.entry,text = "Enter name for save file.") #Create text to instruct player to type name
        instruct.place(x = 0,y = 50)                                    #Place label
        field = Entry(self.entry)                                       #Create entry box for player
        field.place(x = 150,y = 50)                                     #place entry in frame
        confirm = Button(self.entry, text = "Ok", command = (lambda:self.start(field.get())), font  = buttonFont) #create button for player
        confirm.place(x = 125,y = 135)                                  #Set buttons
        buttonReturn = Button(self.entry, text = "Return to Menu", command = (lambda:self.GameToStart(0)), font  = buttonFont)#create button for returning to start screen
        buttonReturn.place(x = 90, y = 185)                             #place button to popup window
        self.gameScreen = Frame(self.root,bg = "black")                 #Create a frame to hold textbox, choice buttons?, and background?
        self.gameScreen.pack(fill = BOTH,expand = True)                 #Pack frame to window
        self.textbox = Frame(self.gameScreen)                           #Create frame that will hold text in the game
        self.textbox.config(height = 500, width = 500)                  #Set dimensions for frame
        self.textbox.pack()                                             #pack frame into gameScreen
        self.scroll = Scrollbar(self.textbox)                           #create scrollbar 
        self.scroll.pack(side = RIGHT, fill = Y)                        #pack scrollbar into window
        self.canvas = Canvas(self.textbox, scrollregion = (0,0,0,1000),height = 400, width = 400, bg = "white",yscrollcommand = self.scroll.set )#create canvas that will hold text. set scrollbar to scroll canvas vertically
        self.canvas.pack(side = LEFT)                                   #pack canvas left side of frame
        self.scroll.config( command = self.canvas.yview)                #set the scrollbar change the canvas
        option = Button(self.gameScreen, text = "Options", command = (lambda:self.optionMenu()), font  = buttonFont) #create button for options
        option.pack()                                                   #pack button into frame
        self.GUI_HandlerBKG("")#Test stuff will delete
        #self.GUI_HandlerDSC("*Static interrupts the voice on the other end. The static dies out after a few moments.*")#Test stuff will delete
        self.GUI_HandlerNPC("What if I can't find anyone else?")#Test stuff will delete
        choco = Choice()#Test stuff will delete
        choco.setChoice("I'll come running like Indiana Jones to rescue you!",0)#Test stuff will delete
        choco.setChoice("You'll have to find a way to get out of there ",0)#Test stuff will delete
        self.GUI_HandlerCHC(choco)#Test stuff will delete
        
    def start(self,name):
        #files = userFile.getFileNames() #get name of save files
        room = True     #flag if theres room for save files
        dupe = False    #flag if theres already save file with current 
        files = ['billy','edd','mandy','matt'] #test list will delete later
        for names in files:     #for loop tht goes through names. 
            if(names == name):  #If variable name =s one them set flag to true
                dupe = True
                break           #break loop
        if(len(files) == 5):    #if length of list with names = 5 then set room flag to false
            room = False
        if(dupe):   #if the name entry is a already exists as save file. case matters.place warning label
            dupeWarning = Label(self.entry,text = "A file with this name already exists",justify = CENTER)
            dupeWarning.place(x = 50,y = 70)
        if(room == False):#if the max limit of files is reached place warning label.
            roomWarning = Label(self.entry,text = "Max number of save files reached. Please return to Start Menu and go to Load Game to delete a file.",wraplength = 205,justify = CENTER)
            roomWarning.place(x = 50,y = 90)
        if( room and dupe == False):#if both flags don't trip errors
            #self.userFile.saveFile(name)   #create save file
            self.entry.destroy()    #destroy window

    #method for when choice buttons are clicked
    def buttonClick(self,lineNumber):
        #dataFile.CurrentLine = lineNumber  #update currentline
        self.buttonFrame.destroy()         #destroy frame that holds choice buttons

    def optionMenu(self):
        buttonFont = tkFont.Font(size = 15)
        self.options = Toplevel(self.root,height = 250, width = 300)
        self.options.title("Option Menu")
        toggleMUS = Button(self.options, text = "Toggle Music", command = (lambda:self.soundPlayer.toggleMusic()), font  = buttonFont)
        toggleMUS.pack()
        toggleSE = Button(self.options, text = "Toggle Sound Effects", command = (lambda:self.soundPlayer.toggleSFX()), font  = buttonFont)
        toggleSE.pack()
        closeOptions = Button(self.options, text = "Return to Game", command = (lambda:self.options.destroy()), font  = buttonFont)
        closeOptions.pack()
        startMenu = Button(self.options, text = "Return to Menu", command = (lambda:self.GameToStart(1)), font  = buttonFont)
        startMenu.pack()

    #Method to switch load screen to start screen
    def LoadToStart(self):
        self.loadScreen.destroy()   #Destroys loadscreen frame.
        self.startScreen.pack()     #put start screen back into window.

    #Method to move new game to start screen
    def GameToStart(self,window):
        if (window == 0):
            self.entry.destroy()    #destroy window used to get save file name
        else:
            self.options.destroy()  #destroy game option menu
        self.gameScreen.destroy()  #destroy frame holding text box
        self.startScreen.pack() #pack start screen into main window
    

    #method that handles description keyword lines
    #Current bug: Text maybe shown incorrect. Examples: Text maybe overlapped with other text(Max line limit is 2 in size 15 font).
    #Current format for create_text(X coordinate(I think the coordinate is middle of text),Ycoordinate, font color, font, max width of text in pixels,text is centered so that left side is (x,y))
    def GUI_HandlerDSC(self,description):
        DSCfont = tkFont.Font(size = 15)    #create custom font
        self.canvas.create_text(0,self.y,fill = "blue",text = description, font = DSCfont,width = 400,anchor = W)#create text to put onto canvas
        self.y += 50    #update y coordinate for adding text to canvas.

    #method handles npc keyword lines
    #Has same bugs as description does. Create_text format is same too.
    def GUI_HandlerNPC(self,dialouge):
        NPCfont = tkFont.Font(size = 15)
        self.canvas.create_text(0,self.y,fill = "green", text = dialouge, font = NPCfont,width = 400,anchor = W)
        self.y += 50

    #method handles choice keywords lines
    def GUI_HandlerCHC(self,choice):
        CHCfont = tkFont.Font(size = 13)            #Create custom font for choices
        self.buttonFrame = Frame(self.gameScreen)   #Create frame for buttons
        self.buttonFrame.pack(side = BOTTOM)        #place frame on bottom of gamescreen
        buttons = []
        for x in range(0,len(choice.answers)):
            buttons.append(Button(self.buttonFrame,text = choice.answers[x], font = CHCfont,wraplength = 240,command = (lambda: self.buttonClick(choice.results[x]))))

        buttons[0].grid(row = 0, column = 0)        #Place buttons 
        buttons[1].grid(row = 0, column = 1)

    #method for backgrounds
    #Maybe do background frames for left and right of textbox
    #Would require the use of two files for each frame tho.
    def GUI_HandlerBKG(self,background):
        self.back = Frame(self.gameScreen)
        self.back.place(x=0,y=0)
        self.test = Canvas(self.back,height = 500, width = 284,bg = "red",bd=0)
        self.test.pack()
        self.backR = Frame(self.gameScreen)
        self.backR.place(x=710,y=0)
        self.testR = Canvas(self.backR,height = 500, width = 285,bg = "red",bd=0)
        self.testR.pack()

    #Method for music keyword lines
    def GUI_HandlerMUS(self,music):
        soundPlayer.updateMusic(music) #Tells soundPlayer to play music

    #Method for sound effect keywords
    def GUI_HandlerSFX(self,sound):
        soundPlayer.playSound(sound)    #Tells soundPlayer to play the sound effect
