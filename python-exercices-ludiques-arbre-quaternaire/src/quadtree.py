from __future__ import annotations


class QuadTree:
    NB_NODES: int = 4

    def __init__(self, hg: bool | QuadTree, hd: bool | QuadTree, bd: bool | QuadTree, bg: bool | QuadTree):
        self.list = [hg, hd, bd, bg]

        pass

    @property
    def depth(self) -> int:
        """ Recursion depth of the quadtree"""
        return 1

    @staticmethod
    def fromFile(filename: str) -> QuadTree:
        """ Open a given file, containing a textual representation of a list"""
        try:
            with open(filename) as f:
                lst = json.load(f)
                return QuadTree.fromList(lst)
        except:
            print("Unexpected Error while opening file")

        pass

    @staticmethod
    def fromList(data: list) -> QuadTree:
        """ Generates a Quadtree from a list representation"""

        for elem in data:
            if elem.type(list):
                """ Call this method recursively on list"""
                this.fromList(elem)
            elif elem.type(bool):
                self.list.append(elem)

        pass

    @staticmethod
    def browseTree(tree: list) -> Void:

        for elem in tree:
            if elem.type(list):
                self.browseTree(elem)
            elif elem == 1:
                print("plein")
            elif elem == 0:
                print("vide")
            else:
                print("error")
                return

        pass


class TkQuadTree(QuadTree):
    def paint(self):
        """ TK representation of a Quadtree"""
        pass


l = [1, 0, 0, 1]
q = QuadTree.fromList(l)
q2 = QuadTree.fromFile("../files/quadtree_easy.txt")
