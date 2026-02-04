class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        
        def letter_frequency(string):
            letters_string = [0] * 26
            for l in string:
                position = ord(l) - ord('a')
                letters_string[position] +=1
            return letters_string
        
        for st in strs:
            st_freq = letter_frequency(st)
            key = tuple(st_freq)
            d[key].append(st)
        return list(d.values())


        
        # for i in range(len(strs)):
        #     letters_i = letter_frequency(strs[i])
        #     if strs[i] in visited:
        #         continue
        #     anagram = [strs[i]]
        #     visited.add(strs[i])
        #     for j in range(i,len(strs)):
        #         letters_j = letter_frequency(strs[j])
        #         if strs[j] in visited:
        #             continue
        #         if letters_i == letters_j:
        #             anagram.append(strs[j])
        #             visited.add(strs[j])
            
        #     result.append(anagram)
                
        # return result
                
                
        