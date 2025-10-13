class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        out=[]
        for i in range(n):
            if (i+1)%15==0:
                out.append("FizzBuzz")
                continue
            elif (i+1)%3==0:
                out.append("Fizz")
            elif (i+1)%5==0:
                out.append("Buzz")
            else:
                out.append(str(i+1))
        return out