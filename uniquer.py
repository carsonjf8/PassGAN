import time

f4 = open('../51010 samples/new/104.txt', 'rt', encoding='utf8')
f5 = open('../51010 samples/new/105.txt', 'rt', encoding='utf8')
f6 = open('../51010 samples/new/106.txt', 'rt', encoding='utf8')
f7 = open('../51010 samples/new/107.txt', 'rt', encoding='utf8')
f8 = open('../51010 samples/new/108.txt', 'rt', encoding='utf8')
f9 = open('../51010 samples/new/109.txt', 'rt', encoding='utf8')

file_reader_list = [f4, f5, f6, f7, f8, f9]
mag = 4

# iterates through files
for reader in file_reader_list:
    start = time.time()
    
    # read in data
    print('Reading data...')
    data = reader.readlines()
    orig_len = len(data)

    # create sets from data
    print('Creating set...')
    data_set = set(data)
    data_list = list(data_set)
    new_len = len(data_list)

    # write data to out file
    print('Writing to file (' + str(orig_len) + ', ' + str(new_len) + ')...')
    out = open('../51010 samples/new/10' + str(mag) + '_unique.txt', 'wt', encoding='utf8')
    out.writelines(data_list)

    end = time.time()
    print('Done', mag, (end - start))
    print()
    mag += 1
