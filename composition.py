#composition.py

import translation
import rotation
import scale

def main( x1, y1, x2, y2, xt, yt, d, xs, ys, xTrans, yTrans ):

    line = rotation.main( x1, y1, x2, y2, xt, yt, d )
    length = len( line )
    line = scale.main( line[ 0 ].x, line[ 0 ].y, line[ length - 1 ].x, line[ length - 1 ].y, xt, yt, xs, ys )
    length = len( line )
    line = translation.main( line[ 0 ].x, line[ 0 ].y, line[ length - 1 ].x, line[ length - 1 ].y, xTrans, yTrans )

    return line
