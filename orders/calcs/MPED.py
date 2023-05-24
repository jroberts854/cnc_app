from io import StringIO
import pandas as pd


def calc(model, qty, options):

    # Order-Wide Options

    body_lam = "TBD"
    top_lam = "TBD"
    face_lam = "TBD"

    for row in options:
        # Possible database col names:
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
        if optionName == 'Cabinet Top':
            top_lam = row[1].split(" ")
            top_lam = top_lam[0]
        elif optionName == 'Cabinet Face':
            face_lam = row[1].split(" ")
            face_lam = face_lam[0]
        elif optionName == 'Cabinet Body':
            body_lam = row[1].split(" ")
            body_lam = body_lam[0]

    #########################
    # CALC LOGIC BELLOW
    #########################
    partType, style, depth, width = model.split('-')

    # WORKPEICE NAME PARAMTERS
    if style[0:4] == "BBFLR":
        wps = partType + "-BBFLR"

    elif style[0:4] == "BBFLL":
        wps = partType + "-BBFLL"

    elif style[0:3] == "BBL":
        wps = partType + "-BBL"

    elif style[0:5] == "BBBBL":
        wps = partType + "-BBBBL"

    elif style[0:4] == "BBOL":
        wps = partType + "-BBOL"

    elif style[0:4] == "BBOR":
        wps = partType + "-BBOR"

    wpn = partType + "-" + style[:-1]
    mid = partType + "-" + style[:-1] + "-MID"
    # SIDE X,Y PARAMTERS
    if style[-1] == "D":
        side_y = float(depth) * 25.4 - 46.81
        mid_Y = float(depth) * 25.4 - 68.22

    elif style[-1] == "W":
        side_y = float(depth) * 25.4 - 27.76
        mid_Y = float(depth) * 25.4 - 49.17
    else:
        side_y = float(depth) * 25.4 - 21.41
        mid_Y = float(depth) * 25.4 - 42.82

    # DOOR X PARAMTERS
    bDoorx = "172.375"
    bDoorlx = "172.375"
    fDoorlx = "346.75"
    lDoorx = "347.75"

    bDoory = float(width) * 25.4 / 2 - 4.5
    fDoorly = float(width) * 25.4 / 2 - 4.5
    lDoory = float(width) * 25.4 - 7
    side_x = 698.5
    back = "MPED-BACK"

    if style[0:3] == "BBL":
        bDoory = float(width) * 25.4 - 7
        bDoorly = float(width) * 25.4 - 7

    if "O" in style:
        bDoory = float(width) * 25.4 / 2 + 4.705
        fDoorly = float(width) * 25.4 / 2 + 4.705

    # DOOR QTY PARAMTERS
    if style[0:5] == "BBBBL":
        bDoor_qty = int(qty) * 2

    else:
        bDoor_qty = int(qty)

    # STRETCHER QTY
    if style == "BBLD" or style == "BBLW":
        stretcher_qty = int(qty) * 2
    else:
        stretcher_qty = int(qty)

    # LEFT SIDE PART
    leftSide = wpn + "-LEFT-SIDE", "0", "LEFT-SIDE", str(qty), "0", str(side_x), \
               str(side_y), "19.41", body_lam, "0", wpn + "-LEFT-SIDE.pgmx\n"
    leftSide = ";".join(leftSide)

    # RIGHT SIDE PART
    rightSide = wpn + "-RIGHT-SIDE", "0", "RIGHT-SIDE", str(qty), "0", str(side_x), \
                str(side_y), "19.41", body_lam, "0", wpn + "-RIGHT-SIDE.pgmx\n"
    rightSide = ";".join(rightSide)

    # BACK PART
    back = back, "0", "BACK", str(qty), "0", str(side_x), str(float(width) * 25.4 - 42.82), \
           "19.41", body_lam, "0", back + ".pgmx\n"
    back = ";".join(back)

    # MID PART
    midp = mid, "0", "BBFL-MID", str(qty), "0", "350.75", str(mid_Y), \
           "19.41", body_lam, "0", mid + ".pgmx\n"
    midp = ";".join(midp)

    # MID FIX SHELF PART
    f_shelf = "MPED-FIXED-SHELF", "0", "MPED-FIXED-SHELF", str(qty), "0", str(float(width) * 25.4 - 42.82), str(mid_Y), \
              "19.41", body_lam, "0", "MPED-FIXED-SHELF.pgmx\n"
    f_shelf = ";".join(f_shelf)

    # BOTTOM
    bottom = "MPED-BOTTOM", "0", "BOTTOM", str(qty), "0", str(float(width) * 25.4 - 42.82), str(mid_Y), \
             "19.41", body_lam, "0", "MPED-BOTTOM.pgmx\n"
    bottom = ";".join(bottom)

    # STRETCHER
    stretcher = "STRETCHER", "0", "STRETCHER", str(stretcher_qty), "0", str(float(width) * 25.4 - 42.82), "101.6", \
                "19.41", body_lam, "0", "STRETCHER.pgmx\n"
    stretcher = ";".join(stretcher)

    # TOP
    topp = "MPED-TOP", "0", "MPED-TOP", str(qty), "0", str(float(width) * 25.4), str(float(depth) * 25.4), \
           "19.41", top_lam, "0", "MPED-TOP.pgmx\n"
    topp = ";".join(topp)

    # BOX DOOR
    bDoorP = "BOX-DOOR", "0", "BOX-DOOR", str(bDoor_qty), "0", str(bDoorx), str(bDoory), \
             "19.41", face_lam, "0", "BOX-DOOR.pgmx\n"
    bDoorP = ";".join(bDoorP)

    # BOX DOOR WITH LOCK
    bDoorlP = "BOX-DOOR-CL", "0", "BOX-DOOR-L", str(bDoor_qty), "0", str(bDoorlx), str(bDoory), \
              "19.41", face_lam, "0", "BOX-DOOR-CL.pgmx\n"
    bDoorlP = ";".join(bDoorlP)

    # FILE DOOR WITH LOCK
    fDoorlP = "MPED-FILE-DOOR-CL", "0", "FILE-DOOR-L", str(qty), "0", str(fDoorlx), str(bDoory), \
              "19.41", face_lam, "0", "MPED-FILE-DOOR-CL.pgmx\n"
    fDoorlP = ";".join(fDoorlP)

    # LATERAL DOOR
    lDoorlP = "LAT-DOOR", "0", "LAT-DOOR", str(qty), "0", str(lDoorx), str(lDoory), \
              "19.41", face_lam, "0", "LAT-DOOR.pgmx\n"
    lDoorlP = ";".join(lDoorlP)

    # BOX DRAWRER QUANTITIES
    if style[0:3] == "BBL" or style[0:4] == "BBFL" or style[0:4] == "BBOL":
        bd_fb_qty = int(qty) * 4
        bd_sd_qty = int(qty) * 4
        bd_btm_qty = int(qty) * 2

    elif style[0:5] == "BBBBL":
        bd_fb_qty = int(qty) * 8
        bd_sd_qty = int(qty) * 8
        bd_btm_qty = int(qty) * 4

    # FILE DRAWRER QUANTITIES
    if style[0:4] == "BBFL":
        fd_fb_qty = int(qty) * 2
        fd_sd_qty = int(qty) * 2
        fd_btm_qty = int(qty) * 1
    else:
        fd_fb_qty = ''
        fd_sd_qty = ''
        fd_btm_qty = ''
        pass

    ld_fb_qty = int(qty) * 2
    ld_sd_qty = int(qty) * 2
    ld_btm_qty = int(qty) * 1

    # BOX DRAWRER X,Y
    if style[0:5] == "BBBBL" or style[0:4] == "BBFL" or style[0:4] == "BBOL":
        bfd_fb_xy = float(width) * 25.4 / 2 - 83
    elif style[0:3] == "BBL":
        bfd_fb_xy = float(width) * 25.4 - 95.12

    ld_fb_xy = float(width) * 25.4 - 95.12

    # BOX DRAWER BOX

    bd_fb = "BOX-DRAWER-FRONT-BACK", "0", "DRAWER-BOX-FRONT-BACK", str(bd_fb_qty), "0", str(bfd_fb_xy), "101.6", \
            "12.7", "S405", "0", "BOX-DRAWER-FRONT-BACK.pgmx \n"
    bd_fb = ";".join(bd_fb)

    bd_sd = "BOX-DRAWER-SIDE", "0", "DRAWER-BOX-SIDE", str(bd_sd_qty), "0", "412.75", "101.6", \
            "12.7", "S405", "0", "BOX-DRAWER-SIDE.pgmx \n"
    bd_sd = ";".join(bd_sd)

    bd_btm = "DRAWER-BOTTOM", "0", "DRAWER-BOTTOM", str(bd_btm_qty), "0", "384.35", str(bfd_fb_xy), \
             "12.7", "S405", "0", "DRAWER-BOTTOM.pgmx \n"
    bd_btm = ";".join(bd_btm)

    # LATERAL DRAWER BOX
    ld_fb = "LATERAL-DRAWER-FRONT-BACK", "0", "DRAWER-BOX-FRONT-BACK", str(ld_fb_qty), "0", str(bfd_fb_xy), "241.3", \
            "12.7", "S405", "0", "LATERAL-DRAWER-FRONT-BACK.pgmx \n"
    ld_fb = ";".join(ld_fb)

    ld_sd = "LATERAL-DRAWER-SIDE", "0", "DRAWER-BOX-SIDE", str(ld_sd_qty), "0", "412.75", "241.3", \
            "12.7", "S405", "0", "LATERAL-DRAWER-SIDE.pgmx \n"
    ld_sd = ";".join(ld_sd)

    ld_btm = "DRAWER-BOTTOM", "0", "DRAWER-BOTTOM", str(ld_btm_qty), "0", "384.35", str(bfd_fb_xy), \
             "12.7", "S405", "0", "DRAWER-BOTTOM.pgmx \n"
    ld_btm = ";".join(ld_btm)

    # FILE DRAWER BOX

    fd_fb = "FILE-DRAWER-FRONT-BACK", "0", "DRAWER-BOX-FRONT-BACK", str(fd_fb_qty), "0", str(ld_fb_xy), "241.3", \
            "12.7", "S405", "0", "FILE-DRAWER-FRONT-BACK.pgmx \n"
    fd_fb = ";".join(fd_fb)

    fd_sd = "FILE-DRAWER-SIDE", "0", "DRAWER-BOX-SIDE", str(fd_sd_qty), "0", "412.75", "241.3", \
            "12.7", "S405", "0", "FILE-DRAWER-SIDE.pgmx \n"
    fd_sd = ";".join(fd_sd)

    fd_btm = "DRAWER-BOTTOM", "0", "DRAWER-BOTTOM", str(fd_btm_qty), "0", "384.35", str(ld_fb_xy), \
             "12.7", "S405", "0", "DRAWER-BOTTOM.pgmx \n"
    fd_btm = ";".join(fd_btm)

    # CSV PRINT LOGIC

    csvParts = leftSide
    csvParts += rightSide
    csvParts += back
    csvParts += stretcher
    csvParts += bottom

    if style == "BBLT" or style == "BBLD" or style == "BBLW":
        pass
    else:
        csvParts += midp
        csvParts += f_shelf

    if style[-1] == "T":
        csvParts += topp

    csvParts += bDoorP
    csvParts += bDoorlP
    if "F" in style:
        csvParts += fDoorlP
    else:
        pass
    csvParts += lDoorlP + "\n"
    csvParts += bd_fb
    csvParts += bd_sd
    csvParts += bd_btm + "\n"

    if style[0:4] == "BBFL":
        csvParts += fd_fb
        csvParts += fd_sd
        csvParts += fd_btm + "\n"

    csvParts += ld_fb
    csvParts += ld_sd
    csvParts += ld_btm + "\n"
    #########################
    # CALC LOGIC ABOVE
    #########################
    return csvParts


