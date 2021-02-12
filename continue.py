# __Author__ __Lencof__
# continue.py

while True:
    s = input('Enter anything : ')
    if s == 'exit':
        break
    if len(s) < 3:
        print('Too few')
        continue
    print('Enterrd string of sufficient lenght')
