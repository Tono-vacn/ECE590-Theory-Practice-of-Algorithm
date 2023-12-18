import copy
from state import *
from collections import deque 

# DFA is a class with four fields:
# -states = a list of states in the DFA
#  Note that the start state is always state 0
# -accepting = A dictionary, the key is the state id 
#  and value is a boolean indicating which states are acceping
# -alphabet = a list of symbols in the alphabet of the regular language.
#  Note that & can not be included because we use it as epsilon
# -startS = it is the start state id which we assume it is always 0
class DFA:
    def __init__(self):
        self.states = []
        self.is_accepting= dict()
        self.alphabet = []
        self.startS = 0
        self.wrongEnd = False
        pass
    def __str__(self):
        print("States: ", self.states)
        print("Accepting: ", self.is_accepting)
        print("Alphabet: ", self.alphabet)
        print("Start State: ", self.startS)
        pass  
    # You should write this function.
    # It takes two states and a symbol/char. It adds a transition from 
    # the first state of the DFA to the other input state of the DFA.
    def addTransition(self, s1, s2, sym):
        #here must use list to store the next state due to dfa to nfa
        s1.transition[sym] = [s2]
        return
        pass 
    # You should write this function.
    # It returns a DFA that is the complement of this DFA
    def complement(self):
        n = DFA()
        n.states = copy.deepcopy(self.states)
        n.is_accepting = copy.deepcopy(self.is_accepting)
        n.alphabet = copy.deepcopy(self.alphabet)
        n.startS = self.startS
        n.wrongEnd = not self.wrongEnd
        for s in n.states:
            n.is_accepting[s.id] = not n.is_accepting[s.id]
        return n
        pass
    # You should write this function.
    # It takes a string and returns True if the string is in the language of this DFA
    def isStringInLanguage(self, string):
        pos = 0
        for c in string:
            if c not in self.alphabet or c not in self.states[pos].transition:
                return self.wrongEnd
            else:
                pos = self.states[pos].transition[c][0].id
        return self.is_accepting[pos]
        pass
    # You should write this function.
    # It runs BFS on this DFA and returns the shortest string accepted by it
    def shortestString(self):
        q = deque()
        q.append((0,''))
        visited = set()
        #BFS
        while q:
            pos,cur_s = q.popleft()
            if self.is_accepting[pos]:
                return cur_s
            if pos in visited:
                continue
            visited.add(pos)
            for npos in self.states[pos].transition:
                q.append((self.states[pos].transition[npos][0].id,cur_s + npos))
        
        #there is probability that start state is accepting state
        return float('inf')    
        pass
    pass