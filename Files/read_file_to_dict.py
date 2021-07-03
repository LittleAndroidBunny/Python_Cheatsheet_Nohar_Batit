def read_csv(csv_path):
    """
    Read a csv file (with a header) into a dictionary
    where the dictionary structure will be
    {header_col1: [val1_line1, val1_line2, ...], header_col2: [val2_line1, val2_line2, ...], ...}

    """
    with open(csv_path, 'r') as in_csv:
        header = in_csv.readline().strip().split(',')
        data = {i: [] for i in header}
        for line in in_csv:
            line = line.strip().split(',')
            for i in range(len(line)):
                try:
                    data[header[i]].append(float(line[i]))
                except ValueError:
                    data[header[i]].append(line[i])
    return data

# f = open("Data1.txt")
file = 'Data1.txt'  # file name
with open(file) as f:
    main_list = [i.strip().replace('"', '').split(';') for i in f.readlines()]
# for i in main_list:
#     for j in range(len(i)):
#         if i[j].lstrip("-").replace('.', '').isdigit():
#             i[j] = float(i[j])
#             if i[j] - int(i[j]) == 0:
#                 i[j] = int(i[j])
# for i in main_list:
#     main_dict[counter] = i
#     counter += 1

# list_16 = []
# list_17 = []
# main_dict = {}
# counter = 0
# # we remember we start from index 0
# file = 'Data1.txt'
# with open(file) as f:
#     main_list = [i.strip().replace('"', '').split(';') for i in f.readlines()]
# for i in main_list:
#     for j in range(len(i)):
#         if i[j].lstrip("-").replace('.', '').isdigit():
#             i[j] = float(i[j])
#             if i[j] - int(i[j]) == 0:
#                 i[j] = int(i[j])
# for i in main_list:
#     main_dict[counter] = i
#     counter += 1