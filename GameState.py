from StateMachine import *
from DataFile_Handler import *

##===================================================================
## GameState

Char = type ("Char", (object,), {})

class GameState(Char):
    def __init__(self):
        self.StateMachine = StateMachine(self, self)
        self.DataFile = DataFile_Handler("ACT1.txt")
        self.Keyword = ""
        self.Line = ""

        ## States
        self.StateMachine.addState("StartState", StartState(self.StateMachine))
        self.StateMachine.addState("TransitionState", TransitionState(self.StateMachine))
        self.StateMachine.addState("ReadState", ReadState(self.StateMachine))
        self.StateMachine.addState("WaitState", WaitState(self.StateMachine))

        ## Transitions
        self.StateMachine.addTransition("toStartState", StateTransition("StartState"))
        self.StateMachine.addTransition("toTransitionState", StateTransition("TransitionState"))
        self.StateMachine.addTransition("toReadState", StateTransition("ReadState"))
        self.StateMachine.addTransition("toWaitState", StateTransition("WaitState"))

        ## Set first state to start state
        self.StateMachine.setState("StartState")

    def execute(self):
        self.StateMachine.execute()

    def callGUI_Manager(self):
        #do stuff
        pass

    def Display_Start_Menu(self):
        #self.GUI_Manager.Display_Start_Menu()
        pass

    def callDataFile_Handler(self):
        self.Line = self.DataFile.keyword_Handler(-1)
        #if(isinstance(self.Line, list)):
        #    self.Keyword = self.Line[0]
        #print(type(self.Line))
        print (self.Line)

    def DataFile_DSC_Handler(self):
        self.DataFile.updateLine()
        #self.GUI_Manager.printDSC(self.Line[1])

    def DataFile_NPC_Handler(self):
        self.DataFile.updateLine()
        #self.GUI_Manager.printNPC(self.Line[1])

    def DataFile_CHC_Handler(self):
        #self.GUI_Manager.addChoices(self.Line[1], self.Line[2], self.Line[4], self.Line[5])
        pass

    def DataFile_SFX_Handler(self):
        pass

    def DataFile_MUS_Handler(self):
        pass

    def DataFile_BKG_Handler(self):
        pass

    def DataFile_LIK_Handler(self):
        pass
        
    def DataFile_JMP_Handler(self):
        self.DataFile.jumpToLine(self.Line[1])

    def DataFile_FIN_Handler():
        pass

    

    #def UserFile_FIN_Handler(self):  #player name, data file, likeability
    #    DataFile.endAct(self.line[1])
    #    act = DataFile.GetAct()
    #    UserFile.updateUser([UserFile.getName(), DataFile.getAct(), UserFile.getLikeabilty()])
    #    UserFile.SaveFile()

    


if __name__ == '__main__':
    game = GameState()
    for i in range(0, 20):
        startTime = clock()
        timeInterval = 1
        while(startTime + timeInterval > clock()):
            pass
        game.execute()
    