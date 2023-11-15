from __future__ import annotations


class QuadTree:
    NB_NODES: int = 4

    def __init__(self, hg: bool | QuadTree, hd: bool | QuadTree, bd: bool | QuadTree, bg: bool | QuadTree):
        self.list = [hg, hd, bd, bg]
        self.depth = 0
        pass

    @property
    def depth(self) -> int:
        """ Recursion depth of the quadtree"""
        return self.depth

    @staticmethod
    def fromFile(filename: str) -> QuadTree:
        """ Open a given file, containing a textual representation of a list"""
        try:
            with open(filename) as f:
                lst = json.load(f)
                return QuadTree.fromList(lst)
        except:
            print("Unexpected Error while opening file")

    @staticmethod
    def fromList(data: list) -> QuadTree:
        """ Generates a Quadtree from a list representation"""

        data_temp = []
        for elem in data:
            if elem.type(list):
                """ Call this method recursively on element if its a list"""
                temp_quad_tree = QuadTree.fromList(elem)
                data_temp.append(temp_quad_tree)
            elif elem.type(bool):
                data_temp.append(elem)
            else:
                raise Exception("Error: this is not a valid QuadTree element")
        return QuadTree(data_temp)


class TkQuadTree(QuadTree):
    def paint(self):
        """ TK representation of a Quadtree"""
        pass


l = [1, 0, 0, 1]
q = QuadTree.fromList(l)
q2 = QuadTree.fromFile("../files/quadtree_easy.txt")
