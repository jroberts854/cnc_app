import csv

import pandas as pd
from io import StringIO, BytesIO




def mod_height(mod):
    if float(mod[:-1]) == 12 or float(mod[:-1]) == 28:
        mod_height = float(mod[:-1]) * 25.4 - 12.7
    else:
        mod_height = float(mod[:-1]) * 25.4
    return mod_height

def fm_mod(mod):
    mod_z = 25.4

    if mod[-1] == "A":
        mod_z = 6.4
        mod_name = "DESK-FM-MOD-ACRYLIC"
    elif mod[-1] == "L":
        mod_z = 25.4
        mod_name = "DESK-MOD-LR-LAMINATE"
    return {"mod_z":mod_z,"mod_name":mod_name}



def modesty(model): #NAME
    partType, style,height, depth, width, grommet, mod = model.split('-')

    modesty_spec = {}
    mod_z = 25.4

    if style in ["FMB","FMR"]:
        mod_z = fm_mod(mod)["mod_z"]
        mod_name = fm_mod(mod)["mod_name"]
        mod_x = float(width) * 25.4-609.6
        mod_y = float(mod[:2])*25.4
        mod_qty = 1
    elif partType == "BR":
        mod_name = "DESK-BRIDGE-MOD"
        mod_y = float(width) * 25.4
        mod_x = mod_height(mod)
        mod_qty = 1
    elif partType == "RTN":
        if style[-1] == "R":
            mod_name = "RETURN-MOD-R"
        else:
            mod_name = "RETURN-MOD-L"
        mod_y = float(width) * 25.4 - 27.4
        mod_x = mod_height(mod)
        mod_qty = 1
    elif style == "RCL":
        mod_x = float(width) * 25.4-52.8
        mod_y = mod_height(mod)
        mod_qty = 1
        mod_name = "DESK-MOD-LR"
    elif style == "RCR":
        mod_x = float(depth) * 25.4-52.8
        mod_y = mod_height(mod)
        mod_qty = 1
        mod_name = "DESK-MOD-LR"
    elif style[-2:] == "MS":
        mod_x = mod_x = (float(width) * 25.4 - 80.2) / 2
        mod_y = mod_height(mod)
        mod_qty = 2
        mod_name = "DESK-MOD-LR"
    else:
        mod_name = "DESK-MOD-LR"
        mod_y = mod_height(mod)
        mod_x = float(width) * 25.4 - 54.8
        mod_qty = 1

    modesty_spec["mod_name"] = mod_name
    modesty_spec["mod_x"] = mod_x
    modesty_spec["mod_y"] = mod_y
    modesty_spec["mod_z"] = mod_z
    modesty_spec["mod_qty"] = mod_qty

    return modesty_spec

