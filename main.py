def on_button_pressed_a():
    basic.show_string("YO")
    basic.clear_screen()
    basic.show_string("WELCOME, THIS IS ABOUT ME :D")
    basic.show_leds("""
        . # # # #
                . # . . #
                . # . . #
                # # . # #
                # # . # #
    """)
    basic.clear_screen()
    basic.show_leds("""
        . # # . .
                . # . # .
                . # . . .
                # # . . .
                # # . . .
    """)
    music.play_melody("C5 A C5 G C5 A C5 G ", 40)
    basic.show_leds("""
        . . . . .
                # . . . .
                # . . . .
                # # # # #
                # # # # #
    """)
    basic.show_string("zzzzz")
    basic.clear_screen()
    basic.show_leds("""
        . # # # .
                # . # . #
                # # # # #
                # # # # #
                # . # . #
    """)
    basic.show_string("GAMES!")
    basic.show_leds("""
        . . . . .
                . # . # .
                # . . . #
                # . # . #
                # # # # #
    """)
    basic.show_string("I LOVE CATS")
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_string("SHAKE TO PLAY")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global hand
    hand = randint(0, 3)
    if hand == 1:
        basic.show_leds("""
            # # # # #
                        # . . . #
                        # . . . #
                        # . . . #
                        # # # # #
        """)
    elif hand == 2:
        basic.show_leds("""
            . . . . .
                        . # # # .
                        . # # # .
                        . # # # .
                        . . . . .
        """)
    else:
        basic.show_leds("""
            # # . . #
                        # # . # .
                        . . # . .
                        # # . # .
                        # # . . #
        """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

hand = 0
basic.show_string("BOOTING UP..... PRESS A OR B TO CONTINUE", 75)
basic.pause(5000)