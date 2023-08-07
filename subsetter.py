import time

subsets = [
    10000, # 4
    100000, # 5
    1000000, # 6
    10000000, # 7
    100000000, # 8
    1000000000 # 9
]

f4 = open('../51010 samples/new/104.txt', 'wt', encoding='utf8')
f5 = open('../51010 samples/new/105.txt', 'wt', encoding='utf8')
f6 = open('../51010 samples/new/106.txt', 'wt', encoding='utf8')
f7 = open('../51010 samples/new/107.txt', 'wt', encoding='utf8')
f8 = open('../51010 samples/new/108.txt', 'wt', encoding='utf8')
f9 = open('../51010 samples/new/109.txt', 'wt', encoding='utf8')
file_writer_list = [f4, f5, f6, f7, f8, f9]

f = open('../51010 samples/two_new_samples0.txt', 'rt', encoding='utf8')
count = 0
# iterate through passwords
for line in f:
    # print progress
    if count % 1000000 == 0:
        print(count)
    # iterate through subset files
    for i, s in enumerate(subsets):
        # write to files that it belongs to
        if count < s:
            file_writer_list[i].write(line)
    count += 1
