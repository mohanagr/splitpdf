#! /usr/bin/python3.6

import os
import sys

if __name__ == '__main__':

    # needs Ghostscript and pdftk installed. Both can be installed by sudo apt install.
    # please google if that doesn't work.
    if(len(sys.argv)<2):
        print("specify filepath")
        sys.exit(1)

    if(len(sys.argv)>3):
        print("too many params passed")
        sys.exit(1)

    if(len(sys.argv)==3):

        filepath = sys.argv[1]
        mode = sys.argv[2]
        if(mode=='-n'):
            mode = False
        else:
            print("-n is the only acceptable arg")
            sys.exit(1)
        print("will only provide page counts and numbers")
    else:
        filepath = sys.argv[1]
        mode = True
        print("will dump the PDFs")


    try:
        _ = os.mkdir("tmp")
    except FileExistsError:
        _ = os.system("rm -r tmp")
        _ = os.mkdir("tmp")

    gscmd = f"gs -o - -sDEVICE=inkcov {filepath} > ./tmp/coloroutput.txt"

    if(os.system(gscmd)==0):
        print("Extracted color info")
    else:
        print("FAILED")

    with open("./tmp/coloroutput.txt", 'r') as f:
        lines = f.readlines()

    lines = lines[4:] # skip headers
    lines = lines[1::2] # get only color info

    colors = [[float(c) for c in line.strip().split('  ')[:3]] for line in lines] # this is a (n_pages x 3) array. columns are C, M, Y
    # if unfortunately your book is not black and white, but has some other base color, please subtract mean from C, M, Y.


    coloredpages = []
    bwpages = []
    for i, row in enumerate(colors):
        if(min(row)>0.001):
            coloredpages.append(str(i+1))
        else:
            bwpages.append(str(i+1))
    cp = ' '.join(coloredpages)
    bwp = ' '.join(bwpages)

    if(mode):
        pdfcmd = "pdftk {0} cat {1} output ./{2}_out.pdf"
        _ = os.system(pdfcmd.format(filepath, cp, "color"))
        _ = os.system(pdfcmd.format(filepath, bwp, "bw"))

    print(f"Total number of colored pages: {len(coloredpages)}\n{cp}")
    print(f"Total number of b/w pages: {len(bwpages)}\n{bwp}")
    _ = os.system("rm -r tmp")
