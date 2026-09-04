'''
██████╗ ███████╗ █████╗ ██████╗     ███╗   ███╗███████╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗    ████╗ ████║██╔════╝
██████╔╝█████╗  ███████║██║  ██║    ██╔████╔██║█████╗  
██╔══██╗██╔══╝  ██╔══██║██║  ██║    ██║╚██╔╝██║██╔══╝  
██║  ██║███████╗██║  ██║██████╔╝    ██║ ╚═╝ ██║███████╗
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝     ╚═╝     ╚═╝╚══════╝
Good Day, sir. This is Samanthak(26BEC7166) from B2 Slot.
This code cannot be run just by executing the python file, it needs to be executed using the manim library.
It requires the Manim library and numpy package to be installed.
To download the output video directly, please proceed to the google drive link below:
https://drive.google.com/drive/folders/1nsIezsMjlbo1fTuzth0xJkqWWYEWRSZH?usp=sharing
'''
from manim import *
import numpy as np

# ------------------------------------------------------------------------------
# GLOBAL CONFIGURATION
# ------------------------------------------------------------------------------
config.background_color = "#050510"


class Module2FullPresentation(Scene):
    def construct(self):
        # Master timeline running each scene sequentially
        self.play_scene_1_hook()
        self.play_scene_2_intro()
        self.play_act_3a_floating_point()
        self.play_act_3b_identity_vs_equality()
        self.play_act_3c_short_circuit()
        self.play_act_3d_precedence()
        self.play_act_3f_string_multiplication()
        self.play_act_3e_chained_comparison()
        self.play_act_3g_ternary_operator() 
        self.play_scene_4_branching() 
        self.play_scene_5_sinker()
        self.play_scene_6_outro()

    # --------------------------------------------------------------------------
    # SCENE 1: THE HOOK (0:00 - 0:15)
    # --------------------------------------------------------------------------
    def play_scene_1_hook(self):
        self.camera.background_color = "#050510"

        # 1. Terminal Error Elements
        error_title = Text("FATAL SYNTAX ERRORS", font_size=52, color=RED, weight=BOLD)
        error_code = Text(">>> SyntaxError: unexpected token at line 1", font_size=22, color=GRAY)
        
        error_box = SurroundingRectangle(error_title, color=RED, buff=0.3, corner_radius=0.1)
        error_group = VGroup(error_box, error_title, error_code)
        
        error_title.move_to(error_box.get_center())
        error_code.next_to(error_box, DOWN, buff=0.3)

        # 2. Sudden Glitch Pop-In
        self.play(
            Create(error_box, run_time=0.3),
            FadeIn(error_title, scale=1.2, run_time=0.3),
            Flash(ORIGIN, color=RED, num_lines=24, flash_radius=1.5, time_width=0.2)
        )
        self.play(Write(error_code), run_time=0.5)

        # 3. Erratic Shaking / Glitch Pulse
        self.play(
            Wiggle(error_group, scale_value=1.1, rotation_angle=0.04),
            run_time=1.2
        )

        # 4. Shockwave Burst & Shrink Out
        self.play(
            Flash(ORIGIN, color=RED, line_length=2.0, num_lines=32, flash_radius=1.8),
            ShrinkToCenter(error_group),
            run_time=0.5
        )
        self.wait(0.5)



    # --------------------------------------------------------------------------
    # SCENE 2: THE INTRO (0:15 - 0:28)
    # --------------------------------------------------------------------------
    def play_scene_2_intro(self):
        # 1. Deep Space Background Stars
        stars = VGroup(*[
            Dot(
                point=np.array([
                    np.random.uniform(-7, 7), 
                    np.random.uniform(-4, 4), 
                    0
                ]), 
                radius=np.random.uniform(0.01, 0.03), 
                color=WHITE, 
                fill_opacity=np.random.uniform(0.2, 0.8)
            ) for _ in range(150)
        ])
        self.add(stars)

        # 2. Text Elements Setup
        module_text = Text("MODULE 2: OPERATORS & BRANCHING", color=WHITE, weight=BOLD)
        module_text.scale(0.8)
        module_text.shift(UP * 0.8)

        course_text = Text("CSE1012: Problem Solving using Python", color=YELLOW)
        course_text.scale(0.6)
        course_text.next_to(module_text, DOWN, buff=0.35)

        instructor_text = Text("Course Instructor: Praveen Tiwari Sir", color=LIGHT_GRAY)
        instructor_text.scale(0.48)
        instructor_text.next_to(course_text, DOWN, buff=0.25)

        # 3. Rigid, Low-Poly Geometric Underline
        zigzag_points = [
            [-5.0, -1.8, 0],
            [-3.5, -2.4, 0],
            [-2.0, -1.7, 0],
            [-0.5, -2.6, 0],
            [ 1.0, -1.8, 0],
            [ 2.5, -2.5, 0],
            [ 4.0, -1.9, 0],
            [ 5.0, -2.3, 0]
        ]
        
        zigzag_line = VMobject().set_points_as_corners(zigzag_points)
        zigzag_line.set_color([BLUE_C, TEAL_C])
        zigzag_line.set_stroke(width=4)

        # 4. Animation Sequence
        self.wait(0.5)
        self.play(FadeIn(module_text, shift=UP * 0.2), run_time=1.2)
        self.play(FadeIn(course_text, shift=UP * 0.2), run_time=1.2)
        self.play(FadeIn(instructor_text, shift=UP * 0.2), run_time=1.2)
        self.play(Create(zigzag_line), run_time=2.2)
        self.wait(2)

        # 5. Clean up Scene 2 elements before Scene 3
        self.play(
            FadeOut(module_text),
            FadeOut(course_text),
            FadeOut(instructor_text),
            FadeOut(zigzag_line),
            FadeOut(stars),
            run_time=0.8
        )
        
        pass

    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    # ACT 3A: FLOATING POINT BETRAYAL (0:28 - 0:45)
    # --------------------------------------------------------------------------
    def play_act_3a_floating_point(self):
        header = Text("TRAP 1: Floating-Point Math", font_size=32, color=YELLOW).to_edge(UP)
        self.play(FadeIn(header, shift=DOWN))

        # 1. Main Equation Expression
        expr = Text("0.1 + 0.2 == 0.3", font_size=42, color=WHITE).shift(UP * 1.2)
        self.play(Write(expr))
        self.wait(0.5)

        # 2. Fake Answer (Green True?) -> Glitch to Red FALSE!
        fake_ans = Text("True?", font_size=38, color=GREEN).next_to(expr, DOWN, buff=0.4)
        self.play(FadeIn(fake_ans, shift=UP * 0.2))
        self.wait(0.5)

        real_ans = Text("FALSE! ❌", font_size=46, color=RED, weight=BOLD).next_to(expr, DOWN, buff=0.4)
        self.play(
            Transform(fake_ans, real_ans),
            Flash(real_ans, color=RED, line_length=0.4, num_lines=16),
            Wiggle(expr)
        )
        self.wait(0.5)

        # 3. Precision Error Breakdown
        actual_val = Text("0.1 + 0.2 = 0.30000000000000004", font_size=28, color=YELLOW)
        actual_val.next_to(fake_ans, DOWN, buff=0.5)
        self.play(Write(actual_val))
        self.play(Indicate(actual_val, color=YELLOW, scale_factor=1.1))
        self.wait(1)

        # 4. Division Comparison
        div_norm = Text("7 / 2  = 3.5  (Float Division)", font_size=26, color=TEAL)
        div_floor = Text("7 // 2 = 3    (Floor Division)", font_size=26, color=TEAL)
        div_group = VGroup(div_norm, div_floor).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        div_group.next_to(actual_val, DOWN, buff=0.5)

        self.play(FadeIn(div_group, shift=UP * 0.2))
        self.wait(2)

        # Cleanup Act 3A
        self.play(
            FadeOut(header), FadeOut(expr), FadeOut(fake_ans), 
            FadeOut(actual_val), FadeOut(div_group),
            run_time=0.8
        )

    # --------------------------------------------------------------------------
    # ACT 3B: CLONES VS IDENTICAL TWINS (0:45 - 1:05)
    # --------------------------------------------------------------------------
    def play_act_3b_identity_vs_equality(self):
        header = Text("TRAP 2: Equality (==) vs Identity (is)", font_size=32, color=YELLOW).to_edge(UP)
        self.play(FadeIn(header, shift=DOWN))

        # 1. Variable Assignments
        code_a = Text("a = [1, 2]", font_size=32, color=WHITE)
        code_b = Text("b = [1, 2]", font_size=32, color=WHITE)
        code_group = VGroup(code_a, code_b).arrange(RIGHT, buff=1.8).shift(UP * 1.5)
        self.play(Write(code_group))

        # 2. Visual Memory Boxes
        box_a = Rectangle(height=1.2, width=2.2, color=BLUE).next_to(code_a, DOWN, buff=0.6)
        box_b = Rectangle(height=1.2, width=2.2, color=BLUE).next_to(code_b, DOWN, buff=0.6)
        
        val_a = Text("[1, 2]", font_size=24, color=WHITE).move_to(box_a)
        val_b = Text("[1, 2]", font_size=24, color=WHITE).move_to(box_b)

        # Memory Tags
        mem_a = Text("0x7f...1", font_size=18, color=GRAY).next_to(box_a, UP, buff=0.1)
        mem_b = Text("0x7f...2", font_size=18, color=GRAY).next_to(box_b, UP, buff=0.1)

        self.play(
            GrowFromCenter(box_a), GrowFromCenter(box_b),
            FadeIn(val_a), FadeIn(val_b),
            FadeIn(mem_a), FadeIn(mem_b)
        )
        self.wait(0.5)

        # 3. Equality Test (Value Match)
        eq_test = Text("a == b  ➔  TRUE  (Value Match)", font_size=28, color=GREEN)
        eq_test.shift(DOWN * 0.8)
        self.play(Write(eq_test))
        self.play(Indicate(VGroup(val_a, val_b), color=GREEN))
        self.wait(1)

        # 4. Identity Test (Memory Mismatch)
        id_test = Text("a is b  ➔  FALSE! ❌ (Memory Mismatch)", font_size=28, color=RED)
        id_test.next_to(eq_test, DOWN, buff=0.4)
        self.play(Write(id_test))
        self.play(
            Indicate(VGroup(mem_a, mem_b), color=RED),
            Flash(id_test, color=RED, num_lines=12, time_width=0.2)
        )
        self.wait(2)

        # Cleanup Act 3B
        self.play(
            FadeOut(header), FadeOut(code_group), FadeOut(box_a), FadeOut(box_b),
            FadeOut(val_a), FadeOut(val_b), FadeOut(mem_a), FadeOut(mem_b),
            FadeOut(eq_test), FadeOut(id_test),
            run_time=0.8
        )

    # --------------------------------------------------------------------------
    # ACT 3C: SHORT-CIRCUITING SPEED HACK (1:05 - 1:25)
    # --------------------------------------------------------------------------
    def play_act_3c_short_circuit(self):
        header = Text("TRAP 3: Membership & Short-Circuiting", font_size=32, color=YELLOW).to_edge(UP)
        self.play(FadeIn(header, shift=DOWN))

        # 1. Membership Operator Quick Check
        mem_code = Text("'free_food' in campus_event", font_size=30, color=WHITE).shift(UP * 1.5)
        mem_res = Text("➔  TRUE", font_size=30, color=GREEN, weight=BOLD).next_to(mem_code, RIGHT, buff=0.4)
        self.play(Write(mem_code))
        self.play(FadeIn(mem_res, shift=LEFT))
        self.wait(1.2)

        # 2. Short-Circuit Expression Setup
        expr_part1 = Text("True", font_size=36, color=GREEN)
        expr_or = Text(" or ", font_size=36, color=WHITE)
        expr_part2 = Text("any_other_statement()", font_size=36, color=YELLOW)
        
        sc_expr = VGroup(expr_part1, expr_or, expr_part2).arrange(RIGHT).shift(DOWN * 0.2)
        self.play(FadeOut(mem_code), FadeOut(mem_res))
        self.play(Write(sc_expr))
        self.wait(0.5)

        # 3. Laser Sweep & Strike-through Animation
        slash = Line(
            start=expr_part2.get_corner(DL) + LEFT * 0.1,
            end=expr_part2.get_corner(UR) + RIGHT * 0.1,
            color=RED,
            stroke_width=6
        )
        skipped_text = Text("SKIPPED!", font_size=28, color=RED, weight=BOLD).next_to(expr_part2, DOWN, buff=0.3)

        laser_beam = Line(
            start=sc_expr.get_corner(UL) + UP * 0.2,
            end=sc_expr.get_corner(DL) + DOWN * 0.2,
            color=TEAL,
            stroke_width=4
        )

        self.play(ShowPassingFlash(laser_beam, time_width=0.3, run_time=0.6))
        self.play(
            expr_part2.animate.set_color(GRAY),
            Create(slash),
            FadeIn(skipped_text, scale=1.2),
            Flash(skipped_text, color=RED, num_lines=12)
        )
        self.wait(2)

        # Cleanup Act 3C
        self.play(
            FadeOut(header), FadeOut(sc_expr), FadeOut(slash), FadeOut(skipped_text),
            run_time=0.8
        )

    # --------------------------------------------------------------------------
    # ACT 3D: UNARY MINUS VS EXPONENTIATION (0:28 - 0:45 region)
    # --------------------------------------------------------------------------
    def play_act_3d_precedence(self):
        header = Text("TRAP 4: Precedence (-3 ** 2)", font_size=32, color=YELLOW).to_edge(UP)
        self.play(FadeIn(header, shift=DOWN))

        # 1. Main Expression
        expr = Text("-3 ** 2 == 9", font_size=42, color=WHITE).shift(UP * 1.2)
        self.play(Write(expr))
        self.wait(0.5)

        # 2. Fake Answer -> Glitch to Red FALSE!
        fake_ans = Text("True?", font_size=38, color=GREEN).next_to(expr, DOWN, buff=0.4)
        self.play(FadeIn(fake_ans, shift=UP * 0.2))
        self.wait(0.5)

        real_ans = Text("FALSE! ❌", font_size=46, color=RED, weight=BOLD).next_to(expr, DOWN, buff=0.4)
        self.play(
            Transform(fake_ans, real_ans),
            Flash(real_ans, color=RED, line_length=0.4, num_lines=16),
            Wiggle(expr)
        )
        self.wait(0.5)

        # 3. Explicit Parentheses Breakdown
        expl_text = Text("-(3 ** 2) = -9", font_size=32, color=YELLOW).next_to(fake_ans, DOWN, buff=0.5)
        note_text = Text("** binds tighter than unary -", font_size=24, color=TEAL).next_to(expl_text, DOWN, buff=0.3)
        
        self.play(Write(expl_text))
        self.play(FadeIn(note_text, shift=UP * 0.2))
        self.play(Indicate(expl_text, color=YELLOW))
        self.wait(2)

        # Cleanup Act 3D
        self.play(
            FadeOut(header), FadeOut(expr), FadeOut(fake_ans), 
            FadeOut(expl_text), FadeOut(note_text),
            run_time=0.8
        )

    # --------------------------------------------------------------------------
    # ACT 3E: CHAINED COMPARISONS
    # --------------------------------------------------------------------------
    def play_act_3e_chained_comparison(self):
        header = Text("PRO TIP: Chained Comparisons", font_size=32, color=YELLOW).to_edge(UP)
        self.play(FadeIn(header, shift=DOWN))

        # 1. Verbose Comparison Expression
        verbose_code = Text("1 < x and x < 10", font_size=38, color=WHITE).shift(UP * 0.5)
        self.play(Write(verbose_code))
        self.wait(1)

        # 2. Morph into Pythonic Chained Comparison
        chained_code = Text("1 < x < 10", font_size=46, color=GREEN, weight=BOLD).shift(UP * 0.5)
        box = SurroundingRectangle(chained_code, color=GREEN, buff=0.25, corner_radius=0.1)

        self.play(
            Transform(verbose_code, chained_code),
            Create(box),
            run_time=1.2
        )
        self.play(Flash(chained_code, color=GREEN, line_length=0.4, num_lines=16))

        # 3. Informational Subtext
        subtext = Text("Clean, readable, & math-like syntax!", font_size=26, color=TEAL).next_to(box, DOWN, buff=0.5)
        self.play(Write(subtext))
        self.wait(2)

        # Cleanup Act 3E
        self.play(
            FadeOut(header), FadeOut(verbose_code), FadeOut(box), FadeOut(subtext),
            run_time=0.8
        )

    # --------------------------------------------------------------------------
    # ACT 3F: STRING MULTIPLICATION TRAP
    # --------------------------------------------------------------------------
    def play_act_3f_string_multiplication(self):
        header = Text("TRAP 5: String Multiplication ('5' * 3)", font_size=32, color=YELLOW).to_edge(UP)
        self.play(FadeIn(header, shift=DOWN))

        # 1. Main Expression
        expr = Text("'5' * 3 == 15", font_size=42, color=WHITE).shift(UP * 1.2)
        self.play(Write(expr))
        self.wait(0.5)

        # 2. Fake Answer -> Glitch to Red FALSE!
        fake_ans = Text("True?", font_size=38, color=GREEN).next_to(expr, DOWN, buff=0.4)
        self.play(FadeIn(fake_ans, shift=UP * 0.2))
        self.wait(0.5)

        real_ans = Text("FALSE! ❌", font_size=46, color=RED, weight=BOLD).next_to(expr, DOWN, buff=0.4)
        self.play(
            Transform(fake_ans, real_ans),
            Flash(real_ans, color=RED, line_length=0.4, num_lines=16),
            Wiggle(expr)
        )
        self.wait(0.5)

        # 3. String Repetition Result
        res_text = Text("'5' * 3 = '555'", font_size=36, color=TEAL, weight=BOLD).next_to(fake_ans, DOWN, buff=0.5)
        note_text = Text("Multiplying a string repeats it sequence-wise!", font_size=24, color=YELLOW).next_to(res_text, DOWN, buff=0.3)

        self.play(Write(res_text))
        self.play(FadeIn(note_text, shift=UP * 0.2))
        self.play(Indicate(res_text, color=TEAL))
        self.wait(2)

        # Cleanup Act 3F
        self.play(
            FadeOut(header), FadeOut(expr), FadeOut(fake_ans), 
            FadeOut(res_text), FadeOut(note_text),
            run_time=0.8
        )

    # --------------------------------------------------------------------------
    # ACT 3G: TERNARY OPERATOR (INLINE CONDITIONAL)
    # --------------------------------------------------------------------------
    def play_act_3g_ternary_operator(self):
        header = Text("PRO TIP: Ternary Operator (Inline Conditional)", font_size=32, color=YELLOW).to_edge(UP)
        self.play(FadeIn(header, shift=DOWN))

        # 1. Multi-line traditional if-else block
        # Using LIGHT_GRAY instead of GRAY to ensure strict Pylance/Manim color compatibility
        line1 = Text("if x > 0:", font_size=28, color=LIGHT_GRAY)
        line2 = Text("    y = 1", font_size=28, color=LIGHT_GRAY)
        line3 = Text("else:", font_size=28, color=LIGHT_GRAY)
        line4 = Text("    y = 0", font_size=28, color=LIGHT_GRAY)
        
        block = VGroup(line1, line2, line3, line4).arrange(DOWN, aligned_edge=LEFT, buff=0.15).shift(UP * 0.8)
        self.play(Write(block))
        self.wait(1)

        # 2. Collapse into single-line ternary
        ternary_text = Text("y = 1 if x > 0 else 0", font_size=36, color=YELLOW, weight=BOLD).shift(DOWN * 0.5)
        box = SurroundingRectangle(ternary_text, color=YELLOW, buff=0.25, corner_radius=0.1)

        self.play(
            ReplacementTransform(block, ternary_text),
            Create(box),
            run_time=1.2
        )
        self.play(Flash(ternary_text, color=YELLOW, line_length=0.4, num_lines=16))

        # 3. Syntax Breakdown Subtext
        subtext = Text("value_if_true  if  condition  else  value_if_false", font_size=22, color=TEAL)
        subtext.next_to(box, DOWN, buff=0.4)
        self.play(FadeIn(subtext, shift=UP * 0.2))
        self.wait(2)

        # Cleanup Act 3G
        self.play(
            FadeOut(header), FadeOut(ternary_text), FadeOut(box), FadeOut(subtext),
            run_time=0.8
        )

    # --------------------------------------------------------------------------
    # SCENE 4: BRANCHING MAZE (Shifted & Scaled to fit within frame)
    # --------------------------------------------------------------------------
    def play_scene_4_branching(self):
        header = Text("Control Flow & Branching", font_size=32, color=YELLOW).to_edge(UP)
        self.play(FadeIn(header, shift=DOWN))

        # 1. Input Variable Setup (Shifted further left and slightly smaller)
        var_text = Text("level = 65", font_size=26, color=TEAL, weight=BOLD).shift(UP * 2.2 + LEFT * 4.2)
        self.play(Write(var_text))

        # 2. Decision Flowchart Nodes (Shifted left to LEFT * 0.6, width reduced to 3.6)
        if_box = RoundedRectangle(height=0.75, width=3.6, corner_radius=0.15, color=BLUE)
        if_text = Text("if level > 80:", font_size=20, color=WHITE).move_to(if_box)
        if_node = VGroup(if_box, if_text).shift(UP * 1.0 + LEFT * 0.6)

        elif_box = RoundedRectangle(height=0.75, width=3.6, corner_radius=0.15, color=BLUE)
        elif_text = Text("elif level > 50:", font_size=20, color=WHITE).move_to(elif_box)
        elif_node = VGroup(elif_box, elif_text).shift(DOWN * 0.5 + LEFT * 0.6)

        else_box = RoundedRectangle(height=0.75, width=3.6, corner_radius=0.15, color=LIGHT_GRAY)
        else_text = Text("else:", font_size=20, color=LIGHT_GRAY).move_to(else_box)
        else_node = VGroup(else_box, else_text).shift(DOWN * 2.0 + LEFT * 0.6)

        self.play(
            Create(if_node),
            Create(elif_node),
            Create(else_node)
        )

        # Connecting Flow Lines (Shortened branch extension)
        path_start = Line(var_text.get_bottom(), if_box.get_left(), color=WHITE)
        path_if_to_elif = Line(if_box.get_bottom(), elif_box.get_top(), color=WHITE)
        path_branch = Line(elif_box.get_right(), elif_box.get_right() + RIGHT * 0.8, color=GREEN)

        self.play(
            Create(path_start),
            Create(path_if_to_elif),
            Create(path_branch)
        )

        # 3. Glowing Data Packet (Glowing Dot)
        core_dot = Dot(color=YELLOW, radius=0.08)
        glow_dot = Dot(color=YELLOW, radius=0.2, fill_opacity=0.35)
        packet = VGroup(glow_dot, core_dot).move_to(var_text.get_bottom())

        self.play(FadeIn(packet))
        
        # Move Packet to IF Block
        self.play(packet.animate.move_to(if_box.get_left()), run_time=0.8)

        # IF Evaluation: FALSE!
        cross = Cross(if_box, scale_factor=0.5, stroke_width=5, color=RED)
        false_label = Text("FALSE ❌", font_size=18, color=RED, weight=BOLD).next_to(if_box, RIGHT, buff=0.15)
        
        self.play(
            Create(cross),
            FadeIn(false_label, shift=LEFT),
            Flash(if_box, color=RED, num_lines=12)
        )
        self.wait(0.4)

        # Route Packet Down to ELIF Block
        self.play(
            packet.animate.move_to(elif_box.get_top()),
            run_time=0.8
        )

        # ELIF Evaluation: TRUE!
        true_label = Text("TRUE ✔", font_size=18, color=GREEN, weight=BOLD).next_to(elif_box, DOWN, buff=0.12)

        self.play(
            elif_box.animate.set_color(GREEN),
            FadeIn(true_label, shift=UP),
            Flash(elif_box, color=GREEN, num_lines=12)
        )
        self.wait(0.4)

        # Move Packet along Active Branch
        self.play(
            packet.animate.move_to(elif_box.get_right() + RIGHT * 0.8),
            run_time=0.8
        )

        # 4. Final Output Display (Sized down to stay within frame)
        res_text = Text("Access Granted:", font_size=18, color=GREEN, weight=BOLD)
        res_box = SurroundingRectangle(res_text, color=GREEN, buff=0.15, corner_radius=0.1)
        res_group = VGroup(res_box, res_text).next_to(path_branch, RIGHT, buff=0.15)

        self.play(
            ReplacementTransform(packet, res_group),
            run_time=0.6
        )
        self.play(Flash(res_group, color=GREEN, num_lines=16))
        self.wait(2)

        # Cleanup Scene 4
        self.play(
            FadeOut(header), FadeOut(var_text), FadeOut(if_node), FadeOut(elif_node),
            FadeOut(else_node), FadeOut(path_start), FadeOut(path_if_to_elif),
            FadeOut(path_branch), FadeOut(cross), FadeOut(false_label),
            FadeOut(true_label), FadeOut(res_group),
            run_time=0.8
        )

    # --------------------------------------------------------------------------
    # SCENE 5: THE SINKER (1:50 - 2:05)
    # --------------------------------------------------------------------------
    def play_scene_5_sinker(self):
        # 1. Text Setup
        line1 = Text("Code isn't just syntax...", font_size=36, color=WHITE)
        line2 = Text("It's a way to turn our imagination into reality", font_size=34, color=YELLOW, weight=BOLD)
        
        quote_group = VGroup(line1, line2).arrange(DOWN, buff=0.6).move_to(ORIGIN)

        # 2. Vector Outline Writing Animation
        self.play(Write(line1), run_time=2.0)
        self.wait(0.5)

        self.play(Write(line2), run_time=2.5)
        self.play(
            Indicate(line2, color=YELLOW, scale_factor=1.05),
            Flash(line2.get_center(), color=YELLOW, line_length=0.5, num_lines=20),
            run_time=1.2
        )
        self.wait(2.5)

        # 3. Clean up Scene 5 before Outro
        self.play(
            FadeOut(quote_group),
            run_time=0.8
        )

    # --------------------------------------------------------------------------
    # SCENE 6: OUTRO (2:05 - 2:15)
    # --------------------------------------------------------------------------
    def play_scene_6_outro(self):
        # 1. Credits & Social Links Setup
        author_text = Text("Created by Samanthak Prajwal Vuddanti", font_size=28, color=WHITE, weight=BOLD)
        course_text = Text("CSE1012-> Module 2: Operatos and Branches", font_size=20, color=YELLOW)
        
        insta_text = Text("My instagram: @samanthakprajwal", font_size=18, color=TEAL)
        yt_text = Text("3Blue1Brown: youtube.com/3Blue1Brown (Creator of Manim)", font_size=18, color=LIGHT_GRAY)
        
        tech_text = Text("Made using the Manim Python Library", font_size=15, color=GRAY)

        credits_group = VGroup(
            author_text,
            course_text,
            insta_text,
            yt_text,
            tech_text
        ).arrange(DOWN, buff=0.28).shift(UP * 0.3)

        # 2. Native Geometric Badge / Logo
        outer_circle = Circle(radius=0.55, color=TEAL, stroke_width=3)
        inner_square = Square(side_length=0.6, color=BLUE).rotate(PI / 4)
        center_dot = Dot(color=YELLOW, radius=0.09)
        
        logo_badge = VGroup(outer_circle, inner_square, center_dot).next_to(credits_group, DOWN, buff=0.35)

        # 3. Animation Sequence
        self.play(FadeIn(author_text, shift=UP * 0.2), run_time=0.8)
        self.play(FadeIn(course_text, shift=UP * 0.2), run_time=0.6)
        
        # Fade in Instagram & YouTube credits
        self.play(
            FadeIn(insta_text, shift=RIGHT * 0.2),
            FadeIn(yt_text, shift=LEFT * 0.2),
            run_time=0.8
        )
        self.play(FadeIn(tech_text, shift=UP * 0.2), run_time=0.6)

        # Animate vector badge
        self.play(
            Create(outer_circle),
            SpinInFromNothing(inner_square),
            GrowFromCenter(center_dot),
            run_time=1.0
        )
        self.play(Flash(logo_badge, color=TEAL, num_lines=16, flash_radius=0.8))
        self.wait(2.5)

        # 4. Final Scene Fade Out
        self.play(
            FadeOut(credits_group),
            FadeOut(logo_badge),
            run_time=1.2
        )
        self.wait(0.5)
