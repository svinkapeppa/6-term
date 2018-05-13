import math

import draw
import numpy as np


class Mesh:
    def __init__(self, faces, coordinates=None):
        self.faces = faces
        vertices = set(i for f in faces for i in f)
        self.n = max(vertices) + 1
        if coordinates is not None:
            self.coordinates = np.array(coordinates)

        assert set(range(self.n)) == vertices
        for f in faces:
            assert len(f) == 3
        if coordinates is not None:
            assert self.n == len(coordinates)
            for c in coordinates:
                assert len(c) == 3

    @classmethod
    def create_from_obj(cls, filename):
        """
            TODO
        """
        faces, vertices = draw.obj_read(filename)
        return cls(faces, vertices)

    def distance(self, u, v):
        """
            TODO
        """
        return math.sqrt((self.coordinates[u][0] - self.coordinates[v][0]) ** 2 +
                         (self.coordinates[u][1] - self.coordinates[v][1]) ** 2 +
                         (self.coordinates[u][2] - self.coordinates[v][2]) ** 2)

    def draw(self):
        """
            TODO
        """
        draw.draw(self.faces, self.coordinates.tolist())

    def angular_defect(self, vertex):
        """
            Calculates an angular defect of the given vertex
            Input: vertex <int> - index from 0 to self.n - 1
            Output: defect <float> - angular defect of the given vertex
        """
        defect = 2 * math.pi
        for face in self.faces:
            if vertex in face:
                tmp = list(face)
                tmp.remove(vertex)
                u = tmp[0]
                v = tmp[1]
                top = self.distance(vertex, u) ** 2 + self.distance(vertex, v) ** 2 - self.distance(u, v) ** 2
                bottom = 2 * self.distance(vertex, u) * self.distance(vertex, v)
                defect -= math.acos(top / bottom)
        return defect

    def build_laplacian_operator(self, anchors=None, anchor_weight=1.):
        """
            Calculates laplacian matrix
            Input:  anchors <list<int>> - list of anchors
                    anchor_weight <float> (optional) - weight of anchors
            Output: laplacian <numpy.ndarray> - laplacian matrix
        """
        if anchors is None:
            anchors = []
        raise NotImplementedError

    def smooth(self, degree=0.5):
        """
            Smoothes the surface
            Input:  degree <float> (optional) - degree of smoothing
        """
        raise NotImplementedError

    def transform(self, anchors, anchor_coordinates, anchor_weight=1.):
        """
            TODO
            Input:  anchors
                    anchor_coordinates
                    anchor_weight
        """
        raise NotImplementedError


def dragon():
    """
        TODO
    """
    mesh = Mesh.create_from_obj("obj/dragon.obj")
    # raise NotImplementedError
    mesh.draw()
