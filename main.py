def problem_1(text_file):
    counter = 0
    for line in text_file:
        for char in line:
            if char != "\n":
                counter += 1
        counter = 0

def problem_2(text_file):
    egg_size = {1:0,
                2:0,
                3:0,
                4:0,
                5:0}
    num_nests = len(text_file)
    rounds = []
    for i in range(len(text_file)):
        nest = text_file[i]
        for key in egg_size:
            if nest[0] == key:
                egg_size[key] += 1
                continue
            if  nest[1] == key:
                egg_size[key] += 1
                continue
            else:
                egg_size[key] = 0
        max_key = max(egg_size, key=egg_size.get)
        rounds.append((max_key,egg_size[max_key]))



    return rounds

#if (nest[0] == text_file[n-1][0] or nest[0] == text_file[n-1][1]) and (nest[1] == text_file[n-1][0] or nest[1] == text_file[n-1][1]):
#                    egg_size[nest[0]] += 1
         #           egg_size[nest[1]] += 1
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