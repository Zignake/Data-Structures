class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self .children.append(child)

    def print_tree(self):
        print

    
Tree = TreeNode('Pokemon')
Grass = TreeNode('Grass')
Fire = TreeNode('Fire')
Water = TreeNode('Water')

Grass.add_child(TreeNode('Bulbasaur'))
Grass.add_child(TreeNode('Ivysaur'))
Fire.add_child(TreeNode('Charmander'))
Fire.add_child(TreeNode('Charmeleon'))
Water.add_child(TreeNode('Squirtle'))
Water.add_child(TreeNode('Wartortle'))

Tree.add_child(Grass)
Tree.add_child(Water)
Tree.add_child(Fire)