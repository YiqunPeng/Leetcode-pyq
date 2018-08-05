class Solution:
    # one pass
    # time: O(n)
    # space: O(n)
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        nums = [0] * 10
        bulls, cows = 0, 0
        
        for i in range(len(secret)):
            s, g = int(secret[i]), int(guess[i])
            if s == g:
                bulls += 1
            else:
                if nums[s] < 0: cows += 1
                if nums[g] > 0: cows += 1
                nums[s] += 1
                nums[g] -= 1
        
        return str(bulls) + 'A' + str(cows) + 'B'
        
    
    # two pass
    # time: O(n)
    # space: O(n)
    # def getHint(self, secret, guess):
    #     """
    #     :type secret: str
    #     :type guess: str
    #     :rtype: str
    #     """
    #     bulls, cows = 0, 0

    #     secret_dict = collections.defaultdict(int)
    #     for i in range(len(secret)):
    #         if secret[i] == guess[i]:
    #             bulls += 1
    #         else:
    #             secret_dict[secret[i]] += 1

    #     for i in range(len(secret)):
    #         if secret[i] != guess[i] and secret_dict[guess[i]] > 0:
    #             cows += 1
    #             secret_dict[guess[i]] -= 1

    #     return str(bulls) + 'A' + str(cows) + 'B'
        