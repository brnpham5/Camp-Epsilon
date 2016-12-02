#Version 0.1.0
from Tkinter import *
import tkFont
import ttk
##from soundHandler import soundHandler


class GUI_Manager2:
    ##soundPlayer = soundHandler()    #object for soundHandler. used to play music and sound effects

    def __init__(self, master = None):
        ## Declarations
        self.main_frame = ttk.Frame(master)                 #Set main frame, the other three smaller frames will go inside the main frame
        self.root = master                                  #Save tk object to loal var 
        self.mainFrameHeight = 600
        self.mainFrameWidth = 1000
        master.maxsize(height = 600,width = 1200)

        ## Start Menu Frame
        self.start_frame = Frame(self.main_frame)

        ## Gameplay Frame
        self.game_frame = Frame(self.main_frame)

        ## Background frame
        self.bkg_frame = ttk.Frame(self.game_frame)

        ## Dialogue frame
        self.dialog_frame = ttk.Frame(self.game_frame)          #Set dialog-frame for gameplay
        self.dialog_text = Text(self.dialog_frame)              #Text portion of dialog frame
        self.dialog_scroll = Scrollbar(self.dialog_frame)       #Scrollbar of dialog frame
        self.dialog_yview = 1                                   #yview of dialogue frame
        
        ## User Frame
        self.user_frame = ttk.Frame(self.game_frame)            #Set-user frame for gameplay, user's choices and options will go into this frame
        
        ## Main frame
        master.resizable(width = False, height = False)     #Make window not resizable 
        self.main_frame.pack()                              #Pack the main frame into place
        self.main_frame.config( height = 600, width = 1000)  #Set the height and width of the main frame
        self.main_frame.config(relief = RIDGE)              #Style the border
        self.main_frame.config(padding = (15, 15))          #Add padding to main frame
        

    ##Display the start menu    
    def startMenu(self, title, buttonNewGame, buttonContinue, buttonExit, menuBackground):
        self.bkg_canvas = Canvas(self.start_frame, width = 1000, height = 600)      #Set canvas for background
        self.bkg_canvas.pack(expand = YES, fill = BOTH, side = LEFT)        #Pack canvas     
        self.bkg = PhotoImage(file = menuBackground)                            #Set background file
        self.bkg_canvas.create_image(0,0, image = self.bkg, anchor = NW)
        
        style = ttk.Style()
        style.configure('TButton', background = 'black', foreground = 'black', font = ('Times New Roman', 24, 'bold'))
        style.map('TButton', foreground = [('pressed', 'red'),
                                         ('disabled', 'grey')])

        ## Font Setup
        titleFont = tkFont.Font(size = 30)                  #Create custom font for buttons
        
        ## Title
        title.config(text = "Camp Epsilon", font = titleFont)
        title.place(bordermode = OUTSIDE, height = 90, width = 300, relx = 0.375, rely = .007)                           #set label in place and set dimensions
        title.lift()

        ## New Game Button
        buttonNewGame.configure(text = "New Game", cursor ='pirate')        #created button for start screen 
        buttonNewGame.place(bordermode = OUTSIDE, height = 30, width = 250, relx = 0.40, rely = .20)                     #Set button in place, set dimensions
        buttonNewGame.lift()

        #buttonNewGameWindow = self.bkg_canvas.create_window(window = buttonGame)
        ## Load Game Button
        buttonContinue.configure(text = "Continue Game", cursor ='pirate')     #create button for load screen
        buttonContinue.place(bordermode = OUTSIDE, height = 30, width = 250, relx = 0.40, rely = .30)                      #set button in place, set dimensions
        buttonContinue.lift()

        ## Exit Game Button
        buttonExit.configure(text = "Exit Game", cursor ='pirate')                                          #create button for game exit
        buttonExit.place(bordermode = OUTSIDE, height = 30, width = 250, relx = 0.40, rely = .40)                      #set button in place, set dimensions 
        buttonExit.lift()

        #soundplayer.updateMusic(placeholder)               #play music on screen
    
    ## Display the game menu
    def gameScreen(self,optionButton):
        ## Game Frame Configuration
        self.game_frame.config(background = 'black', height = self.mainFrameHeight, width = self.mainFrameWidth)
        
        ## Set Font
        buttonFont = tkFont.Font(size = 15)

        ## Background Frame Configuration
        self.bkg_frame.grid(row = 0, column = 0, rowspan = 2, sticky = 'nsew', padx = 10, pady = 10)    #Position the frame and add padding         
        self.bkg_frame.config(width = 450)                                                              #Set the width of the frame
        self.bkg_frame.config(relief = RIDGE)                                                           #Style the border

        ## Dialogue Frame Configuration
        self.dialog_frame.grid(row = 0, column = 1, sticky = 'nsew', padx = 10, pady = 10)              #Position the frame and add padding
        self.dialog_frame.config(height = 270, width = 450)                                             #Set height and width of the frame
        self.dialog_frame.config(relief = RIDGE)                                                        #Style the border
        self.dialog_text.config(state = DISABLED)
        self.dialog_text.config(wrap = WORD) 

        ## User Frame Configuration
        self.user_frame.grid(row = 1, column = 1, sticky = 'nsew', padx = 10, pady = 10)                #Position the frame and add padding
        self.user_frame.config(height = 270, width = 450)                                               #Set height and width of the frame
        self.user_frame.config(relief = RIDGE)  
        
        ## Option Button Configuration
        optionButton.config(text = "Option", font = buttonFont)
        optionButton.place(relx = 0.70, rely = 0.95)                                                        #Style the border

        self.game_frame.pack()



    #Method that creates popup window for file name entry. Changes start screen to game screen
    def newGame(self, entry_frame, instruction, entryBox, buttonConfirm, buttonReturn):
        style = ttk.Style()
        style.configure('TButton', background = 'black', foreground = 'black', font = ('Times New Roman', 15, 'bold'))
        style.map('TButton', foreground = [('pressed', 'red'),
                                         ('disabled', 'grey')])

        ## Entry Toplevel window
        entry_frame.config(height = self.mainFrameHeight, width = self.mainFrameWidth)      #Overlay frame on top of main_frame                              #Make window not resizable

        ## Player prompt and entry box
        instruction.config(text = "Please enter your name: ")
        instruction.place(relx = 0.42, rely = 0.4)
        entryBox.place(relx = 0.42, rely = 0.45)                                      #place entry in frame

        ## Confirm button
        buttonConfirm.config(text = "Ok", cursor = 'pirate')                   #create button for player
        buttonConfirm.place(relx = 0.42, rely = 0.5)                                    #Set buttons

        ## Return button
        buttonReturn.config(text = "Return to Menu", cursor = 'pirate')    #create button for returning to start screen
        buttonReturn.place(relx = 0.48, rely = 0.5)                                 #place button to popup window

        entry_frame.pack()

    def loadMenu(self, loadMenu_frame, namesList, loadButtonList, fileCount, backButton):
        ##Overlay load frame and configuration
        loadMenu_frame.config(height = self.mainFrameHeight, width = self.mainFrameWidth)
        loadMenu_frame.pack_propagate(False)
        loadMenu_frame.pack()

        ## Font Setup
        buttonFont = tkFont.Font(size = 15)

        ## Display list of buttons
        for i in range(0, fileCount):
            loadButtonList[i].config(text = namesList[i], font = buttonFont)
            loadButtonList[i].pack()

        ## Display Back Button
        backButton.config(text = "Back", font = buttonFont)
        backButton.pack()

    def loadChoice(self, load_topLevel, nameLabel, loadConfirm_Button, loadDelete_Button, loadCancel_Button):
        style = ttk.Style()
        style.configure('TButton', background = 'black', foreground = 'black', font = ('Times New Roman', 15, 'bold'))
        style.map('TButton', foreground = [('pressed', 'red'),
                                         ('disabled', 'grey')])

        ##Overlay load_topLevel
        load_topLevel.config(height = 250, width = 300)
        load_topLevel.resizable(height = False, width = False)

        ## Display Labels
        nameLabel.config()
        nameLabel.place(relx = 0.25, rely = 0.35)

        ## Display Confirm Button
        loadConfirm_Button.config(text = "Confirm")
        loadConfirm_Button.place(relx = 0.1, rely = 0.5) 

        ## Display Delete Button
        loadDelete_Button.config(text = "Delete")
        loadDelete_Button.place(relx = 0.40, rely = 0.5)

        ## Display Cancel Button
        loadCancel_Button.config(text = "Cancel")
        loadCancel_Button.place(relx = 0.70, rely = 0.5)

    def optionMenu(self):
        buttonFont = tkFont.Font(size = 15)
        self.options = Toplevel(self.main_frame ,height = 250, width = 300)
        self.options.title("Option Menu")
        toggleMUS = Button(self.options, text = "Toggle Music", command = (lambda:self.soundPlayer.toggleMusic()), font  = buttonFont)
        toggleMUS.pack()
        toggleSE = Button(self.options, text = "Toggle Sound Effects", command = (lambda:self.soundPlayer.toggleSFX()), font  = buttonFont)
        toggleSE.pack()
        closeOptions = Button(self.options, text = "Return to Game", command = (lambda:self.options.destroy()), font  = buttonFont)
        closeOptions.pack()
        startMenu = Button(self.options, text = "Return to Menu", command = (lambda:self.GameToStart(1)), font  = buttonFont)
        startMenu.pack()

    ## Print the dialogue
    def print_dialogue(self, message):
        ## Set Font
        DSCfont = tkFont.Font(font = ('Times New Roman', 15))

        ## Print to dialogue frame by temporarily enabling then disabling text, update yview
        self.dialog_text.config(state = NORMAL)
        self.dialog_text.insert(END, message)
        self.dialog_yview += 2
        self.dialog_text.yview(self.dialog_yview)
        self.dialog_text.config(state = DISABLED)
        self.dialog_text.pack()

    ## Print the background
    def print_background(self, background):
        self.bkg_canvas.pack_forget()
        self.bkg_canvas = Canvas(self.bkg_frame, width = 450, height = 500)      #Set canvas for background
        self.bkg_canvas.pack(expand = YES, fill = BOTH,side =LEFT)        #Pack canvas     
        self.bkg = PhotoImage(file = background)                            #Set background file
        self.bkg_canvas.create_image(0,0, image = self.bkg, anchor = NW)    #Place background on the canvas
        
    ## Display the player choices
    def display_choice(self, button1, button2, choice1, choice2):
        ## Font Setup
        buttonFont = tkFont.Font(size = 15)

        ## button1
        button1.config(text = choice1, font = buttonFont)
        button1.pack()

        ## button2
        button2.config(text = choice2, font = buttonFont)
        button2.pack()
    
    ## Destroy the choice buttons
    def hide_choice(self, button1, button2):
        button1.destroy()
        button2.destroy()
