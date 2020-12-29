class Solution:
    def reachNumber(self, target: int) -> int:
        gsum=0
        steps=0
        target = abs(target)
        if target==0:
            return 0
        while gsum<target:
            gsum+=steps
            steps+=1
        while (gsum-target)%2==1:
            gsum+=steps
            steps+=1
        return steps-1

if __name__ == "__main__":
    sol = Solution();
    x = int(input())
    print(sol.reachNumber(x))