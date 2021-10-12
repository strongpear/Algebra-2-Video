# Author: Jason Lee
# Goal: Create Animations to make an introductory video about Algebra 2

from manim import *

class Introduction(ThreeDScene):
    def construct(self):

        # Define all of the Mobjects
        text = Text(r"Welcome to Algebra 2!")
        circle = Circle(radius = 1, color = BLUE)
        circle.set_fill(BLUE, opacity = 0.8)
        sphere = Sphere(radius = 1) # Sphere "top-down perspective"

        # Animate
        self.play(Write(text))
        self.wait()
        self.play(ApplyMethod(text.to_corner, UL)) # Move text to upper left corner
        self.add_fixed_in_frame_mobjects(text) # Fix text so it doesnt transform
        self.set_camera_orientation(phi = 0, theta = 0)
        self.play(Create(circle))
        self.wait(1)
        self.play(ReplacementTransform(circle, sphere)) # Transform circle to sphere
        self.move_camera(phi = PI / 3)
        self.begin_ambient_camera_rotation(rate = 0.1) # Rotate around object
        self.wait(5)
        self.play(FadeOut(text), Uncreate(sphere))
        self.wait()

class FirstScene(Scene):    # Talk about variables
    def construct(self):

        # Define all of the Text
        text = Text(r"Arithmetic")
        text1 = Text(r"Algebra", color = RED).shift(UP * 3)
        text2 = Text(r"That thing").shift(DOWN * 2, LEFT)
        text3 = Text(r"Variables", color = RED).shift(DOWN * 2, LEFT)
        var = Tex(r"x", color = RED)
        var2 = Tex(r"x", color = RED)
        eq1_1 = Tex(r" + 2 = 3")
        eq1_2 = Tex(r"1").next_to(eq1_1, LEFT)
        eq1 = VGroup(eq1_1, eq1_2)
        eq2_1 = Tex(r" * 5 = 20")
        eq2_2 = Tex(r"4").next_to(eq2_1, LEFT)
        eq2 = VGroup(eq2_1, eq2_2)

        # Animate
        self.play(Write(text))
        self.wait(2)
        self.play(ApplyMethod(text.shift, UP * 3))  # Title up top
        self.play(FadeIn(eq1))
        self.play(ApplyMethod(eq1.shift, LEFT * 3)) # 1+2 = 3 to left
        self.play(FadeIn(eq2))
        self.play(ApplyMethod(eq2.shift, RIGHT * 3)) # 4 * 5 = 20 to the right
        self.wait(5)

        self.play(Transform(eq1_2, var.next_to(eq1_1, LEFT)),
         Transform(eq2_2, var2.next_to(eq2_1, LEFT)))           # Transform into "x"'s
        arrow1 = Arrow(text2, var)
        arrow2 = Arrow(text2, var2)
        self.play(Write(text2), Create(arrow1), Create(arrow2)) # Arrows to variables
        self.wait(2)
        self.play(Transform(text2, text3))
        self.wait(2)
        self.play(Transform(text, text1))
        self.wait(3)
        self.play(FadeOut(eq1, eq2, text, text2), Uncreate(arrow1), Uncreate(arrow2))

