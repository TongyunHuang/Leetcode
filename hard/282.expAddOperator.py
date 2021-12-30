class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        """
        Follow solution - Basic Idea:
        procedure recurse(digits, index, expression):
            if we have reached the end of the string:
                if the expression evaluates to the target:
                    Valid Expression Found
            else:
                try out operator 'NO OP' and recurse
                try out operator * and recurse
                try out operator + and recurse
                try out operator - and recurse
        """
        N = len(num)
        answers = []
        def recurse(index, prev_operand, current_operand, value, string):
            # have reach the end of string
            if index == N:
                # If the final value == target expected 
                if value == target and current_operand == 0:
                    answers.append("".join(string[1:]))
                return
            
            # Extending the current operand by one digit
            current_operand = current_operand * 10 + int(num[index])
            str_op = str(current_operand)
            
            # check digit not start with 0
            if current_operand > 0:
                # NO OP recursion
                recurse(index+1, prev_operand, current_operand, value, string)
                
            # Addition
            string.append('+')
            string.append(str_op)
            recurse(index+1, current_operand, 0, value+current_operand, string)
            string.pop()
            string.pop()
            
            # can substrct or multiply only if there are some previous operands
            if string:
                
                #SUBTRACTION
                string.append('-')
                string.append(str_op)
                recurse(index + 1, -current_operand, 0, value - current_operand, string)
                string.pop()
                string .pop()
                
                # MULTIPLICATION
                string.append('*')
                string.append(str_op)
                recurse(index+1, current_operand * prev_operand, 0, value - prev_operand + (current_operand * prev_operand), string)
                string.pop()
                string.pop()
        recurse(0,0,0,0,[])
        return answers
                
                