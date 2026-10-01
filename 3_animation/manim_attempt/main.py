from manim import *

class Aesthetics(Scene):
    def construct(self):
        detail_color = ManimColor("#FFB000")
        background_color = ManimColor("#131313")
        
        # Just do lines
        start = 0
        end = 10+10+10
        line_side = []
        line_up = []
        for i in range(0, 2):
            for j in range(start, end):
                # starting_point = [LEFT, j*RIGHT, 0]
                # ending_point = [LEFT, RIGHT*100, 0]
                line_side.append(Line(LEFT, RIGHT*100).set_color(detail_color).set_opacity(0.2))
                if i == 1:
                    line_up.append(Line(UP, DOWN*100).set_color(detail_color).set_opacity(0.2))

        self.add(VGroup(line_side).arrange(DOWN, buff=.5))
        self.add(VGroup(line_up).arrange(RIGHT, buff=.5))

        self.camera.background_color = background_color

        # Space mono isn't working, try to restart computer after installing it?
        # Check to make sure it is working.
        self.add(VGroup([Text("Bob Was HEre", font="Space Grotesk"), Text("Whereas disregard", font="Space Mono")]).arrange(DOWN))
        # self.add(Text("Bob Was HEre", font="Space Mono"))
        
# Make the thumbnail here? Might be easier than using inkscape or something.
class Thumbnail(Scene):
    def construct(self):
        detail_color = ManimColor("#FFB000")
        background_color = ManimColor("#131313")
        
        # Just do lines
        start = 0
        end = 10+10+10
        line_side = []
        line_up = []
        for i in range(0, 2):
            for j in range(start, end):
                # starting_point = [LEFT, j*RIGHT, 0]
                # ending_point = [LEFT, RIGHT*100, 0]
                line_side.append(Line(LEFT, RIGHT*100).set_color(detail_color).set_opacity(0.1))
                if i == 1:
                    line_up.append(Line(UP, DOWN*100).set_color(detail_color).set_opacity(0.1))

        self.add(VGroup(line_side).arrange(DOWN, buff=.5))
        self.add(VGroup(line_up).arrange(RIGHT, buff=.5))

        self.camera.background_color = background_color

        # Space mono isn't working, try to restart computer after installing it?
        # Check to make sure it is working.
        self.add(Text("The Analysis No One Uses", font_size=80, t2w={'No One':ULTRAHEAVY}, color=detail_color, font="Space Grotesk", weight="BOOK").move_to([0, 2, 0]))
        self.add(Text("Build", font_size=50, color=detail_color, font="Space Grotesk").move_to([-2.5, -2.5, 0]))
        self.add(Text("Measure", font_size=50, color=detail_color, font="Space Grotesk"))
        self.add(Text("Learn", font_size=50, color=detail_color, font="Space Grotesk").move_to([2.5, -2.5, 0]))
        self.add(Arrow(start=[-2,-2, 0], end=[-0.5, -0.5, 0], color=detail_color))
        self.add(Arrow(start=[0.5, -0.5, 0], end=[2, -2, 0], color=detail_color))
        self.add(Arrow(start=[1.5, -2.5, 0], end=[-1.5, -2.5, 0], color=detail_color))
        # uv run manim -pqk ./main.py Thumbnail

# Start storyboarding, then transfer over?
# Annotated box
class AnnotatedBox(Scene):
    def construct(self):
        box = RoundedRectangle(corner_radius=.5, height = 5, width = 10)
        fill_background = Rectangle(color=BLACK, fill_opacity=1).move_to([box.get_left()[0]/3, box.get_top()[1],0])
        # fill_background.color = BLACK
        fill_background.stroke_color = BLACK
        self.add(box)
        self.add(fill_background)
        self.add(Text("Label Text").move_to([box.get_left()[0]/3, box.get_top()[1],0]))
