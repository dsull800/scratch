class Solution:
    def candy(self, ratings: List[int]) -> int:
        modified_ratings = [3* 10**4] + ratings + [3* 10**4]
        candies = [1] * len(modified_ratings)
        for index, rating in enumerate(ratings):
            if modified_ratings[index + 2] >= modified_ratings[index+1] >= modified_ratings[index]:
                candies[index+1] = candies[index]
                if modified_ratings[index + 2] > modified_ratings[index+1] > modified_ratings[index]:
                    candies[index+1] = candies[index] + 1
                else:
                    candies[index+1] = candies[index]
            elif modified_ratings[index + 2] <= modified_ratings[index+1] >= modified_ratings[index]:
                if modified_ratings [index + 2] < modified_ratings[index+1] > modified_ratings[index]:
                    candies[index+1] = max(candies[index+2], candies[index]) + 1
                else:
                    candies[index+1] = max(candies[index+2], candies[index])
            elif modified_ratings[index + 2] >= modified_ratings[index+1] <= modified_ratings[index]:
                if modified_ratings [index + 2] > modified_ratings[index+1] < modified_ratings[index]:
                    if min(candies[index+2], candies[index]) - 1 == 0:
                        candies[index+1] = 1
                        for i in range(1, index + 1):
                            candies[i] += 1
                    else:
                        candies[index+1] = min(candies[index+2], candies[index]) - 1
                else:
                    candies[index+1] = min(candies[index+2], candies[index])
            elif modified_ratings[index + 2] <= modified_ratings[index+1] <= modified_ratings[index]:
                if modified_ratings[index + 2] < modified_ratings[index+1] < modified_ratings[index]:
                    candies[index+1] = candies[index+2] + 1
                else:
                    candies[index+1] = candies[index+2]
        print(candies[1:-1])
        return sum(candies[1:-1])
