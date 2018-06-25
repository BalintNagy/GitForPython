# Create a method that decrypts texts/reversed_zen_order.txt
# Write the files content into a new file called decrypt3_yyyymmmdd.txt
# Give yyyymmdd the current date with the given format

def crypto_3revorder(file_name):
    import datetime
    f = open(file_name, 'r')
    f2 = open('texts/decrypt3_' + datetime.datetime.now().strftime('%Y%m%d') + '.txt', 'w')
    raw_rows = f.readlines()
    for i in range(0, len(raw_rows)):
        decrypted_row = raw_rows[len(raw_rows) - i - 1]
        if decrypted_row[len(decrypted_row)-1] != '\n':
            decrypted_row += '\n'
        f2.write(decrypted_row)
    f.close()
    f2.close()

#crypto_3revorder('texts/reversed_zen_order.txt')

import string

print(string.printable)
    
