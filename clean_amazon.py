import csv

with open ('new_amazon.csv' , 'w') as f:
    w = csv.writer(f)
    w.writerow(["Name" , "info" , "price" , "Ratings" , "No. of reviews"])
with open('finalamazon.csv' , 'r',   encoding='utf8') as f:
    reader = list(csv.reader(f))[2:]
    with open ('new_amazon.csv' , 'a' , newline="" ,  encoding='utf8' ) as w:
        write = csv.writer(w)
        f = 0
        for i in reader:
            b = i[0].find("(")
            l = i[0].find("|")
            c = i[0].find(",")
            name = ""
            info = ""


            if b!=-1 and l!=-1 and c!=-1:
                if b < l and b<c:
                    name = i[0][:b]
                    info = i[0][b:]
                    f = f+1
                if l < b and l<c:
                    # print(i[0][:l])
                    name = i[0][:l]
                    info = i[0][l:]
                    f = f+1
                if c < b and c<l:
                    # print(i[0][:c])
                    name = i[0][:c]
                    info = i[0][c:]
                    f = f+1
            elif b!=-1 and l!=-1:
                if b < l:
                    # print(i[0][:b])
                    name = i[0][:b]
                    info = i[0][b:]
                    f = f+1
                if l < b :
                    # print(i[0][:l])
                    name = i[0][:l]
                    info = i[0][l:]
                    f = f+1
            elif b!=-1 and c!=-1:
                if b < c:
                    # print(i[0][:b])
                    name = i[0][:b]
                    info = i[0][b:]
                    f = f+1
                if c < b :
                    # print(i[0][:c])
                    name = i[0][:c]
                    info = i[0][c:]
                    f = f+1
            elif c!=-1 and l!=-1:
                if c < l:
                    # print(i[0][:c])
                    name = i[0][:c]
                    info = i[0][c:]
                    f = f+1
                if l < c :
                    # print(i[0][:l])
                    name = i[0][:l]
                    info = i[0][l:]
                    f = f+1
            elif l!=-1:
                # print(i[0][:l])
                name = i[0][:l]
                info = i[0][l:]
                f = f+1
            elif b!=-1:
                # print(i[0][:b])
                name = i[0][:b]
                info = i[0][b:]
                f = f+1
            elif c!=-1:
                # print(i[0][:c])
                name = i[0][:c]
                info = i[0][c:]
                f = f+1
            else:
                print(i[0])
                name = i[0]
                info = i[0]
                f = f+1
            # print(name , "---------------" , info)
            # print(name)
            # print(info)
            if name != "" and info != "":
                write.writerow([name , info , i[1] , i[2] , i[3]])

print(f)