class Solution:
    def generate(self, numRows):
        result = []
        if numRows == 1:
            result.append([1])

        elif numRows == 2:
            result.append([1])
            result.append([1, 1])

        else:
            result = [[1], [1,1]]

            for i in range(2, numRows):
                new = [1]
                latest = result[-1]

                a_range = range(0, len(latest) - 1)
                b_range = range(1, len(latest))

                for a,b in zip(a_range, b_range):
                    new.append(latest[a] + latest[b])

                new.append(1)

                result.append(new)

        return result


if __name__=="__main__":
    numRows = 2

    solution = Solution()
    result = solution.generate(numRows)
    print(result)
