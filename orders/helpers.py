from os.path import exists
import pandas as pd
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

# ip_file_name = r'C:\Users\jrobe\OneDrive - THE FURNITURE GUYS\TFG OFFICE\PRODUCTION\CUT LIST\TEST-CODE\MAY-TEST.xlsx'
# parts_folder = r'C:\Users\jrobe\OneDrive - THE FURNITURE GUYS\TFG OFFICE\PRODUCTION\PRODUCTION-2019\CNC PARTS'
def make_fail_excel(fail_list,fail_file_name):
    df = pd.DataFrame(fail_list, columns=['File Names'])  # Create a DataFrame from the list
    df.to_excel(fail_file_name,'.xlsx', index=False)



def file_checker(excel_file,parts_folder):


    cutlist_df = pd.read_excel(excel_file,sheet_name="CUTLIST") #pandas.read_excel('records.xlsx', sheet_name='Employees')
    cutlist_df = cutlist_df.dropna(subset=["FILE"])

    # print(cutlist_df)
    filename_list = []
    # for file in cutlist_df["WORKPEICE NAME"]:
    for file in cutlist_df["FILE"]:
        filename_list.append(file)
    # folder = r'C:\Users\jrobe\OneDrive - THE FURNITURE GUYS\TFG OFFICE\PRODUCTION\PRODUCTION-2019\CNC PARTS'
    t = 0
    f = 0
    # needs = cb_list
    fails = []
    for file in filename_list:
        file = file.strip("\n")
        # print(file)
        lookup = f'{parts_folder}\{file}'
        if exists(lookup)==True:
            Passes = True
            t += 1
            # print("pass" , Passes)
        else:
            # fails = False
            fails.append(file)

            f += 1
    # print("fails" , fails,file)
    return fails

# fail = file_checker(excel_file,parts_folder)
# print(fail)


def make_csv(ip_file_name,op_file_folder):
    cutlist_df = pd.read_excel(ip_file_name,sheet_name="CUTLIST")
    cutlist_df = cutlist_df.drop('ORDER_NUM', axis=1)

    print(cutlist_df)
    for group, data in cutlist_df.groupby(['Z', 'MATERIAL']):
        cutlist = ip_file_name.split("\\")[-1].split("-")[:2]

        #contained NaN
        data = data[~data['TYPE'].isnull()]
        data = data[~data['GRAIN'].isnull()]
        data = data[~data['QTY'].isnull()]
        data = data[~data['XQTY'].isnull()]


       # convert float to int
        data[['TYPE']] = data[['TYPE']].astype(int)
        data[['GRAIN']] = data[['GRAIN']].astype(int)
        data[['QTY']] = data[['QTY']].astype(int)
        data[['XQTY']] = data[['XQTY']].astype(int)



        x = int(group[0])
        mat = group[1]
        # file_name = '{}-{}-{}'.format("-".join(cutlist), mat, x)
        file_name = '{}-{}'.format(mat, x)


        folder = r'C:\Users\jrobe\OneDrive - THE FURNITURE GUYS\TFG OFFICE\PRODUCTION\PRODUCTION-2019\CNC PARTS\TEST/'.replace(
            '\\', '/')

        # folder = r'C:\Users\jrobe\OneDrive - THE FURNITURE GUYS\TFG OFFICE\PRODUCTION\PRODUCTION-2019\CNC PARTS\TEST'


        # print("{}{}.csv".format(folder, file_name))
        print("hc folder",folder)
        print("gui folder",op_file_folder)
        # print("file_name",file_name)

        data.to_csv("{}{}.csv".format(op_file_folder, file_name), sep=';', index=False,header=False)


csv_file = r'C:\Users\jrobe\OneDrive - THE FURNITURE GUYS\TFG OFFICE\PRODUCTION\PRODUCTION-2019\CNC PARTS\TEST\AA60-19.csv'

def csv_to_calc_sheets(csv_file):
    csv_df = pd.read_csv(csv_file,sep=";")

    csv_df = csv_df.drop(csv_df.columns[[0, 1, 2,4,9,10]], axis=1)
    csv_df = csv_df.dropna()


    print(csv_df.values)

    # qty = csv_df.iloc[:, 3]
    # x = csv_df.iloc[:, 5]
    # y = csv_df.iloc[:, 6]
    # mat = csv_df.iloc[:, 8]
    # thickness = csv_df.iloc[:, 7]
    # sheet = f'{mat}-{thickness}'
    #
    # parts = [qty,x.value,y.value,sheet.value]
    # print(parts)

    # print(qty)
    # print(x)
    # print(y)
    # print(sheet)


    # print(cutlist_df)
    # for group, data in cutlist_df.groupby(['Z', 'MATERIAL']):
    #     sheets = csv_file.split("\\")[-1].split("-")[:2]

    # contained NaN
    # data = data[~data['TYPE'].isnull()]
    # data = data[~data['GRAIN'].isnull()]
    # data = data[~data['QTY'].isnull()]
    # data = data[~data['XQTY'].isnull()]
    #
    # # convert float to int
    # data[['TYPE']] = data[['TYPE']].astype(int)
    # data[['GRAIN']] = data[['GRAIN']].astype(int)
    # data[['QTY']] = data[['QTY']].astype(int)
    # data[['XQTY']] = data[['XQTY']].astype(int)

    # x = int(group[0])
    # mat = group[1]
    # file_name = '{}-{}-{}'.format("-".join(cutlist), mat, x)
    # file_name = '{}-{}'.format(mat, x)

csv_to_calc_sheets(csv_file)
