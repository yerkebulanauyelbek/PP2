class Solution(object):
    def interpret(self, command):
        a=command.replace("(al)","al")
        return a.replace("()","o")