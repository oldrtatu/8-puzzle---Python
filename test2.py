class Board:

    def __init__(self, root, parent = None, position = None):
        self.root = root
        self.parent = parent
        self.children = []
        self.position = position
        if(parent is not None):
            parent.children.append(self)

    def p_print(self):
        for i in range(0,len(self.root)):
            if(i == 2 or i == 5):
                print(self.root[i])
            else:
                print(self.root[i],end=" ")
        print()
        print()



class Move:

    def __init__(self, Node):
        self.node = Node;

    def up(self):
        copy = list(self.node.root)
        index = copy.index(0)
        if(index - 3 >= 0):
            copy[index], copy[index - 3] = copy[index - 3], copy[index]
            return Board(copy, self.node, 'up')
            print(copy)


    def down(self):
        copy = list(self.node.root)
        index = copy.index(0)
        if(index + 3 <= 8):
            copy[index], copy[index + 3] = copy[index + 3], copy[index]
            return Board(copy, self.node, 'down')

    def left(self):
        copy = list(self.node.root)
        index = copy.index(0)
        if(index%3!=0):
            copy[index], copy[index - 1] = copy[index - 1], copy[index]
            return Board(copy, self.node, 'left')
            print(copy)


    def right(self):
        copy = list(self.node.root)
        index = copy.index(0)
        if(index%3!=2):
            copy[index], copy[index + 1] = copy[index + 1], copy[index]
            return Board(copy, self.node, 'right')


class Play:

    def __init__(self, initial, method=None):
        self.initial = initial
        self.method = method
        self.path = []
        self.cost = 0
        self.depth = 0
        self.max_depth = 0
        self.node_expanded = 0

        if(method == 'bfs'):
            self.create_tree()
        elif(method == 'dfs'):
            self.dfs()


    def exist(self, what, from_node):
        answer = True
        for i in from_node:
            if(what == i.root):
                answer = False
                break
        return answer

    def bfs(self):
        frontier = []
        explored = []
        answer = [[1,2,3,4,5,6,7,8,0], [0,1,2,3,4,5,6,7,8]]
        frontier.append(self.initial)
        while(frontier):
            element = frontier.pop()
            explored.append(element)
            if(element.root in answer):
                element.p_print()
                print(self.node_expanded)
                break

            check = Move(element)

            up_element = check.up()
            down_element = check.down()
            left_element = check.left()
            right_element = check.right()

            if(up_element):
                if(self.exist(up_element.root, frontier) and self.exist(up_element.root, explored)):
                    frontier.insert(0, up_element)
                    self.node_expanded += 1

            if(down_element):
                if(self.exist(down_element.root, frontier) and self.exist(down_element.root, explored)):
                    frontier.insert(0, down_element)
                    self.node_expanded += 1

            if(left_element):
                if(self.exist(left_element.root, frontier) and self.exist(left_element.root, explored)):
                    frontier.insert(0, left_element)
                    self.node_expanded += 1

            if(right_element):
                if(self.exist(right_element.root, frontier) and self.exist(right_element.root, explored)):
                    frontier.insert(0, right_element)
                    self.node_expanded += 1

        while(element.parent is not None):
            self.path.append(element.position)
            element = element.parent
        print(self.path)



    def dfs(self):
        frontier = []
        explored = []
        answer = [[1,2,3,4,5,6,7,8,0], [0,1,2,3,4,5,6,7,8]]
        frontier.append(self.initial)
        while(frontier):
            element = frontier.pop()
            explored.append(element)
            if(self.node_expanded == 200000):
                print("error")
                return 0
            if(element.root in answer):
                element.p_print()
                print(self.node_expanded)
                break

            check = Move(element)

            up_element = check.up()
            down_element = check.down()
            left_element = check.left()
            right_element = check.right()

            if(right_element):
                if(self.exist(right_element.root, frontier) and self.exist(right_element.root, explored)):
                    frontier.append(right_element)
                    self.node_expanded += 1

            if(left_element):
                if(self.exist(left_element.root, frontier) and self.exist(left_element.root, explored)):
                    frontier.append(left_element)
                    self.node_expanded += 1

            if(down_element):
                if(self.exist(down_element.root, frontier) and self.exist(down_element.root, explored)):
                    frontier.append(down_element)
                    self.node_expanded += 1

            if(up_element):
                if(self.exist(up_element.root, frontier) and self.exist(up_element.root, explored)):
                    frontier.append(up_element)
                    self.node_expanded += 1

        while(element.parent is not None):
            self.path.append(element.position)
            element = element.parent
        print(self.path)



    def create_tree(self):
        frontier = []
        explored = []
        frontier.append(self.initial)
        while(frontier):
            element = frontier.pop()
            explored.append(element)
            check = Move(element)

            up_element = check.up()
            down_element = check.down()
            left_element = check.left()
            right_element = check.right()

            if(up_element):
                if(self.exist(up_element.root, frontier) and self.exist(up_element.root, explored)):
                    frontier.insert(0, up_element)
                    self.node_expanded += 1

            if(down_element):
                if(self.exist(down_element.root, frontier) and self.exist(down_element.root, explored)):
                    frontier.insert(0, down_element)
                    self.node_expanded += 1

            if(left_element):
                if(self.exist(left_element.root, frontier) and self.exist(left_element.root, explored)):
                    frontier.insert(0, left_element)
                    self.node_expanded += 1

            if(right_element):
                if(self.exist(right_element.root, frontier) and self.exist(right_element.root, explored)):
                    frontier.insert(0, right_element)
                    self.node_expanded += 1
            print(self.node_expanded)


a = Board([3,1,2,6,4,5,0,7,8])
c = Play(a,'bfs')
