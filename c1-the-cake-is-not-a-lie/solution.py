case_1 = "abcabcabcabc"
case_2 = "abccbaabccba"

def solution(s):

    """Find the amount of times the smallest subsequence of a sequence repeats without remainders 

    Parameters:
        s (str): Sequence of letters
    
    Returns:
        int: Max number of repeats without a remainder
    """

    length = len(s)

    # starting with the smallest repeating substring, loop over the sequence
    for i in range(1, int(length/2 + 1) ):
        repeat_count, remainder = divmod(length, i)

        # check if the substring fits evenly and that the repeated substring equals the sequence 
        if( remainder == 0 and s == s[:i]*repeat_count):
            # print('Smallest substring:: \'{}\' It repeats {} times'.format(s[:i], repeat_count))
            return repeat_count
    else:
        # print('Smallest substring: \'{}\' It repeats 1 time.'.format(s[:i], repeat_count))
        return 1
 

print("<CASE 1---------->")

print(solution(case_1))

print("<CASE 2---------->")
print(solution(case_2))


print("<CASE 3---------->")

print(solution("abcjddfgujrjsdfg"))



