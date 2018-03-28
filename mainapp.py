import itertools

all_permutations = list(itertools.product(['L', 'R'], repeat=13)) # 13


file = open('zadanie_3_triangle_small.txt', 'r')

raw_file_tab = []
final_tab = []

for line in file:
    raw_file_tab.append(line.split(' '))

for tab in raw_file_tab:
    new_tab_element = []
    for element in tab:
        if element:
            new_tab_element.append(int(element.rstrip('\n')))
    final_tab.append(new_tab_element)


print('All possible permutations: ', len(all_permutations))

for line in final_tab:
    print(line)
print('\n')

the_biggest_sum = 0

for permutation in all_permutations:

    this_permutation_sum = final_tab[0][0]
    row = 1


    if permutation[0] == 'L' and row == 1:
        index = 0
    elif permutation[0] == 'R' and row == 1:
        index = 1

    for i in range(0, len(permutation)):
        if permutation[i] == 'L':
            pass

        elif permutation[i] == 'R' and row != 1:
            index += 1


        this_permutation_sum += final_tab[row][index]
        if the_biggest_sum < this_permutation_sum:
            the_biggest_sum = this_permutation_sum

        row += 1

print('The biggest sum: ', the_biggest_sum)