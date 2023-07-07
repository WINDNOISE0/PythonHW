def shared_path(a):
    import os
    
    path = os.path.dirname(a)
    file_name = os.path.basename(a)
    name, format_ = os.path.splitext(file_name)
    
    return path, name, format_

a = r'C:\Users\jaril\OneDrive\Рабочий стол\HW.txt'

result = shared_path(a)

print(result)