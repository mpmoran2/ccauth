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
ccsum = 0
double_list = []
double_string = ""

number = list(card_num)

for (idx,val) in enumerate(number):
    if idx % 2 !=0: #odd
        odd_sum += int(val)
    else: #even
        double_list.append(int(val)*2)

for x in double_list:
    double_string += str(x)

new_double = list(double_string)

for x in new_double:
    even_sum += int(x)

ccsum = odd_sum + even_sum
if ccsum % 10 == 0:
    print("Card Validated!")
else:
    print("Invalid Card Data")


