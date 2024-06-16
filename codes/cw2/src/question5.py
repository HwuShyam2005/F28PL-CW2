# CW2, QUESTION 5

# a. (5 marks) 

def toDecimal(n):
    #TO KEEP AN TRACK OF THE REMAINDERS AND POSITIONS
    remainder_dict = {}   
    
    #AN LIST FOR STORING THE NON_REPEATING DIGITS
    non_repeating = []    
    
    #AN LIST FOR STORING THE REPEATING DIGITS
    repeating = []        
    
    #STARTING WITH THE NUMERATOR AS 1 FOR UNIT FRACTION
    numerator = 1         
    
    #TRACKING THE POSITION OF EACH DIGITS IN THE EXPANSION
    position = 0          
    
    # WHILE THE NUMERATOR IS NOT ZERO
    #UNTIL REPEATING CYCLE IS FOUND OR THE DIVISION PROCESS ENDS
    while numerator != 0:
        #CONDITION FOR THE NUMERATOR BEING AN REMAINDER_DICT
        # IF SO THEN THE REPEATING CYCLE HAS BEEN FOUND AND IDENTIFY THE START OF THE REPEATING CYCLE  
        if numerator in remainder_dict:
            repeating_start = remainder_dict[numerator]
            
            #SEPERATION OF REPEATING DIGITS FROM THE NON_REPEATING DIGITS
            repeating = non_repeating[repeating_start:]
            non_repeating = non_repeating[:repeating_start]
            break
        
        #CONDITION FOR NUMERATOR NOT AN REMAINDER_DICT
        else:
            #STORING THE PRESENT NUMERATOR AND ITS POSITION
            remainder_dict[numerator] = position
            
            #APPLYING DIVISION TO OBTAIN NEXT DIGIT
            quotient, numerator = divmod(numerator * 10, n)
            
            #APPENDING THE QUOTIENT TO NON_REPEATING
            non_repeating.append(quotient)
            
            #ADDING THE POSITION FOR NEXT DIGIT
            position += 1
    
    #RETURNING THE BOTH REPEATING AND NON_REPEATING LISTS
    return non_repeating, repeating


# TODO: explain your code in a comment below.

#IN THIS CODE THERE IS A FUNCTION CALLED TODECIMAL WHICH TAKES INTEGER N AS AN INPUT .
#CREATES A DECIMAL EXPANSION 1/N AND SEPARATES EXPANSION INTO TWO PARTS (REPEATING AND NON_REPEATING)

#VARIABLES INITIALIZATIONS ->
# "REMAINDER_DICT" (DICTIONARY FOR KEEPING TRACK OF REMAINDERS AND THEIR POSITION FOUND DURING DIVISION)
# "NON_REPEATING AND REPEATING" (TWO LISTS FOR STORING NON_REPEATING AND REPEATING DIGITS RESPECTIVELY)
# "NUMERATOR" (INITIALIZED TO 1 AS WE ARE WORKING WITH UNIT FRACTIONS)
# "POSITION" (USED FOR TRACKING POSITION EACH DIGIT IN THE EXPANSION)

#THE DIVISION LOOP ->
#WE WILL CHECK IF THE NUMERATOR IS NOT EQUAL TO ZERO
#WHICH INDICATES THE END OF THE DIVISION PROCESS
#WE CHECK IF THE NUMERATOR IS PRESENT IN REMAINDER_DICT AS IT INDICATES THE REPEATING CYCLE IS FOUND

#CONDITION 1 (IF THE NUMERATOR IS PRESENT IN REMAINDER_DICT) ->
#IDENTIFY START OF REPEATING CYCLE
#SEPERATE THE REPEATING DIGITS FROM THE NON_REPEATING ONES 
#BREAK THE LOOP AS DIVISION PROCESS IS COMPLETE

#CONDITION 2 (IF NUMERATOR IS NOT PRESENT IN THE REMAINDER_DICT) ->
#STORE CURRENT NUMERATOR IN THE POSITION IN REMAINDER_DICT
#APPLY DIVISION TO OBTAIN NEXT DIGIT IN THE EXPANSION
#APPEND THE QUOTIENT TO THE NON_REPEATING LIST
#ADD THE POSITION AND RETURN THE RESUlst

#FINALLY RETURN BOTH NON_REPEATING AND REPEATING LISTS
#REPEATING LIST WILL CONSIST OF DIGITS THAT REPEAT IN DECIMAL EXPANSION
#NON_REPEATING LIST WILL CONSIST OF DIGITS BEFORE REPEATING CYCLE STARTS


