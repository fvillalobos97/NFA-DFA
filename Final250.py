## Felicia Villalobos & Alex Larosee
## A4:DFA-NFA converter 

def epsilonClosure(transitions, newState, state):
    for trans in transitions:
        if trans[0] == state:
            if trans[1] == 'eps':
                if trans[2] not in newState:
                    newState.append(trans[2])
                    print(newState)
                    epsilonClosure(transitions, newState, trans[2])
    return newState

def makeArc(transitions, DFAstate, alphabet):
    '''determine DFA transition function on all inputs'''
    state1 = []
    arcData = ''
    print(alphabet)
    statesofDFA = {}
    
    for char in alphabet:
        for trans in transitions:
            if trans[0] in DFAstate:
                if trans[1] == char:
                    print('char is', char)
                    state1.append(trans[2])
                    arcData = char  
                    x = {state1: arcData}
                    print(x)
                    
    print('state1=', state1)
    print('arc=', arcData) 
                
            

class DFA:
    def __init__(self, transitions, finalstates,alphabet):
        '''will call all of the methods we need to make a DFA'''
        counter = 0
        newState = [0]
        DFA_states = []

        DFAstate = epsilonClosure(transitions, newState, 0)
        DFAstate.append(DFAstate)
        symbol = 'b'
        makeArc(transitions,DFAstate,alphabet)
        

class NFA:
    def __init__(self,filename):
        '''will process the file to  and call the DFA class'''
        acrs = {}
        states = {}
        transitions = []
        acceptingStates = []
       
        #process the file 
        f = open(filename, 'r')
      


        #get the alphabet
        alphabet = f.readline()
        alphabet = alphabet.replace('\n','')
        print('alphabet:',alphabet)

        
        #number of transition arcs
        tarcs = eval(f.readline())
        print(tarcs, 'transition arcs found')
#        
        
        #update transition lists
        for i in range(tarcs):
            x = eval(f.readline())
            transitions.append(x)
        
        print(transitions)
        
        finalstates = eval(f.readline())
        print('accepted states:',finalstates,'\n')

        DFA(transitions, finalstates, alphabet)
        
        
        

def main():
    #take in filename
    filename = input('filename:')
    NFA(filename)


main()






