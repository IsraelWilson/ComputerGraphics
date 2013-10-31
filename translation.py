#Translation.py

#translates the location of a line
#and returns teh points where its
#new location is

import one_color
import copy

def main( x1, y1, x2, y2, xt, yt ):
    temp = one_color.struc()
    points = []

    temp.x = x1 + xt
    temp.y = y1 + yt
    points.append( copy.deepcopy( temp ) )

    temp.x = x2 + xt
    temp.y = y2 + yt
    points.append( copy.deepcopy( temp ) )

    

    return points
