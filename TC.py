#often times in programming we have to import modules that contain code we can use
#itertools is going to help with permutations  
import itertools
 
#this is called a dictonary, and it is basically a list of keys (in this case the numbers we are taking) and their values (their factors)
factors=dict([
   (2,[1]),
   (3,[1]),
   (4,[1,2]),
   (5,[1]),
   (6,[1,2,3]),
   (7,[1]),
   (8,[1,2,4]),
   (9,[1,3]),
   (10,[1,2,5]),
   (12,[1,2,3,4,6]) 
])

#this is called a function. Similar to math, you can put an imput and manipulate it to get an output. That is what the () are for. 
#In this case, though, I am programming something inside the function and having it run at the end 
def taxcollectorgame (): 
   
    #this variable is going to hold the max value of "my total" 
    #we are starting both of these variables to 0, and they will be updated throughout the program
    maxmt = 0
    count = 0


    factorsOfList = [4,6,8,9,10,12]
    possibleOrderings = list(itertools.permutations(factorsOfList))
    #this finds all the permutations of a list (or n!)
    #in this example I am using 0, 1, and 2 (which would be 3 values so 3! is 6)
    # this will return a list of,lists [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)] of n!
    # to go through each list you can do
    for items in possibleOrderings:
        #this is the print command: it will print what you say within the quotes or print a variable if you write the variable name 
        print("new order")
        count = count + 1
        #there are only two prime numbers that are not factors of other numbers meaning that we will get one and the tax collector will get the other. 
        #those two are 7 and 11, so we will no matter what take the bigger one of the two 
        mt = 11
        tct = 1
        #a very useful tool in python is lists, so here I am creating 3 lists that will be used in the rest of the program
        #they contain a list of values that we can manipulate 
        used = list()
        taken = list()
        double = list()
        for item in items:
            pick = item

            
            print('pick :' + str(pick))
            print('used: ' + str(used))
            print('taken: ' + str(taken))
            if(pick == 11): 
                continue
            if(len(factors[pick])>1 and pick not in used):
                #this is appending the list with our pick (bacially adding the value to the list)
                used.append(pick)
                #these types of commands filter the lists
                #the first one is saying that we are taking the list without the 1 
                #the second says we are filtering out the values in taken (this is the list with factors we already used)
                #this makes sure we don't duplicate the numbers that have already been crossed off
                listWithoutOne = [x for x in factors[pick] if x != 1]
                listWithoutOneOrTaken = [x for x in listWithoutOne if x not in taken]
                print('list without one or taken: ' + str(listWithoutOneOrTaken))
                #this is taking the sum of the list
                tm = sum(listWithoutOneOrTaken) 
                tct = tct + tm  
                print('tct ' + str(tct)) 
                taken.extend(listWithoutOneOrTaken)
                if (tm > 0 and pick not in taken):
                    mt = mt + pick
                    print('mt ' + str(mt))                
                    if(pick == 6  or pick == 4): 
                        taken.append(pick)
                else: 
                    print('mt ' + str(mt)) 
                    double.append(pick) 

            #this is saying once the list length is 6 (meaning we have chosen 4, 6, 8, 9, 10, and 12) we are going to do this
            if(len(used) == 6): 
                doubleWithoutTaken = [x for x in double if x not in taken]
                print('double without taken: ' + str(doubleWithoutTaken))
                extra = sum(doubleWithoutTaken)
                #this is adding the 7 to the tax collector, becuase it would be left over (after I can't take any more turns)
                tct = tct + 7 + extra 
                print('my total:' + str(mt))
                #this is saying if the my total is greater than the current max, then update it to the max 
                #this will keep track of the max as the program goes on
                if (mt>maxmt): 
                    maxmt = mt
                print('tax collector total: ' + str(tct))
                break
    print('\nmax my total: ' + str(maxmt))
    ntct = 78 - maxmt 
    print('tax collector total: ' + str(ntct)) 
    print('this program tried '+ str(count) + ' solutions!')
    #and sometimes it is fun to make a joke at the end of the program after all the troubleshooting 
    print('Tax collector program is out')
    print(':o zzzzz ahhh zzzzz ahhh zzzz :o')

#this is the line that runs the function
taxcollectorgame()

 














    