import random

def beststr(n):
    def rndchr():
        x=random.randrange(2)
        if x==0:
            return 'a'
        return 'b'
    lena = random.randrange(1,n+1)
    ans = []
    ans.extend([rndchr()]*lena)
    ans.extend([rndchr()]*(n-lena))
    return "".join(ans)
  
print(beststr(10))