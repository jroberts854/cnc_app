import requests
import openpyxl
import pandas as pd
import os


from orders.calc import calc
import json
import pprint

url= "https://uloll00m1i.execute-api.ca-central-1.amazonaws.com/master/"
response = requests.get(url)
data = response.json()

# csvparts = {"WORKPIECE": [], "TYPE": [], "DESCRIPTION": [], "QTY": [],"XQTY": [], "X": [], "Y": [], "Z": [], "MATERIAL": [], "GRAIN": [],"FILE": []}


def get_order(order_id):
    response = requests.get(f"{url}/orders/{order_id}")
    order_data = response.json()
    # print(order_data)
    return order_data

order_list = [7530,7529]
order_models = {}
for list_order in order_list:
    order_models[list_order]=[]
    # print(list_order)
    orders = get_order(list_order)
    # print(orders.keys())
    # print(orders["quote"])
    order = orders["quote"]
    orderproducts = order["orderproducts"]
    # pprint.pprint(orderproducts)
    # cnc_order = {}
    cnc_order = []
    for product in orderproducts:
        model = product["model"]
        # print(model)
        qty = product["quantity"]
        options = product["options"]
        # print(model)
        option_codes = []
        for option in options:
            # pprint.pprint(option)
            option_code = option['code']
            option_type = option["option_type"]
            option_codes.append([option_type,option_code])
        # print(model,"-",option_codes)
        # cnc_order[model]=[qty,option_codes]

        cnc_order.append([model,qty,option_codes])

        # print(cnc_order)

    #loop trough cnc order
    # for order_model in cnc_order:
    for order_model in cnc_order:
        # print("order model",order_model)
        model = order_model[0]
        # model = "DESK-RFF-28.5-20.00-72.00-NG-12M"
        # order_model = model
        qty = order_model[1]
        option_codes = order_model[2]

        # print(model,qty,option_codes)
        result_df = calc(model, qty, option_codes)
        order_models[list_order].append([model,result_df])

        # result_str = result_df.to_csv(index=False, sep=';', header=0)
        # cnc_parts = {}

        # print(result_df)
        # print(result)

# print(order_models)

# looping trough order models
print("looping trough order models")
for order_number,value in order_models.items():
    print(order_number)
    print("LENGHT",len(value))
    model = value[0]
    # calcs_df = value[1]
    print(model)
    # print(calcs_df)




        # result.to_excel("CUSTLIST.xlsx")
        # print(result.to_csv(index=False, sep=';', header=0))

        # print(type(result))
        # df = pd.DataFrame(result)
        # print(df)
        # df = df.to_excel("CUTLIST.xlsx")
        # label = f"ORDER {list_order}-{model}"
        # # print(model)
        # # print(result)
        #
