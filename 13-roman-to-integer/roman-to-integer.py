class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        num=0
        i=0
        while(i<len(s)):
            if(i==len(s)-1):
                num+=dic[s[i]]
            elif(s[i]=="I"):
                if(s[i+1]=="V"):
                    num+=4
                    i+=1
                elif(s[i+1]=="X"):
                    num+=9
                    i+=1
                else:
                    num+=1
            elif(s[i]=="X"):
                if(s[i+1]=="L"):
                    num+=40
                    i+=1
                elif(s[i+1]=="C"):
                    num+=90
                    i+=1
                else:
                    num+=10
            elif(s[i]=="C"):
                if(s[i+1]=="D"):
                    num+=400
                    i+=1
                elif(s[i+1]=="M"):
                    num+=900
                    i+=1
                else:
                    num+=100
            else:
                num+=dic[s[i]]
            i+=1
        return num

            
            

        