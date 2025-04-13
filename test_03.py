# NEETCODE (006)

# Leetcode 49. Group Anagrams
# Wrong asnwer at strs = ["",""] 
from collections import Counter
def groupAnagrams_00(strs: list[str]) ->list[list[str]]:
    res = [[strs[0]]]
    for val in strs:
        value_added = False
        for group in res:
            if Counter(val) == Counter(group[0]):
                value_added = True
                if val not in group:
                    group.append(val)
                
                break
        
        if value_added == False:
            res.append([val])
    return res

# NOTE: This one was rough. I spent too long trying to get the system to work.
# Once I start adding boolean toggles all over the place I kinda feel like I messed up.
# Definitely doesn't feel elegant. ANYWAY... onto the elegant solution.
# ---------------------------------------------------------------------------------------------------

# Solution accepted. Beats 83.07%

# Core Insights:
# 1.) Sort the values in a string in alphabetical order--> "".join(sorted(val))"
# 2.) Using a dictionary to get values that then you return as a list.

def groupAnagrams(strs: list[str]) ->list[list[str]]:
        local_dict = dict()

        for val in strs:
            sorted_val = "".join(sorted(val))       # I thought this was too much work to be valuable here. Guess not.
            if sorted_val not in local_dict.keys():
                local_dict[sorted_val]=[]           # This is also an interesting pattern because you're saying if this
            local_dict[sorted_val].append(val)      # doesn't exist, make it into a list [] then ALWAYS do the following
                                                    # line
        return list(local_dict.values())


def main() -> None:
    print('Hello')
    print(groupAnagrams(["eat","tea","tan","ate","nat","bat"])) # [["bat"],["nat","tan"],["ate","eat","tea"]]
    print(groupAnagrams([""])) # [[""]]
    print(groupAnagrams(strs = ["a"]))  # [["a"]]


if __name__ == '__main__':
    main()