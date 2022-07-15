import numpy as np
class GameState():
    def __init__(self, state, goal_state, level, parent = None, heuristic_func = None):
        self.__state = state
        self.__goal_state = goal_state
        self.__level = level
        self.__heuristic_func = heuristic_func
        self.__heuristic_score = level
        self.__parent = parent
        self.calculate_fitness()
        
    def __hash__(self):
        return hash(str(self.__state))
        
    def __lt__(self, other):
        return self.__heuristic_score < other.__heuristic_score
    
    def __eq__(self, other):
        return self.__heuristic_score == other.__heuristic_score
    
    def __gt__(self, other):
        return self.__heuristic_score > other.__heuristic_score
    
    def get_state(self):
        return self.__state
    
    def get_score(self):
        return self.__heuristic_score
    
    def get_level(self):
        return self.__level
    
    def get_parent(self):
        return self.__parent
    
    def calculate_fitness(self):
        self.__heuristic_score += self.misplaced_tiles(self.__heuristic_func[0]) + self.manhattan(self.__heuristic_func[1])
        
            
        
    
    def misplaced_tiles(self,w0):
        heuristic_score = 0
        for cur_tile, goal_tile in zip(self.__state, self.__goal_state):
                if cur_tile != goal_tile:
                    heuristic_score += 1
        return w0 * heuristic_score
    
    def manhattan(self,w1):
        heuristic_score = 0
        for cur_tile in self.__state:
                cur_idx = self.__state.index(cur_tile)
                goal_idx = self.__goal_state.index(cur_tile)
                cur_i, cur_j = cur_idx // int(np.sqrt(len(self.__state))), cur_idx % int(np.sqrt(len(self.__state)))
                goal_i, goal_j = goal_idx // int(np.sqrt(len(self.__state))), goal_idx % int(np.sqrt(len(self.__state)))
                heuristic_score += self.calculate_manhattan(cur_i, cur_j, goal_i, goal_j)
        
        return w1 * heuristic_score


    def calculate_manhattan(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)