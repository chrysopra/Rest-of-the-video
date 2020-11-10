from manimlib.imports import *
import numpy as np

class graph1(GraphScene):
    CONFIG={
        "x_min": -1,
        "x_max": 7,
        "x_tick_frequency": 1,
        "x_leftmost_tick": -1,
        "x_labeled_nums": None,
        "x_axis_label": None,
        "y_min": -1,
        "y_max": 4,
        "y_tick_frequency": 1,
        "y_bottom_tick": -1,
        "y_labeled_nums": None,
        "y_axis_label": None,
        
    }


    def show_function_graph(self):
        self.setup_axes(animate=True)
        def func(x):
            return x**(1/x)
        graph = self.get_graph(func, x_min=0, x_max=7, color = WHITE)
        graph1 =self.get_graph(func, x_min=2.71, x_max=7, color = RED)
        
        vert = self.get_vertical_line_to_graph(2.71, graph, color = RED)
        
        dot = Dot(self.coords_to_point(2.71, 0))
        
        e = TexMobject("e")
        e.next_to(dot, 0.3*DOWN)
        e.scale(1)

        path1 = self.get_graph(lambda x: x**(1/x), x_min = 3, x_max = 4)
        path2 = self.get_graph(lambda x: x**(1/x), x_min = 4, x_max = 5)
        path3 = self.get_graph(lambda x: x**(1/x), x_min = 5, x_max = 7)
        path4 = self.get_graph(lambda x: x**(1/x) + 0.38, x_min = 5, x_max = 7)
        
        dash = DashedVMobject(vert)

        dot1 = Dot(self.coords_to_point(3, self.func_to_graph(3)))
        dot1.set_color(YELLOW)
        dot1.scale(1)

        dot2 = Dot(self.coords_to_point(4, self.func_to_graph(4)))
        dot3 = Dot(self.coords_to_point(5, self.func_to_graph(5)))
        dot4 = Dot(self.coords_to_point(7, self.func_to_graph(7)))

        coordinat1 = TexMobject("\\left[",
                                "3",
                                ",",
                                "f("
                                "3",
                                ")",
                                "\\right]"
                                )
        coordinat1.next_to(dot1, 0.5*UP)
        coordinat1.scale(0.7)

        coordinat2 = TexMobject("\\left[",
                                "4",
                                ",",
                                "f("
                                "4",
                                ")",
                                "\\right]"
                                )
        coordinat2.next_to(dot2, 0.5*UP)
        coordinat2.scale(0.7)

        coordinat3 = TexMobject("\\left[",
                                "5",
                                ",",
                                "f("
                                "5",
                                ")",
                                "\\right]"
                                )
        coordinat3.next_to(dot3, 0.5* UP)
        coordinat3.scale(0.7)

        coordinat4 = TexMobject("\\left[",
                                "7",
                                ",",
                                "f("
                                "7",
                                ")",
                                "\\right]"
                                )
        coordinat4.next_to(dot4, 0.5*UP)
        coordinat4.scale(0.7)

        self.wait(6)
        self.play(ShowCreation(graph))
        self.wait(6)
        self.play(ShowCreation(dash), Write(e), run_time = 1.5)
        self.play(ShowCreation(graph1), run_time = 1.5)
        self.wait(7)
        self.play(ShowCreation(dot1), FadeIn(coordinat1))
        self.wait(2)
        self.play(MoveAlongPath(dot1, path1), Transform(coordinat1, coordinat2))
        self.wait(2)
        self.play(MoveAlongPath(dot1, path2), Transform(coordinat1, coordinat3))
        self.wait(2)
        self.play(FadeOut(dot1), FadeOut(coordinat1), MoveAlongPath(dot1, path3), MoveAlongPath(coordinat1, path4))
        self.wait(10)

    def construct(self):
        self.show_function_graph()
    def func_to_graph(self,x):
        return(x**(1/x))
