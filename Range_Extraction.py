"""
A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example ("12, 13, 15-17")
Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

Example:

solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-6,-3-1,3-5,7-11,14,15,17-20"
"""

def solution(args):
    res = ''
    list_range = []
    for i in range(len(args)-1):
        if args[i]+1 != args[i+1]:
            if not list_range:
                res += str(args[i]) + ','
                if i == len(args)-2: res+=str(args[i+1])+','
            else:
                if len(list_range)>=3:
                    range_str = str(list_range[0]) + '-' + str(list_range[-1]) + ','
                    res += range_str
                else:
                    for e in list_range:
                        res += str(e) + ','
                if i == len(args) - 2: res += str(args[i+1])+','
            list_range = []
        else:
            if not list_range:
                list_range.append(args[i])
                list_range.append(args[i+1])
                if i == len(args)-2:
                    for e in list_range:
                        res += str(e) + ','
            else:
                list_range.append(args[i+1])
                if i == len(args) - 2:
                    res += str(list_range[0]) + '-' + str(list_range[-1]) + ','

    return res[:-1]
