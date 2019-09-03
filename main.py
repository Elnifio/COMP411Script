import os, re

def main():
    path = "./"
    all_dirs = os.listdir(path)
    all_c_files = []
    all_test_ins = []
    all_test_outs = []

    for item in all_dirs:
        if re.match(r'ex\d\.c', item):
            all_c_files.append({'Name': item, 'Input_counts': [], 'Output_counts': []})
        elif re.match(r'ex\din\d', item):
            all_test_ins.append(item)
        elif re.match(r'ex\dout\d', item):
            all_test_outs.append(item)

    for item in all_c_files:
        exe_name = item['Name'].split(".")[0]
        os.system("gcc %s -o %s" % (item['Name'], exe_name))

    for c_file in all_c_files:
        exe_name = c_file['Name'].split(".")[0]
        in_name = exe_name + 'in'
        out_name = exe_name + 'out'

        for item in all_dirs:
            if re.match(r'%s\d' % in_name, item):
                c_file['Input_counts'].append(item)
            elif re.match(r"%s\d" % out_name, item):
                c_file['Output_counts'].append(item)
        
        c_file['Input_counts'].sort()
        c_file['Output_counts'].sort()
        
        for input_file in c_file['Input_counts']:
            input_number = input_file[-1]
            os.system("./%s < %s > %sresult%s" % (exe_name, input_file, exe_name, input_number))

        for output_file in c_file['Output_counts']:
            output_number = output_file[-1]
            diff_result = os.system("diff %sresult%s %s" % (exe_name, output_number, output_file))
            if diff_result == 0:
                print("%s match %sresult%s" % (output_file, exe_name, output_number))
            else:
                print("Output doesn't match expected in file %s : %sresult%s" % (output_file, exe_name, output_number))
        

if __name__ == "__main__":
    main()

