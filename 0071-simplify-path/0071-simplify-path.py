class Solution:
    def simplifyPath(self, path: str) -> str:
        # Split by '/' to get all components
        components = path.split("/")
        stack = []
        
        for comp in components:
            if comp == "" or comp == ".":
                continue
            elif comp == "..":
                # Go to parent directory if stack isn't empty
                if stack:
                    stack.pop()
            else:
                # Valid directory name
                stack.append(comp)
        
        # Join the stack with '/' and ensure it starts with '/'
        return "/" + "/".join(stack)