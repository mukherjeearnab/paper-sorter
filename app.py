import readermodel
import os
from shutil import copyfile

# print(readermodel.showClass('test.pdf'));
s_path = './Papers'
p_path = './SortedPapers'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.txt' in file:
            files.append(os.path.join(r, file))

index = 0
for file in files:
    print(f)
    try:
        Class = readermodel.showClass(file)
        copyfile(file, p_path + '/' + Class + '/' + str(index) + '.pdf')
        print(index, Class)
    except Exception as e:
        print(e)
print('DONE')
