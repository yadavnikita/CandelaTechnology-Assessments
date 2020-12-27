import csv


outfile = open("trace.txt", 'w')
outfile_1 = open("final.txt",'w')
with open("Stations.csv", 'r') as infile:
    reader = csv.reader(infile, delimiter=',')
    for row in reader:
        EID = row[0]
        cx_time = row[18]
        line = "{},{}\n".format(EID, cx_time)
        outfile.write(line)
outfile.close()

my_file = open("trace.txt", 'r+')
new = my_file.readlines()
rem_backs = list(map(lambda x: x.strip(), new))
again = rem_backs[0]
x_slice = rem_backs[7:17]
l_slice = rem_backs[18:58]
virtual = x_slice + l_slice
mod_1 = [again] + virtual

def sort_list(list1, list2):
    zipped_pairs = zip(list2, list1)
    show = [x for _, x in sorted(zipped_pairs)]
    return show
u_slice = mod_1[1:]
new_slice = mod_1[1:]

for index, item in enumerate(new_slice):
    new_slice[index] = item.split(',')[0]

for index, item in enumerate(u_slice):
    u_slice[index] = int(item.split(",")[1]) / 1000

z_sort = sort_list(new_slice, u_slice)
Output = sorted(u_slice, key=lambda x: float(x))
str_num = ['{:.3f}'.format(x) for x in Output]

for i in range(0,len(z_sort)):
    str_add = z_sort[i] + ',' + str_num[i] +'\n'
    outfile_1.write(str_add)
outfile_1.close()

my_file1 = open("final.txt", 'r+')
n_lines = my_file1.readlines()
z_slice = list(map(lambda x: x.strip(), n_lines))

mod = [again] + z_slice
print(mod)



