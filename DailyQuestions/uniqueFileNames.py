class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        word_dict = {}
        k = 0
        new_folder = ""
        new_f = []
        res = []
        
        for folder in names:
            if folder in word_dict:
                k = word_dict[folder]
                new_folder = folder + "(" + str(k) + ")"
                word_dict[folder] += 1
                
                while new_folder in word_dict:
                    k += 1
                    new_folder = folder + "(" + str(k) + ")"
                
                word_dict[new_folder] = 1
                res.append(new_folder)
                
            else:
                word_dict[folder] = 1
                res.append(folder)
                
        return res
