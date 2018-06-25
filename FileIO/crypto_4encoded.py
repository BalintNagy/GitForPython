# Create a method that decrypts texts/encoded_zen_lines.txt
# Write the file's content into a new file with a name of
# "decryt4_[the current timestamp]" where the timestamp format shoud be 'hhmmss'

def crypto_4encoded(file_name):
    import datetime, string
    f = open(file_name, 'r')
    f2 = open('texts/decrypt4_' + datetime.datetime.now().strftime('%H%M%S') + '.txt', 'w')
    for raw_row in f.readlines():
        decrypted_row = []
        for raw_word in raw_row.split():
            decrypted_word = ''
            for i in raw_word:
                decrypted_word += sorted(string.printable)[sorted(string.printable).index(i) - 1]
            decrypted_row.append(decrypted_word)
        f2.write(' '.join(decrypted_row) + '\n')
    f2.close()
    f.close()

crypto_4encoded('texts/encoded_zen_lines.txt')

