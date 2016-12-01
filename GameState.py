import StateMachine
import DataFile_Handler
import UserFile_Handler
import Tkinter
import GUI_Manager2
import pygame

from time import clock

##===================================================================
## GameState

Char = type ("Char", (object,), {})

class GameState(Char):
    def __init__(self):
        ## Initialize References
        self.StateMachine = StateMachine.StateMachine(self, self)
        self.DataFile = DataFile_Handler.DataFile_Handler("ACT1.txt")
        self.UserFile = UserFile_Handler.UserFile_Handler()

        ## Game Data
        self.choices = []               # List of choices

        ## Set first state to Transition State
        self.StateMachine.setState("TransitionState")

        ## StateMachine Automator
        self.nextstep_id = 0
        self.state_On = True
        self.state_Timer = 1000

        ## Initialize Tkinter and GUI_Manager
        self.tk = Tkinter.Tk()
        self.GUI_Manager = GUI_Manager2.GUI_Manager2(self.tk)
        self.gameInitialize()
        self.tk.mainloop()

    ## Execute command for State Machine
    def execute(self):
        self.StateMachine.execute()

    ## Initialize the game
    def gameInitialize(self):
        ## Click to start game
        def leftClick_Handler(event):
            ##Unbind the button, clear the message
            self.tk.unbind("<Button-1>")
            message.destroy()
            
            ## Display Start Menu
            self.display_StartMenu()

        ## Bind left click to call leftClick_Handler
        self.tk.bind("<Button-1>", leftClick_Handler)

        ## Place start message
        message = Tkinter.Message(self.tk, text = "Click anywhere to start")
        message.place(bordermode = Tkinter.OUTSIDE, height = self.GUI_Manager.mainFrameHeight, width = self.GUI_Manager.mainFrameWidth)

    ## TESTER: Speed up timer with each click
    def click_Handler(self, event):
        self.StateMachine_Forward()

    ## Display State Menu
    def display_StartMenu(self):
        print("Start Menu")
        ## Setup Title
        title = Tkinter.Label(self.GUI_Manager.start_frame)

        ## Create Buttons
        buttonNewGame = Tkinter.Button(self.GUI_Manager.start_frame, command = lambda: self.display_NewGame_Menu())
        buttonContinue = Tkinter.Button(self.GUI_Manager.start_frame, command = lambda: self.display_LoadMenu())
        buttonExit = Tkinter.Button(self.GUI_Manager.start_frame, command = lambda: self.tk.quit())

        self.GUI_Manager.start_frame.place(bordermode = Tkinter.OUTSIDE, height = self.GUI_Manager.mainFrameHeight, width = self.GUI_Manager.mainFrameWidth)
        
        ## Call GUI_Manager to display buttons
        self.GUI_Manager.startMenu(title, buttonNewGame, buttonContinue, buttonExit)

    ## Hide Start Menu
    def hide_StartMenu(self):
        self.GUI_Manager.start_frame.place_forget()
    
    ## Display the new game menu
    def display_NewGame_Menu(self):
        print("New Game")
        ## Create Toplevel entry
        entry_frame = Tkinter.Frame(self.GUI_Manager.main_frame)

        ## Create player prompt and entry box
        instruction = Tkinter.Label(entry_frame)
        entryBox = Tkinter.Entry(entry_frame)

        ## Confirm button
        buttonConfirm = Tkinter.Button(entry_frame, command = lambda: self.createNewGame(entry_frame, entryBox))

        ## Return button
        buttonReturn = Tkinter.Button(entry_frame, command = lambda: entry_frame.destroy())

        ## Call GUI_Manager to display NewGame Menu
        self.GUI_Manager.newGame(entry_frame, instruction, entryBox, buttonConfirm, buttonReturn)

    ## Create a new game when new game option is chosen from start menu
    def createNewGame(self, entry, entryBox):
        ## Get name from entry
        name = entryBox.get()

        ## Call userfile handler to set name
        self.UserFile.setPlayerName(name)

        ## Save file
        self.UserFile.saveFile()

        ## Clear the screen
        self.GUI_Manager.start_frame.place_forget()
        entry.destroy()

        ## Display the gamescreen
        self.display_GameScreen()

        ## Start State Machine
        self.StateMachine_Start()

    ## Load Menu
    def display_LoadMenu(self):
        ##Create load menu frame
        loadMenu_frame = Tkinter.Frame(self.GUI_Manager.main_frame)

        ##Check SaveFile.txt, Get names, number of files
        fileNames = self.UserFile.getFileNames()
        fileCount = len(fileNames)

        ##Create list of load buttons
        loadList = []
        for i in range(0, fileCount):
            buttonConfirm = Tkinter.Button(loadMenu_frame, command = lambda x = fileNames[i]: self.loadButton_Handler(loadMenu_frame, x))
            loadList.append(buttonConfirm)
        
        ##Create back button
        backButton = Tkinter.Button(loadMenu_frame, command = lambda: loadMenu_frame.destroy())

        ##Pass buttons to GUI_Manager: load screen
        self.GUI_Manager.loadMenu(loadMenu_frame, fileNames, loadList, fileCount, backButton)

    ## Handler to check load button press
    def loadButton_Handler(self, loadMenu_frame, name):
        ##Create topLevel
        load_topLevel = Tkinter.Toplevel(loadMenu_frame)
        ##Create label to display name
        nameLabel = Tkinter.Label(load_topLevel, text = name)

        ##Create Buttons: continue, delete, cancel
        loadConfirm_Button = Tkinter.Button(load_topLevel, command = lambda: self.loadConfirm_Handler(loadMenu_frame, name))
        loadDelete_Button = Tkinter.Button(load_topLevel, command = lambda: self.loadDelete_Handler(loadMenu_frame, name))
        loadCancel_Button = Tkinter.Button(load_topLevel, command = lambda: load_topLevel.destroy())

        ##Pass to GUI_Manager: loadChoice
        self.GUI_Manager.loadChoice(load_topLevel, nameLabel, loadConfirm_Button, loadDelete_Button, loadCancel_Button)

    def loadConfirm_Handler(self, loadMenu_frame, name):
        ##Call UserFile_Handler to load data from name
        self.UserFile.loadFile(name)

        ##Update Act
        self.DataFile.newAct(self.UserFile.getDataFile())

        ## Clear the screen
        self.GUI_Manager.start_frame.place_forget()
        loadMenu_frame.destroy()

        ## Display the gamescreen
        self.display_GameScreen()

        ## Start State Machine
        self.StateMachine_Start()

    def loadDelete_Handler(self, loadMenu_frame, name):
        ##Call UserFile_Handler to delete file with specific name
        self.UserFile.deleteFile(name)

        ##Refresh Load Screen
        loadMenu_frame.destroy()
        self.display_LoadMenu()

    ## Display the gamescreen.
    def display_GameScreen(self):
        print("Game Screen")
        ##Option Menu Toggle
        self.optionOn = False

        ## Create Option Menu button
        self.optionButton = Tkinter.Button(self.GUI_Manager.game_frame, command = lambda: self.OptionMenu_toggle())

        ## Call GUI_Manager to display screen
        self.GUI_Manager.gameScreen(self.optionButton)

        ## TESTER: Click to progress game
        self.tk.bind("<Button-1>", self.click_Handler)

    def OptionMenu_toggle(self):
        if(self.optionOn) == False:
            self.optionOn = True
            self.GUI_Manager.display_optionMenu()
        else:
            self.optionOn = False
            self.GUI_Manager.hide_optionMenu()
            self.GUI_Manager.


    def OptionMenu_toggleMus(self):
        pass

    def OptionMenu_toggleSFX(self):
        pass

    def OptionMenu_close(self):
        pass
        
    def OptionMenu_returnToStart(self):
        pass

    def hide_OptionMenu(self):
        pass


    ## DataFile_Handler call
    def DataFile_getKey(self):
        line = self.DataFile.keyword_Handler()
        return line[0]

    def DataFile_parseKey(self):
        line = self.DataFile.keyword_Handler()
        options = {
            ''      : lambda: self.DataFile.updateLine(),
            "DSC"   : lambda: self.Keyword_DSC_Handler(line[1]),
            "NPC"   : lambda: self.Keyword_NPC_Handler(line[1]),
            "CHC"   : lambda: self.Keyword_CHC_Handler(self.choices, line[1], line[2]),
            "SFX"   : lambda: self.Keyword_SFX_Handler(line[1]),
            "MUS"   : lambda: self.Keyword_MUS_Handler(line[1]),
            "BKG"   : lambda: self.Keyword_BKG_Handler(line[1]),
            "LIK"   : lambda: self.Keyword_LIK_Handler(line[1]),
            "JMP"   : lambda: self.Keyword_JMP_Handler(line[1]),
            "FIN"   : lambda: self.Keyword_FIN_Handler(line[1]),
            "BRN"   : lambda: self.Keyword_BRN_Handler(line[1]),
            "ENC"   : lambda: self.Keyword_ENC_Handler(self.choices)
        }
        
        options[line[0]]()

        return line[0]

    ## DSC Keyword Handler: Call GUI_Manager to print text
    def Keyword_DSC_Handler(self, text):
        print("DSC")
        self.GUI_Manager.print_dialogue(text + '\n')
        self.DataFile.updateLine()

    ## NPC Keyword Handler: Call GUI_Manager to print text
    def Keyword_NPC_Handler(self, text):
        print("NPC")
        self.GUI_Manager.print_dialogue(text + '\n')
        self.DataFile.updateLine()

    ## CHC Keyword Handler: Store choice line number and string
    def Keyword_CHC_Handler(self, choices, line, text):
        print("CHC")
        choices.append(line)
        choices.append(text)
        self.DataFile.updateLine()

    ## ENC Keyword Handler: Call GUI_Manager to configure buttons.
    def Keyword_ENC_Handler(self, choices):
        print("ENC")
        ## Create Choice Buttons
        self.button1 = Tkinter.Button(self.GUI_Manager.user_frame, command = lambda: self.Choice1_Handler(choices[1]))
        self.button2 = Tkinter.Button(self.GUI_Manager.user_frame, command = lambda: self.Choice2_Handler(choices[3]))

        ## Call GUI_Manager to print choices onto buttons
        self.GUI_Manager.display_choice(self.button1, self.button2, choices[1], choices[3])

        ## TESTER: Unbind Left Click Story Progress
        self.tk.unbind("<Button-1>")

        ## Stop State Machine
        self.StateMachine_Stop()

    ## Helper to CHC_Handler: Called when button1 is pressed
    def Choice1_Handler(self, choice):
        self.GUI_Manager.print_dialogue(choice + '\n')
        self.DataFile.setLineNumber(int(self.choices[0]))
        self.Choice_Clear()
        self.StateMachine_Start()

    ## Helper to CHC_Handler: Called when button2 is pressed
    def Choice2_Handler(self, choice):
        self.GUI_Manager.print_dialogue(choice + '\n')
        self.DataFile.setLineNumber(int(self.choices[2]))
        self.Choice_Clear()
        self.StateMachine_Start()

    ## Helper to ENC_Handler: Clear choices, clear buttons
    def Choice_Clear(self):
        ## Clear choices
        self.choices[:] = []

        ## Call GUI_Handler to hide buttons
        self.GUI_Manager.hide_choice(self.button1, self.button2)

        ## TESTER: Rebind left click story progress
        self.tk.bind("<Button-1>", self.click_Handler)

    ## SFX Keyword Handler: Call Sound_Manager to play sound effect
    def Keyword_SFX_Handler(self, text):
        print("SFX")
        self.DataFile.updateLine()

    ## MUS Keyword Handler: Call Sound_Manager to loop music
    def Keyword_MUS_Handler(self, text):
        print("MUS")
        self.DataFile.updateLine()

    ## BKG Keyword Handler: Call GUI_Manager to display background
    def Keyword_BKG_Handler(self, text):
        print("BKG")
        ## Remove endline char
        text = text[:-1]

        ## Remove space
        text = text[1:]

        ## Call GUI_Manager to print the background (image must be specific size)
        self.GUI_Manager.print_background(text)

        self.DataFile.updateLine()

    ## LIK Keyword Handler: Call UserFile_Handler to update Likeability
    def Keyword_LIK_Handler(self, likeability):
        print("LIK")
        ## Get current likeability
        currentLike = self.UserFile.getLike()

        ## Update likeability 1 = increment, 0 = decrement
        if (int(likeability) == 1):
            currentLike += 1
        elif(int(likeability == 0)):
            currentLike -= 1

        ## Update likeability in UserFile
        self.UserFile.setLike(currentLike)

        self.DataFile.updateLine()
    
    ## JMP Keyword Handler: Call DataFile_Handler to jump to specific line in file
    def Keyword_JMP_Handler(self, line):
        print("JMP")
        self.DataFile.setLineNumber(int(line))

    ## FIN Keyword Handler: Call UserFile_Handler to save
    ##                      Call DataFile_Handler to open new act
    def Keyword_FIN_Handler(self, version):
        print("FIN")
        ## Call DataFile_Handler to get the next act based on parameters nextAct
        self.DataFile.endAct(int(version))

        ## Get Current act
        currentAct = self.DataFile.getCurrentAct()

        ## Update UserFile
        self.UserFile.setDataFile(currentAct)

        ## Save UserFile
        self.UserFile.saveFile()

    ## BRN Keyword Handler: Call DataFile_Handler to update branch variable: 0 = decrement, 1 = increment
    def Keyword_BRN_Handler(self, changeInValue):
        print("BRN")
        self.DataFile.updateNextAct(int(changeInValue))
        self.DataFile.updateLine()

    def StateMachine_Start(self):
        print("State machine started")
        self.state_On = True
        self.state_Timer = 1000
        def step():
            while self.state_On:
                self.execute()
                self.nextstep_id = self.tk.after(self.state_Timer, nextstep)
                yield
        nextstep = step().next
        self.nextstep_id = self.tk.after(self.state_Timer, nextstep)

    def StateMachine_Stop(self):
        print("State machine stopped")
        self.tk.after_cancel(self.nextstep_id)
        self.state_On = False

    def StateMachine_Forward(self):
        print("State machine forward")
        self.state_Timer = 1

if __name__ == '__main__':
    game = GameState()
