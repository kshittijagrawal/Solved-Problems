class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = address.replace(".", "[.]")
        return res