import xlwings as xw
import shutil


def reform(string):
    line = string.split("\n")
    name_list = []
    for ele in line:
        pre_name = ele.split(".")[1].split("1")[0]
        name_list.append(pre_name.replace(" ", ""))
    # print(name_list)
    return name_list


def excel(colum, content):
    """ 目前姓名要排在第B列 """
    shutil.copy("origin", "")

    app = xw.App(visible=True, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    wb = app.books.open('人员花名册.xlsx')

    sheet1 = wb.sheets["sheet1"]

    name_list = reform()
    print(name_list)
    for i in range(1, 83):
        i_name = "B" + str(i)
        if sheet1.range(i_name).value in name_list:
            print(sheet1.range(i_name).value)
            sheet1.range(colum + str(i)).value = content

    wb.save()
    wb.close()
    app.quit()
