def calc(model, qty, options):
    # Order-Wide Options

    cabinetbody = "TBD"
    cabinetface = "TBD"
    cabinettop = "TBD"

    for row in options:
        # Possible database col names:
        if row[0] == 'Cabinet Body':
            cabinetbody = row[1].split(" ")
            cabinetbody = cabinetbody[0]
        elif row[0] == 'Cabinet Face':
            cabinetface = row[1].split(" ")
            cabinetface = cabinetface[0]
        elif row[0] == 'Cabinet Top':
            cabinettop = row[1].split(" ")
            cabinettop = cabinettop[0]

    # Product Level Options

    for row in options:
        optionName = row[0]
        if optionName == 'Cabinet Body':
            cabinetbody = row[1].split(" ")
            cabinetbody = cabinetbody[0]
        elif optionName == 'Cabinet Face':
            cabinetface = row[1].split(" ")
            cabinetface = cabinetface[0]
        elif optionName == 'Cabinet Top':
            cabinettop = row[1].split(" ")
            cabinettop = cabinettop[0]

    #########################
    # CALC LOGIC BELLOW
    #########################
    # partType, style, depth = model.split('-')
    partType,group, style,top,height, depth,width = model.split('-')

    # WORKPEICE NAME PARAMTERS
    if style[:-1] == "BF":
        wps = partType + "-BF"

    elif style[:-1] == "BFH":
        wps = partType + "-BFH"


    elif style[:-1] == "BBF":
        wps = partType + "-BBF"

    elif style[:-1] == "FF":
        wps = partType + "-FF"

    elif style == "MBBF" or style == "MFF":
        wps = partType + "-MBBF"

    elif style == "MFF":
        wps = partType + "-MFF"


    elif style == "MBF":
        wps = partType + "-MBF"

    elif style == "PD" or "DB":
        wps = partType + "-PD"

    # STRETCHER QTY
    if style[-1] == "T":
        stretcher_qty = int(qty)
    elif style[-1] == "D" or "W":
        stretcher_qty = int(qty) * 2
    elif style == "PD":
        stretcher_qty = int(qty) * 2

    # SIDE X,Y PARAMTERS
    if style == "PD":
        side_x = 152.4
        side_y = int(depth) * 25.4 - 21.41

    elif style == "BBFT" or style == "FFT":
        side_x = 698.5
        side_y = float(depth) * 25.4 - 21.41

    elif style == "BBFD" or style == "FFD":
        side_x = 698.5
        side_y = float(depth) * 25.4 - 46.81

    elif style == "BBFW" or style == "FFW":
        side_x = 698.5
        side_y = float(depth) * 25.4 - 27.76

    elif style == "MBBF" or style == "MFF":
        side_x = 580.3
        side_y = float(depth) * 25.4 - 21.41

    elif style == "MBF":
        side_x = 426.15
        side_y = float(depth) * 25.4 - 21.41

    elif style == "BFT":
        side_x = 524.125
        side_y = float(depth) * 25.4 - 21.41

    elif style == "BFD":
        side_x = 524.125
        side_y = float(depth) * 25.4 - 46.81

    elif style == "BFW":
        side_x = 524.125
        side_y = float(depth) * 25.4 - 27.76

    elif style == "HBFW":
        side_x = 457.2
        side_y = float(depth) * 25.4 - 27.76

    elif style == "HBFD":
        side_x = 457.2
        side_y = float(depth) * 25.4 - 46.81

    else:
        side_x = 698.5
        side_y = float(depth) * 25.4 - 21.41

    # DOOR X PARAMTERS

    if style == "PD":
        bDoorx = "165.1"
        bDoorlx = "NONE"
        fDoorx = "NONE"
        fDoorlx = "NONE"

    elif style == "HBFW" or style == "HBFD":  # I ADDED 'BFT' #
        bDoorx = "NONE"
        bDoorlx = "150.4"
        fDoorx = "302.8"
        fDoorlx = "NONE"


    elif style == "BFT":  # I ADDED 'BFT' #
        bDoorx = "NONE"
        bDoorlx = "172.375"
        fDoorx = "347.75"
        fDoorlx = "NONE"


    elif style == "MBBF":
        bDoorx = "149.15"
        bDoorlx = "149.15"
        fDoorx = "295.41"
        fDoorlx = "NONE"

    elif style == "MFF":
        bDoorx = "NONE"
        bDoorlx = "NONE"
        fDoorx = "295.41"
        fDoorlx = "300.3"

    elif style == "MBF":
        bDoorx = "NONE"
        bDoorlx = "146.15"
        fDoorx = "295.41"
        fDoorlx = "NONE"

    else:
        bDoorx = "172.375"
        bDoorlx = "172.375"
        fDoorx = "347.75"
        fDoorlx = "346.75"

    # BACK PARAMTERS
    if style == "PD":
        back = "SPED-PD-BACK"
    else:
        back = "SPED-BACK"

    # PRINT LEFT SIDE PART
    leftSide = wps + "-LEFT-SIDE-CL", "0", "LEFT-SIDE", str(qty), "0", str(side_x), \
               str(side_y), "19.41", cabinetbody, "0", wps + "-LEFT-SIDE-CL.pgmx\n"
    leftSide = ";".join(leftSide)

    # PRINT RIGHT SIDE PART
    rightSide = wps + "-RIGHT-SIDE-CL", "0", "RIGHT-SIDE", str(qty), "0", str(side_x), \
                str(side_y), "19.41", cabinetbody, "0", wps + "-RIGHT-SIDE-CL.pgmx\n"
    rightSide = ";".join(rightSide)

    # PRINT BACK PART
    back = back, "0", "BACK", str(qty), "0", str(side_x), "355.6", \
           "19.41", cabinetbody, "0", back + ".pgmx\n"
    back = ";".join(back)

    # PRINT STRETCHER
    stretcher = "STRETCHER", "0", "STRETCHER", str(stretcher_qty), "0", "355.6", "101.6", \
                "19.41", cabinetbody, "0", "STRETCHER.pgmx\n"
    stretcher = ";".join(stretcher)

    # PRINT TOP
    topp = "SPED-TOP", "0", "SPED-TOP", str(qty), "0", str(float(depth) * 25.4), "398.42", \
           "19.41", cabinettop, "0", "SPED-TOP.pgmx\n"
    topp = ";".join(topp)

    # PRINT BOTTOM
    bottomp = "SPED-BOTTOM", "0", "SPED-BOTTOM", str(qty), "0", str(side_y), "398.42", \
              "19.41", cabinetbody, "0", "SPED-BOTTOM.pgmx\n"
    bottomp = ";".join(bottomp)

    # PRINT BOX DOOR - no handle
    bDoornhP = "BOX-DOOR-NH", "0", "BOX-DOOR-NH", str(qty), "0", bDoorx, "391.42", \
               "19.41", cabinetface, "0", "BOX-DOOR-NH.pgmx\n"
    bDoornhP = ";".join(bDoornhP)

    # PRINT BOX DOOR
    bDoorP = "BOX-DOOR", "0", "BOX-DOOR", str(qty), "0", bDoorx, "391.42", \
             "19.41", cabinetface, "0", "BOX-DOOR.pgmx\n"
    bDoorP = ";".join(bDoorP)

    # PRINT BOX DOOR WITH LOCK
    bDoorlP = "BOX-DOOR-CL", "0", "BOX-DOOR-L", str(qty), "0", bDoorlx, "391.42", \
              "19.41", cabinetface, "0", "BOX-DOOR-CL.pgmx\n"
    bDoorlP = ";".join(bDoorlP)

    # PRINT FILE DOOR
    fDoorP = "FILE-DOOR", "0", "FILE-DOOR", str(qty), "0", fDoorx, "391.42", \
             "19.41", cabinetface, "0", "FILE-DOOR.pgmx\n"
    fDoorP = ";".join(fDoorP)

    # PRINT FILE DOOR WITH LOCK
    fDoorlP = "FILE-DOOR-CL", "0", "FILE-DOOR-L", str(qty), "0", fDoorlx, "391.42", \
              "19.41", cabinetface, "0", "FILE-DOOR-CL.pgmx\n"
    fDoorlP = ";".join(fDoorlP)

    # CSV PRINT LOGIC

    csvParts = leftSide
    csvParts += rightSide
    csvParts += back

    if style == "MBF" or style == "MBBF" or style == "MFF":
        pass
    else:
        csvParts += stretcher

    if style == "MBF" or style == "MBBF" or style == "MFF" or style == "BFT" or style == "BBFT" or style == "FFT":
        csvParts += topp

    if style == "MBF" or style == "MBBF" or style == "MFF":
        csvParts += bottomp

    if style == "BBFW" or style == "BBFD" or style == "MBBF" or style == "BBFT":
        csvParts += bDoorP

    if style == "PD":
        csvParts += bDoornhP

    if style == "FFW" or style == "FFD" or style == "MFF" or style == "FFT" or style == "PD":
        pass
    else:
        csvParts += bDoorlP

    if style == "PD":
        pass
    else:
        csvParts += fDoorP

    if style == "FFW" or style == "FFD" or style == "MFF" or style == "FFT":
        csvParts += fDoorlP

    #########################
    # CALC LOGIC ABOVE
    #########################

    # print(type(csvParts))
    return csvParts


