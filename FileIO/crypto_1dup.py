#Create a method that decrypts the texts/duplicated_chars.txt
#Write the decrypted content into a new file called decrypt1.txt

def crypto_1dup(input_file_name, output_file_name):
    f = open(input_file_name, 'r')
    f2 = open(output_file_name, 'w')
    raw_rows = f.readlines()
    for raw_row in raw_rows:
        decrypted_row = []
        for raw_word in raw_row.split():
            decrypted_word = ''
            for i in range(0, len(raw_word), 2):
                decrypted_word += raw_word[i]
            decrypted_row.append(decrypted_word)
        f2.write(' '.join(decrypted_row) + '\n')
    f.close()
    f2.close()  
                
crypto_1dup('texts/duplicated_chars.txt', 'texts/decrypt1.txt')