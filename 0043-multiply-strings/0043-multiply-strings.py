class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        res = [0] * (m + n)
        
        # Multiply each digit and add to the corresponding position
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                
                # Current positions in the result array
                p1, p2 = i + j, i + j + 1
                
                # Add to existing value and handle carry
                total = mul + res[p2]
                res[p2] = total % 10
                res[p1] += total // 10
        
        # Convert result array to string, skipping leading zero
        result_str = "".join(map(str, res))
        return result_str.lstrip("0")