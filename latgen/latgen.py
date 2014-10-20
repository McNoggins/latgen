# -*- coding: utf-8 -*-
import numpy as np

def honeycomb(depth=1,pitch=1.0):
    """Generate the points of a regular honeycomb lattice.

    Keyword arguments:
    depth -- the depth of the honeycomb lattice, counted in number of
    points starting from the central point (default 1)
    
    pitch -- the lattice pitch (default 1.0)
    
    Return arguments:
    X,Y -- Lists of lattice points
    """

    # Initialize some empty lists
    X=[]
    Y=[]

    hx=float(pitch)
    hy=0.5*np.sqrt(3.0)*hx

    # Generate every row using a loop
    for rowid in range(depth):

        if (rowid % 2) == 0: # Even row
            for colid in range(depth - rowid/2):
                # Base point
                X.extend([colid*hx])
                Y.extend([rowid*hy])

                # Execute for non-zero rows
                if (rowid != 0):
                    # Y-symmetry
                    X.extend([colid*hx])
                    Y.extend([-rowid*hy])

                # Execute for non-zero columns
                if (colid != 0):
                    # X-symmetry
                    X.extend([-colid*hx])
                    Y.extend([rowid*hy])

                # Execute for non-zero rows and columns
                if (colid != 0 and rowid !=0):
                    # X-Y symmetry
                    X.extend([-colid*hx])
                    Y.extend([-rowid*hy])


        elif (rowid % 2) == 1: # Odd row
            for colid in range(depth-(rowid +1)/2 ):
                # Base point
                X.extend([ (0.5+colid)*hx])
                Y.extend([ rowid*hy])

                # X symmetry
                X.extend([ -(0.5+colid)*hx])
                Y.extend([ rowid*hy])

                # Y symmetry
                X.extend([ (0.5+colid)*hx])
                Y.extend([ -rowid*hy])

                # X-Y symmetry
                X.extend([ - (0.5+colid)*hx])
                Y.extend([ -rowid*hy])

    # Lexical sort of lists
    ind = np.lexsort((X,Y))
   
    xsort=[X[i] for i in ind]
    ysort=[Y[i] for i in ind]

    # Return sorted lists
    return xsort,ysort
