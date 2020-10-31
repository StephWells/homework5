def read_book(file_name=''):
    inside_filename = file_name
    result = []
    with open(inside_filename, 'r', encoding='utf8') as text_file:
        line = text_file.readline()
        while line != '':
            result.append(line.rstrip('\n'))
            line = text_file.readline()
    result[0] = result[0].replace('\ufeff', '') 
    return result

def write_file(file_name='log.txt', records=[]):
    inside_filename = file_name
    in_records = records
    with open(inside_filename, 'w') as text_file:
        for record in in_records:
            string_record = ''
            if type(record) is str:
                string_record = record
            else:
                for field in record:
                    string_record += f'{field} '
            string_record = string_record.rstrip(' ') + '\n'
            text_file.write(string_record)

    print(f'Write to {inside_filename} executed.')

def calc_letters():
    #BOOK_TEXT = 'book.txt'  #Remove the comment symbol to test the book.txt scenario
    BOOK_TEXT = 'book_bbbbb.txt'
    ALL_LETTERS = "It has all letters."
    MISSING_LETTERS = "It doesn't have all letters."
    BEG_ORD = ord('A')
    END_ORD = ord('Z') +1 

    book_lines = read_book(BOOK_TEXT) 
    book_letter = ''.join(book_lines).replace(' ', '').upper() 
    book_letter = ''.join(sorted(book_letter)) 

    letter_freq = [0 for x in range(0, END_ORD + 1)] 

    
    for letter in book_letter:
        letter_ord = ord(letter)
        if letter_ord in range(BEG_ORD, END_ORD):
            letter_freq[letter_ord] += 1

    
    result = []
    for i in range(BEG_ORD, END_ORD): 
        result.append((chr(i), letter_freq[i]))
        
    
    if len([0 for item in result if item[1] == 0]) == 0:
        result.append(f'\n{ALL_LETTERS}') 
    else:
        result.append(f'\n{MISSING_LETTERS}') 
    
    write_file('summary.txt', result)

calc_letters()