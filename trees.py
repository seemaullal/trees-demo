"""Tree class and tree node class."""
# double edged queue
# good for both stacks and queue
# but for stacks you can just use a Python list
from collections import deque

class Node:
    """Node in a tree."""

    # never use an mutable default arg like on line 11
    # def __init__(self, data, children = []):
    def __init__(self, data, children = None):
        if not children:
            children = []
        self.data = data # Data (can be any type)
        self.children = children # List of Nodes

    def __repr__(self):
        """Reader-friendly representation."""

        return f"<Node {self.data}>"

    # breadth first search (level by level)
    def find_bfs(self, data):
        to_visit = deque([self])

        while to_visit:
            current = to_visit.popleft()

            if current.data == data:
                return current

            to_visit.extend(current.children)
            # to_visit.extend(current.children)

    def find(self, data):
        """Return node object with this data.

        Start here. Return None if not found.
        """

        to_visit = [self]

        while to_visit:
            # remove from the end
            # (remove the newest thing in the list/stack first)
            current = to_visit.pop()

            if current.data == data:
                return current
            for node in current.children:
                # add to the end of the list/stack
                to_visit.append(node)
            # to_visit.extend(current.children)
        # Node was not found
        # We tried all possibilities
        return None # technically not required


class Tree:
    """Tree."""

    def __init__(self, root):
        self.root = root

    def __repr__(self):
        """Reader-friendly representation."""

        return f"<Tree root={self.root}>"

    def find_in_tree(self, data):
        """Return node object with this data.

        Start at root.
        Return None if not found.
        """

        return self.root.find(data)


if __name__ == "__main__":
    # Make an example tree and search for things in it

    resume = Node("resume.txt", [])
    recipes = Node("recipes.txt", [])
    jane = Node("jane/", [resume, recipes])
    server = Node("server.py", [])
    jessica = Node("jessica/", [server])
    users = Node("Users/", [jane, jessica])
    root = Node("/", [users])

    tree = Tree(root)
    print("server.py = ", tree.find_in_tree("server.py"))  # should find
    print("style.css = ", tree.find_in_tree("style.css"))  # should not find
