from manim import *

class Full(GraphScene):
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            x_axis_label="Groups",
            x_min=0,
            x_max=8,
            x_labeled_nums=[0,4,8],
            x_axis_width=5,
            y_axis_label="Molarity",
            y_min=0.05,
            y_max=0.1,
            y_labeled_nums=[0.05,0.1],
            y_axis_height=4,
            **kwargs)

    def construct(self):
        Table1.construct(self)
        SD.construct(self)
        Table1.move(self)
        Graph.construct(self)
        SD_Explained.construct(self)

class Table1(Scene):
    global table
    global tex_table
    table = r"""
    \begin{table}[]
    \centering
    \begin{tabular}{|l|l|l|l|l|}\hline
    \multicolumn{5}{|c|}{Group Averages}  \\\hline
    0.0773 & 0.0786 & 0.0857 & 0.0728 & 0.0640 \\
    \hline
    0.0631 & 0.0666 & 0.1296 & 0.0563 & 0.0820 \\
    \hline
    \end{tabular}
    \end{table}
    """
    tex_table = Tex(table)

    def construct(self):
        self.play(Write(tex_table))
        self.wait(2)
        self.play(ApplyMethod(tex_table.scale,0.5))
        self.play(ApplyMethod(tex_table.shift,4.5*LEFT+3.3*DOWN))

    def move(self):
        self.play(ApplyMethod(tex_table.shift,5*UP))

class SD(Scene):
    global sd
    global caption
    sd=MathTex("s=","\sqrt\\frac{\sum(x_i-\mu)^2}{n-1}")
    caption=Text("Standard Deviation")
    caption.shift(0.5*UP)

    def construct(self):

        self.play(Write(sd))
        self.wait()
        self.play(ApplyMethod(sd.shift,0.5*DOWN))
        self.play(Write(caption))
        self.play(FadeOut(caption))
        self.play(ApplyMethod(sd.shift,LEFT*5+UP*3.55))

def vertical_line(self, x, y, graph, line_class=Line, **line_kwargs):
    if "color" not in line_kwargs:
        line_kwargs["color"] = graph.get_color()
    return line_class(
        self.coords_to_point(x, y),
        self.input_to_graph_point(x, graph),
        **line_kwargs,
    )

class Graph(GraphScene):
    def construct(self):
        data = [0.0773, 0.0786, 0.0857, 0.0728, 0.0640, 0.0631, 0.0666, 0.0563, 0.0820]
        x = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        self.graph_origin = 2 * DOWN + -0.2 * RIGHT
        self.setup_axes(animate=True)

        dot_collection = VGroup()
        for time, val in enumerate(data):
            dot = Dot().move_to(self.coords_to_point(x[time], val))
            self.play(Create(dot))
            dot_collection.add(dot)
        
        self.wait()

        mean = self.get_graph(lambda x: 0.0718)
        mean_label = self.get_graph_label(mean, label="mean")
        self.play(Create(mean),Write(mean_label))

        for time, val in enumerate(data):
            line = vertical_line(self, x[time], val, mean, color=YELLOW)
            self.play(Create(line))

class SD_Explained(Scene):
    def construct(self):
        explanation_1=Text("Standard deviation is a")
        explanation_2=Text("measure of the typical")
        explanation_3=Text("distance each data point")
        explanation_4=Text("is from the sample mean")
        explanation_1.scale(0.6)
        explanation_1.shift(0*DOWN+4*LEFT)
        explanation_2.scale(0.6)
        explanation_2.shift(1*DOWN+4*LEFT)
        explanation_3.scale(0.6)
        explanation_3.shift(2*DOWN+4*LEFT)
        explanation_4.scale(0.6)
        explanation_4.shift(3*DOWN+4*LEFT)

        explanation2_1=Text("The yellow lines each")
        explanation2_2=Text("show the \"deviation\"")
        explanation2_3=Text("of each data point from")
        explanation2_4=Text("the mean")
        explanation2_1.scale(0.6)
        explanation2_1.shift(0*DOWN+4*LEFT)
        explanation2_2.scale(0.6)
        explanation2_2.shift(1*DOWN+4*LEFT)
        explanation2_3.scale(0.6)
        explanation2_3.shift(2*DOWN+4*LEFT)
        explanation2_4.scale(0.6)
        explanation2_4.shift(3*DOWN+4*LEFT)

        explanation3_1=Text("One data point (0.1296) was")
        explanation3_2=Text("an outlier, this is not")
        explanation3_3=Text("on the graph and is not")
        explanation3_4=Text("used in our calculations")
        explanation3_1.scale(0.6)
        explanation3_1.shift(0*DOWN+4*LEFT)
        explanation3_2.scale(0.6)
        explanation3_2.shift(1*DOWN+4*LEFT)
        explanation3_3.scale(0.6)
        explanation3_3.shift(2*DOWN+4*LEFT)
        explanation3_4.scale(0.6)
        explanation3_4.shift(3*DOWN+4*LEFT)

        self.play(Write(explanation_1),Write(explanation_2),Write(explanation_3),Write(explanation_4))
        self.wait(4)
        self.play(Transform(explanation_1,explanation2_1),Transform(explanation_2,explanation2_2),Transform(explanation_3,explanation2_3),Transform(explanation_4,explanation2_4))
        self.wait(4)
        self.play(Transform(explanation_1,explanation3_1),Transform(explanation_2,explanation3_2),Transform(explanation_3,explanation3_3),Transform(explanation_4,explanation3_4))
        self.wait(4)