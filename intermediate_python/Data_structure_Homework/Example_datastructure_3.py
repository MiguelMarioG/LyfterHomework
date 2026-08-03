class TreeNode:
    def __init__(self, data: str, left=None, right=None):
        self.data = data
        self.left = left 
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None


    def insert(self, data: str):
        new_node = TreeNode(data)
        if self.root is None:
            self.root = new_node
            return
        self._insert_recursive(self.root, new_node)


    def _insert_recursive(self, current: TreeNode, new_node: TreeNode) -> bool:
        if current.left is None:
            current.left = new_node
            return True
        if current.right is None:
            current.right = new_node
            return True
        if self._insert_recursive(current.left, new_node):
            return True
        return self._insert_recursive(current.right, new_node)


    def print_structure(self, node=None, level=0):
        if level == 0:
            node = self.root
            if node is None:
                print("The Tree is empty")
                return
            print(f"ROOT: {node.data}")
        if node is None:
            return
        if node.left:
            indent = "  " * (level + 1)
            print(f"{indent}├── (L): {node.left.data}")
            self.print_structure(node.left, level + 1)
        if node.right:
            indent = "  " * (level + 1)
            print(f"{indent}└── (R): {node.right.data}")
            self.print_structure(node.right, level + 1)


tree = BinaryTree()

tree.insert("Root")

tree.insert("L1-Left")
tree.insert("L1-Right")

tree.insert("L2-Son1_of_L1_Left")
tree.insert("L2-Son2_of_L1_Left")
tree.insert("L2-Son1_of_L1_Right")
tree.insert("L2-Son2_of_L1_Right")

print("--- Full Tree Structure by Levels ---")
tree.print_structure()