import pandas as pd
from io import StringIO


def calc(model, qty, options):

    # Order-Wide Options

    toplaminate = "TBD"

    for row in options:
        # Possible database col names:
        # Acrylic, Base Laminate, Body Laminate, Bottom Fabric, Cabinet Base, Cabinet Body, Cabinet Face, Cabinet Top, Fabric, Face Laminate, Laminate, Metal, Top Fabric, Top Laminate
        if row[0] == 'Top top':
            toplaminate = row[1].split(" ")
            toplaminate = toplaminate[0]

    # Product Level Options

    for row in options:
        optionName = row[0]
        if optionName == 'Top Laminate':
            toplaminate = row[1].split(" ")
            toplaminate = toplaminate[0]

    #########################
    # CALC LOGIC BELLOW
    #########################
    # partType, style, depth, width = model.split('-')
    partType, style, grommet,section,depth, width = model.split('-')

    y = float(depth) * 25.4

    if style == "ELIPSE":
        if float(width) > 108 and float(width) <= 150:
            x = float(width) * 25.4 / 2
            y_2 = "NONE"
            y_3 = float(depth) * 25.4
            wpn = partType + "-" + style + "-TOP" + "-LEFT"
            wpn2 = "NONE"
            wpn3 = partType + "-" + style + "-TOP" + "-RIGHT"

        elif float(width) > 150:
            x = float(width) * 25.4 / 3
            y_2 = float(depth) * 25.4
            y_3 = float(depth) * 25.4
            wpn = partType + "-" + style + "-TOP" + "-LEFT"
            wpn2 = "TT-REC-TOP"
            wpn3 = partType + "-" + style + "-TOP" + "-RIGHT"

        else:
            x = float(width) * 25.4
            y_2 = "NONE"
            y_3 = "NONE"
            wpn = partType + "-" + style + "-TOP"
            wpn2 = "NONE"
            wpn3 = "NONE"

    elif style == "TRAPIZIOD":
        if float(width) > 108 and float(width) < 222:
            if float(depth) >= 60:
                x = float(width) * 25.4 / 2
                y_2 = "NONE"
                y_3 = float(depth) * 25.4 - 304.8
                wpn = partType + "-" + style + "-TOP" + "-LEFT" + "-DOUBLE-D60"
                wpn2 = "NONE"
                wpn3 = partType + "-" + style + "-TOP" + "-RIGHT" + "-DOUBLE-D60"
            else:
                x = float(width) * 25.4 / 2
                y_2 = "NONE"
                y_3 = float(depth) * 25.4 - 152.4
                wpn = partType + "-" + style + "-TOP" + "-LEFT" + "-DOUBLE"
                wpn2 = "NONE"
                wpn3 = partType + "-" + style + "-TOP" + "-RIGHT" + "-DOUBLE"


        elif float(width) >= 222:
            if float(depth) >= 60:
                x = float(width) * 25.4 / 3
                y_2 = float(depth) * 25.4 - 203.2
                y_3 = float(depth) * 25.4 - 406.4
                wpn = partType + "-" + style + "-TOP" + "-LEFT" + "-TRIPLE-D60"
                wpn2 = partType + "-" + style + "-TOP" + "-MID" + "-TRIPLE-D60"
                wpn3 = partType + "-" + style + "-TOP" + "-RIGHT" + "-TRIPLE-D60"
            else:
                x = float(width) * 25.4 / 3
                y_2 = float(depth) * 25.4 - 101.6
                y_3 = float(depth) * 25.4 - 203.2
                wpn = partType + "-" + style + "-TOP" + "-LEFT" + "-TRIPLE"
                wpn2 = partType + "-" + style + "-TOP" + "-MID" + "-TRIPLE"
                wpn3 = partType + "-" + style + "-TOP" + "-RIGHT" + "-TRIPLE"


        else:
            x = float(width) * 25.4
            y_2 = "NONE"
            y_3 = "NONE"
            wpn = partType + "-" + style + "-TOP" + "-SINGLE"
            wpn2 = "NONE"
            wpn3 = "NONE"


    else:
        if float(width) > 108 and float(width) < 222:
            x = float(width) * 25.4 / 2
            y_2 = "NONE"
            y_3 = float(depth) * 25.4
            wpn = partType + "-" + style + "-TOP" + "-LEFT"
            wpn2 = "NONE"
            wpn3 = partType + "-" + style + "-TOP" + "-RIGHT"

        elif float(width) >= 222:
            x = float(width) * 25.4 / 3
            y_2 = float(depth) * 25.4
            y_3 = float(depth) * 25.4
            wpn = partType + "-" + style + "-TOP" + "-LEFT"
            wpn2 = "TT-REC-TOP"
            wpn3 = partType + "-" + style + "-TOP" + "-RIGHT"

        else:
            x = float(width) * 25.4
            y_2 = "NONE"
            y_3 = "NONE"
            wpn = partType + "-" + style + "-TOP"
            wpn2 = "NONE"
            wpn3 = "NONE"

    # PART 1
    part = wpn, "0", "TABLE-TOP", str(qty), "0", str(x), \
           str(y), "25.4", toplaminate, "0", wpn + ".pgmx\n"
    part = ";".join(part)

    # PART 2
    part2 = wpn2, "0", "TABLE-TOP", str(qty), "0", str(x), \
            str(y_2), "25.4", toplaminate, "0", wpn2 + ".pgmx\n"
    part2 = ";".join(part2)

    # PART 3
    part3 = wpn3, "0", "TABLE-TOP", str(qty), "0", str(x), \
            str(y_3), "25.4", toplaminate, "0", wpn3 + ".pgmx\n"
    part3 = ";".join(part3)

    # CSV PRINT LOGIC

    csvParts = part

    if style == "ELIPSE":
        if float(width) > 108 and float(width) <= 150:
            csvParts += part3
        elif float(width) > 150:
            csvParts += part2
            csvParts += part3

    else:
        if float(width) > 108 and float(width) < 222:
            csvParts += part3

        elif float(width) >= 222:
            csvParts += part2
            csvParts += part3

    csvParts += '\n'
    #########################
    # CALC LOGIC ABOVE
    #########################
    return csvParts


if __name__ == "__main__":


    orders = [
        {"model": "TT-ARK-36-72", "qty": 1, "options": [
        ['Top Laminate', "S645 Maple"],

    ]},


    ]

    for order in orders:
        result = calc(order["model"], order["qty"], order["options"])


        df = pd.read_csv(StringIO(result), sep=';', header=None)
        print(order["model"],order["qty"])

        print(df.to_string(index=False, header=0),"\n")




    # import sys
    #
    # script = sys.argv.pop(0)
    # if sys.argv:
    #     print(calc(sys.argv[0], 1, []))
    # else:
    #     print("Usage: python3 {} MODEL-NAME-18-30".format(script))
