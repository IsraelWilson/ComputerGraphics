#scale.py

#This file will scale an image by the appropriate
#size specified

import translation

def main ( x1, y1, x2, y2, xt, yt, xs, ys ):

    line = translation.main( x1, y1, x2, y2, -xt, -yt )

    x1 = round( line[ 0 ].x * xs )
    y1 = round( line[ 0 ].y * ys )

    x2 = round( line[ 1 ].x * xs )
    y2 = round( line[ 1 ].y * ys )

    line = translation.main( x1, y1, x2, y2, xt, yt )


    return line
