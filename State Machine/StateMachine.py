from time import clock

##===================================================================
## Transitions

class StateTransition(object):
    def __init__(self, toState):
        self.toState = toState

    def execute(self):
        print "Transitoning..."

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
        print "In Start State"
        pass

    def execute(self):
        ##Wait until the user makes a playthrough choice
        ##On New Game, call GameState.UserFile_Manager to create a new save file, then set transition to TransitionState
        ##On Load Game, call GameState.UserFile_Manager to load existing save, then set transition to TransitionState
        self.StateMachine.toTransition("toTransitionState")
        pass
        
    def exit(self):
        ##Call GameState.GUI_Manager to close the start menu, open the game menu
        print "Leaving Start State"
        pass

class TransitionState(State):
    def __init__(self, StateMachine):
        super(TransitionState, self).__init__(StateMachine)

    def enter(self):
        print "In Transition State"
        pass

    def execute(self):
        ##Call GameState.DataFile_Handler to open the sent DataFile name, set transition to ReadState
        self.StateMachine.toTransition("toReadState")
        pass
        
    def exit(self):
        print "Leaving Transition State"
        pass

class ReadState(State):
    def __init__(self, StateMachine):
        super(ReadState, self).__init__(StateMachine)

    def enter(self):
        print "In Read State"
        pass

    def execute(self):
        ##Call GameState.DataFile_Handler to parse keyword
        ##Depending on the returned value, set transition to:
            ##On ENC, WaitState
            ##On FIN, TransitionState
            ##On Anything else, ReadState
        self.StateMachine.toTransition("toWaitState")
        pass
        
    def exit(self):
        print "Leaving Read State"
        pass

class WaitState(State):
    def __init__(self, StateMachine):
        super(WaitState, self).__init__(StateMachine)

    def enter(self):
        print "In Wait State"
        pass

    def execute(self):
        ##Wait for user choice, print user choice, clear buttons, set line number to appropriate position
        self.StateMachine.toTransition("toReadState")
        pass
        
    def exit(self):
        print "Leaving Wait State"
        pass


##===================================================================
## Finite State Machine

class StateMachine(object):
    def __init__(self, character):
        self.char = character
        self.states = {}
        self.transitions = {}
        self.curState = None
        self.prevState = None
        self.trans = None

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

##===================================================================
## GameState

Char = type ("Char", (object,), {})

class GameState(Char):
    def __init__(self):
        self.StateMachine = StateMachine(self)

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

        self.StateMachine.setState("StartState")

    def execute(self):
        self.StateMachine.execute()

    def callGUI_Manager(self):
        #do stuff

if __name__ == '__main__':
    game = GameState()

    for i in range(0, 10):
        startTime = clock()
        timeInterval = 1
        while(startTime + timeInterval > clock()):
            pass
        game.execute()
    

##===================================================================
## DoStuff

class DoStuff(object):
    def __init__(self):
        pass