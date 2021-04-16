import datetime
import blinkt

def get_current_week():
    return datetime.date.today().isocalendar()[1]

def shift_array( week_num, array ):
    # right_rotation: https://stackoverflow.com/a/52139025
    rotations = week_num % len( array )
    return array[ -rotations: ] + array[ :-rotations ]

def show_led_array(array):
    blinkt.clear()
    blinkt.set_brightness( 0.05 )
    i = 0
    for color in array:
        blinkt.set_pixel( i,     color[0], color[1], color[2] )
        blinkt.set_pixel( i + 1, color[0], color[1], color[2] )
        i += 2
    blinkt.show()

def main():
    t_color     = (   0, 255, 0   )
    evan_color  = ( 14,  255, 208 )
    dylan_color = ( 250, 126, 1   )
    sam_color   = ( 255, 0,   0   )

    blinkt.set_clear_on_exit( False )

    roommates = [ t_color, evan_color, dylan_color, sam_color ]
    roommates_shifted = shift_array( get_current_week(), roommates )

    show_led_array( roommates_shifted )

main()