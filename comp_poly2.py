#comp_poly.py

import translation
import draw_polygon
import scale
import rotation

def main( x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, xt, yt, xTrans, yTrans, xs, ys, d ):

    line1 = translation.main( x1, y1, x2, y2, xTrans, yTrans )
    line2 = translation.main( x2, y2, x3, y3, xTrans, yTrans )
    line3 = translation.main( x3, y3, x4, y4, xTrans, yTrans )
    line4 = translation.main( x4, y4, x5, y5, xTrans, yTrans )
    line5 = translation.main( x5, y5, x1, y1, xTrans, yTrans )

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

    line1 = scale.main( x1, y1, x2, y2, xt, yt, xs, ys )
    line2 = scale.main( x2, y2, x3, y3, xt, yt, xs, ys )
    line3 = scale.main( x3, y3, x4, y4, xt, yt, xs, ys )
    line4 = scale.main( x4, y4, x5, y5, xt, yt, xs, ys )
    line5 = scale.main( x5, y5, x1, y1, xt, yt, xs, ys )

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

    line1 = rotation.main( x1, y1, x2, y2, xt, yt, d )
    line2 = rotation.main( x2, y2, x3, y3, xt, yt, d )
    line3 = rotation.main( x3, y3, x4, y4, xt, yt, d )
    line4 = rotation.main( x4, y4, x5, y5, xt, yt, d )
    line5 = rotation.main( x5, y5, x1, y1, xt, yt, d )

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
