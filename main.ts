input.onButtonPressed(Button.A, function () {
    basic.showString("YO")
    basic.clearScreen()
    basic.showString("WELCOME, THIS IS ABOUT ME :D")
    basic.showLeds(`
        . # # # #
        . # . . #
        . # . . #
        # # . # #
        # # . # #
        `)
    basic.clearScreen()
    basic.showLeds(`
        . # # . .
        . # . # .
        . # . . .
        # # . . .
        # # . . .
        `)
    music.playMelody("C5 A C5 G C5 A C5 G ", 40)
    basic.showLeds(`
        . . . . .
        # . . . .
        # . . . .
        # # # # #
        # # # # #
        `)
    basic.showString("zzzzz")
    basic.clearScreen()
    basic.showLeds(`
        . # # # .
        # . # . #
        # # # # #
        # # # # #
        # . # . #
        `)
    basic.showString("GAMES!")
    basic.showLeds(`
        . . . . .
        . # . # .
        # . . . #
        # . # . #
        # # # # #
        `)
    basic.showString("I LOVE CATS")
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    basic.showString("SHAKE TO PLAY")
})
input.onGesture(Gesture.Shake, function () {
    hand = randint(0, 3)
    if (hand == 1) {
        basic.showLeds(`
            # # # # #
            # . . . #
            # . . . #
            # . . . #
            # # # # #
            `)
    } else if (hand == 2) {
        basic.showLeds(`
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            `)
    } else {
        basic.showLeds(`
            # # . . #
            # # . # .
            . . # . .
            # # . # .
            # # . . #
            `)
    }
})
let hand = 0
basic.showString("BOOTING UP..... PRESS A OR B TO CONTINUE", 75)
basic.pause(5000)
