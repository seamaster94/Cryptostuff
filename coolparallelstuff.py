# coding=utf-8
__author__ = 'nen'


import glob
from fractions import gcd
import threading

def coolstuff(n, huge_list, counter):
    for thingy in huge_list[counter:]:
        if n == thingy:
            continue
        gcdresult = gcd(thingy, n)
        if gcdresult != 1:
            print(gcdresult, n, thingy)

    print('Thread ended['+str(counter)+"]")

huge_list = list()
i = 1
for file in glob.glob("files/*"):
    with open(file) as foo:
        output = foo.read()
    # ugly stuff
    output = output.split("encrypted")[0][2:]
    huge_list.append(int(output))


##########################################################
# I'VE GOT MY COOL FILES!
count = 0
threads = []
for counter, n in enumerate(huge_list):

    thread = threading.Thread(target=coolstuff, args=(n, huge_list, counter))
    threads += [thread]

print(threads)
for x in threads:
    x.start()
    print(str(count + 1) + "/" + str(len(huge_list)))
    count += 1
for x in threads:
    x.join()
print("finished")

#import time
#time.sleep(100000)

