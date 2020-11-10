from manimlib.imports import *

class intro(Scene):
    def construct(self):
        intro = TexMobject("2020",
                           "^{2021}"
                           )
        intro[0].set_color(YELLOW)
        intro[1].set_color(GREEN)
        intro.scale(2)
        intro.move_to(UP + 3*LEFT)
        
        intro1 = TexMobject("2021",
                            "^{2020}"
                            )
        intro1[0].set_color(GREEN)
        intro1[1].set_color(YELLOW)
        intro1.move_to(UP + 3*RIGHT)
        intro1.scale(2)

        intro2 = TextMobject("or")
        intro2.scale(1.5)
        intro2.move_to(0.7*UP)

        bigger = TextMobject("Which is bigger?")
        bigger.scale(1.5)
        bigger.move_to(1.5*DOWN)

        first = TexMobject("\\text{First, take a look at the graph} \\",
                           "f(x) = x^{\\frac{1}{x}}"
                           )
        first.to_edge(UP)
        first.scale(0.7)

        first1 = TexMobject("\\text{First, take a look at the graph} \\",
                           "f(x) = x^{\\frac{1}{x}}"
                           )
        first1.next_to(first, 2*UP)
        first1.scale(0.7)

        notice = TexMobject("f(x) \\",
                            "\\text{is} \\",
                            "\\text{decreasing}",
                            "\\ \\text{for} \\",
                            "x > e"
                            )
        notice.to_edge(UP)
        notice[2].set_color(RED)
        notice.scale(0.7)

        this = TextMobject("(this can easily be proven using calculus)")
        this.scale(0.5)
        this.next_to(notice, 0.5*DOWN)

        set1 = TexMobject("f(3)")
        set1.move_to(1.5*UP)
        set1.scale(1)
        
        set2 = TexMobject("f(3)",
                          "> f(4)"
                          )
        set2.move_to(1.5*UP)
        set2.scale(1)
        
        set3 = TexMobject("f(3)",
                          "> f(4)",
                          "> f(5)"
                          )
        set3.move_to(1.5*UP)
        set3.scale(1)
        
        set4 = TexMobject("f(3)",
                          "> f(4)",
                          "> f(5)",
                          ">",
                          "\\cdots",
                          ">",
                          "f(",
                          "2020",
                          ")"
                          )
        set4.move_to(1.5*UP)
        set4.scale(1)

        set5 = TexMobject("f(3)",
                          "> f(4)",
                          "> f(5)",
                          ">",
                          "\\cdots",
                          ">",
                          "f(",
                          "2020",
                          ")",
                          ">",
                          "f(",
                          "2021",
                          ")",
                          ">",
                          "\\cdots"
                          )
        set5.move_to(1.5*UP)
        set5.scale(1)

        last1 = TexMobject("f(",
                           "2020",
                           ")",
                           ">",
                           "f(",
                           "2021",
                           ")"
                           )
        last1.scale(1.5)
        last1[0].set_color(YELLOW)
        last1[1].set_color(YELLOW)
        last1[2].set_color(YELLOW)
        last1[4].set_color(GREEN)
        last1[5].set_color(GREEN)
        last1[6].set_color(GREEN)

        last2 = TexMobject("{2020",
                           "^{1 \\over",
                           "2020}}",
                           ">",
                           "{2021",
                           "^{1 \\over",
                           "2021}}"
                           )
        last2[0].set_color(YELLOW)
        last2[2].set_color(YELLOW)
        last2[4].set_color(GREEN)
        last2[6].set_color(GREEN)
        last2.scale(1.5)

        last3 = TexMobject("\\left(",
                           "{2020",
                           "^{1 \\over",
                           "2020}}",
                           "\\right)",
                           "^{",
                           "2020",
                           "\\cdot",
                           "2021}",
                           ">",
                           "\\left(",
                           "{2021",
                           "^{1 \\over",
                           "2021}}",
                           "\\right)",
                           "^{",
                           "2020",
                           "\\cdot",
                           "2021}"
                           )
        last3[1].set_color(YELLOW)
        last3[3].set_color(YELLOW)
        last3[6].set_color(YELLOW)
        last3[8].set_color(GREEN)
        last3[11].set_color(GREEN)
        last3[13].set_color(GREEN)
        last3[16].set_color(YELLOW)
        last3[18].set_color(GREEN)
        last3.scale(1.5)

        last4 = TexMobject("2020",
                           "^{2021}",
                           ">",
                           "2021",
                           "^{2020}"
                           )
        last4[0].set_color(YELLOW)
        last4[1].set_color(GREEN)
        last4[3].set_color(GREEN)
        last4[4].set_color(YELLOW)
        last4.scale(1.5)

        qed = TextMobject("Q.E.D")
        qed.next_to(last4, 3*DOWN)
        qed.scale(1)
                           
                        
        self.wait()
        self.play(Write(intro),
                  Write(intro1),
                  Write(intro2),
                  Write(bigger),
                  run_time = 3
                  )
        self.wait(3)
        self.play(Uncreate(intro),
                  Uncreate(intro1),
                  Uncreate(intro2),
                  Uncreate(bigger),
                  run_time = 2
                  )
        self.wait(2)
        self.wait(4)
        self.play(FadeInFromDown(first),
                  run_time=2
                  )
        self.wait(6)
        self.play(ReplacementTransform(first, first1), FadeIn(notice), FadeIn(this), run_time = 2)
        self.wait(11)
        self.play(Write(set1))
        self.wait(2)
        self.play(ReplacementTransform(set1, set2[0]), FadeIn(set2[1]))
        self.wait(2)
        self.play(ReplacementTransform(set2[0], set3[0]),
                  ReplacementTransform(set2[1], set3[1]),
                  FadeIn(set3[2])
                  )
        self.wait(2)
        self.play(ReplacementTransform(set3[0], set4[0]),
                  ReplacementTransform(set3[1], set4[1]),
                  ReplacementTransform(set3[2], set4[2]),
                  FadeIn(set4[3]),
                  FadeIn(set4[4]),
                  FadeIn(set4[5]),
                  FadeIn(set4[6]),
                  FadeIn(set4[7]),
                  FadeIn(set4[8])
                  )
        self.wait(2)
        self.play(ReplacementTransform(set4[0], set5[0]),
                  ReplacementTransform(set4[1], set5[1]),
                  ReplacementTransform(set4[2], set5[2]),
                  ReplacementTransform(set4[3], set5[3]),
                  ReplacementTransform(set4[4], set5[4]),
                  ReplacementTransform(set4[5], set5[5]),
                  ReplacementTransform(set4[6], set5[6]),
                  ReplacementTransform(set4[7], set5[7]),
                  ReplacementTransform(set4[8], set5[8]),
                  FadeIn(set5[9]),
                  FadeIn(set5[10]),
                  FadeIn(set5[11]),
                  FadeIn(set5[12]),
                  FadeIn(set5[13]),
                  FadeIn(set5[14])
                  )
        self.wait(2)
        self.play(set5[6].set_color, YELLOW,
                  set5[7].set_color, YELLOW,
                  set5[8].set_color, YELLOW,
                  set5[10].set_color, GREEN,
                  set5[11].set_color, GREEN,
                  set5[12].set_color, GREEN
                  )
        self.wait(2)
        self.play(ReplacementTransform(set5[6], last1[0]),
                  ReplacementTransform(set5[7], last1[1]),
                  ReplacementTransform(set5[8], last1[2]),
                  ReplacementTransform(set5[9], last1[3]),
                  ReplacementTransform(set5[10], last1[4]),
                  ReplacementTransform(set5[11], last1[5]),
                  ReplacementTransform(set5[12], last1[6]),
                  FadeOut(notice),
                  FadeOut(this),
                  FadeOut(set5[0]),
                  FadeOut(set5[1]),
                  FadeOut(set5[2]),
                  FadeOut(set5[3]),
                  FadeOut(set5[4]),
                  FadeOut(set5[5]),
                  FadeOut(set5[13]),
                  FadeOut(set5[14])
                  )
        self.wait(5)
        self.play(FadeOut(last1[0]),
                  FadeOut(last1[2]),
                  FadeOut(last1[4]),
                  FadeOut(last1[6]),
                  ReplacementTransform(last1[1].copy(), last2[0]),
                  ReplacementTransform(last1[1], last2[2]),
                  ReplacementTransform(last1[5].copy(), last2[4]),
                  ReplacementTransform(last1[5], last2[6]),
                  FadeIn(last2[1]),
                  ReplacementTransform(last1[3],last2[3]),
                  FadeIn(last2[5])
                  )
        self.wait(5)
        self.play(FadeIn(last3[0]),
                  ReplacementTransform(last2[0], last3[1]),
                  ReplacementTransform(last2[1], last3[2]),
                  ReplacementTransform(last2[2], last3[3]),
                  FadeIn(last3[4]),
                  FadeIn(last3[5]),
                  FadeIn(last3[6]),
                  FadeIn(last3[7]),
                  FadeIn(last3[8]),
                  ReplacementTransform(last2[3], last3[9]),
                  FadeIn(last3[10]),
                  ReplacementTransform(last2[4], last3[11]),
                  ReplacementTransform(last2[5], last3[12]),
                  ReplacementTransform(last2[6], last3[13]),
                  FadeIn(last3[14]),
                  FadeIn(last3[15]),
                  FadeIn(last3[16]),
                  FadeIn(last3[17]),
                  FadeIn(last3[18])
                  )
        self.wait(5)
        self.play(ReplacementTransform(last3[1], last4[0]),
                  ReplacementTransform(last3[8], last4[1]),
                  ReplacementTransform(last3[9], last4[2]),
                  ReplacementTransform(last3[11], last4[3]),
                  ReplacementTransform(last3[16], last4[4]),
                  FadeOut(last3[0]),
                  FadeOut(last3[2]),
                  FadeOut(last3[3]),
                  FadeOut(last3[4]),
                  FadeOut(last3[5]),
                  FadeOut(last3[6]),
                  FadeOut(last3[7]),
                  FadeOut(last3[10]),
                  FadeOut(last3[12]),
                  FadeOut(last3[13]),
                  FadeOut(last3[14]),
                  FadeOut(last3[15]),
                  FadeOut(last3[17]),
                  FadeOut(last3[18])
                  )
        self.wait(3)
        self.play(Write(qed))
        self.wait(15)
                  
                  
                  
                  
                  
                  
        
