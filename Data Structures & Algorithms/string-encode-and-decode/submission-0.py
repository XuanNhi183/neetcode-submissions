class Solution:

    def encode(self, strs: List[str]) -> str:
        part=[]
        for word in strs:
            number = len(word)
            strings= str(number) + "@" + word
            part.append(strings)
        return "".join(part)

    # 5@Hello5@World
    # 12@Hello5@World --> lấy các phần tử trước #
    def decode(self, s: str) -> List[str]:
        result=[]
        i=0
        while i < len(s):
            j = s.find("@",i)
            number=s[i:j]
            start=j+1
            end=start+int(number)
            word=s[start:end]
            result.append(word)
            i = end
        return result



