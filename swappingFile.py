def swap_file_data():
    with open("sample1.csv", 'r') as a:
        data_a = a.read()
    
    with open("sample2.csv", 'r') as b:
        data_b = b.read()

    with open("file1", 'w') as a:
        a.write(data_b)

    with open("file2", 'w') as b:
        b.write(data_a)

swap_file_data()