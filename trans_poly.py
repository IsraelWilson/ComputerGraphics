#trans_poly.py

import translation
import draw_polygon

def main( x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, xt, yt ):

    line1 = translation.main( x1, y1, x2, y2, xt, yt )
    line2 = translation.main( x2, y2, x3, y3, xt, yt )
    line3 = translation.main( x3, y3, x4, y4, xt, yt )
    line4 = translation.main( x4, y4, x5, y5, xt, yt )
    line5 = translation.main( x5, y5, x1, y1, xt, yt )

    x1 = line1[ 0 ].x
    y1 = line1[ 0 ].y
    x2 = line2[ 0 ].x
    y2 = line2[ 0 ].y
    x3 = line3[ 0 ].x
    y3 = line3[ 0 ].y
    x4 = line4[ 0 ].x
    y4 = line4[ 0 ].y
    x5 = line5[ 0 ].x
    y5 = line5[ 0 ].y

    line = draw_polygon.main( x1, y1, x2, y2, x3, y3, x4, y4, x5, y5 )

    return line
