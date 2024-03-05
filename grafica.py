from manim import *
from numpy import sqrt

class graphPrueba(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 6, 1],
            y_length=[6.0],
            tips=False,
            axis_config={"include_numbers": True},
            y_axis_config={"unit_size": 2}
        )

        #Formulas 
        f_x = lambda x: sqrt(x)
        x_approx = 2
        y_tangent_1 = lambda x: 1 + (1/2)*(x-1) 
        y_tangent_2 = lambda x: y_tangent_1(x) - (1/8)*(x-1)**2
        y_tangent_3 = lambda x: y_tangent_2(x) + (3/48)*(x-1)**3
        y_tangent_4 = lambda x: y_tangent_3(x) - (15/384)*(x-1)**4
        y_tangent_5 = lambda x: y_tangent_4(x) + (105/3840)*(x-1)**5
        poli_taylor = lambda x: y_tangent_5(x)

        #text 
        function = MathTex(r'f(x) = \sqrt(x)', font_size=30).to_edge(UR).shift(1/2,-1/2)
        root_two = MathTex(fr'f({x_approx}) = {f_x(x_approx)}', font_size=30).to_edge(UR).shift(0,-1/2)
        taylor_aprox = MathTex(fr'P({x_approx}) = {poli_taylor(x_approx)}', font_size=30).to_corner(RIGHT).shift(0,1/2)

        #plotting
        Graph_f = ax.plot(f_x, x_range=[0,10])

        self.play(Create(ax), run_time= 3)
        Wait(2)
        self.add(function, root_two)
        self.play(Create(Graph_f),run_time= 4)

        plot = ((y_tangent_1,GREEN), (y_tangent_2,RED), (y_tangent_3,BLUE), (y_tangent_4,YELLOW), (y_tangent_5,ORANGE))
        plots = []
        n = 0    
        for i,j in plot:
            graph = ax.plot(i, color = j)
            plots.append(graph)
            self.play(Create(graph), run_time = 4)
        self.wait(1) 
        for i in plots:
            self.remove(plots[n])
            self.wait(1)
            n += 1

        self.wait(2) 
        graph_poli_taylor = ax.plot(poli_taylor, color = BLUE_D)

        self.play(Create(graph_poli_taylor), run_time = 4)
        self.wait(1)
        self.add(taylor_aprox)
        self.wait(5)

