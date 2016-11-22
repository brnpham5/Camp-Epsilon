from time import clock
from GameState import *

##===================================================================
## Transitions

class StateTransition(object):
    def __init__(self, toState):
        self.toState = toState

    def execute(self):
        pass

##===================================================================
## States

##Base class for states
class State(object):
    def __init__(self, StateMachine):
        self.StateMachine = StateMachine

    def enter(self):
        pass

    def execute(self):
        pass
        
    def exit(self):
        pass

class StartState(State):
    def __init__(self, StateMachine):
        super(StartState, self).__init__(StateMachine)

    def enter(self):
        ##Call GameState.GUI_Manager to display the Start Menu
        pass

    def execute(self):
        ##Wait until the user makes a playthrough choice
        ##On New Game, call GameState.UserFile_Manager to create a new save file, then set transition to TransitionState
        ##On Load Game, call GameState.UserFile_Manager to load existing save, then set transition to TransitionState
        self.StateMachine.toTransition("toTransitionState")
        pass
        
    def exit(self):
        ##Call GameState.GUI_Manager to close the start menu, open the game menu
        pass

class TransitionState(State):
    def __init__(self, StateMachine):
        super(TransitionState, self).__init__(StateMachine)

    def enter(self):
        pass

    def execute(self):
        ##Call GameState.DataFile_Handler to open the sent DataFile name, set transition to ReadState
        self.StateMachine.toTransition("toReadState")
        pass
        
    def exit(self):
        pass

class ReadState(State):
    def __init__(self, StateMachine):
        super(ReadState, self).__init__(StateMachine)

    def enter(self):

        pass

    def execute(self):
        ##Call GameState.DataFile_Handler to parse keyword
        ##Depending on the returned value, set transition to:
            ##On ENC, WaitState
            ##On FIN, TransitionState
            ##On Anything else, ReadState
        self.StateMachine.GameState.callDataFile_Handler()
        self.StateMachine.toTransition("toReadState")
        pass
        
    def exit(self):
        pass

class WaitState(State):
    def __init__(self, StateMachine):
        super(WaitState, self).__init__(StateMachine)

    def enter(self):
        pass

    def execute(self):
        ##Wait for user choice, print user choice, clear buttons, set line number to appropriate position
        self.StateMachine.toTransition("toReadState")
        pass
        
    def exit(self):
        pass


##===================================================================
## Finite State Machine

class StateMachine(object):
    def __init__(self, character, GameState):
        
        ## Initialize state data
        self.char = character
        self.states = {}
        self.transitions = {}
        self.curState = None
        self.prevState = None
        self.trans = None

        ##Initialize Reference to Game State
        self.GameState = GameState

    def addTransition(self, transName, transition):
        self.transitions[transName] = transition

    def addState(self, stateName, state):
        self.states[stateName] = state

    def setState(self, stateName):
        self.prevState = self.curState
        self.curState = self.states[stateName]

    def toTransition(self, toTrans):
        self.trans = self.transitions[toTrans]

    def execute(self):
        if(self.trans):
            self.curState.exit()
            self.trans.execute()
            self.setState(self.trans.toState)
            self.curState.enter()
            self.trans = None
        self.curState.execute()