def gable(model):
    partType, style,height, depth, width, grommet, mod = model.split('-')

    gable_spec = {}
    l_gable_x = float(height) * 25.4-25.4
    r_gable_x = float(height) * 25.4-25.4

    fml_gable_name = "DESK-GABLE-FRONT-LEFT"
    fmr_gable_name = "DESK-GABLE-FRONT-RIGHT"
    fml_gable_y = 457.2
    fmr_gable_y = 457.2

    rcr_panel_name = "DESK-RCR-PANEL-RIGHT"
    rcl_panel_name = "DESK-RCL-PANEL-LEFT"


    #GABLE NAME
    if style == "BF" or style == "RRF":
        l_gable_name = "DESK-GABLE-RF-LEFT"
        r_gable_name = "DESK-GABLE-RF-RIGHT"
    elif style == "FMB" or style == "FMR":
        l_gable_name = "DESK-GABLE-FM-LEFT"
        r_gable_name = "DESK-GABLE-FM-RIGHT"
    else:
        l_gable_name = "DESK-GABLE-FF-LEFT"
        r_gable_name = "DESK-GABLE-FF-RIGHT"

    # GABLE DIMENSIONS
    rc_panel_y = 0
    if style == "BF":
        l_gable_y = float(depth) * 25.4 - 152.4
        r_gable_y = float(depth) * 25.4 - 152.4
    elif style == "ECUL" or style == "WVL":
        l_gable_y = float(depth) * 25.4 - 304.8
        r_gable_y = float(depth) * 25.4
    elif style == "ECUR" or style == "WVR":
        l_gable_y = float(depth) * 25.4
        r_gable_y = float(depth) * 25.4 - 304.8
    elif style == "ECUR" or style == "WVR":
        l_gable_y = float(depth) * 25.4
        r_gable_y = float(depth) * 25.4 - 304.8
    elif style == "ECUR" or style == "WVR":
        l_gable_y = float(depth) * 25.4
        r_gable_y = float(depth) * 25.4 - 304.8
    elif style[:6] == "RFFLHG":
        l_gable_y = 304.8
        r_gable_y = float(depth) * 25.4
    elif style[:6] == "RFFRHG":
        l_gable_y = float(depth) * 25.4
        r_gable_y = 304.8
    elif style[:7] == "RFFLRHG":
        l_gable_y = 304.8
        r_gable_y = 304.8
    elif style in ["FMB","FMR"]:
        l_gable_y = (float(depth)-6) * 25.4
        r_gable_y = (float(depth)-6) * 25.4
    elif style in ["RCR","RCL"]:
        l_gable_y = 304.8
        r_gable_y = 304.8
        rc_panel_y = float(depth) * 25.4-25.4
    else:
        l_gable_y = float(depth) * 25.4
        r_gable_y = float(depth) * 25.4
        rc_panel_y = 0

    # GABLE QUANTITY
    if partType == "DESK":
        l_gable_qty = 1
        r_gable_qty = 1
    elif partType == "RTN":
        if style[-1] == "L":
            l_gable_qty = 1
            r_gable_qty = 0
        else:
            l_gable_qty = 0
            r_gable_qty = 1
    elif partType == "BR":
        l_gable_qty = 0
        r_gable_qty = 0


    gable_spec["l_gable_name"] = l_gable_name
    gable_spec["r_gable_name"] = r_gable_name
    gable_spec["fml_gable_name"] = fml_gable_name
    gable_spec["fmr_gable_name"] = fmr_gable_name

    gable_spec["rcl_panel_name"] =rcl_panel_name
    gable_spec["rcr_panel_name"] =rcr_panel_name

    gable_spec["l_gable_y"] = l_gable_y
    gable_spec["r_gable_y"] = r_gable_y
    gable_spec["fml_gable_y"] = fml_gable_y
    gable_spec["fmr_gable_y"] = fmr_gable_y
    gable_spec["rc_panel_y"] =rc_panel_y


    gable_spec["l_gable_x"] = l_gable_x
    gable_spec["r_gable_x"] = r_gable_x
    gable_spec["fml_gable_x"] = l_gable_x
    gable_spec["fmr_gable_x"] = r_gable_x
    gable_spec["rc_panel_x"] = r_gable_x

    gable_spec["l_gable_qty"] = l_gable_qty
    gable_spec["r_gable_qty"] = r_gable_qty

    if style in ["FMB", "FMR"]:
        gable_spec["fml_gable_qty"] = 1
        gable_spec["fmr_gable_qty"] = 1
    else:
        gable_spec["fml_gable_qty"] = 0
        gable_spec["fmr_gable_qty"] = 0



    if style[-2:] == "MS":
        gable_spec["m_gable_name"] = "DESK-HALF-GABLE"
        gable_spec["m_gable_x"] = l_gable_x
        gable_spec["m_gable_y"] = 304.8
        gable_spec["m_gable_qty"] = 1
    else:
        gable_spec["m_gable_name"] = "DESK-HALF-GABLE"
        gable_spec["m_gable_x"] = l_gable_x
        gable_spec["m_gable_y"] = 304.8
        gable_spec["m_gable_qty"] = 0
    return gable_spec


