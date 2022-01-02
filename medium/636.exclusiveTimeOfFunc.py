class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        """
        Idea:
        - add start to stack (func_idx, actual_start_time)
        - if encounter a new func_idx, add pended time to corres idx
        - if curr fin, pop from the stack, add time until end
        """
        exclu_t = [0 for i in range(n)]
        stack = []
        for i, log in enumerate(logs):
            info = log.split(':')
            idx, state, time = info[0], info[1], info[2]
            # case1: start state and stack is empty -> add to stack
            if state == 'start':
                if len(stack) == 0:
                    stack.append( [ int(idx), int(time) ] )
            # case2: start state and stack is nonempty -> add prev time to prev func
            # && add curr to top of stack
                else:
                    last_idx, last_time = stack[-1][0], stack[-1][1]
                    exclu_t[last_idx] += int(time) - last_time
                    stack.append(( [ int(idx), int(time) ] ))
            
            # case3: end state (stack has to nonempty and same func) -> pop and add exce time
            # if stack nonempty, set the func's actual_startt_time to end time
            else:
                curr = stack.pop(-1)
                exclu_t[int(idx)] += (int(time) - curr[1] + 1)
                if len(stack) > 0:
                    stack[-1][1] = int(time) + 1
        return exclu_t
                
            