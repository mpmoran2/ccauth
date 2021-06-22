# Lhon's Algorithm
    # save number
    # assign index value to the string for each intiger
    # sum of odds
    # collect evens
        #find double of each intiger
        # if double digits, at them together ex: 10 is 1+0=1 
        # sum of the evens
    # add the 2 sums together
    # divide by 10
        #if remainder is 0 it is valid

# do the simpilist approach then optimize

card_num = "5610591081018250"
odd_sum = 0
even_sum = 0
number = list(card_num)

for (idx,val) in enumerate(number):
    if idx % 2 !=0:
        odd_sum += int(val)
    else:
        pass

print(odd_sum)