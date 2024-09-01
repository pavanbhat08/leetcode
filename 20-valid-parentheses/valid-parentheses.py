class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) %2 != 0:
            return False
        lst = []
        for letter in s:
            if len(lst) >0:
                prev = lst[-1]
                if letter== "]" and prev =="[":
                    lst.pop()
                elif letter== "}" and prev =="{":
                    lst.pop()
                elif letter== ")" and prev =="(":
                    lst.pop()
                else:
                    lst.append(letter)
            else:
                lst.append(letter)
        if len(lst)>0:
            return False
        else:
            return True

        