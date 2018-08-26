from heapq import heappop, heappush, heapify

class Solution:
    # heap
    # time: O(n * (logn + W))
    # space: O(n)
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        n = len(hand)
        if n % W != 0: return False
        
        heap = []
        
        cards = collections.defaultdict(int)
        for card in hand:
            cards[card] += 1
            heap.append(card)
        
        heapify(heap)
        
        while heap:
            min_card = heappop(heap)

            if cards[min_card] == 0:
                continue
            
            for i in range(W):
                if cards[min_card + i] == 0:
                    return False
                else:
                    cards[min_card+i] -= 1

        return all(v == 0 for v in cards.values())