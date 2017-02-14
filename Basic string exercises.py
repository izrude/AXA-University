
#==============================================================================
# A. donuts
# 
# Given an int count of a number of donuts, return a string of the form 'Number of donuts: ', where  is the number passed in. However, if the count is 10 or more, then use the word 'many' instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5' and donuts(23) returns 'Number of donuts: many'
#==============================================================================

def donuts(count):
    # +++your code here+++
    try : 
        count + 1
        if count < 10 : 
            output = 'Number of donuts: ' + str(count)    
        elif count >= 10 :
            output = 'Number of donuts: many'
    
        return output
    
    except : 
        print 'Enter a integer number'
    

#test 
#print donuts('eight')        
#print donuts(8)
#print donuts(18)        





#==============================================================================
# B. both_ends
# 
# Given a string s, return a string made of the first 2 and the last 2 chars of the original string, so 'spring' yields 'spng'. However, if the string length is less than 2, return instead the empty string.
#==============================================================================

def both_ends(s):
    # +++your code here+++
    if len(s) >= 2 :
        output = s[0:2] + s[-2] + s[-1]
    else :
        output = ''
    return output



#test     
#both_ends('ABCD')
#both_ends('ABC')    
#both_ends('AB')    
#both_ends('A')    
    
    
    
    
    



#==============================================================================
# C. fix_start
# 
# Given a string s, return a string where all occurences of its first char have been changed to '*', except do not change the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more. Hint: s.replace(stra, strb) returns a version of string s where all instances of stra have been replaced by strb.
#==============================================================================


def fix_start(s):
    # +++your code here+++
    if len(s) > 0 :        
        frst = s[0]
        output = frst + s[1:].replace(frst,'*')
        return output
    else : print 'Enter a string'


#test
#print fix_start('ABCDAAA')








#==============================================================================
# D. MixUp
# 
# Given strings a and b, return a single string with a and b separated by a space '<a> <b>', except swap the first 2 chars of each string.
# 
# e.g.
# 'mix', pod' -> 'pox mid'
# 'dog', 'dinner' -> 'dig donner'
# 
# Assume a and b are length 2 or more.
#==============================================================================

def mix_up(a, b):
    # +++your code here+++
    if len(a) >=2 and len(b) >=2 :
        a_frst2 = a[0:2]
        a_other = a[2:]
        b_frst2 = b[0:2]
        b_other = b[2:]
        
        output = b_frst2 + a_other + ' ' + a_frst2 + b_other
        return output
    else : print 'Enter strings at least 2 digit'


#test
#mix_up('ABC','abc')
#mix_up('AB','ab')







#==============================================================================
# D. verbing
# 
# Given a string, if its length is at least 3, add 'ing' to its end. Unless it already ends in 'ing', in which case add 'ly' instead. If the string length is less than 3, leave it unchanged. Return the resulting string.
#==============================================================================


def verbing(s):
    # +++your code here+++
    if len(s) >= 3:
        if s[len(s)-3:] == 'ing':
            output = s + 'ly'
        else:
            output = s + 'ing'
    else : output = s
    return output 

    
#test
#verbing('fly')
#verbing('according')
#verbing('do')







#==============================================================================
# E. not_bad
# 
# Given a string, find the first appearance of the substring 'not' and 'bad'. If the 'bad' follows the 'not', replace the whole 'not'...'bad' substring with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields: This dinner is good!
#==============================================================================


def not_bad(s):
    # +++your code here+++
    fnd_not = s.find('not',1)
    fnd_bad = s.find('bad',fnd_not)
    
    if fnd_not > 0 and fnd_bad > 0 :
        output = s[:fnd_not] + 'good' + s[fnd_bad+3:]
    else : output = s
    return output


#test
#not_bad('This dinner is not that bad!')







#==============================================================================
# F. front_back
# 
# Consider dividing a string into two halves. If the length is even, the front and back halves are the same length. If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form a-front + b-front + a-back + b-back
#==============================================================================

def front_back(a, b):
    # +++your code here+++
    len_a = float(len(a))
    len_b = float(len(b))
    hlf_a = int(round(len_a/2))
    hlf_b = int(round(len_b/2))
    output = a[:hlf_a] + b[:hlf_b] + a[hlf_a:] + b[hlf_b:]
    return output


#test
#a = 'ABCDE'
#b = 'abcdef'
#front_back(a,b)










#==============================================================================
# Test all:
#     
# test function + main function
#==============================================================================


def test(got, expected):
    prefix = 'OK' if got == expected else ' X'
    # !r prints a Python representation of the strings (complete with quotes)
    print ' {} got: {!r} expected: {!r}'.format(prefix, got, expected)

def main():
    print 'donuts'
    # Each line calls donuts, compares its result to the expected for that call.
    test(donuts(4), 'Number of donuts: 4')
    test(donuts(9), 'Number of donuts: 9')
    test(donuts(10), 'Number of donuts: many')
    test(donuts(99), 'Number of donuts: many')

    print
    print 'both_ends'
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')

  
    print
    print 'fix_start'
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print
    print 'mix_up'
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')


main()


def main2():
    print 'verbing'
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')
    
    print
    print 'not_bad'
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print
    print 'front_back'
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')


main2()

