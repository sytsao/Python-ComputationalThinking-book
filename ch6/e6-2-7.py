#e6-2-7  csv 檔讀取與寫入
import csv
with open('data6.csv','r') as fin:
    with open('data6_out.csv','w') as fout:
        csvreader = csv.reader(fin, delimiter=',')
        csvwriter = csv.writer(fout, delimiter=',')
        header = next(csvreader)
        print(header)
        csvwriter.writerow(header)
        for row in csvreader:
            row[6] = row[6].replace('/','-')
            print(','.join(row))
            csvwriter.writerow(row)
