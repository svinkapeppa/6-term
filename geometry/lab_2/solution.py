import math

import draw
import numpy as np
from scipy.sparse import coo_matrix, vstack
from scipy.sparse.linalg import lsqr


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
    def create(cls, filename):
        """
            Creates mesh
            Input:  filename <string> - path to the file with object
            Output: object of class Mesh
        """
        faces, vertices = draw.read(filename)
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
            Draws object
        """
        draw.draw(self.faces, self.coordinates.tolist())

    def angular_defect(self, vertex):
        """
            Calculates an angular defect of the given vertex
            Input:  vertex <int> - index from 0 to self.n - 1
            Output: defect <float> - angular defect of the given vertex
        """
        defect = 2 * math.pi
        for face in self.faces:
            if vertex in face:
                tmp = list(face)
                tmp.remove(vertex)
                u, v = tmp
                top = self.distance(vertex, u) ** 2 + self.distance(vertex, v) ** 2 - self.distance(u, v) ** 2
                bottom = 2 * self.distance(vertex, u) * self.distance(vertex, v)
                defect -= math.acos(top / bottom)
        return defect

    def laplacian_operator(self, anchors=None, anchor_weight=1.):
        """
            Calculates laplacian matrix
            Input:  anchors <list<int>> - list of anchors
                    anchor_weight <float> (optional) - weight of anchors
            Output: laplacian <scipy.sparse.coo_matrix> - laplacian matrix
        """
        neighbors = np.zeros(self.n)
        data = np.array([])
        row = np.array([])
        column = np.array([])
        seen = set()
        
        # Precalculate N(i) for each vertex
        for face in self.faces:
            a, b, c = face
            neighbors[a] += 1
            neighbors[b] += 1
            neighbors[c] += 1
        
        # Diagonal elements
        data = -1 * np.ones(self.n)
        row = np.arange(self.n)
        column = np.arange(self.n)    
        
        # Build laplacian operator
        for face in self.faces:
            a, b, c = face
            if (a, b) not in seen:
                data = np.append(data, 1 / neighbors[a])
                row = np.append(row, a)
                column = np.append(column, b)
                seen.add((a, b))
            if (a, c) not in seen:
                data = np.append(data, 1 / neighbors[a])
                row = np.append(row, a)
                column = np.append(column, c)
                seen.add((a, c))
            if (b, a) not in seen:
                data = np.append(data, 1 / neighbors[b])
                row = np.append(row, b)
                column = np.append(column, a)
                seen.add((b, a))
            if (b, c) not in seen:
                data = np.append(data, 1 / neighbors[b])
                row = np.append(row, b)
                column = np.append(column, c)
                seen.add((b, c))
            if (c, a) not in seen:
                data = np.append(data, 1 / neighbors[c])
                row = np.append(row, c)
                column = np.append(column, a)
                seen.add((c, a))
            if (c, b) not in seen:
                data = np.append(data, 1 / neighbors[c])
                row = np.append(row, c)
                column = np.append(column, b)
                seen.add((c, b))
        L = coo_matrix((data, (row, column)))
        
        # Anchors
        if anchors is not None:
            data = anchor_weight * np.ones(len(anchors))
            row = np.arange(len(anchors))
            column = np.array(anchors)
            end = coo_matrix((data, (row, column)), shape=(len(anchors), self.n))
            return vstack([L, end])
        else:
            return L

    def smooth(self, scale=0.5):
        """
            Smoothes the surface
            Input:  scale <float> (optional) - scale of smoothing
        """
        L = self.laplacian_operator(anchors=np.arange(self.n), anchor_weight=scale)
        b = np.vstack((np.zeros((self.n, 3)), self.coordinates * scale))
        x = lsqr(L, b[:, 0])[0].reshape(-1, 1)
        y = lsqr(L, b[:, 1])[0].reshape(-1, 1)
        z = lsqr(L, b[:, 2])[0].reshape(-1, 1)
        self.coordinates = np.hstack((x, y, z))

    def transform(self, anchors, anchor_coordinates, anchor_weight=1.):
        """
            Performs smooth transformation
            Input:  anchors <list<int>> - list of anchors
                    anchor_coordinates <list<float>> - their coordinates
                    anchor_weight <float> - weight of anchors
        """
        L = self.laplacian_operator(anchors=anchors, anchor_weight=anchor_weight)
        b = np.vstack((np.ones((self.n, 3)), anchor_coordinates * anchor_weight))
        x = lsqr(L, b[:, 0])[0].reshape(-1, 1)
        y = lsqr(L, b[:, 1])[0].reshape(-1, 1)
        z = lsqr(L, b[:, 2])[0].reshape(-1, 1)
        self.coordinates = np.hstack((x, y, z))


def dragon():
    """
        Applies functions written above to `dragon.obj`
    """
    anchors = np.random.randint(0, mesh.n, 200)
    anchor_coordinates = (mesh.coordinates[anchors] * 1.6) - 11
    
    mesh = Mesh.create("obj/dragon.obj")
    mesh.smooth(scale=0.3)
    mesh.transform(anchors=anchors, anchor_coordinates=anchor_coordinates)
    mesh.draw()
