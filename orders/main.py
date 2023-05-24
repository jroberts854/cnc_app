import pprint

from orders.api import get_products,get_cnc_calc,orders_to_xslx
from orders.helpers import file_checker

# excel_file = r'C:\Users\jrobe\OneDrive - THE FURNITURE GUYS\TFG OFFICE\PRODUCTION\CUT LIST\TEST-CODE\MAY-TEST.xlsx'
# parts_folder_name = r'C:\Users\jrobe\OneDrive - THE FURNITURE GUYS\TFG OFFICE\PRODUCTION\PRODUCTION-2019\CNC PARTS'

def run(order_list,cutlist_filename):
    print("running order",order_list)
    cutlist ={}
    for order in order_list:
        print("processing order",order)
        product_data = get_products(order)
        cnc_data = get_cnc_calc(product_data)
        cutlist[order] = cnc_data

        # result = cnc_calc(order_data(order))
    # pprint.pprint(cutlist)
    orders_to_xslx(cutlist, cutlist_filename)







if __name__ == '__main__':
    order_list = [
        7549,
        7522,
        # 7538,
        # 7520,
        # 7534,
        # 7540,
        # 7499,
        # 7531,
        # 7532,
            ]
    run(order_list)



