#3DviewDisplay.py
import TDview
import TDviewAlignment
import display


def main( xVRP, yVRP, zVRP, d, a, b, xt, yt, sf, *args ):
    
    UVN = TDview.main( a, b )
    alignedPoints = TDviewAlignment.main( xVRP, yVRP, zVRP, d, UVN[ 0 ], UVN[ 1 ], UVN[ 2 ], UVN[ 3 ], UVN[ 4 ], UVN[ 5 ], UVN[ 6 ], UVN[ 7 ], UVN[ 8 ], args )
    displayImage = display.main( d, xt, yt, sf, alignedPoints )

    return displayImage
