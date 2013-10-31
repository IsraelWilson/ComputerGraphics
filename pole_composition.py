#pole_composition.py


import translation
import scale
import rotation
import draw_line


def main( x1, y1, x2, y2, xt, yt, xf, yf, d, xs, ys ):

    line = translation.main( x1, y1, x2, y2, xt, yt )

    line = rotation.main( line[ 0 ].x, line[ 0 ].y, line[ 1 ].x, line[ 1 ].y, xf, yf, d )

    line = scale.main( line[ 0 ].x, line[ 0 ].y, line[ 1 ].x, line[ 1 ].y, xf, yf, xs, ys )
    

    line = draw_line.main( line[ 0 ].x, line[ 0 ].y, line[ 1 ].x, line[ 1 ].y )
    

    return line
