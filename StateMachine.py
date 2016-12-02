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

class TransitionState(State):
    def __init__(self, StateMachine):
        super(TransitionState, self).__init__(StateMachine)

    def enter(self):
        pass

    def execute(self):
        ##Call GameState.DataFile_Handler to open the sent DataFile name, set transition to ReadState
        print("TransitionState")
        self.StateMachine.toTransition("toReadState")
        
    def exit(self):
        pass

class ReadState(State):
    def __init__(self, StateMachine):
        super(ReadState, self).__init__(StateMachine)

    def enter(self):
        pass

    def execute(self):
        print("ReadState")
        ## Call GameState to parse and execute keyword
        keyword = self.StateMachine.GameState.DataFile_parseKey()
        ##Depending on the returned value, set transition to:
            ##On ENC, WaitState
            ##On FIN, TransitionState
            ##On Anything else, ReadState
        if(keyword == "ENC"):
            self.StateMachine.toTransition("toWaitState")
        elif (keyword == "FIN"):
            self.StateMachine.toTransition("toTransitionState")
        else:
            self.StateMachine.toTransition("toReadState")
        
    def exit(self):
        pass

class WaitState(State):
    def __init__(self, StateMachine):
        super(WaitState, self).__init__(StateMachine)

    def enter(self):
        #self.StateMachine.GameState.StateMachine_Stop()
        pass

    def execute(self):
        print("Wait State")
        ##Wait for user choice, print user choice, clear buttons, set line number to appropriate position
        self.StateMachine.toTransition("toReadState")
        
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

        ## Set States
        self.addState("TransitionState", TransitionState(self))
        self.addState("ReadState", ReadState(self))
        self.addState("WaitState", WaitState(self))

        ## Set Transitions
        self.addTransition("toTransitionState", StateTransition("TransitionState"))
        self.addTransition("toReadState", StateTransition("ReadState"))
        self.addTransition("toWaitState", StateTransition("WaitState"))

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