if __name__ == "__main__":
    # result = calc("SPED-BBFD-24", 1, [["Cabinet Body","W150 Ash"],["Cabinet Face","S645 White"]])
    # print(result)

    orders = [
        {"model": "PED-SP-BBF-NT-27.5-20.00-15.50", "qty": 1, "options": [
            ["Cabinet Body","W150 Ash"],
            ["Cabinet Face","S645 White"],
        ]},

##        {"model": "SPED-PD-20", "qty": 1, "options": [
##            ["Cabinet Body", "W150 Ash"],
##            ["Cabinet Face", "S645 White"],
##        ]},
##
##        {"model": "SPED-BBFD-20", "qty": 1, "options": [
##            ["Cabinet Body", "W150 Ash"],
##            ["Cabinet Face", "S645 White"],
##        ]},
##
##        {"model": "SPED-BFD-20", "qty": 1, "options": [
##            ["Cabinet Body", "W150 Ash"],
##            ["Cabinet Face", "S645 White"],
##        ]},

        # {"model": "SPED-BBFW-24", "qty": 8, "options": [
        #     ["Cabinet Body", "W150 Ash"],
        #     ["Cabinet Face", "S645 White"],
        # ]},
        #
        # {"model": "SPED-FFD-24", "qty": 4, "options": [
        #     ["Cabinet Body", "W150 Ash"],
        #     ["Cabinet Face", "S645 White"],
        # ]},
        #
        # {"model": "SPED-BBFD-30", "qty": 2, "options": [
        #     ["Cabinet Body", "W150 Ash"],
        #     ["Cabinet Face", "S645 White"],
        # ]},

    ]





    for order in orders:
        result = calc(order["model"], order["qty"], order["options"])
        print(result)
