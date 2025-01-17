#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd


# In[4]:


def check_compatible(text):
    count=0
    brackets = {'}': '{', ']': '[', ')': '('}
    
    for i,char in enumerate(text):   
        if char in brackets.values():
            count+=1
        elif char in brackets.keys():
            count-=1
        else:
            pass
        
    if count !=0:
        print(f"Niezgodna liczba nawiasów.")
    else:
        print("Zgodna liczba nawiasów.")  
        
        
def check_brackets(text):
    
    check_compatible(text)
    
    stack = []
    brackets = {'}': '{', ']': '[', ')': '('}
    errors = []   
    
    for i, char in enumerate(text):
        # Jeśli znak jest nawiasem otwierającym
        if char in brackets.values():

            if char == '(' and any(item[0] == '(' for item in stack):
                errors.append((char, i))
                
            # Jeśli znak jest nawiasem '(' i na stosie są nawiasy '{'i '[' lub '[' lub '{' lub stos jest pusty
            elif char == '(' and (
                                  any(item[0] == '{' for item in stack) and any(item[0] == '[' for item in stack) \
                                  or any(item[0] == '[' for item in stack) \
                                  or any(item[0] == '{' for item in stack) \
                                  or stack == []
                                    ):
                stack.append((char, i))
                
            # Jeśli znak jest nawiasem '[' i na stosie jest nawias '['
            elif char == '[' and any(item[0] == '[' for item in stack):
                errors.append((char, i)) 
                
            # Jeśli znak jest nawiasem '[' i na stosie jest nawias '{' lub stos jest pusty
            elif char == '[' and ( 
                                  any(item[0] == '{' for item in stack) or stack == []
                                 ):
                stack.append((char, i))

            # Jeśli znak jest nawiasem '[' i na stosie jest nawias '('    
            elif char == '[' and any(item[0] == '(' for item in stack):
                stack.append((char, i))

            # Jeśli znak jest nawiasem '{' i  stos jest pusty
            elif char == '{' and stack == []: 
                stack.append((char, i))            

            # Jeśli znak jest nawiasem '{' i na stosie jest nawias '{'    
            elif char == '{' and any(item[0] == '{' for item in stack): 
                errors.append((char, i)) 

            # Jeśli znak jest nawiasem '{' i na stosie jest nawias '(' albo '['
            elif char == '{' and ( 
                                  any(item[0] == '(' for item in stack) or any(item[0] == '[' for item in stack) 
                                 ):
                stack.append((char, i))             
            else:
                errors.append((char, i)) 

        # Jeśli znak jest nawiasem zamykającym
        elif char in brackets.keys():
            if stack and stack[-1][0] == brackets[char]: 
                stack.pop()

            # Jeśli stos jest pusty, to brak otwierającego nawiasu   
            elif not stack:
                errors.append((char, i))

            elif char in brackets.keys():
               # Zmienna unmatched śledzi, czy znaleziono pasujący nawias otwierający
                unmatched = True
                for _ in range(len(stack)):
                    if stack and stack[-1][0] == brackets[char]:
                        stack.pop()
                        unmatched = False
                        break
                    else:
                        errors.append(stack.pop())
                # Dodaj, jeśli brak pasującego otwierającego nawiasu
                if unmatched:  
                    errors.append((char, i))
                    
    # Pozostałe na stosie nawiasy otwierające są nadmiarowe
    while stack:
        char, i = stack.pop()
        errors.append((char, i))
    
    return errors


text = "{[()([]}"
# text = ")){[()([]}"
# text = "{([)]}"
# text = "(][()]}()(("
# text = "({([()](}[()]()("

errors = check_brackets(text)

if errors:
    print(f"Tekst: {text} - niepoprawne nawiasy znalezione na pozycjach:")
    for char, i in errors:
        print(f"Nawias '{char}' na pozycji {i}")
else:
    print("Wszystkie nawiasy są poprawne.")

