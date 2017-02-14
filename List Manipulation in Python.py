#List Manipulation in Python



#==============================================================================
# A. match_ends
# Given a list of strings, return the count of the number of strings where the string length is 2 or more and the first and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.
#==============================================================================

# define function
def match_ends(words):
    # +++your code here+++
    count = 0   #count = the number of word matched with conditions
    for word in words:
        if len(word) > 1 and word[0] == word[-1] : 
            count = count + 1
    return count
    
    
# test
#words = list()
#
#while True:
#    word = raw_input("Please enther a word: ")
#    if len(word) < 1 : break
#    words.append(word)
#
#print match_ends(words)








#==============================================================================
# B. front_x
# Given a list of strings, return a list with the strings in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them before combining them.
#==============================================================================

# define function
def front_x(words):
    # +++your code here+++
    x_lst = list()
    other = list()
    
    for word in words:
        if word.startswith('x') :
            x_lst.append(word)
        else:
            other.append(word)
            
    x_lst.sort()
    other.sort()
    return x_lst + other

    
# test
#words = list()
#
#while True:
#    word = raw_input("Please enther a word: ")
#    if len(word) < 1 : break
#    words.append(word)
#
#print front_x(words)






#==============================================================================
# C. sort_last
# 
# Given a list of non-empty tuples, return a list sorted in increasing order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.
#==============================================================================



            
def sort_last(tuples):
    # +++your code here+++
    index = range(len(tuples))                        # [0,1,2,3]             
    
    dictionary = dict()            
    for i in index:
        dictionary[i] = tuples[i][-1]                 # {(0:x0, 1:x1, 2:x2, 3:x3)}
    
    aaa = list()
    for x,y in dictionary.items() : aaa.append((y,x))   # [(x0,0), (x1,1), (x2,2), (x3,3)]
    aaa.sort()
    
    bbb = list()
    for tple in aaa:
        k = tple[1]                     
        bbb.append(tuples[k])
    return bbb


# test
#tple_lst = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
#            
#print sort_last(tple_lst)
    





#==============================================================================
# D. remove_adjacent
# 
# Given a list of numbers, return a list where all adjacent == elements have been reduced to a single element, so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or modify the passed in list.
#==============================================================================


def remove_adjacent(nums):
    # +++your code here+++
    output = list()
    
    previous = None
    for number in nums:
        if previous == None : 
            output.append(number)
        else :
            if number == previous : continue
            else : output.append(number)
        previous = number    
        
    return output


#test    
#lst = [1,2,2,3]
#remove_adjacent(lst)







#==============================================================================
# E. linear_merge
# 
# Given two lists sorted in increasing order, create and return a merged list of all the elements in sorted order. You may modify the passed in lists. Ideally, the solution should work in "linear" time, making a single pass of both lists.
#==============================================================================


def linear_merge(list1, list2):
    # +++your code here+++    
    output = list1 + list2
    output.sort()

    return output

    
#test

#list1 = ['aa','cc','dd']
#list2 = ['bb','ee','ff']
#
#linear_merge(list1,list2)







#==============================================================================
# Test all :
#     
# test function + main function
#==============================================================================


def test(got, expected):
    prefix = 'OK' if got == expected else ' X'
    # !r prints a Python representation of the strings (complete with quotes)
    print ' {} got: {!r} expected: {!r}'.format(prefix, got, expected)

    
def main():
    print 'match_ends'
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print
    print 'front_x'
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
        ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
        ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
        ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])
    
    print
    print 'sort_last'
    test(sort_last([(1, 3), (3, 2), (2, 1)]),
         [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]),
         [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


main()




