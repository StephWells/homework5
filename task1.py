def read_entries(file_name='',delimiter=None): #function to get data inside file

    in_filename = file_name
    in_delim = delimiter
    result = []

    try:
        with open(in_filename, 'r') as text_file:
            in_entries = [line.split(in_delim) for line in text_file]
            pass
            result = in_entries
    except IOError: #Exception handling
        print(f'{in_filename} does not exist in the current folder. Operation aborted.')
        return None
    return result


def scores_task(): #Function to complete task1
    import sys
    TEXT_FILE = 'scores.txt' #To test the exceptions, please remove the number symbol from the other FILE_NAMES. Only one FILE_NAME should be tested at a time for prime results.
    #TEXT_FILE = 'no_scores.txt' #IO Error to handle when a FILE_NAME is not in the current folder.
    #TEXT_FILE = 'scores_bad.txt' #ValueError exception to handle scores that were not converted to numbers.
    LOG_OUTPUT_FILE = 'log.txt'


    file_entries = read_entries(TEXT_FILE) #IOErrors handled in function call
    
    if file_entries != None:
        valid_entries = []
        for entry in file_entries:
            try:
                fname = str(entry[0]) #first name
                grade = int(entry[1]) #score
                valid_entries.append([fname, grade])
            except ValueError: 
                print(f'Bad score value for {entry[0]}, ignored.')
        
        student_amt = len(valid_entries) #Number of students
        class_avg = sum(entry[1] for entry in valid_entries) / student_amt #Average of student scores
    
        
        print(f'The class average is {class_avg:.0f} for {student_amt} students.') #Print in the terminal
        
        original_stdout = sys.stdout #Save a reference of output

        with open(LOG_OUTPUT_FILE, 'w') as f: #Print in the text file
            sys.stdout = f
            print(f'The class average is {class_avg:.0f} for {student_amt} students.')
            sys.standout = original_stdout
    
        
scores_task() #end