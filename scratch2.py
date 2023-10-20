class Solution:
    def candy(self, ratings) -> int:
        modified_ratings = [3 * 10 ** 4] + ratings + [3 * 10 ** 4]
        candies = [1] * len(modified_ratings)
        for index, rating in enumerate(ratings):
            gt_end = modified_ratings[index + 2] < modified_ratings[index + 1]
            lt_end = modified_ratings[index + 2] > modified_ratings[index + 1]
            eq_end = modified_ratings[index + 2] == modified_ratings[index + 1]
            gt_beg = modified_ratings[index] < modified_ratings[index + 1]
            lt_beg = modified_ratings[index] > modified_ratings[index + 1]
            eq_beg = modified_ratings[index] == modified_ratings[index + 1]
            if gt_beg and gt_end:
                candies[index + 1] = max(candies[index], candies[index + 2]) + 1
            elif gt_beg and lt_end:
                candies[index + 1] = candies[index] + 1
            elif gt_beg and eq_end:
                candies[index + 1] = candies[index] + 1
            elif lt_beg and gt_end:
                candies[index + 1] = min(candies[index] - 1, candies[index + 2] + 1)
            elif lt_beg and lt_end:
                candies[index + 1] = min(candies[index], candies[index + 2]) - 1
            elif lt_beg and eq_end:
                candies[index + 1] = min(candies[index + 2], candies[index] - 1)
            elif eq_beg and gt_end:
                candies[index + 1] = min(candies[index + 2] + 1, candies[index])
            elif eq_beg and lt_end:
                candies[index + 1] = min(candies[index + 2] - 1, candies[index])
            elif eq_beg and eq_end:
                candies[index + 1] = 1
            # print(candies)
            if candies[index + 1] < 1:
                # print(f'{index} looping')
                candies[index + 1] = 1
                for i in range(index + 1, -1, -1):
                    if candies[i] >= candies[i - 1] and modified_ratings[i] < modified_ratings[i - 1]:
                        # print('increment')
                        candies[i - 1] += 1
                    else:
                        break
            # print(candies)

        print(candies[1:-1])
        return sum(candies[1:-1])





