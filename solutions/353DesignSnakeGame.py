class SnakeGame:

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.w, self.h = width, height
        self.food = food
        self.idx = 0
        self.snake = collections.deque([(0, 0)])
        self.snake_set = set([(0, 0)])
        self.game_state = True
        

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        if not self.game_state: return -1
        
        directions = {'U': (-1, 0), 'L': (0, -1), 'R': (0, 1), 'D': (1, 0)}
        
        head = self.snake[0]
        n_x = head[0] + directions[direction][0]
        n_y = head[1] + directions[direction][1]
        
        if not (0 <= n_x < self.h and 0 <= n_y < self.w):
            self.game_state = False
            return -1 
        
        if (n_x, n_y) != self.snake[-1] and (n_x, n_y) in self.snake_set:
            self.game_state = False
            return -1
        
        if self.idx < len(self.food) and self.food[self.idx] == [n_x, n_y]:
            self.idx += 1
        else:
            self.snake_set.remove(self.snake[-1])
            self.snake.pop()
        
        self.snake.appendleft((n_x, n_y))
        self.snake_set.add((n_x, n_y))
    
        return self.idx
        

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)