# b. (3 marks)
# DEFINE A CLASS CALLED FRACTION CLASS FOR HANDLING FRACTION OPERATIONS
class MyFraction:
   #INITIALIZE FRACTION WITH NUMERATOR AND DENOMINATOR
    def __init__(self, numerator, denominator=1):
     #IF THE DENOMINATOR IS 0 AND IF SO , WE RAISE AN ERROR
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")

        #TO CALCULATE GREATEST COMMON DIVISOR FOR SIMPLIFYING THE FRACTION
        gcd_val = self._gcd(numerator, denominator)
        
        #NORMALIZE THE FRACTION BY DIVIDING BOTH NUMERATOR AND DENOMINATOR WITH GREATEST COMMON DIVISOR
        self.numerator = numerator // gcd_val
        self.denominator = denominator // gcd_val

        #NORMALIZE NEGATIVE FRACTIONS FOR HAVING THE NEGATIVE SIGNS ONLY ON THE NUMERATOR
        if self.denominator < 0:  # NORMALIZE NEGATIVE FRACTIONS
            self.numerator *= -1
            self.denominator *= -1
    
    #DEFINE A METHOD CALLED GCD TO CALCULATE GREATEST COMMON DIVISOR BY USING EUCLIDEAN ALGORITHM
    def _gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    #A METHOD FOR APPROXIMATING THE FRACTION WITH AN DENOMINATOR NOT BIGGER THAN THE LIMIT
    def limit_denominator(self, limit):
        if self.denominator <= limit:
            return self
        else:
            #ROUNDING THE APPROXIMATE VALUE WITH THE NEAREST INTEGER
            approx = round(self.numerator / self.denominator)
            #RETURNING THE APPROXIMATE FRACTION WITH AN DENOMINATOR OF 1
            return MyFraction(approx, 1)

    #A METHOD TO OVERRIDE ADDITIONAL OPERATIONS FOR FRACTIONS
    def __add__(self, other):
        new_num = self.numerator * other.denominator + other.numerator * self.denominator
        new_denom = self.denominator * other.denominator
        return MyFraction(new_num, new_denom)

    #A METHOD TO OVERRIDE STRING REPRESENTATION OF FRACTION
    def __str__(self):
        if self.denominator != 1:
            return f"{self.numerator}/{self.denominator}"
        else:
            return str(self.numerator)

#AN FUNCTION TO CONVERT DECIMAL EXPANSION INTO AN SIMPLIFIED FRACTION
def toFrac(nonrep, rep):
    nonrep_val = sum(digit * 10 ** (len(nonrep) - i - 1) for i, digit in enumerate(nonrep))
    rep_val = sum(digit * 10 ** (1 - i - len(rep)) for i, digit in enumerate(rep))

    nonrep_frac = MyFraction(nonrep_val, 10 ** len(nonrep))
    rep_frac = MyFraction(rep_val, (10 ** len(nonrep)) * ((10 ** len(rep)) - 1)) if rep else MyFraction(0)

    total_frac = nonrep_frac + rep_frac
    simplified_frac = total_frac.limit_denominator(10000)

    return simplified_frac.numerator, simplified_frac.denominator

# TODO: explain your code in a comment below.

#WE FIRST DEFINE A CLASS CALLED MY FRACTION TO HANDLE FRACTION OPERATIONS
#WE INITIALIZE FRACTION WITH NUMERATOR AND DENOMINATOR
#WE ALSO CHECK IF THE DENOMINATOR IS 0 AND IF SO , WE RAISE AN ERROR
#THEN WE CALCULATE GREATEST COMMON DIVISOR FOR SIMPLIFYING THE FRACTION
#THEN WE NORMALIZE THE FRACTION BY DIVIDING BOTH NUMERATOR AND DENOMINATOR WITH GREATEST COMMON DIVISOR

#WE THEN DEFINE A METHOD CALLED GCD TO CALCULATE GREATEST COMMON DIVISOR BY USING EUCLIDEAN ALGORITHM
#THEN AN METHOD TO APPROXIMATE THE FRACTION WITH AN DENOMINATOR NOT BIGGER THAN THE LIMIT
#WE ALSO DO AN ELSE CONDITION FOR INSIDE HERE BY ROUNDING THE APPROXIMATE VALUE TO NEAREST INTEGER AND RETURN 
#APPROXIMATE FRACTION WITH DENOMINATOR OF 1
#ONE METHOD TO OVERRIDE ADDITIONAL OPERATIONS FOR FRACTIONS
#ANOTHER METHOD IS ADDED TO OVERRIDE STRING REPRESENTATION OF FRACTION

#THEN A FUNCTION TO CONVERT DECIMAL EXPANSION INTO AN SIMPLIFIED FRACTION
#AND FINALLY RETURN WITH SIMPLIFIED_FRAC.NUMERATOR AND SIMPLIFIED_FRAC.DENOMINATOR

# ----------

# We are not running unit tests on the Python coursework.
# One way to check your work is to run this Python file by
# navigating to it in the terminal and then running
# `python3 question5.py`. You should get the resulsts commented
# next to each line if everything is right.

#TEST CASES FOR BOTH A AND B PARTS 
#EXPECTED OUTPUTS IN "#"
if __name__ == "__main__":
    print("-----(a)-----")
    print(toDecimal(4))  # ([2,5],[])
    print(toDecimal(12)) # ([0,8],[3])
    print(toDecimal(7))  # ([],[1,4,2,8,5,7])
    print("-----(b)-----")
    print(toFrac([2,5],[]))  # (1,4)
    print(toFrac([0,8],[3])) # (1,12)
    print(toFrac([1],[3]))   # (2,15)
