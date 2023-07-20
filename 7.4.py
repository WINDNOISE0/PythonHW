import os

def batch_rename_files(desired_name, number_digits, source_extension, destination_extension, range_start, range_end):
    files = os.listdir('.')
    
    files = [file for file in files if file.endswith(source_extension)]

    files.sort()
    
    counter = 1
    
    for file in files:
        original_name_range = file[range_start-1:range_end]
        
        new_name = original_name_range + desired_name + str(counter).zfill(number_digits) + '.' + destination_extension
        
        os.rename(file, new_name)
        
        counter += 1

batch_rename_files('newname_', 3, '.txt', 'docx', 3, 6)