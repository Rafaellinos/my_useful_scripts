import csv
import sys

print("""
    Digite o arquivo para editar
""")
inputfile = sys.argv[1]
outcsv = inputfile[:-4]+"_edited.csv"
print(f"""
Arquivo input > {inputfile}
Arquivo output > {outcsv}
""")
csv_ = []
with open(inputfile, 'r', newline='') as f:
    reader = csv.reader(f)

    for row in reader:
        csv_.append(row)

# print(csv_)
    
with open(outcsv, 'w', newline='') as f1:
    writter = csv.writer(f1, delimiter=',')
    for i, row in enumerate(csv_):
        if i == 0:
            writter.writerow(['SM ID','Fase','Título da Tarefa','Descrição','Prioridade'])
            continue
        writter.writerow([row[3],row[6],row[3]+"-"+row[4],row[0]+"-"+row[1]+"-"+row[3]+"\n"+row[4],row[7]])
    

    # csv_writter.writerow([email,subject, message])
