# coding=utf-8
__author__ = 'nen'

"""
No padding and e is very small.
Decryption with m**e %n becomes m**e if m**e < n (obviously).

so to decrypt just take eth root of m.
clever algorithm below!

start doubling until you get in range of m, then smart(ass)ly increase and decrease shit!

du chasch au approach oder so!
"""

from binascii import unhexlify

def compute_root(target, e, n):
     """
     takes input as decimal, gives back plaintext ;)
     """
     target, n = int(target), int(n)
     start = 10 # doesnt really matter since you double your stuff! 
#should be above zero though
     last = 0

     while 1:
         if start**e < target:
             last = start
             start *= 2
         elif start**e == target:
             print(start)
             return unhexlify(str(hex(start))[2:])
         else:
             break

     probably_not_root_counter = 0
     while 1:

         if start == last:
             probably_not_root_counter += 1
         if probably_not_root_counter > 10: #dont know if this is right?
             return 0
         if start**e < target:
             tmp = start
             if abs(start-last) == 1:
                 probably_not_root_counter += 1
                 start += 1
                 continue
             start += abs(start-last)//2
             last = tmp
         elif start**e > target:
             tmp = start
             if abs(start-last) == 1:
                 probably_not_root_counter += 1
                 start -= 1
                 continue
             start -= abs(start-last)//2
             last = tmp
         elif start**e == target:
             return unhexlify(str(hex(start))[2:])


n = int(0xb0bfcadbf4df67e2ad21e0ff340a3bb399aa4d19d1e53515a5fedc00832847e27471b1ddba5861255f4c4d76900f1a5ea7a182c64135bbe390f96e97cde8b94f10a8787af7810b5cc7484a7bfab658e2a5e2abfa9b8507007f79fcc47b36ee114986d1b8c7e8d9d039e8ad2561d681282851ce02140c9d6ba7af89029144c84047a41e509fa28e316790b23cffbf9374222c7b96e738d351d222ab3d511328f2ddf692502b79270fa9040ffb1ca670527830c53d9c3756c295d737ba76b3364a3c386921fc23685b9f44752417d3b2dc8b2e74a9606b0b308b2fec37bc442899d1f45c88089fb5dd95e21222bd70d405d4480ded522f713684c7d7fd5829b497)
c = int(0x99dfd0065e16337a0bfc4bc62962fc302612992bd8078d74d819bb915ebfbcf0fe3ac25fa2459f3efc5d2b064f0e8254305b021ed48c014c771e7c2992dfd8eb3dcddf2acfda38e09a1f6bda61eff900079116da12e0cf3170b0fe94c9429e8081a40cc2ccc97add62428c6b58c6c9378a926569276eccaa605aa7ffcc81927305b53e9f3fcc3fde3ac8d7c8b0dd67fcc11274ecef05b27381f229938a034cb7758cc560723ace18b889f7030186a4c0ef7ecd4a13ff306b69237c570e5ec95215515a199dc8c5638e2e97118d754872725fcfd58735cbb231f50bd9653aa322d53e0ccf90e220ca9bb3ed2fc9f2899048eb78410855657f60fda730b9a261c0)

counter = 0
while 1:
     if not compute_root(c+counter*n, 3, 1):
         counter += 1
     else:
         print("else")
         print(compute_root(c + counter * n, 3, 1))
     if not counter%1000:
         print(counter)




#result = compute_root(4096, 3, 9875982798537) #if result:
#    print(result)

