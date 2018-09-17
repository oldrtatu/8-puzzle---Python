import pickle

class Tree:

    def __init__(self, root, color, parent = None):
        self.root = root
        self.parent = parent
        self.color = color
        self.children = []
        if parent is not None:
            self.parent.children.append(self)

#
# root = Tree(2, 'red')
#
# child = Tree(5, 'black', root)
#
#
# pickle_out = open('object.pickle', 'wb')
# pickle.dump(root, pickle_out)
# pickle_out.close()


tr = open('object.pickle', 'rb')
obj = pickle.load(tr)
