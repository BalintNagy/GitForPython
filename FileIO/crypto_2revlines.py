# Create a method that decrypts texts/reversed_zen_lines.txt
# Write the file content into a new file called decrypt2_[x].txt
# Where [x] is the first word of the decrypted file's content

def crypto_2revlines(file_name):
    decrypted_rows = []
    
    f = open(file_name, 'r')
    raw_rows = f.readlines()
    for raw_row in raw_rows:
        decrypted_row = ''
        for i in range(0, len(raw_row)):
            if raw_row[len(raw_row) - i - 1] != '\n':
                decrypted_row += raw_row[len(raw_row) - i - 1]
        decrypted_rows.append(decrypted_row + '\n')
    f.close()
    
    output_file_name = 'texts/decrypt2_' + decrypted_rows[0].split()[0] + '.txt'
    f2 = open(output_file_name, 'w')
    for decrypted_row in decrypted_rows:
        f2.write(decrypted_row)
    f2.close() 
                
crypto_2revlines('texts/reversed_zen_lines.txt')
