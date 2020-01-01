class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        store={5:0,10:0,20:0}
        for i in bills:
            if i == 5:
                store[5]+=1
            elif i==10:
                if store[5]==0:
                    return False
                else:
                    store[5]-=1
                    store[10]+=1
            elif i==20:
                if store[5] and store[10]:
                    store[5]-=1
                    store[10]-=1
                elif store[5] >=3:
                    store[5]-=3
                else:
                    return False
        return True
