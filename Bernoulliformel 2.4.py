import math
from time import sleep

# from Maximilian Stacherowski and David Völlm

def binominalkoeffizient(n,k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

def bernoulliformel(n,k,p):
    return binominalkoeffizient(n,k) * math.pow(p,k) * pow(1.0 - p,n - k)

print("The better calculator!")   
Art = input("Bernoulli: with k(0)[n, p, k]; without k(1)[n, p]; exit(x):   ")
while Art != "x":
    if Art == "1":
        n = int(eval(input("    n: ")))
        p = float(eval(input("    p: ")))
        for k in range(n+1):
            print("   k=" + str(k) + ": " + str(bernoulliformel(n,k,p)))

        while input(" continue(enter); exit(x):   ") != "x":
            n = int(eval(input("    n: ")))
            p = float(eval(input("    p: ")))
            for k in range(n+1):
                print("   k=" + str(k) + ": " + str(bernoulliformel(n,k,p)))

    else:
        if Art == "0":
            n = int(eval(input("    n: ")))
            p = float(eval(input("    p: ")))
            k = int(eval(input("    k: ")))
            print("  =" + str(bernoulliformel(n,k,p)))

            while input(" continue(enter); exit(x):   ") != "x":
                n = int(eval(input("    n: ")))
                p = float(eval(input("    p: ")))
                k = int(eval(input("    k: ")))
                print("   =" + str(bernoulliformel(n,k,p)))


        else:
                print("  You need to type:\n    0: For the normal Bernoulliformular with n, p, k \n    1: For every possible k from 0 to n with the parameters n, p \n    x: For closing the programm\n")
        
    Art = input("with k(0)[n, p, k]; without k(1)[n, p]; exit(x):   ")