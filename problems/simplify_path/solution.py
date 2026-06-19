class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        print(path.split('/'))
        for dir in path.split('/'):
            if dir == "..":
                if stack:
                    stack.pop()
            elif dir == "." or not dir:
                continue
            else:
                stack.append(dir)
        simplified = '/'.join(stack)
        return '/' + simplified

        