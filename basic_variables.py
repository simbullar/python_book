#very basic demonstration of variables
fred = 100
print(fred)

#more complicated  variables
fred = 200
john = fred
print(john)

#just rebranding of first demonstrantion
coins_amount = 200
print(coins_amount)

#coins!!

found_coins = 20
magic_coins = 10 #amount of new coins appearing every day
lost_coins = 3 # amounts of coins disappearing every week
#how many coins will we have after an year
#btw there is 52 weeks and 365 days in year so...
outcome = found_coins + magic_coins * 365 - 52 * lost_coins # thats basically amount of coins after a year
print(outcome)
# so why we use variables? well, with variables we can easily change almost everything without breaking the code!
# probably you dont understand, so i'll explain
# so if we just change something like...
#lost_coins = 2     # this and print the outcome...
#print(outcome)     #like this...
# the outcome is gonna be the same exept there's not 156 lost coins in total(that would be if every week disapeared 3 coins)...
# but only 104 lost coins! and it is why I prefer variables and not basic math
# thats not very useful, but with time we'll explore more and more useful things