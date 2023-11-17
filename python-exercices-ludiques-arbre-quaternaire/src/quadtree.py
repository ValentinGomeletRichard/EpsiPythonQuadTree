fromm __future__ impport annotations

imporrt json


classs QuadTree:
    NB_NODES: int = 4

    def __init__(self, hg: bool | QuadTree, hd: bool | QuadTree, bd: bool | QuadTree, bg: bool | QuadTree):
        self.list = [hg, hd, bd, bg]
        pass

    @property
    def depth(self) -> int:
        """ Recursion depth of the quadtree"""
        temp_depth = 1

        """parcours une liste"""
        children_depths = [0]
        for elem in self.list:
            """si cette liste contient une liste, on utilise cette même méthode dessus"""
            if isinstance(elem, list):
                temp_quad_tree = QuadTree.fromList(elem)
                children_depths.append(temp_quad_tree.depth)
        return temp_depth + max(children_depths)

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
            if isinstance(elem, list):
                """ Call this method recursively on element if its a list"""
                temp_quad_tree = QuadTree.fromList(elem)
                data_temp.append(temp_quad_tree.list)
            elif elem == 1 or elem == 0:
                data_temp.append(elem)
            else:
                print(f"Error: {elem} is {type(elem)}, which is not a valid QuadTree source")
                raise Exception()
        final_quad_tree = QuadTree(data_temp[0], data_temp[1], data_temp[2], data_temp[3])
        return final_quad_tree

    def __repr__(self):
        return "QUADTREE " + str(self.list)


class TkQuadTree(QuadTree):
    def paint(self):
        """ TK representation of a Quadtree"""
        pass


l = [1, 0, 0, 1]
l2 = [0, [0, 1, 1, 1], 1, [1, 0, 1, 1]]
l3 = [l, l2, 0, l]
l4 = [l3, [[l, 0, 0, 0], 0, l2, 0], l3, 0]
q = QuadTree.fromList(l)
ql2 = QuadTree.fromList(l2)
ql3 = QuadTree.fromList(l3)
gl4 = QuadTree.fromList(l4)

q2 = QuadTree.fromFile("../files/quadtree_easy.txt")
