# __Author__ __Lencof__
# continue.py

while True: 
    s = input('Enter anything : ') # your text
    if s == 'exit': # your text 
        break 
    if len(s) < 3: # < 3 more
        print('Too few') # your text
        continue 
    print('Enterrd string of sufficient lenght') # your text

# $ python continue.py
'''Enter anything : 24
Too few
Enter anything :'''
