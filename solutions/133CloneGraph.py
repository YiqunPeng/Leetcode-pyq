# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node: return None
        
        n_node = UndirectedGraphNode(node.label)
        q, n_q = [node], [n_node]

        n_dic = {}
        n_dic[node.label] = n_node

        nodes = set()
        nodes.add(node)
        
        while q:
            n = q.pop(0)
            n_n = n_q.pop(0)
            for nb in n.neighbors:
                new_node = None
                if nb.label in n_dic:
                    new_node = n_dic[nb.label]
                    n_n.neighbors.append(new_node)
                else:
                    new_node = UndirectedGraphNode(nb.label)
                    n_dic[nb.label] = new_node
                    n_n.neighbors.append(new_node)
                if nb not in nodes:
                    nodes.add(nb)
                    q.append(nb)
                    n_q.append(new_node)
        
        return n_node

            