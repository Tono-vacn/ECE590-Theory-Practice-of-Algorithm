from nfa import *
from state import *

class Regex:
    #generate a string representation of the regex
    def __repr__(self):
        ans=str(type(self))+"("
        sep=""
        for i in self.children:
            ans = ans + sep + repr(i)
            sep=", "
            pass
        ans=ans+")"
        return ans
    def transformToNFA(self):
        pass
    pass

class ConcatRegex(Regex):
    def __init__(self, r1, r2):
        self.children=[r1,r2]
        pass
    def __str__(self):
        return "{}{}".format(self.children[0],self.children[1])
    def transformToNFA(self):
        n1 = self.children[0].transformToNFA()
        n2 = self.children[1].transformToNFA()
        lth1 = len(n1.states)
        n1.addStatesFrom(n2)
        for i in range(lth1):
            if n1.is_accepting[i]:
                n1.addTransition(n1.states[i], n1.states[lth1], '&')
                n1.is_accepting[i] = False
            #n1.addTransition(n1.states[i], n2.states[i], '&'))        
        return n1
        pass

class StarRegex(Regex):
    def __init__(self, r1):
        self.children=[r1]
        pass
    def __str__(self):
        return "({})*".format(self.children[0])
    def transformToNFA(self):
        n = self.children[0].transformToNFA()
        for s in n.states:
            if n.is_accepting[s.id]:
                n.addTransition(s, n.states[0])
                #n.is_accepting[s.id] = False
        n.is_accepting[0] = True
        return n
        pass

class OrRegex(Regex):
    def __init__(self, r1, r2):
        self.children=[r1,r2]
        pass
    def __str__(self):
        return "(({})|({}))".format(self.children[0],self.children[1])
    def transformToNFA(self):
        n1 = self.children[0].transformToNFA()
        n2 = self.children[1].transformToNFA()
        lth1 = len(n1.states)
        n1.addStatesFrom(n2)
        n1.addTransition(n1.states[0], n1.states[lth1])
        return n1
        pass
    pass

class SymRegex(Regex):
    def __init__(self, sym):
        self.sym=sym
        pass
    def __str__(self):
        return self.sym
    def __repr__(self):
        return self.sym
    def transformToNFA(self):
        n = NFA()
        n.states.extend([State(0), State(1)])
        n.is_accepting[0] = False
        n.is_accepting[1] = True
        n.addTransition(n.states[0], n.states[1], self.sym)
        n.alphabet.append(self.sym)
        return n
        pass
    pass

class EpsilonRegex(Regex):
    def __init__(self):
        pass
    def __str__(self):
        return '&'
    def __repr__(self):
        return '&'
    def transformToNFA(self):
        n = NFA()
        n.states.append(State(0))
        n.is_accepting[0] = True
        return n
        pass
    pass

class ReInput:
    def __init__(self,s):
        self.str=s
        self.pos=0
        pass
    def peek(self):
        if (self.pos < len(self.str)):
            return self.str[self.pos]
        return None
    def get(self):
        ans = self.peek()
        self.pos +=1
        return ans
    def eat(self,c):
        ans = self.get()
        if (ans != c):
            raise ValueError("Expected " + str(c) + " but found " + str(ans)+
                             " at position " + str(self.pos-1) + " of  " + self.str)
        return c
    def unget(self):
        if (self.pos > 0):
            self.pos -=1
            pass
        pass
    pass

# R -> C rtail
# rtail -> OR C rtail | eps
# C -> S ctail
# ctail -> S ctail | eps
# S -> atom stars
# atom -> (R) | sym | &
# stars -> * stars | eps


#It gets a regular expression string and returns a Regex object. 
def parse_re(s):
    inp=ReInput(s)
    def parseR():
        return rtail(parseC())
    def parseC():
        return ctail(parseS())
    def parseS():
        return stars(parseA())
    def parseA():
        c=inp.get()
        if c == '(':
            ans=parseR()
            inp.eat(')')
            return ans
        if c == '&':
            return EpsilonRegex()
        if c in ')|*':
            inp.unget()
            inp.fail("Expected open paren, symbol, or epsilon")
            pass
        return SymRegex(c)
    def rtail(lhs):
        if (inp.peek()=='|'):
            inp.get()
            x = parseC()
            return rtail(OrRegex(lhs,x))
        return lhs
    def ctail(lhs):
        if(inp.peek() is not None and inp.peek() not in '|*)'):
            temp=parseS()
            return ctail(ConcatRegex(lhs,temp))
        return lhs
    def stars(lhs):
        while(inp.peek()=='*'):
            inp.eat('*')
            lhs=StarRegex(lhs)
            pass
        return lhs
    return parseR()