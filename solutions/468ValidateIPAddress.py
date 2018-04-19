class Solution:
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        def is_ipv4(s):
            valid = [(ord('0')+i) for i in range(10)]
            segs = s.split('.')
            if len(segs) != 4: return False
            for seg in segs:
                if len(seg) not in [1, 2, 3]: return False
                for c in seg:
                    if ord(c) not in valid: return False
                seg_i = int(seg)
                if seg_i > 255: return False
                if seg_i != 0 and seg[0] == '0': return False
                if seg_i == 0 and len(seg) != 1: return False
            return True
          
            
        def is_ipv6(s):
            valid = [(ord('0')+i) for i in range(10)] + [(ord('a')+i) for i in range(6)] + [(ord('A')+i) for i in range(6)]
            segs = s.split(':')
            if len(segs) != 8: return False
            for seg in segs:
                if len(seg) not in [1, 2, 3, 4]: return False
                for c in seg:
                    if ord(c) not in valid: return False
            return True
                       
        
        if is_ipv4(IP):
            return "IPv4"
        elif is_ipv6(IP):
            return "IPv6"
        else:
            return "Neither"