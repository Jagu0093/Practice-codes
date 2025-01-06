def can_see_stage(seats):
    # Your code here
    for i in range(len(seats)):
        for j in range(i+1,len(seats)):
            if seats[j][i] >= seats[i][i]:
                return False
    return True