# Zoom into box
class ZoomBox(MovingCameraScene):
    def construct(self):
        box = RoundedRectangle(corner_radius=.5, height = 5, width = 10)
        fill_background = Rectangle(color=BLACK, fill_opacity=1).move_to([box.get_left()[0]/3, box.get_top()[1],0])
        # fill_background.color = BLACK
        fill_background.stroke_color = BLACK
        self.add(box)
        self.add(fill_background)
        self.add(Text("Label Text").move_to([box.get_left()[0]/3, box.get_top()[1],0]))
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.set(width=box.width*.95).move_to([box.get_center()[0], box.get_top()[1]/8, 0]))
        self.wait()
        self.play(Restore(self.camera.frame))
        self.wait()
# Do stuff in box?
class DoStuff(MovingCameraScene):
    def construct(self):
        box = RoundedRectangle(corner_radius=.5, height = 5, width = 10)
        fill_background = Rectangle(color=BLACK, fill_opacity=1).move_to([box.get_left()[0]/3, box.get_top()[1],0])
        # fill_background.color = BLACK
        fill_background.stroke_color = BLACK
        self.add(box)
        self.add(fill_background)
        self.add(Text("Label Text").move_to([box.get_left()[0]/3, box.get_top()[1],0]))
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.set(width=box.width*.95).move_to([box.get_center()[0], box.get_top()[1]/8, 0]))
        self.wait()
        hello = Text("hello").move_to([box.get_left()[0]*.8, box.get_center()[1], 0])
        # .8 -> .75 because too close to the edge
        world = Text("world").move_to([box.get_right()[0]*.75, box.get_center()[1], 0])
        # .8 -> .6/.55 because spacing of words
        from_to = Arrow([box.get_left()[0]*.6, box.get_center()[0], 0], [box.get_right()[0]*.55, box.get_center()[0], 0])
        self.play(Write(hello))
        self.play(Write(world))
        self.play(Write(from_to))
        self.play(Restore(self.camera.frame))
        self.wait()
        self.play(FadeOut(hello), FadeOut(world), FadeOut(from_to))
    
