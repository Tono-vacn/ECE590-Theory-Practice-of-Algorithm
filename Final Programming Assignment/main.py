import copy
from regex import parse_re
from regex import *
from state import * 
from nfa import *
from dfa import *

# You should write this function.
# It takes an NFA and returns a DFA.
def nfaToDFA(nfa):
    #epsilon record for all states
    rec = dict()
    
    for state in nfa.states:
        s = set()
        s.add(state)
        while s!=nfa.epsilonCloseSet(s):
            s = nfa.epsilonCloseSet(s)
        rec[state.id] = set([st.id for st in s])
    
    d = DFA()
    d.alphabet = copy.deepcopy(nfa.alphabet)
    
    d.states.append(State(0))
    #len_states = len(nfa.states)
    nfa_states_rec = [rec[0]]
    
    dfa_pos = 0
    
    d.is_accepting[0] = False
    for val in nfa_states_rec[0]:
        if nfa.is_accepting[val]:
            d.is_accepting[0] = True
            break
    
    while dfa_pos < len(d.states):
        for sym in d.alphabet:
            s = set()
            for val in nfa_states_rec[dfa_pos]:
                if sym in nfa.states[val].transition:
                    for st in nfa.states[val].transition[sym]:
                        s.add(st.id)
            if not s:
                continue
            
            temp = copy.deepcopy(s)
            for val in s:
                temp.update(rec[val])
            s = temp
            
            if s not in nfa_states_rec:
                nfa_states_rec.append(s)
                d.states.append(State(len(d.states)))
                
                d.is_accepting[len(d.states)-1] = False
                for val in s:
                    if nfa.is_accepting[val]:
                        d.is_accepting[len(d.states)-1] = True
                        break
                ###test###
                # print(1,dfa_pos, nfa_states_rec.index(s),len(d.states))
                d.addTransition(d.states[dfa_pos], d.states[-1], sym)
                #len_states += 1
                
            else:
                ###test###
                # print(-1,dfa_pos, nfa_states_rec.index(s),len(d.states))
                
                d.addTransition(d.states[dfa_pos], d.states[nfa_states_rec.index(s)], sym)
        dfa_pos += 1
        # if dfa_pos >= len(d.states):
        #     break
    return d
    
    pass
# You should write this function.
# It takes an DFA and returns a NFA.
def dfaToNFA(dfa):
    n = NFA()
    n.states = copy.deepcopy(dfa.states)
    n.is_accepting = copy.deepcopy(dfa.is_accepting)
    n.alphabet = copy.deepcopy(dfa.alphabet)
    return n
    pass

def unionNFA(nfa1, nfa2):
    n = NFA()
    n.addStatesFrom(nfa1)
    n.addStatesFrom(nfa2)
    n.addTransition(n.states[0], n.states[len(nfa1.states)])
    return n
    pass

# You should write this function.
# It takes two regular expressions and returns a 
# boolean indicating if they are equivalent
def equivalent(re1, re2):
    n1,n2 = re1.transformToNFA(), re2.transformToNFA()
    
    # print(n1.is_accepting)
    # print(n2.is_accepting)
    
    d1,d2 = nfaToDFA(n1), nfaToDFA(n2)
    d1c,d2c = d1.complement(), d2.complement()
    n1c,n2c = dfaToNFA(d1c), dfaToNFA(d2c)
    n1c_u_n2, n1_u_n2c = unionNFA(n1c, n2), unionNFA(n1, n2c)
    d1c_u_d2, d1_u_d2c = nfaToDFA(n1c_u_n2), nfaToDFA(n1_u_n2c)
    d1c_u_d2_c, d1_u_d2c_c = d1c_u_d2.complement(), d1_u_d2c.complement()
    # n1c_u_n2_c, n1_u_n2c_c = dfaToNFA(d1c_u_d2_c), dfaToNFA(d1_u_d2c_c)
    
    # if True in d1c_u_d2_c.is_accepting.values() or True in d1_u_d2c_c.is_accepting.values():
    #     return False
    
    s1,s2 = d1c_u_d2_c.shortestString(), d1_u_d2c_c.shortestString()
    if s1!=float('inf') or s2!=float('inf'):
        return False
    
    ###test###
    # print(n1c_u_n2_c.is_accepting)
    # print(n1_u_n2c_c.is_accepting)
    
    return True
    
    pass



