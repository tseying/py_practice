#coding=utf-8
#关于符号的字符串一定是有偶数个的！！！
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if char == '(':
                stack.append(')')
                continue
            if char == '[':
                stack.append(']')
                continue
            if char == '{':
                stack.append('}')
                continue

            if char == ')':
                if (len(stack) != 0) and (stack[-1] == ')'):
                    stack.pop()
                    continue
                else:
                    return False
            if char == ']':
                if (len(stack) != 0) and (stack[-1] == ']'):
                    stack.pop()
                    continue
                else:
                    return False
            if char == '}':
                if (len(stack) != 0) and (stack[-1] == '}'):
                    stack.pop()
                    continue
                else:
                    return False
        if (len(stack) != 0):
            return False



        return True     #return相当于终止，函数返回给外界的值




# =========================================
solution = Solution()
s1 = '()'
s2 = '[]{}()'
s3 = '(]'
s4 = '([)]'
s5 = '{[]}'
print solution.isValid(s1)
print solution.isValid(s2)
print solution.isValid(s3)
print solution.isValid(s4)
print solution.isValid(s5)