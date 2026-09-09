
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=''
        for string in strs:
            encoded+=f'{len(string)}#'+string
        return encoded

    
    def decode(self, s: str) -> List[str]:
        decoded=[]
        index=''
        pointer=0
        while pointer<len(s):
            if s[pointer].isdigit():
                index+=s[pointer]
                pointer+=1

            elif s[pointer]=='#' and index.isdigit():
                length=int(index)
                sub_string=s[pointer+1:pointer+1+length]
                decoded.append(sub_string)
                pointer=pointer+1+length
                index=''
            else:
                pointer+=1
        return decoded

        
            


