# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

def can_make_palindrome(s):

    def can_make_palindrome_helper(l, r, allow_branch):
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                if allow_branch:
                    if can_make_palindrome_helper(l+1, r, False) or can_make_palindrome_helper(l, r-1, False):
                        return True
                    return False
                return False
        return True

    return can_make_palindrome_helper(0, len(s) - 1, True)

print(can_make_palindrome('dd'))