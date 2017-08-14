#e6-2-8使用 xlrd/xlwt 讀寫 excel 檔案
import xlrd
import xlwt
L1=[]
data=xlrd.open_workbook('data7.xls')
table=data.sheets()[0]
print('表格內共有 %d 列' %(table.nrows))
print('表格內共有 %d 行' %(table.ncols))
print('原始資料內容 =')
for i in range(0,table.nrows):
    sum=0
    L2=[]
    for j in range(0,table.ncols):
        print(table.cell(i,j).value)
        sum+= table.cell(i,j).value
        L2.append(table.cell(i,j).value)
    L2.append(sum)
    L1.append(L2).
wb = xlwt.Workbook()
ws = wb.add_sheet('成績計算')
for i in range(0,table.nrows):
    for j in range(0,table.ncols+1):
        ws.write(i, j, L1[i][j])
wb.save('data7_out.xls')
