#!/bin/python3
import os
import sys
import re


#
# Complete the buildString function below.
#
def buildString(a, b, s):
    total = 0
    string = ""
    i = 0
    while i < len(s):        
        maior = 0
        if re.search(s[i], string):            
            itert = re.finditer(s[i], string)
            indices = [m.start(0) for m in itert]          
            indice = 0
            for j in range(len(indices)):               
                repete = 1
                cont = 0
                parou = False    
                while parou == False:                                 
                    if i + repete < len(s) and indices[j] + repete < len(string): 
                        if string[indices[j] + repete] == s[i + repete]:   
                            repete += 1
                            cont += 1    
                        else:                            
                            parou = True
                    else:
                        parou = True
                if maior < cont:
                    maior = cont
                    indice = indices[j]
            
            k = 0
            string += s[i]
            while k < maior:
                string += s[indice + k + 1]
                k += 1
            if maior == 0:
                total += a
            else:
                total += b 
            i = i + maior 
        else:
            string += s[i]  
            total +=  a
        i += 1
    return (total)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nab = input().split()

        n = int(nab[0])

        a = int(nab[1])

        b = int(nab[2])

        s = input()

        result = buildString(a, b, s)
        print(result)
        fptr.write(str(result))
        fptr.write('\n')


    fptr.close()
