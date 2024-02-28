from typing import List

def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    result: List[bool] = [True] * len(candies)
    max_candy: int = max(candies)
    i: int = 0
        
    while(i < len(candies)):
        result[i] = True if candies[i] + extraCandies >= max_candy else False
        i += 1
    
    return result
    

if __name__ == '__main__':
    candies: List[int] = [4, 2, 1, 1, 2]
    extra: int = 1
    out: List[bool] = [True, False, False, False, False]
    
    assert kidsWithCandies(candies, extra) == out