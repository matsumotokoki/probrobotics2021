from map import Map 

class Agent(object):
    def __init__(self,init_pos = [1,1],goal_pos = [10,10]):
        self.pos = [init_pos[0], init_pos[1]]
        self.goal_pos = goal_pos
        self.action_space = 4
        self.done = False

    def action(self,a,d):
        if a == 0 and d[0]:
            self.pos[1] += 1
        elif a == 1 and d[1]:
            self.pos[1] -= 1
        elif a == 2 and d[2]:
            self.pos[0] += 1
        elif a == 3 and d[3]:
            self.pos[0] -= 1
        else:
            pass
    
    def get_state(self):
        state = self.pos[0]*12 + self.pos[1]
        return state 

    def check_done(self):
        if self.pos[0] == self.goal_pos[0] and \
           self.pos[1] == self.goal_pos[1]:
            done = True
        else: done = False
        return done
