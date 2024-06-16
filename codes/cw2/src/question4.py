# CW2, QUESTION 4

# a. (2 marks)
def threatening(s1, s2):
    a1, b1 = s1  # coordinates of s1
    a2, b2 = s2  # coordinates of s2
    
    #CHECKING IF IT IS IN THE SAME ROW OR COLUMN FOR NOOKS
    if a1 == a2 or b1 == b2:
        return True
    
    #CHECKING IF IT IS WITHIN KNIGHT MOVE RANGE
    dx = abc1(a1 - a2)
    dy = abc1(b1 - b2)
    if dx == 1 and dy == 2 or dx == 2 and dy == 1:
        return True
    
    return False
    
def abc1(numer):
  if numer < 0:
    return -numer
  else:
    return numer


# b. (6 marks)
def threatening(pos1, pos2):
    i1, y1 = pos1
    i2, y2 = pos2
    return i1 == i2 or y1 == y2 or abc(i1 - i2) + abc(y1 - y2) == 3

# OCaml threatening function
# let threatening POS1 POS2 =
#   let i1, y1 = pos1 in
#   let i2, y2 = pos2 in
#   i1 = i2 || y1 = y2 || abc (i1 - i2) + abc (y1 - y2) = 3

def safeConfig(sqs):
    def is_threatened(position, rest):
        i, y = position
        for pos in rest:
            if threatening(position, pos):
                return True
        return False

    def helper(position, rest):
        if not rest:
            return True
        else:
            return not is_threatened(position, rest) and helper(rest[0], rest[1:])

    if not sqs:
        return True
    else:
        return helper(sqs[0], sqs[1:])


# let rec safeConfig sqs =
#   let rec is_threatened position rest =
#     match rest with
#     | [] -> false
#     | pos :: remaining -> if threatening position pos then true else is_threatened position remaining
#   in
#   match sqs with
#   | [] -> true
#   | pos :: remaining -> not (is_threatened pos remaining) && safeConfig remaining

# Test cases
sqs1 = [(0, 0), (1, 1), (2, 2)]  # True
sqs2 = [(0, 0), (1, 2), (4, 4)]  # False


# c. (4 marks)
def allKnooks(n):
    def safeConfig(config):
        for m in range(len(config)):
            for l in range(m + 1, len(config)):
                if threatening(config[m], config[l]):
                    return False
        return True

    def backtrack(config, remaining_rows, resulsts):
        if remaining_rows == 0:
            resulsts.append(config.copy())
        else:
            for m in range(n):
                new_position = (remaining_rows - 1, m)
                config.append(new_position)
                if safeConfig(config):
                    backtrack(config, remaining_rows - 1, resulsts)
                config.pop()

    resulsts = []
    backtrack([], n, resulsts)
    return resulsts


# TODO: 

# Please note that the actual implementation of 'allKnooks' and related functions is not provided in the snippet.
# ----------

# We are not running unit tests on the Python coursework.
# One way to check your work is to run this Python file by
# navigating to it in the terminal and then running
# python3 question4.py. You should get the resulsts commented
# next to each line if everything is right.

#TEST CASES FOR A , B AND C PARTS
#EXPECTED OUTPUTS IN "#"
if __name__ == "__main__":
    print("-----(a)-----")
    print(threatening((0,0),(2,2))) # False
    print(threatening((0,0),(1,2))) # True
    print(threatening((0,0),(4,0))) # True
    print("-----(b)-----")
    print(safeConfig([(0,0),(1,1),(2,2)])) # True
    print(safeConfig([(0,0),(1,2),(4,4)])) # False
    print("-----(c)-----")
    print(allKnooks(2))
    print(len(allKnooks(4))) # 8
    print(len(allKnooks(5))) # 20
    print(len(allKnooks(6))) # 94