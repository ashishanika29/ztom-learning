# -* coding: utf=8 -*-

"""
Encoding and Decoding UTF-8 & ASCII

"""
alphaNumberic37_encoding = {0: 'Undefined', 1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 
                            10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S',
                            20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z', 27: '0', 28: '1', 29:'2',
                            30: '3', 31: '4', 32: '5', 33: '6', 34: '7', 35: '8', 36: '9'}


alphaNumberic37_decoding = {'Undefined': 0, 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
                            'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19,
                            'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26, '0': 27, '1': 28, '2': 29,
                            '3': 30, '4': 31, '5': 32, '6': 33, '7': 34, '8': 35, '9': 36 }

month_0_11_encoding = {0:'M', 1:'N', 2:'O', 3:'P', 4:'Q', 5:'R', 6:'S', 7:'T', 8:'U', 9:'V', 10:'W', 11:'X'}

month_0_11_decoding = {'M': 0,'N': 1, 'O': 2, 'P': 3, 'Q': 4, 'R': 5, 'S': 6, 'T': 7, 'U': 8,'V': 9, 'W': 10, 'X': 11}

#convert PPIN (Protected Processor Identification Number) to Serial Number
def ppin_to_sn(my_ppin):
    #find mark lot number , convert string to hex
    my_ppin_hex_str = '0x' + my_ppin
    my_ppin = int(my_ppin_hex_str,16)
    mark_lot_number = my_ppin >> 21 & 0x3FFFFFFFFFF
    my_sn = ''
    while (mark_lot_number % 37):
        my_sn = alphaNumberic37_encoding[mark_lot_number %37] + my_sn
        mark_lot_number = mark_lot_number // 37
    
    #find Month Year
    month_year_mark = my_ppin >> 14 & 0x7F
    month = month_year_mark // 10
    month = month_0_11_encoding[month]
    year = month_year_mark % 10

    #find dev_num mark
    dev_number = my_ppin & 0x3FFF
    my_sn = my_sn + str(month) + str(year) + str(dev_number).zfill(4)
    return my_sn

#convert Serial Number to PPIN (Protected Processor Identification Number)
def sn_to_ppin(my_sn):
    my_ppin = 0
    #find lot number & mark ppin
    for index in range(0,7):
        my_ppin = my_ppin*37
        my_ppin = my_ppin + alphaNumberic37_decoding[my_sn[index]] 
    
    #find month year and mark ppin
    month_year_mark = int(month_0_11_decoding[my_sn[7]])*10 + int(my_sn[8])
    my_ppin = my_ppin << 7
    my_ppin = my_ppin + month_year_mark
    
    #find Dev # PPIN
    dev_num = 0
    for idx in range (9,13):
        dev_num = dev_num *10
        dev_num = dev_num + int(my_sn[idx])

    my_ppin = my_ppin << 14
    my_ppin = my_ppin + dev_num
    
    return str(format(my_ppin, 'X')).zfill(16)
   

print('Press 1 for SN -> PPIN, 2 for PPIN-->SN ')
choice = input()

read_file = open("C:\\aAFamily\\1-Ashish\\Python\\ztom learning\\InfoSec\\inputSN.txt","r")
write_file = open("C:\\aAFamily\\1-Ashish\\Python\\ztom learning\\InfoSec\\outputPPIN.txt","w")

if choice == '1':
    pass
elif choice == '2':
    read_file.close()
    write_file.close()
    read_file = open("C:\\aAFamily\\1-Ashish\\Python\\ztom learning\\InfoSec\\inputPPIN.txt", "r")
    write_file = open("C:\\aAFamily\\1-Ashish\\Python\\ztom learning\\InfoSec\\outputSN.txt", "w")
else:
    print(choice)
    print(' is a wrong choice')
    exit(1)

while (True):
    line = read_file.readline()
    if not line:
        break
    if len(line.strip()) == 13 or len(line.strip()) == 16 :
        if choice == '1':
            write_file.write(sn_to_ppin(line.strip()))
        elif choice == '2':
            write_file.write(ppin_to_sn(line.strip()))
        write_file.write('\n')
    else:
        write_file.write('Invalid SN or PPIN')

read_file.close()
write_file.close()

print('Conversion done succefully')