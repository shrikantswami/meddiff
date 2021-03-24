def error_warning_scrpper(filename,destination):
    try:
        error_list = []
        with open(filename) as inputfile:
            file_data = inputfile.readlines()
            for data in file_data:
                if ('Error' in data) or ('Warning' in data):
                    error_list.append(data)
        with open(destination, 'w') as destination_file:
            destination_file.writelines(error_list)
    except Exception as e:
        pass


error_warning_scrpper('problem3_input.txt', 'problem3_output.txt')
