# Click on 'Submit' to view the results
# Click on 'Next' to proceed

sample_list = [5, 3, 2, 4, 1]

print(sample_list)          # print command for a list displays the list
print(sample_list[2])       # output specific index from the list
print(sample_list[-3])      # negative indexing of the list
print(sample_list[1:4])     # slice a list between two indices

sample_list.append(6)       # update the list by adding an element
print(sample_list)

sample_list.sort()          # sort the list in an ascending order
print(sample_list)

sample_list.pop(2)
print(sample_list)          # remove the item at the index 2

print(sample_list + sample_list)    # view the result of list concatenation