class SecondScene(Scene):   # Talk about functions
    def construct(self):

        # Define everything
        title = Text(r"Vending Machine").shift(UP * 3).scale(1.5).set_color(BLUE)
        choices = Tex(r"Coke", r"Sprite", r"Water").arrange(DOWN, buff = .5).shift(LEFT * 2)    # Choices for vending machine
        output = VGroup(Tex(r"Coke"), Tex(r"Water?")).shift(RIGHT * 2)                          # outputs for future choices
        graphTitle = Text(r"Function").shift(UP * 3.4).set_color(BLUE_A)
        graphText = VGroup(Tex(r"Which output do we choose?"),
                           Tex(r"This point is guaranteed.")).shift(LEFT * 3, UP * .25).scale(.5)   # Function or not a function
        points = VGroup(Dot(point = [1, 1, 0], color = RED), Dot(point = [1, -1, 0], color = RED))  # points for "solutions"
        arrows = VGroup()
        for choice in choices:
            arrows += Arrow(choice, output, stroke_width = 3)   # Arrows for vending machine
        graphArrows = VGroup(Arrow(graphText, points[0], stroke_width=3), Arrow(graphText, points[1], stroke_width=3))

        # Create graphs
        axes = Axes(x_range = (-4, 4), y_range = (-4, 4), x_length = 8)          
        func1 = ParametricFunction(lambda t: [t ** 2, t, 0], t_range = [-2, 2], color = BLUE)
        func2 = FunctionGraph(lambda x: x ** 2, x_range = (-2, 2), color=YELLOW)

        # Animate
        self.play(FadeIn(title), Write(choices))
        self.play(Create(arrows))
        self.wait(1)
        self.play(Indicate(choices[0]), Write(output[0]))
        self.wait(8)
        self.play(Indicate(choices[1]), ReplacementTransform(output[0], output[1].set_color(RED)))
        self.wait(5)
        self.play(FadeOut(title), FadeOut(choices), Uncreate(arrows), FadeOut(output[1]))

        # Graph scene
        self.play(FadeIn(axes), Create(func1), FadeIn(points))
        self.play(Create(graphArrows), Write(graphText[0]))
        self.wait(5)
        self.play(Transform(func1, func2),
                  Transform(graphText[0],
                  graphText[1].set_color(RED_A)), 
                  Uncreate(graphArrows[1]), 
                  FadeOut(points[1]))
        self.wait(1)
        self.play(Write(graphTitle))
        self.wait(2)
        self.play(FadeOut(graphTitle),
                  Uncreate(graphArrows[0]), 
                  FadeOut(points[0]), 
                  FadeOut(axes),
                  FadeOut(graphText[0]),
                  Uncreate(func1))
        self.wait()

class ThirdScene(Scene):    # Talk about function families
    def construct(self):

        # define
        rectH = 3
        rectW = 4
        pFunc = MathTex("f(x) = x", "f(x) = x^2", "f(x) = sin(x)")
        numgroups = 12
        title = Tex("There's a lot of functions...").to_edge(UP)
        title1 = Tex("Infinitely many!").to_edge(UP)
        title2 = Text("Function Families").to_edge(UP)
        title3 = Text("Basic Functions").scale(0.8).to_corner(UL)
        title4 = Text("Parent Function", color = BLUE).scale(0.8).to_corner(UL)
        bigRect = Rectangle(height = rectH, width = rectW).set_fill(YELLOW, opacity=0.7).set_stroke(width=0)    # Create initial rectangle
        smallRect = Rectangle(height = 1, width = 1).set_fill(YELLOW, opacity=0.7).set_stroke(width=0)          # Small rectangle
        group = VGroup(*[smallRect.copy() for i in range(4)]).arrange(RIGHT)                                    # split big rect into 12 small recrs
        group_1 = VGroup(*[group.copy() for i in range(3)]).arrange(DOWN)

        # Graph scene
        axes = Axes()
        axes_label = axes.get_axis_labels()
        lin_graph = axes.get_graph(lambda x: x, color = BLUE)           # line
        lin_label = axes.get_graph_label(lin_graph, pFunc[0])
        quad_graph = axes.get_graph(lambda x: x ** 2, color = RED)      # Quadratic
        quad_label = axes.get_graph_label(quad_graph, pFunc[1])
        sin_graph = axes.get_graph(lambda x: np.sin(x), color = ORANGE) # Sine
        sin_label = axes.get_graph_label(sin_graph, pFunc[2])
        plot = VGroup(lin_graph, sin_graph, quad_graph)
        labels = VGroup(lin_label, sin_label, quad_label)


        # Animate

        self.play(Create(bigRect), Write(title))
        self.wait(1)
        self.play(Transform(title, title1))
        self.wait(3)
        self.play(Transform(bigRect, group_1), Transform(title, title2))
        self.wait(2)
        self.play(Uncreate(bigRect))
        self.wait()
        self.play(Create(axes), Transform(title, title3))
        self.play(Write(plot[0]), Write(labels[0]))
        for i in range(len(plot) - 1):                  
            self.play(ReplacementTransform(plot[i], plot[i+1]), ReplacementTransform(labels[i], labels[i+1]))       # Transform through graphs
            self.wait(1.5)
        self.wait(2)
        self.play(Transform(title, title4))
        self.wait(3)

        
