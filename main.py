def on_button_pressed_ab():
    global rating
    for index in range(5):
        basic.show_leds("""
            . # # # #
                        . . . . #
                        . . # # #
                        . . . . .
                        . . # . .
        """)
        basic.pause(1000)
        basic.clear_screen()
        basic.pause(1000)
    rating = randint(0, 100)
    basic.show_number(rating)
    basic.pause(1000)
    if rating > 75:
        basic.show_leds("""
            . # . # .
                        # # # # #
                        # # # # #
                        . # # # .
                        . . # . .
        """)
        basic.pause(1000)
        basic.clear_screen()
        basic.pause(1000)
    basic.show_leds("""
        . . . . .
                . # . # .
                # . . . #
                . # . # .
                . . . . .
    """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

rating = 0
basic.show_leds("""
    . . . . .
        . # . # .
        # . . . #
        . # . # .
        . . . . .
""")