if __name__ == "__main__":

    orders = [
        {"model": "MPED-BBL-20-36", "qty": 2, "options": [

            ['Cabinet Top', "W150 White"],
            ['Cabinet Body', "W150 Ash"],
            ['Cabinet Face', "S645 HG"],  # plus $5
        ]},

        # {"model": "BSC-2DBSCT-24-30-72", "qty": 3, "options": [
        #
        #     ['Cabinet Top', "W150 White"],
        #     ['Cabinet Body', "W150 Ash"],
        #     ['Cabinet Face', "S645 HG"],  # plus $5
        # ]},

        # {"model": "BSC-LDBSCT-24-12-72", "qty": 3, "options": [
        #
        #     ['Cabinet Top', "W150 White"],
        #     ['Cabinet Body', "W150 Ash"],
        #     ['Cabinet Face', "S645 HG"],  # plus $5
        # ]},
        #
        # {"model": "BSC-LDBSCT-24-15-72", "qty": 1, "options": [
        #
        #     ['Cabinet Top', "W150 White"],
        #     ['Cabinet Body', "W150 Ash"],
        #     ['Cabinet Face', "S645 HG"],  # plus $5
        # ]},
        #
        # {"model": "BSC-LDBSCT-24-9-72", "qty": 1, "options": [
        #
        #     ['Cabinet Top', "W150 White"],
        #     ['Cabinet Body', "W150 Ash"],
        #     ['Cabinet Face', "S645 HG"],  # plus $5
        # ]},

    ]

    for order in orders:
        result = calc(order["model"], order["qty"], order["options"])

        df = pd.read_csv(StringIO(result), sep=';', header=None)
        print(order["model"], order["qty"])

        print(df.to_string(index=False, header=0), "\n")
