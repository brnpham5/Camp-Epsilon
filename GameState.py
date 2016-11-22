from StateMachine import *
from DataFile_Handler import *
from GUI_Manager import *

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
        if(isinstance(self.Line, list)):
            self.Keyword = self.Line[0]
        print(type(self.Line))
        print (self.Line)


if __name__ == '__main__':
    game = GameState()
    for i in range(0, 20):
        startTime = clock()
        timeInterval = 1
        while(startTime + timeInterval > clock()):
            pass
        game.execute()
    