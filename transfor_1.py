from manim import *

class vectorPrueba(LinearTransformationScene):

    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            show_basis_vectors=False,
            include_background_plane=True
            
        )


    def construct(self):

        #dot_1 = Dot(point=RIGHT + UP)
        #dot_2 = Dot(point=2*RIGHT + 2*UP)

        
        self.add_vector([1,-2], color=RED_A)
        self.add_vector([2,1], color=GREEN_A)

        #matrix = rotation(-3*np.pi/2)
        matrix = [[-3/5,-8/5],[-4/5,6/5]]

        self.apply_matrix(matrix)
        self.wait()

#print(type(LEFT))