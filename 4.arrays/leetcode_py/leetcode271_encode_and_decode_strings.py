"""
LEETCODE PROBLEM #271

Description Directly from: https://leetcode.com/problems/encode-and-decode-strings/

Design an algorithm to encode a list of strings to a single string.
The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:
Input: ["neet","code","love","you"]
Output:["neet","code","love","you"]

Example 2:
Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]

Constraints:
0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.
"""

class Solution:
    def encode(self, strs: list[str]) -> str:
        """
        This doesn't seem like a hard problem.
        Maybe for more juniors, I would totally get it then.

        I'll do the explanation so anyone can get it.
        Let's jump into it.

        We need to account for special chars.
        At the first second I was like,
        let's just use a special char and join all strings.
        But odds are the special char is also gonna be in one of the strings.
        We need to account for that.
        That way, decoding doesn't get messed up.

        Think of this solution as:
        Data conversion, UTF or encryption.
        In either of those 3 you can encode your address.
        Or even better,
        an amount of money which contains a symbol for the currency type.

        This exercise might not be as thorough as JWT for example.
        But it helps you see things from an everyday perspective.

        So then... join by a combination of special chars / delimiter?
        That way we won't mess up decoding the string.
        Note: open the resources section > How UTF-8 works.
        """
        encodedStr = ""

        for s in strs:
            # First step, check the length of each word
            encodedStr += f"{len(s)}#{s}"

        # Note, we can also do this in ONE line,
        # but the above is in case they ask for a manual work
        # return "".join(f"{len(s)}#{s}" for s in strs)
        
        return encodedStr
    def decode(self, s: str) -> list[str]:
        """
        Now.
        We need to check how many numbers are
        before reaching our character.

        That way we know the length of the word.
        AND that's why we need a special character.

        Again, think of an address, any address.
        E.g. 711 Null St., Apt. #2880, 96522
        We have special chars '.', ',' and '#'.
        The address starts with a number.
        The apartment number starts with the '#' sign.
        """

        strs = []
        pointer1 = 0
        while pointer1 < len(s):
            pointer2 = pointer1
            text = ""
            # Did a while because ifs update variables
            # ONLY inside their scope in Python3
            while s[pointer2] != "#":
                pointer2 += 1
            lenText = int(s[pointer1:pointer2])
            pointer2 += 1
            text = s[pointer2:pointer2+lenText]
            strs.append(text)

            pointer1 = pointer2+lenText
        
        return strs

s = Solution()

encoded = s.encode(["neet","code","love","you"])
print(f"encoded: {encoded}")
decoded = s.decode(encoded)
print(f"decoded: {decoded}")