class Animation(MovingCameraScene):
    def construct(self):
        detail_color = ManimColor("#FFB000")
        background_color = ManimColor("#131313")
        
        # self.camera.scale(.5)

        # Just do lines
        start = 0
        end = 10**3
        line_side = []
        line_up = []
        for i in range(0, 2):
            for j in range(start, end):
                # starting_point = [LEFT, j*RIGHT, 0]
                # ending_point = [LEFT, RIGHT*100, 0]
                line_side.append(Line(LEFT, RIGHT*100).set_color(detail_color).set_opacity(0.1))
                if i == 1:
                    line_up.append(Line(UP, DOWN*100).set_color(detail_color).set_opacity(0.1))


        self.camera.background_color = background_color

        # Hook; what symbolism can I use to denote the hooks ideas? 48 words = 19.2 seconds
        question = Text("?", color=detail_color, font_size=100)
        alarm = Text("!", color=detail_color, font_size=150)

        # Commented out to make things quicker
        # self.play(Write(question), duration=.2)
        # self.play(Rotate(question, 2), duration = .2)
        # self.play(Rotate(question, -4), duration = .2)
        # #Alarm is now reference by question
        # self.play(Transform(question, alarm), duration = .1)
        # self.play(ScaleInPlace(question, 2), duration = .2)
        # self.play(FadeOut(question))
        # Introduction; 60 words or about 24 seconds

        # Build measure learn thing
        height = 10.0
        width = 20.0
        
        build_box = RoundedRectangle(color = detail_color, corner_radius=.5, height = height, width = width).set_stroke(opacity=1)
        measure_box = RoundedRectangle(color = detail_color, corner_radius=.5, height = height, width = width)
        learn_box = RoundedRectangle(color = detail_color, corner_radius=.5, height = height, width = width)

        bm_arrow = Arrow(color=detail_color, stroke_width=100, tip_length=10, start= [-9.6, -3.3, 0], end= [-3, 3.3, 0])
        ml_arrow = Arrow(color=detail_color, stroke_width=100, tip_length=10, start= [3, 3.3, 0], end= [9.6, -3.3, 0])
        lb_arrow = Arrow(color=detail_color, stroke_width=70, tip_length=7, start= [6.6, -10, 0], end= [-6.6, -10, 0])

        # Sets the scene up for zoomin' fun
        self.camera.frame.scale(4.25)

        nudge = .25

        build_box.move_to([-20,-10,0])
        measure_box.move_to([0, 10, 0])
        learn_box.move_to([20, -10, 0])

        # build_back = Rectangle(color=background_color, fill_opacity=1).move_to([build_box.get_left()[0] +(width/2), build_box.get_top()[1],0])
        # build_back.stroke_color = background_color

    
        build_text = Text("Build", font="Space Grotesk", font_size=120, weight="BOLD", color=detail_color).move_to(build_box.get_center())#.move_to([build_box.get_left()[0]+(width/2), build_box.get_top()[1],0])
        measure_text = Text("Measure", font="Space Grotesk", font_size=120, weight="BOLD", color=detail_color).move_to(measure_box.get_center())#.move_to([build_box.get_left()[0]+(width/2), build_box.get_top()[1],0])
        learn_text = Text("Learn", font="Space Grotesk", font_size=120, weight="BOLD", color=detail_color).move_to(learn_box.get_center())#.move_to([build_box.get_left()[0]+(width/2), build_box.get_top()[1],0])
        
        # Not crazy about having rectangle then putting something over it
        # self.play(FadeIn(build_back), Write(build_box), Write(measure_box), Write(learn_box), duration=.1)
        self.play(
            # Write(build_partial_box),
                #    Write(build_back), 
                   Write(build_box), Write(measure_box), Write(learn_box), 
                   Write(build_text), Write(measure_text), Write(learn_text), 
                   Write(bm_arrow), Write(ml_arrow), Write(lb_arrow),
                   duration=.1) 
        # self.add(fill_background)

        self.play(FadeIn(VGroup(line_side).arrange(DOWN, buff=.5)), FadeIn(VGroup(line_up).arrange(RIGHT, buff=.5)), duration=.2)
        # self.add(Text("Build", font="Space Grotesk", weight="BOLD", color=detail_color).move_to([build_box.get_left()[0]+(width/2), build_box.get_top()[1],0]))
        self.camera.frame.save_state()
        # build_text.generate_target()
        # build_text.target.scale(0.25)
        # build_text.target.shift(build_box.get_center())
        center_to_top = Line(build_text.get_center(), build_box.get_top())
        # self.add(build_text.move_to([build_box.get_left()[0]+(width/2), build_box.get_top()[1], 0]))
        smidge_below_top = build_box.get_top()
        smidge_below_top[1] -= 0.5
        self.play(
                self.camera.frame.animate.set(width=build_box.width*.95).move_to(build_box.get_center()),
                # MoveAlongPath(build_text, center_to_top),
                build_text.animate.move_to(smidge_below_top).scale(0.5),
                #   FadeIn(build_back),
                FadeOut(build_box)
                  )
        self.wait()

        # Inside build stuff
        # hello = Text("hello", color=detail_color).move_to([build_box.get_left()[0]*.8, build_box.get_center()[1], 0])
        # # .8 -> .75 because too close to the edge
        # world = Text("world", color=detail_color).move_to([build_box.get_right()[0]*(1/.75), build_box.get_center()[1], 0])
        # # .8 -> .6/.55 because spacing of words
        # from_to = Arrow([build_box.get_left()[0]*.6, build_box.get_center()[0], 0], [build_box.get_right()[0]*(1/.55), build_box.get_center()[0], 0], color=detail_color)
        # self.play(Write(hello))
        # self.play(Write(world))
        # self.play(Write(from_to))
        # self.play(Restore(self.camera.frame))
        # self.wait()
        # self.play(FadeOut(hello), FadeOut(world), FadeOut(from_to))
# Rough iteration
# uv run manim -pql ./main.py Animation
# Production finish and check
# uv run manim -pqk --fps=1000 ./main.py Animation
# https://docs.devtaoism.com/docs/html/contents/_3_camera_options.html