def calc(model, qty, options):

    csvparts = {"WORKPIECE": [], "TYPE": [], "DESCRIPTION": [], "QTY": [],"XQTY": [], "X": [], "Y": [], "Z": [], "MATERIAL": [], "GRAIN": [],"FILE": []}
###### OPTIONS ########
    top_lam = "TBD"
    gbl_lam = "TBD"
    mod_lam = "TBD"

    for row in options:
        optionName = row[0]
        if optionName == 'Desk Top':
            top_lam = row[1].split(" ")
            top_lam = top_lam[0]
        if optionName == 'Desk Gable':
            gbl_lam = row[1].split(" ")
            gbl_lam = gbl_lam[0]
        if optionName == 'Desk Modesty':
            mod_lam = row[1].split(" ")
            mod_lam = mod_lam[0]

####### CALC LOGIC #######
    partType, style, height, depth, width, grommet, mod = model.split('-')

    #TOP INFO
    if style[-2:]=="MS":
        top_name = f'{partType}-{style[:-2]}-{grommet}-{"TOP"}'
    else:
        top_name = f'{partType}-{style}-{grommet}-{"TOP"}'

    if partType == "RTN" or partType == "BR":
        top_x = float(depth) * 25.4
        top_y = float(width) * 25.4
        if style[0] == "W":
            top_x = float(depth) * 25.4 -2
            top_y = float(width) * 25.4
    else:
        top_x = float(width) * 25.4
        top_y = float(depth) * 25.4
    top_qty = qty * 1

    #MOD INFO
    mod_name = modesty(model)["mod_name"]
    mod_x = modesty(model)["mod_x"]
    mod_y = modesty(model)["mod_y"]
    mod_z = modesty(model)["mod_z"]
    mod_qty = qty * modesty(model)["mod_qty"]

    #GABLE INFO
    fml_gable_name = gable(model)['fml_gable_name']
    fmr_gable_name = gable(model)['fmr_gable_name']
    fml_gable_x = gable(model)['fml_gable_x']
    fml_gable_y = gable(model)['fml_gable_y']
    fmr_gable_x = gable(model)['fmr_gable_x']
    fmr_gable_y = gable(model)['fmr_gable_y']
    fml_gable_qty = qty * gable(model)['fml_gable_qty']
    fmr_gable_qty = qty * gable(model)['fmr_gable_qty']

    if style == "RCL":
        rc_panel_name = gable(model)['rcl_panel_name']
        rc_panel_qty = qty * 1
    elif style == "RCR":
        rc_panel_name = gable(model)['rcr_panel_name']
        rc_panel_qty = qty * 1
    else:
        rc_panel_name = ""
        rc_panel_qty = 0
    rc_panel_x = gable(model)['rc_panel_x']
    rc_panel_y = gable(model)['rc_panel_y']


    l_gable_name = gable(model)['l_gable_name']
    l_gable_x = gable(model)['l_gable_x']
    l_gable_y = gable(model)['l_gable_y']
    l_gable_qty = qty * gable(model)['l_gable_qty']

    r_gable_name = gable(model)['r_gable_name']
    r_gable_x = gable(model)['r_gable_x']
    r_gable_y = gable(model)['r_gable_y']
    r_gable_qty = qty * gable(model)['r_gable_qty']

    m_gable_name = gable(model)['m_gable_name']
    m_gable_x = gable(model)['m_gable_x']
    m_gable_y = gable(model)['m_gable_y']
    m_gable_qty =qty * gable(model)['m_gable_qty']

    wpn_list  = [top_name,mod_name,rc_panel_name,fml_gable_name,fmr_gable_name,l_gable_name,r_gable_name,m_gable_name]
    type_list = [0,0,0,0,0,0,0,0]
    qty_list  = [top_qty,mod_qty,rc_panel_qty,fml_gable_qty,fmr_gable_qty,l_gable_qty,r_gable_qty,m_gable_qty]
    xqty_list = [0,0,0,0,0,0,0,0]
    x_list = [top_x,mod_x,rc_panel_x,fml_gable_x,fmr_gable_x,l_gable_x,r_gable_x,m_gable_x]
    y_list = [top_y,mod_y,rc_panel_y,fml_gable_y,fmr_gable_y,l_gable_y,r_gable_y,m_gable_y]
    z_list = [25.4,mod_z,25.4,25.4,25.4,25.4,25.4,25.4]
    material_list = [top_lam,mod_lam,gbl_lam,gbl_lam,gbl_lam,gbl_lam,gbl_lam,gbl_lam]
    grain_list = [0,0,0,0,0,0,0,0]
    file=[]
    for name in wpn_list:
        file.append(name +".pgmx")

    csvparts["WORKPIECE"] = wpn_list
    csvparts["TYPE"] = type_list
    csvparts["DESCRIPTION"] = wpn_list
    csvparts["QTY"] = qty_list
    csvparts["XQTY"] = xqty_list
    csvparts["X"] = x_list
    csvparts["Y"] = y_list
    csvparts["Z"] = z_list
    csvparts["MATERIAL"] = material_list
    csvparts["GRAIN"] = grain_list
    csvparts["FILE"] = file

    df = pd.DataFrame(data=csvparts)
    df_filter = df["QTY"] != 0
    df = df[df_filter]


    # print(df)
    # df.to_excel("test_cutlist.xlsx")
    result = df.to_csv(index=False, sep=';', header=0)
    return result