class FourthScene(Scene):   # Talk about transformations and characteristics

    def construct(self):
        title = VGroup(Text("Parent Function", color = BLUE), Text(r"'Child' Functions")).scale(0.8).to_corner(UL)
        axes = Axes()

        # Different transformations
        parent = axes.get_graph(lambda x: x ** 2, color = RED)
        shift = axes.get_graph(lambda x: (x - 2) ** 2 + 2, color = BLUE)
        stretch = axes.get_graph(lambda x: ((x / 2) - 2) ** 2 + 2, color = GREEN)
        ref = axes.get_graph(lambda x: -2 * ((x / 2) - 2) ** 2 + 2, color = YELLOW)
        dots = VGroup(Dot(point = axes.coords_to_point(2, 0), color = BLUE), Dot(point = axes.coords_to_point(6, 0), color = BLUE))
        text = Text("Solutions").move_to(axes.coords_to_point(4, -2))
        arrows = VGroup(Arrow(text, dots[0]), Arrow(text, dots[1]))

        # Animate
        self.add(axes, title[0], parent)
        self.wait(6)

        # Transform through all of the transformations
        self.play(Transform(parent, shift), Transform(title[0], title[1].set_color(YELLOW)))
        self.wait(1)
        self.play(Transform(parent, stretch))
        self.wait(1)
        self.play(Transform(parent, ref))
        self.wait(1)
        self.play(Indicate(title[0]))
        self.wait(4)

        # Solutions
        self.play(Create(dots), Create(arrows))
        self.wait(8)
        self.play(Write(text))
        self.wait(1)
        self.play(FadeOut(axes), FadeOut(title[0]), FadeOut(parent), FadeOut(dots), FadeOut(arrows), FadeOut(text))
        self.wait(2)
        
class FifthScene(Scene):    # Talk about class as a whole
    def construct(self):
        title = Text("Algebra 2").to_edge(UP).scale(1.5)
        list = BulletedList("Parent Function", "Child Functions", "Solving Functions", "Characteristics of Functions")
        list.set_color_by_tex("Parent Function", RED)
        list.set_color_by_tex("Child Functions", GREEN)
        list.set_color_by_tex("Solving Functions", BLUE)
        list.set_color_by_tex("Characteristics of Functions", YELLOW)
        self.play(Write(title))
        self.wait(1)
        for item in list:
            self.play(Write(item))
            self.wait(1)
        self.wait(5)
        self.play(FadeOut(title), FadeOut(list))
        self.wait()

class FinalScene(Scene):        # Talk about applications
    def construct(self):
        title = Text("Who Cares?", color = BLUE).scale(1.5)
        money = VGroup(Tex("Money", color = LIGHT_BROWN), MathTex(r"f(t) = P(1 + \frac{1}{n})^{nt}").scale(0.7)).arrange(DOWN).shift(LEFT * 4)
        mixture = VGroup(Tex("Mixture", color = LIGHT_BROWN), MathTex(r"C(t) = \frac{10 + x}{20 + 3x}").scale(0.7)).arrange(DOWN)
        virus = VGroup(Tex(r"Num of Infections", color = LIGHT_BROWN), MathTex(r"f(t) = \frac{L}{1 + Ce^{-Lkt}}").scale(0.7)).arrange(DOWN).shift(RIGHT * 4)
        self.play(Write(title))
        self.wait(10)
        self.play(ApplyMethod(title.to_edge, UP))
        self.wait()
        self.play(FadeIn(money))
        self.wait(6)
        self.play(FadeIn(mixture))
        self.wait(6)
        self.play(FadeIn(virus))
        self.wait(3)
        self.play(FadeOut(title), FadeOut(money), FadeOut(mixture), FadeOut(virus))

class EndScene(ThreeDScene):        # Outro
    def construct(self):
        start = Prism()
        shapes = VGroup(Cube(), Cylinder(), Cone(), Sphere(), Torus(major_radius=1, minor_radius=0.5))
        endText = Text("Thanks for watching!", color = BLUE).to_edge(UP)
        
        self.play(Write(endText))
        self.add_fixed_in_frame_mobjects(endText)
        self.set_camera_orientation(phi = 60 * DEGREES, theta = 25 * DEGREES)
        self.begin_ambient_camera_rotation(rate = 0.15)
        self.play(Create(start))
        self.wait()
        for shape in shapes:
            self.play(Transform(start, shape))
            self.wait(4)
        
