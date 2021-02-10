# __Author__ __Lencof__
# if.py

number = 70 # you figures 
guess = int(imput('Please enter an integer :')) # your text

if guess == number: # check if they are both the same
    print('Congratulations, you guessed it.') # your text
    print('Although they did not win any prize!') # your text
elif guess < number: # number more
    print('No hidden number is slightly larger than that.') # your text
    
else: 
    print('No, the hidden number is slightly larger than that.') # your text
  
print('Completed') # your text