if __name__ == "__main__":
    options = [
        ['Top Laminate', "W155 ash"],
        ['Modesty Laminate', "S645 ash"],
        ['Gable Laminate', "W150 ash"],

    ]

#     models = [
#         ["DESK-BF-28.5-36-72-CG-12M", 1],
#         # ["DESK-RRF-28.5-30-72-CG-12M",1],
#         # ["DESK-RFF-28.5-30-72-CG-12M",1],
#         # ["DESK-RFFMS-28.5-30-72-CG-12M",1],
#         #
#         # ["DESK-RFFLHG-28.5-24-72.00-NG-18M", 1],
#         # ["DESK-RFFRHG-28.5-24-72.00-NG-18M", 1],
#         # ["DESK-RFFLRHG-28.5-36.00-72.00-NG-18M", 1],
#
#         # ["DESK-RFFLHGMS-28.5-24-72.00-NG-18M", 1],
#         # ["DESK-RFFRHGMS-28.5-24-72.00-NG-18M", 1],
#         # ["DESK-RFFLRHGMS-28.5-36.00-72.00-NG-18M", 1],
#         #
#         # ["DESK-ECUL-28.5-36.00-72.00-NG-18M",1],
#         # ["DESK-ECUR-28.5-36.00-72.00-NG-18M",1],
#         # ["DESK-WVL-28.5-36.00-72.00-NG-18M",1],
#         # ["DESK-WVR-28.5-36.00-72.00-NG-18M",1],
#         # ["DESK-RCL-28.5-36.00-72.00-NG-18M",1],
#         # ["DESK-RCR-28.5-36.00-72.00-NG-18M",1],
#
#         # ["DESK-FMB-28.5-36.00-72.00-NG-16MA",1],
#         # ["DESK-FMB-28.5-36.00-72.00-NG-16ML",1],
#         # ["DESK-FMR-28.5-36.00-72.00-NG-16MA",1],
#         # ["DESK-FMR-28.5-36.00-72.00-NG-16ML",1],
#
#         # ["BR-RB-28.5-24-48-NG-18M",1],
#         # ["BR-WBR-28.5-24-48-NG-18M",1],
#         # ["BR-WBL-28.5-24-48-NG-18M",1],
#         # ["BR-BML-28.5-24-48-NG-18M",1],
#         # ["BR-BMR-28.5-24-48-NG-18M",1],
#         #
#         # ["RTN-WL-28.5-24-48-NG-18M", 1],
#         # ["RTN-WR-28.5-24-48-NG-18M", 1],
#         # ["RTN-BML-28.5-24-48-NG-18M", 1],
#         # ["RTN-BMR-28.5-24-48-NG-18M", 1],
#         # ["RTN-RR-28.5-24-48-NG-18M", 1],
#
#     ]
#     desk_styles = {  # grommet,depth,width,modesty,
#         "DESK-RFF": [["LRG", ], [24], [72]],
#         "DESK-RFFMS": [["LRG", ], [24], [72]],
#         "DESK-RRF": [["LRG"], [30], [72]],
#         "DESK-BF": [["LRG"], [42], [72]],
#         "DESK-RFFLHG": [["LRG"], [24], [72]],
#         "DESK-RFFRHG": [["LRG"], [24], [72]],
#         "DESK-RFFLRHG": [["LRG"], [24], [72]],
#         "DESK-RFFLHGMS": [["LRG"], [24], [72]],
#         "DESK-RFFRHGMS": [["LRG"], [24], [72]],
#         "DESK-RFFLRHGMS": [["LRG"], [24], [72]],
#         "DESK-ECUL": [["COG"], [36], [72]],
#         "DESK-ECUR": [["COG"], [36], [72]],
#         "DESK-WVL": [["COG"], [36], [72]],
#         "DESK-WVR": [["COG"], [36], [72]],
#         "DESK-ECULMS": [["COG"], [36], [72]],
#         "DESK-ECURMS": [["COG"], [36], [72]],
#         "DESK-WVLMS": [["COG"], [36], [72]],
#         "DESK-WVRMS": [["COG"], [36], [72]],
#         "DESK-RCL": [["COG"], [36], [36]],
#         "DESK-RCR": [["COG"], [36], [60]],
#         "DESK-FMR": [["LRG"], [30], [72]],
#         "DESK-FMB": [["LRG"], [30], [72]],
#
#         "BR-RB": [["CG" ], [24],[48]],
#         "BR-WBR": [["CG" ], [24],[48]],
#         "BR-WBL": [["CG" ], [24],[48]],
#         "BR-BML": [["CG" ], [24],[48]],
#         "BR-BMR": [["CG" ], [24],[48]],
#
#         "RTN-WL": [["CG"], [24], [48]],
#         "RTN-WR": [["CG"], [24], [48]],
#         "RTN-BMR": [["CG"], [24], [48]],
#         "RTN-BML": [["CG"], [24], [48]],
#         "RTN-RR": [["CG"], [24], [48]],
#         "RTN-RL": [["CG"], [24], [48]],
#
#     }
#
#     models = []
#
#     mods = ["12M","18M","28M",]
#     fm_mods = ["16MA","16ML"]
#     for style, data in desk_styles.items():
#         for grommet in data[0]:
#             for depth in data[1]:
#                 for width in data[2]:
#                     if style in ['DESK-FMB', 'DESK-FMR']:
#                         for mod in fm_mods:
#                             model = f'{style}-{28.5}-{depth}-{width}-{grommet}-{mod}'
#                             models.append(model)
#                     else:
#                         for mod in mods:
#                             model = f'{style}-{28.5}-{depth}-{width}-{grommet}-{mod}'
#                             models.append(model)
#                     # print(models)
#     c = 0
#     # print(models)
#     for model in models:
#         # result = calc(model[0], model[1], options)
#         result = calc(model, 1, options)
#         # print(result.to_csv())
# #
# #         # parts = parts_list(model[0], 1, options,model[1])
# #         # hardware_list = hardware(model[0], 1)
# #
#         df = pd.read_csv(StringIO(result), sep=';', header=None)
#         # df1 = pd.DataFrame(hardware_list)
#         print(df)
# #         # print(order["model"], order["qty"])
# #         # print(model)
# #         print(df.to_string(index=False, header=0), "\n")
# #         c +=1
# # # print(models)
#     # print(df1.to_string(index=False), "\n")
