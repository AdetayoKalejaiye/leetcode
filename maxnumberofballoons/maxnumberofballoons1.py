class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        key = [1, 1, 2, 2, 1]
        unique = 'balon'
        output = [0, 0, 0, 0, 0]
        for letter in text:
            if letter not in unique:
                continue
            output[unique.find(letter)] += 1
        solution = [output[i]/key[i] for i in range(len(key)) if output[i]/key[1] % 1 == 0]
        solution.sort()
        return int(solution[0])