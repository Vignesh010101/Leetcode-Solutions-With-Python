class Solution:
    def largestVariance(self, s: str) -> int :
        # get each character frequency and indices 
        char_frequency = collections.defaultdict(int)
        char_indices = collections.defaultdict(list)
        # get each index for each char as a list and track frequency 
        for index, char in enumerate(s) : 
            char_frequency[char] += 1 
            char_indices[char].append(index)
        # get the list of possible char keys 
        char_keys = list(char_frequency.keys())
        # get the major and minor keys in order by their frequency, major sorted by highest frequency, minor by lowest 
        char_keys_major = sorted(char_keys, key = lambda char_key : char_frequency[char_key], reverse=True)
        char_keys_minor = sorted(char_keys, key = lambda char_key : char_frequency[char_key])
        # track the global max 
        global_max = 0 
        # use these to generate all pairings as major key in outerloop 
        for major_char in char_keys_major : 
            # skip useless major chars. Occurs greedily now. 
            if char_frequency[major_char] - 1 <= global_max : 
                break
            # minor key in inner loop 
            for minor_char in char_keys_minor :
                # skip on matches  
                if major_char == minor_char : 
                    continue 
                else : 
                    # otherwise, get counts 
                    major_count = 0 
                    minor_count = 0 
                    # track remaining minor 
                    remaining_minor = char_frequency[minor_char]
                    remaining_major = char_frequency[major_char]
                    # get indices list of char matches (reduces time and space complexity greatly)
                    total_indices = sorted([index_1 for index_1 in char_indices[major_char]] + [index_2 for index_2 in char_indices[minor_char]])
                    # for each index in total indices 
                    for index in total_indices : 
                        # if s[index] is major char, increment major count 
                        if s[index] == major_char : 
                            major_count += 1 
                            remaining_major -= 1 
                        else : 
                            # otherwise, based on total indices, it must be minor char
                            # increment minor count and decrement remaining minor 
                            minor_count += 1 
                            remaining_minor -= 1 
                        
                        # then if minor count is gt 0, update global max 
                        global_max = max(global_max, major_count-minor_count) if minor_count > 0 else global_max

                        # if major is lt minor count 
                        if (major_count < minor_count) : 
                            # if remaining major - 1 <= global max -> break 
                            if remaining_major - 1 <= global_max : 
                                break 
                            elif remaining_minor > 0 : 
                                # otherwise, if there's still a shot -> reset 
                                major_count = 0 
                                minor_count = 0 
                            else : 
                                 # if major count lt minor count, but no remaining minor 
                                # if remaining major + major count - minor count <= global max break 
                                # otherwise, remaining major + major count - minor count gt global max 
                                # update then break. Either way, break. Due to this, use global update instead 
                                global_max = max(global_max, (major_count + remaining_major) - minor_count)
                                break
                        else : 
                            continue 

        # return when done 
        return global_max


        