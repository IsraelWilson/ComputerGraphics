#flagFill_composition.py

import translation
import scale
import rotation
import fill_polygon
import draw_polygon
import copy
import one_color

def main( x1, y1, x2, y2, x3, y3, xt, yt, xf, yf, d, xs, ys ):

    points = []
    temp = one_color.struc()

    line1 = translation.main( x1, y1, x2, y2, xt, yt )
    line2 = translation.main( x2, y2, x3, y3, xt, yt )
    line3 = translation.main( x3, y3, x1, y1, xt, yt )

    line1 = rotation.main( line1[ 0 ].x, line1[ 0 ].y, line1[ 1 ].x, line1[ 1 ].y, xf, yf, d )
    line2 = rotation.main( line2[ 0 ].x, line2[ 0 ].y, line2[ 1 ].x, line2[ 1 ].y, xf, yf, d )
    line3 = rotation.main( line3[ 0 ].x, line3[ 0 ].y, line3[ 1 ].x, line3[ 1 ].y, xf, yf, d )

    line1 = scale.main( line1[ 0 ].x, line1[ 0 ].y, line1[ 1 ].x, line1[ 1 ].y, xf, yf, xs, ys )
    line2 = scale.main( line2[ 0 ].x, line2[ 0 ].y, line2[ 1 ].x, line2[ 1 ].y, xf, yf, xs, ys )
    line3 = scale.main( line3[ 0 ].x, line3[ 0 ].y, line3[ 1 ].x, line3[ 1 ].y, xf, yf, xs, ys )

    
    line = fill_polygon.main( line1[ 0 ].x, line1[ 0 ].y, line2[ 0 ].x, line2[ 0 ].y, line3[ 0 ].x, line3[ 0 ].y )
    
    return line
