class StateMachine:
    def __init__(self):
        self.handlers = {}
        self.startState = None
        self.endState = []
        
    def add_state(self,name,handler,end_state = 0):
        name = name.upper()
        self.hadlers[name] = hander
        if end_state:
            self.endState.append(name)
            
    def set_start(self,name):
        self.startStart = name.upper()
        
    def run(self,cargo):
        try:
            handler = self.handlers[self.startState]
        except:
            raise InitializationError("Must call .set_start() before .run")
        if not self.endStates:
            raise InitializationError("at leat one state mut be an end_state")
        while True:
            newState, cargo = handler(cargo)
            if newState.upper() in self.endStates:
                print("reached", newState)
                break
            else:
                handler = self.handlers[newState.upper()]
    
