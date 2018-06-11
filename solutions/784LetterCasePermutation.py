class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if not S: return [""]
        
        s_len = len(S)
        nodes = []
        ans = []
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if S[0] in nums:
            nodes.append(S[0])
        else:
            nodes.append(S[0].lower())
            nodes.append(S[0].lower().upper())
        
        while nodes:
            node_len = len(nodes[0])
            if node_len == s_len:
                ans.append(nodes.pop(0))
            else:
                if S[node_len] in nums:
                    nodes.append(nodes[0] + S[node_len])
                else:
                    nodes.append(nodes[0] + S[node_len].lower())
                    nodes.append(nodes[0] + S[node_len].lower().upper())   
                nodes.pop(0)
        
        return ans