if __name__ == "__main__":
    def testNFA(strRe, s, expected):
        re = parse_re(strRe)
        # test your nfa conversion
        nfa = re.transformToNFA()
        
        ###test###
        
        # print(nfa.is_accepting)
        
        res = nfa.isStringInLanguage(s)
        if res == expected:
            print(strRe, " gave ",res, " as expected on ", s)
        else:
            print("**** ", strRe, " Gave ", res , " on " , s , " but expected " , expected)
            pass
        pass
    
    
    def testDFAComplement(strRe, s, expected):
        # test your dfa conversion
        re = parse_re(strRe)
        nfa = re.transformToNFA()
        dfa_o = nfaToDFA(nfa)
        
        dfa = dfa_o.complement()
        #####test#####
        # print(dfa.is_accepting)
        
        res = dfa.isStringInLanguage(s)
        if res == expected:
            print(strRe, " gave ",res, " as expected on ", s)
        else:
            print("**** ", strRe, " Gave ", res , " on " , s , " but expected " , expected)
            pass
        pass
    
    def testDFA(strRe, s, expected):
        # test your dfa conversion
        re = parse_re(strRe)
        nfa = re.transformToNFA()
        dfa = nfaToDFA(nfa)
        
        #####test#####
        # print(dfa.is_accepting)
        # print(dfa.states)
        # print(dfa.alphabet)
        # print(dfa.startS)
        # print(dfa.states[1].transition)
        
        res = dfa.isStringInLanguage(s)
        if res == expected:
            print(strRe, " gave ",res, " as expected on ", s)
        else:
            print("**** ", strRe, " Gave ", res , " on " , s , " but expected " , expected)
            pass
        pass

    # def testDFA(nfa, s, expected):
    #     # test your dfa conversion
    #     dfa = nfaToDFA(nfa)
    #     res = dfa.isStringInLanguage(s)
    #     if res == expected:
    #         print(strRe, " gave ",res, " as expected on ", s)
    #     else:
    #         print("**** ", strRe, " Gave ", res , " on " , s , " but expected " , expected)
    #         pass
    #     pass
    
    def testUnionNFA(strRe1, strRe2, s, expected):
        re1 = parse_re(strRe1)
        re2 = parse_re(strRe2)
        n1 = re1.transformToNFA()
        n2 = re2.transformToNFA()
        n = unionNFA(n1, n2)
        res = n.isStringInLanguage(s)
        if res == expected:
            print("Union(", strRe1, ", ",strRe2, ") = ", res, " as expected.")
        else:
            print("**** ", "Union(", strRe1, ", ",strRe2, ") = ", res, " but expected " , expected)
            pass
        
        
    def testShortestString(strRe, expected):
        re = parse_re(strRe)
        nfa = re.transformToNFA()
        dfa = nfaToDFA(nfa)
        res = dfa.shortestString()
        if res in expected:
            print("ShortestString(", strRe, ") = ", res, " as expected.")
        else:
            print("**** ", "ShortestString(", strRe, ") = ", res, " but expected " , expected)
            pass
        pass    

    def testEquivalence(strRe1, strRe2, expected):
        re1 = parse_re(strRe1)
        re2 = parse_re(strRe2)
        
        res = equivalent(re1, re2)
        if res == expected:
            print("Equivalence(", strRe1, ", ",strRe2, ") = ", res, " as expected.")
        else:
            print("**** ", "Equivalence(", strRe1, ", ",strRe2, ") = ", res, " but expected " , expected)
            pass
        pass

    def pp(r):
        print()
        print("Starting on " +str(r))
        re=parse_re(r)
        print(repr(re))
        print(str(re))
        pass

    # test your NFA:
    # testNFA('&', '', True)
    # testNFA('aa*', 'a', True)
    # testNFA('a', 'a', True)
    # testNFA('a', 'ab', False)
    # testNFA('ab', 'ab', True)
    # testNFA('a*', '', True)
    # testNFA('a*', 'a', True)
    # testNFA('a*', 'aaa', True)
    # testNFA('a*', 'ab', False)
    # testNFA('a*', 'ba', False)
    # testNFA('a*', 'b', False)
    # testNFA('a*b', 'aab', True)
    # testNFA('a*b', 'ab', True)
    # testNFA('a*b', 'b', True)
    # testNFA('a|b', '', False)
    # testNFA('a|b', 'a', True)
    # testNFA('a|b', 'b', True)
    # testNFA('a|b', 'ab', False)
    # testNFA('ab|cd', '', False)
    # testNFA('ab|cd', 'ab', True)
    # testNFA('ab|cd', 'cd', True)
    # testNFA('ab|cd*', '', False)
    # testNFA('ab|cd*', 'c', True)
    # testNFA('ab|cd*', 'cd', True)
    # testNFA('ab|cd*', 'cddddddd', True)
    # testNFA('ab|cd*', 'ab', True)
    # testNFA('((ab)|(cd))*', '', True)
    # testNFA('((ab)|(cd))*', 'ab', True)
    # testNFA('((ab)|(cd))*', 'cd', True)
    # testNFA('((ab)|(cd))*', 'abab', True)
    # testNFA('((ab)|(cd))*', 'abcd', True)
    # testNFA('((ab)|(cd))*', 'cdcdabcd', True)
    # testNFA('((ab|cd)*|(de*fg|h(ij)*klm*n|q))*', '', True)
    
    # testNFA('((ab|cd)*|(de*fg|h(ij)*klm*n|q))*', 'ab', True)
    testNFA('((ab|cd)*|(de*fg|h(ij)*klm*n|q))*', 'abcd', True)
    # testNFA('((ab|cd)*|(de*fg|h(ij)*klm*n|q))*', 'cd', True)
    # testNFA('((ab|cd)*|(de*fg|h(ij)*klm*n|q))*', 'dfgab', True)
    # testNFA('((ab|cd)*|(de*fg|h(ij)*klm*n|q))*', 'defg', True)
    # testNFA('((ab|cd)*|(de*fg|h(ij)*klm*n|q))*', 'deeefg', True)
    # testNFA('((ab|cd)*|(de*fg|h(ij)*klm*n|q))*', 'hkln', True)
    # testNFA('((ab|cd)*|(de*fg|h(ij)*klm*n|q))*', 'q', True)
    # testNFA('((ab|cd)*|(de*fg|h(ij)*klm*n|q))*', 'hijijkln', True)
    # testNFA('((ab|cd)*|(de*fg|h(ij)*klm*n|q))*', 'hijijklmmmmmmmmmmn', True)
    
    testDFA('&', '', True)
    testDFA('(&)', '', True)
    testDFA('&', 'a', False)
    testDFA('a', '', False)
    testDFA('a', 'a', True)
    testDFA('a', 'ab', False)
    testDFA('(a)', 'a', True)
    testDFA('((a))', 'a', True)
    testDFA('ab', 'ab', True)
    testDFA('abc', 'abc', True)
    testDFA('abcd', 'abcd', True)
    testDFA('a(bc)d', 'abcd', True)
    testDFA('a*', '', True)
    testDFA('a*', 'a', True)
    testDFA('a*', 'aaa', True)
    testDFA('a*b*', 'a', True)
    testDFA('a*b*', 'ab', True)
    testDFA('a*b*', 'b', True)
    testDFA('a*b*', 'aba', False)
    testDFA('a|b', '', False)
    testDFA('a|b', 'a', True)
    testDFA('a|b', 'b', True)
    testDFA('a|b', 'ab', False)
    testDFA('ab|cd', '', False)
    testDFA('ab|cd', 'ab', True)
    testDFA('ab|cd', 'cd', True)
    testDFA('ab|cd*', '', False)
    testDFA('ab|cd*', 'c', True)
    testDFA('ab|cd*', 'cd', True)
    testDFA('ab|cd*', 'cddddddd', True)
    testDFA('ab|cd*', 'ab', True)
    testDFA('((ab)|(cd))*', '', True)
    testDFA('((ab)|(cd))*', 'ab', True)
    testDFA('((ab)|(cd))*', 'cd', True)
    testDFA('((ab)|(cd))*', 'abab', True)
    testDFA('((ab)|(cd))*', 'abcd', True)
    testDFA('((ab)|(cd))*', 'cdcdabcd', True)
    testDFA('((ab|cd)*|(de*fg|h(ij)*klm*n|q))*', '', True)
    testDFA('((ab|cd)*|(de*fg|h(ij)*klm*n|q))*', 'ab', True)
    testDFA('((ab|cd)*|(de*fg|h(ij)*klm*n|q))*', 'abcd', True)
    testDFA('((ab|cd)*|(de*fg|h(ij)*klm*n|q))*', 'cd', True)
    testDFA('((ab|cd)*|(de*fg|h(ij)*klm*n|q))*', 'dfgab', True)
    testDFA('((ab|cd)*|(de*fg|h(ij)*klm*n|q))*', 'defg', True)
    testDFA('((ab|cd)*|(de*fg|h(ij)*klm*n|q))*', 'deeefg', True)
    testDFA('((ab|cd)*|(de*fg|h(ij)*klm*n|q))*', 'hkln', True)
    testDFA('((ab|cd)*|(de*fg|h(ij)*klm*n|q))*', 'q', True)
    testDFA('((ab|cd)*|(de*fg|h(ij)*klm*n|q))*', 'hijijkln', True)
    testDFA('((ab|cd)*|(de*fg|h(ij)*klm*n|q))*', 'hijijklmmmmmmmmmmn', True)
    testDFA('((a|b)*|b)*', 'ababb', True)
    
    testDFAComplement('&', '', False)
    testDFAComplement('(&)', '', False)
    testDFA('&', '', True)
    testDFAComplement('&', 'a', True)
    testDFAComplement('a', '', True)
    testDFAComplement('a', 'a', False)
    testDFA('a', 'ab', False)
    testDFAComplement('a', 'ab', True)
    testDFAComplement('(a)', 'a', False)
    testDFAComplement('((a))', 'a', False)
    
    
    testUnionNFA('a', 'b', 'ab', False)
    testUnionNFA('a', 'b', 'ba', False)
    testUnionNFA('a', 'b', 'c', False)
    testUnionNFA('a', 'b', 'a', True)
    testUnionNFA('a', 'b', 'b', True)
    testUnionNFA('a', '&', 'a', True)
    testUnionNFA('a', '&', 'b', False)
    testUnionNFA('a', '&', '', True)
    
    testShortestString('a', ['a'])
    testShortestString('a*', [''])
    testShortestString('a|b', ['a','b'])
    testShortestString('a|b|c', ['a','b','c'])
    testShortestString('a|ab*c|&|d', [''])
    
    testEquivalence('((a|b)*|b)*','(b)((a|b)*|b)*',False)
    testEquivalence('a*','aa*',False)
    testEquivalence('a|b', 'a|((a|b)|b)', True)
    testEquivalence('(a|b)*', '(a|((a|b)|b))*', True)
    testEquivalence('&', '&&', True)
    testEquivalence('&', '&&a', False)
    testEquivalence('((ab|cd)*|(de*fg|h(ij)*klm*n|q))*', 'hijijklmmmmmmmmmmn',False)
    testEquivalence('((ab|cd)*|(de*fg|h(ij)*klm*n|q))*', '((ab|cd)*|(de*fg|h(ij)*klm*m*n|q))*',True)
    
    pass
    
