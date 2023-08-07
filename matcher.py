import time

gen_files = [
    '../51010 samples/new/104_unique.txt',
    '../51010 samples/new/105_unique.txt',
    '../51010 samples/new/106_unique.txt',
    '../51010 samples/new/107_unique.txt',
    '../51010 samples/new/108_unique.txt',
    '../51010 samples/new/tmp_0123456789_unique.txt',
]
test_file = '../51010 samples/test_rock_you.txt'

test_f = open(test_file, 'rt', encoding='utf8')
test_data = test_f.readlines()
print('len(test_data)', len(test_data))

# iterate through generated password files
for file in gen_files:
    start = time.time()
    matches = 0
    total = 0
    gen_f = open(file, 'rt', encoding='utf8')
    print('loading data')
    gen_data = gen_f.readlines()
    print('data loaded')

    # count password matches between files
    count = 0
    for gd in gen_data:
        if count % 10000000 == 0:
            print(count)
        count += 1
        gd = (gd[:-1]).replace("`", "")
        #print(gd)
        if gd in test_f:
            matches += 1
        total += 1
    gen_f.close()
    end = time.time()
    print(file, matches, total, (end - start))

test_f.close()
print('Done')