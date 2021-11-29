from P_person import P_pers
from V_person import V_pers
from generate_component import generate 


def fiatShamir(Victor, Peter):
    for i in range(100):
        t = Peter.generateT()
        c = Victor.generateBit(t)
        s = Peter.calculateChecker(c)
        if(not Victor.check(s)):
            return False
    return True

def main():
    n, x = generate()

    Victor = V_pers(n, x)
    Peter = P_pers(n, 6198565)


    if fiatShamir(Victor, Peter):
        print("Bent vagy")
    else:
        print("Csalóóó")
    
    
    

if __name__ == "__main__":
    main()