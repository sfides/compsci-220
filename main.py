def problem_1(text_file):
    counter = 0
    for line in text_file:
        for char in line:
            if char != "\n":
                counter += 1
        counter = 0

def problem_2(text_file):
    lines = 0
    num = 0
    valid = {}

    for i in range(len(text_file)):
        valid[text_file[i][0]] = [0,num] #grouping, num time occured
        valid[text_file[i][1]] = [0,num]
    for num_nest in range (len(text_file)):
        for k in range(len(text_file)):
            valid[text_file[k][0]][1] +=1  # grouping, num time occured
            valid[text_file[k][1]][1] +=1
            valid[text_file[k][0]][0] = num_nest  # grouping, num time occured
            valid[text_file[k][1]][0] = num_nest



    return valid

example_input = ((3,5),
                 (4,5),
                 (1,3))
#             if egg not in valid:
 #               lines += 1
  #              lines = 0
   #             valid[egg] = lines
    #        if egg in valid:
     #           valid[egg] += 1 ##
print(problem_2(example_input))