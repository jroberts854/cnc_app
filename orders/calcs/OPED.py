def calc(model, qty, options):
    # Order-Wide Options

    body_lam = "TBD"
    top_lam = "TBD"
    face_lam = "TBD"

    for row in options:
        if row[0] == 'Cabinet Top':
            top_lam = row[1].split(" ")
            top_lam = top_lam[0]
        elif row[0] == 'Cabinet Face':
            face_lam = row[1].split(" ")
            face_lam = face_lam[0]
        elif row[0] == 'Cabinet Body':
            body_lam = row[1].split(" ")
            body_lam = body_lam[0]

    # Product Level Options

    for row in options:
        optionName = row[0]
        if row[0] == 'Cabinet Top':
            top_lam = row[1].split(" ")
            top_lam = top_lam[0]
        elif row[0] == 'Cabinet Face':
            face_lam = row[1].split(" ")
            face_lam = face_lam[0]
        elif row[0] == 'Cabinet Body':
            body_lam = row[1].split(" ")
            body_lam = body_lam[0]

    #########################
    # CALC LOGIC BELLOW
    #########################
    partType, style, depth, width = model.split('-')



    # WORKPEICE NAME PARAMTERS
    if style == "BBFOL":
        wps= partType + "-BBFOL"

    # elif style[0:5] == "BBFOR":
    elif style == "BBFOR":
        wps= partType + "-BBFOR"

    elif style == "FFOL":
        wps= partType + "-FFOL"

    elif style== "FFOR":
        wps= partType + "-FFOR"

    elif style == "BFOL":
        wps= partType + "-BFOL"

    elif style == "BFOR":
        wps= partType + "-BFOR"

    else:
        wps= partType + "-" + style


    #SIDE Y PARAMTERS
    if style [-1] == "D" :
        side_y = float(depth) * 25.4-46.81
        bottom_y = float(depth)*25.4 - 46.81 - 21.41
        top_y = float(depth)*25.4 - 25.4

    elif style [-1] == "W":
        side_y = float(depth) * 25.4-27.76
        bottom_y = float(depth)*25.4 - 27.76 - 21.41
        top_y = float(depth)*25.4 - 6.35

    elif style [-1] == "T":
        side_y = float(depth) * 25.4-21.41
        bottom_y = float(depth)*25.4 - 21.41 - 21.41
        top_y = float(depth)*25.4

    elif "M" in style :
        side_y = float(depth) * 25.4-21.41
        top_y = float(depth)*25.4
        bottom_y = float(depth)*25.4 - 21.41



    #SIDE X PARAMTERS
    if style[0:3] == "BFO" :
        side_x = "524.125"
    elif style [0:4] == "MBBF" or style [0:3] == "MFF":
        side_x = "580.3"
    elif style [0:4] == "MBFO": #ADDED THIS PART - SANG
        side_x = "426.15"
    else:
        side_x = "698.5"


    # DOOR X PARAMTERS
    if "M" in style :
        bDoorx = "149.15"
        bDoorlx = "149.15"
        fDoorx= "295.41"
        fDoorlx= "300.3"
    else:
        bDoorx = "172.375"
        bDoorlx = "172.375"
        fDoorx = "346.75"
        fDoorlx= "346.75"


    bDoory  = "391.42"
    fDoorly = "391.42"




    if "L" in style:
        back = "OPED-BACK-LEFT"
        topp = "OPED-TOP-LEFT"
        bottomP = "OPED-BOTTOM-LEFT"
        bottom_x = float(width)*25.4 - 42.82
        if "M" in style:
            back = "OPED-MBACK-LEFT"
            bottomP = "OPED-MBOTTOM-LEFT"
            bottom_x = float(width)*25.4

    if "R" in style:
        back = "OPED-BACK-RIGHT"
        topp = "OPED-TOP-RIGHT"
        bottomP = "OPED-BOTTOM-RIGHT"
        bottom_x = float(width)*25.4 - 42.82
        if "M" in style:
            back = "OPED-MBACK-RIGHT"
            bottomP = "OPED-MBOTTOM-RIGHT"
            bottom_x = float(width)*25.4


    # Z FOR TOP
    if style [0:2]== "BF" or "M" in style:
        top_z = "19.41"
    else:
        top_z = "25.4"

    # MID PANEL X
    if "M" in style :
        midp_x = float(side_x)
    else :
        midp_x = float(side_x)-21.41



    #PRINT LEFT SIDE PART
    leftSide = wps+ "-LEFT-SIDE", "0","LEFT-SIDE",str(qty),"0",str(side_x),\
               str(side_y),"19.41",body_lam,"0",wps + "-LEFT-SIDE.pgmx \n"
    leftSide=";".join(leftSide)


    #PRINT RIGHT SIDE PART
    rightSide = wps + "-RIGHT-SIDE", "0","RIGHT-SIDE",str(qty),"0",str(side_x),\
                str(side_y),"19.41",body_lam,"0",wps + "-RIGHT-SIDE.pgmx \n"
    rightSide=";".join(rightSide)

    #PRINT MID PANEL PART
    midpanel = wps + "-MID-PANEL", "0","MID-PANEL",str(qty),"0",str(midp_x),\
                str(float(side_y)-21.41),"19.41",body_lam,"0",wps + "-MID-PANEL.pgmx \n"
    midpanel=";".join(midpanel)


    #PRINT BACK PART
    back = back, "0","BACK",str(qty),"0", str(side_x) , str(float(width) *25.4-42.82) ,\
               "19.41",body_lam,"0",back+".pgmx \n"
    back=";".join(back)


    #PRINT STRETCHER
    stretcher = "STRETCHER" , "0" , "STRETCHER",str(qty) ,"0","355.6", "101.6" ,\
               "19.41", body_lam ,"0" , "STRETCHER.pgmx \n"
    stretcher=";".join(stretcher)


    #PRINT ADJUSTABLE SHELF
    adjshelf = "ADJ-SHELF", "0","ADJ-SHELF",str(qty),"0", str(float(width) *25.4-418.33) , str(float(side_y)-21.41) ,\
               "19.41",body_lam,"0","ADJ-SHELF.pgmx \n"
    adjshelf=";".join(adjshelf)


    #PRINT TOP
    topp = topp , "0" ,"OPED-TOP",str(qty) ,"0",str(float(width) *25.4) , str(top_y),\
               str(top_z), top_lam ,"0" , topp + ".pgmx \n"
    topp=";".join(topp)


    #BOTTOM(ADDED THIS LINE - SANG)
    bottomP = bottomP , "0" ,"OPED-BOTTOM",str(qty) ,"0",str(bottom_x) , str(bottom_y),\
               "19.41", body_lam ,"0" , bottomP + ".pgmx \n"
    bottomP=";".join(bottomP)


    #PRINT BOX DOOR
    bDoorP = "BOX-DOOR" , "0" , "BOX-DOOR",str(qty) ,"0",str(bDoorx), str(bDoory) ,\
               "19.41", face_lam ,"0" , "BOX-DOOR.pgmx \n"
    bDoorP=";".join(bDoorP)


    #PRINT BOX DOOR WITH LOCK
    bDoorlP = "BOX-DOOR-CL" , "0" , "BOX-DOOR-L",str(qty) ,"0",str(bDoorlx), str(bDoory) ,\
               "19.41", face_lam ,"0" , "BOX-DOOR-CL.pgmx \n"
    bDoorlP=";".join(bDoorlP)


    #PRINT FILE DOOR WITH LOCK
    fDoorlP = "FILE-DOOR-CL" , "0" , "FILE-DOOR-L",str(qty) ,"0",str(fDoorlx), str(bDoory) ,\
               "19.41", face_lam ,"0" , "FILE-DOOR-CL.pgmx \n"
    fDoorlP=";".join(fDoorlP)


    #PRINT FILE DOOR
    fDoorP = "FILE-DOOR" , "0" , "FILE-DOOR",str(qty) ,"0",str(fDoorx), str(bDoory) ,\
               "19.41", face_lam ,"0" , "FILE-DOOR.pgmx \n"
    fDoorP=";".join(fDoorP)





    #CSV PRINT LOGIC # DELETED stretcher , bDoor, fixedshelf - SANG)

    csvParts = leftSide
    csvParts += rightSide
    csvParts += midpanel
    csvParts += back
    csvParts += adjshelf
    csvParts += fDoorP
    csvParts += bottomP

    if style[-1]== "T" or "M":
        csvParts += topp # DELETED or "M" FROM THIS PART - SANG

    if style [0:2] == "BB" or style [0:3] == "MBB":
        csvParts += bDoorlP
        csvParts += bDoorP # ADDED THIS PART - SANG

    if style [0:2] == "BF" or style [0:3] == "MBF":
        csvParts += bDoorlP # ADDED THIS PART - SANG

    if style [0:2] == "FF" or style [0:3] == "MFF":
        csvParts += fDoorlP # ADDED THIS PART - SANG

    if style [0]=="M" or style [-1]=="T":
        pass
    else:
        csvParts += stretcher


    #########################
    # CALC LOGIC ABOVE
    #########################
    return csvParts


if __name__ == "__main__":
    import sys

    script = sys.argv.pop(0)
    if sys.argv:
        print(calc(sys.argv[0], 1, []))
    else:
        print("Usage: python3 {} MODEL-NAME-18-30".format(script))
