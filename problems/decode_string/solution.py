class Solution:
    def decodeString(self, s: str) -> str:
        output = ""
        num = ""
        i = 0
        while i < len(s):
            if s[i].isnumeric():
                num += s[i]
            elif s[i] == "[":
                local_str = ""
                i +=1
                par_count = 1
                while  par_count != 0:
                    local_str += s[i]
                    i +=1
                    if s[i] == "]":
                        par_count -= 1
                    elif s[i] =="[":
                        par_count += 1
                sub_eval = self.decodeString(local_str)
                for index in range(int(num)):
                    output += sub_eval
                num = ""
            else:
                output += s[i]
            i += 1
        return output




        
            


            

            
        
        