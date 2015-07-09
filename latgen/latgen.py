# -*- coding: utf-8 -*-
import numpy as np

def triangle(depth=1,pitch=1.0):
    """Generate the points of a regular triangle lattice.

    Keyword arguments:
    depth -- the depth of the triangle lattice, counted in number of
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

def honeycomb(depth=1,pitch=1.0):
    """Generate the points of a regular honeycomb lattice (with zigzag edges)

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
    a=float(pitch)

    hx=np.sqrt(3.0)*a
    hy=1.5*a

    # Generate every row using a loop
    for rowid in range(depth):

        if (rowid % 2) == 0: # Even row
            for colid in range(depth - rowid/2):
                # Base point
                X.extend([colid*hx, colid*hx])
                Y.extend([rowid*hy, rowid*hy + a])

                # Execute for non-zero rows
                if (rowid != 0):
                    # Y-symmetry
                    X.extend([colid*hx, colid*hx])
                    Y.extend([-rowid*hy, -rowid*hy + a])

                # Execute for non-zero columns
                if (colid != 0):
                    # X-symmetry
                    X.extend([-colid*hx, -colid*hx])
                    Y.extend([rowid*hy, rowid*hy + a])

                # Execute for non-zero rows and columns
                if (colid != 0 and rowid !=0):
                    # X-Y symmetry
                    X.extend([-colid*hx, -colid*hx])
                    Y.extend([-rowid*hy, -rowid*hy + a])


        elif (rowid % 2) == 1: # Odd row
            for colid in range(depth-(rowid +1)/2 ):
                # Base point
                X.extend([ (0.5+colid)*hx, (0.5+colid)*hx])
                Y.extend([ rowid*hy, rowid*hy + a])

                # X symmetry
                X.extend([ -(0.5+colid)*hx, -(0.5+colid)*hx])
                Y.extend([ rowid*hy, rowid*hy + a])

                # Y symmetry
                X.extend([ (0.5+colid)*hx, (0.5+colid)*hx])
                Y.extend([ -rowid*hy, -rowid*hy + a ])

                # X-Y symmetry
                X.extend([ - (0.5+colid)*hx, -(0.5+colid)*hx])
                Y.extend([ -rowid*hy, -rowid*hy + a])

        # Terminate using zigzag edges
        if (rowid == depth -1 and rowid % 2 == 0):
            print "a"
            for colid in range(depth - rowid/2 - 1):
                
                # Base point
                Xcoord = colid*hx + 0.5*hx
                Ycoord = rowid*hy + 1.5*a
                X.extend([Xcoord])
                Y.extend([Ycoord])
                
                # X symmetry
                X.extend([Xcoord])
                Y.extend([-Ycoord + a])
                
                # Y symmetry
                X.extend([-Xcoord])
                Y.extend([Ycoord])
                
                # X-Y symmetry
                X.extend([-Xcoord])
                Y.extend([-Ycoord + a])
            
        if (rowid == depth - 1 and rowid % 2 == 1):
            print "b"
            for colid in range(depth-(rowid +1)/2 - 1):
                # Base point
                X.extend([(0.5+colid)*colid*hx + 0.5*hx])
                Y.extend([rowid*hy + 1.5*a])

    # Lexical sort of lists
    ind = np.lexsort((X,Y))

    xsort=[X[i] for i in ind]
    ysort=[Y[i] for i in ind]

    # Return sorted lists
    return xsort,ysort
