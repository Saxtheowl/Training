try:
    f = open('/home/roro/work/training/Mark_G._Sobell-Practical_Guide_to_Linux_Commands_Editors_and_Shell_Programming-Prentice_Hall_2013/chapter12/three_liness', 'r')
except:
    print "error on opening the file."
    exit()



for ln in f.readlines():
    print ln.strip()
f.close

"""for ln in f:
    print ln
"""
