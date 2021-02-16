import spend
from datetime import date
import os

print("Hello! Spending App")

path = "F:\\MyAppLifeGoalApp\\AppFiles\\"

approaching_yearly_limit_diff = 100
approaching_monthly_limit_diff = 100

def print_report(report_dict, is_yearly_report):
    type_keys = report_dict.keys()
    for t in type_keys:
        print('\n')
        print(t + ':')
        total = 0
        for st in report_dict[t]:
            if is_yearly_report == 'Y' or is_yearly_report == 'y':
                if report_dict[t][st][2] == -1:
                    print(st + ' = %d, yearly limit = Not Set, yearly assign = %d' % (report_dict[t][st][0], report_dict[t][st][3]))
                else:
                    alert_string = ""
                    if report_dict[t][st][2] - report_dict[t][st][0] < approaching_yearly_limit_diff:
                        alert_string = ", ALERT : Approachin yearly limit: {diff}".format(diff = report_dict[t][st][2] - report_dict[t][st][0])
                    print(st + ' = %d, yearly limit = %d, yearly assign = %d%s' % (report_dict[t][st][0], report_dict[t][st][2], report_dict[t][st][3], alert_string))
            else:
                if report_dict[t][st][1] == -1:
                    print(st + ' = %d, monthly limit = Not Set' % (report_dict[t][st][0]))
                else:
                    alert_string = ""
                    if report_dict[t][st][1] - report_dict[t][st][0] < approaching_monthly_limit_diff:
                        alert_string = ", ALERT : Approachin monthly limit: {diff}".format(diff = report_dict[t][st][1] - report_dict[t][st][0])
                    print(st + ' = %d, monthly limit = %d%s' % (report_dict[t][st][0], report_dict[t][st][1], alert_string))
            total = total + report_dict[t][st][0]
        print('Total %s: %d' % (t, total))

def generate_report(is_yearly_report, year, month):
    # [entry1, entry2, entry3, entry4]
    # entry1 - entry value
    # entry2 - entry monthly report
    # entry3 - entry yearly report
    # entry4 - entry assigned value
    report_dict = {
        "Necessity":{"grocery_veggies": [0, -1, -1, 0], "grocery_meat": [0, -1, -1, 0], "rent": [0, -1, -1, 0], "bills": [0, -1, -1, 0], "one_time": [0, -1, -1, 0]},
        "Entertainment":{"food": [0, -1, -1, 0], "movies": [0, -1, -1, 0], "party": [0, -1, -1, 0], "video_stream": [0, -1, -1, 0], "others": [0, -1, -1, 0]},
        "Vacation":{"hotel": [0, -1, -1, 0], "car_rent": [0, -1, -1, 0], "gas": [0, -1, -1, 0], "tickets": [0, -1, -1, 0], "food": [0, -1, -1, 0], "others": [0, -1, -1, 0]},
        "Car":{"maintainence": [0, -1, -1, 0], "insurance": [0, -1, -1, 0], "gas": [0, -1, -1, 0], "registration": [0, -1, -1, 0], "bills": [0, -1, -1, 0]},
        "Misc":{"makeup": [0, -1, -1, 0], "home_improve": [0, -1, -1, 0], "black_friday": [0, -1, -1, 0], "clothes": [0, -1, -1, 0], "others": [0, -1, -1, 0], "pitu_gift": [0, -1, -1, 0], "others_gift": [0, -1, -1, 0], "one_time": [0, -1, -1, 0], "celebration": [0, -1, -1, 0], "medical": [0, -1, -1, 0]},
        "Payments":{"stocks": [0, -1, -1, 0], "credit_card_payment": [0, -1, -1, 0], "investments": [0, -1, -1, 0], "india_others": [0, -1, -1, 0]},
        "Deposit":{"pay": [0, -1, -1, 0], "bonus": [0, -1, -1, 0], "tax_ret": [0, -1, -1, 0], "others": [0, -1, -1, 0], "savings": [0, -1, -1, 0]}
    }

    file_name = month + '_' + year + '.txt'
    folder_path = path + year + '_folder'
    print("report")
    print("folder = %s, file = %s " % (folder_path, file_name))
    is_print_report = False

    if is_yearly_report == 'Y' or is_yearly_report == 'y':
        print("yearly")
        list_of_files = os.listdir(folder_path)
        print(list_of_files)
        for files in list_of_files:
            if "limit" in files:
                yearly_limit_fname = year + '_limit.txt'
                if yearly_limit_fname in files:
                    limit_file_path = folder_path + '\\' + files
                    limt_fh = open(limit_file_path, "r")
                    for line in limt_fh:
                        #print(line)
                        line_space_split = line.split()
                        #print(line_space_split)
                        entry_val = []
                        for entries in line_space_split:
                            line_colon_split = entries.split(':')
                            #print(line_colon_split)
                            entry_val.append(line_colon_split[1].split('(')[0])
                        #print(entry_val)
                        report_dict[entry_val[0]][entry_val[1]][2] = int(entry_val[2])
                    limt_fh.close()
                else:
                    continue
            elif "assign" in files:
                yearly_assign_fname = year + '_assign.txt'
                if yearly_assign_fname in files:
                    assign_file_path = folder_path + '\\' + files
                    assign_fh = open(assign_file_path, "r")
                    for line in assign_fh:
                        #print(line)
                        line_space_split = line.split()
                        #print(line_space_split)
                        entry_val = []
                        for entries in line_space_split:
                            line_colon_split = entries.split(':')
                            #print(line_colon_split)
                            entry_val.append(line_colon_split[1].split('(')[0])
                        #print(entry_val)
                        report_dict[entry_val[0]][entry_val[1]][3] = report_dict[entry_val[0]][entry_val[1]][3] + int(entry_val[2])
                    assign_fh.close()
                else:
                    continue
            else:
                file_path = folder_path + '\\' + files
                fh = open(file_path, "r")
                for line in fh:
                    #print(line)
                    line_space_split = line.split()
                    #print(line_space_split)
                    entry_val = []
                    for entries in line_space_split:
                        line_colon_split = entries.split(':')
                        #print(line_colon_split)
                        entry_val.append(line_colon_split[1].split('(')[0])
                    #print(entry_val)
                    report_dict[entry_val[0]][entry_val[1]][0] = report_dict[entry_val[0]][entry_val[1]][0] + int(entry_val[2])
                fh.close()
        is_print_report = True
    elif is_yearly_report == 'N' or is_yearly_report == 'n':
        print("monthly")
        file_path = folder_path + '\\' + file_name
        fh = open(file_path, "r")
        for line in fh:
            #print(line)
            line_space_split = line.split()
            #print(line_space_split)
            entry_val = []
            for entries in line_space_split:
                line_colon_split = entries.split(':')
                #print(line_colon_split)
                entry_val.append(line_colon_split[1].split('(')[0])
            #print(entry_val)
            report_dict[entry_val[0]][entry_val[1]][0] = report_dict[entry_val[0]][entry_val[1]][0] + int(entry_val[2])
        fh.close()

        monthly_limit_fname = month + '_' + year + '_limit.txt'
        limit_file_path = folder_path + '\\' + monthly_limit_fname
        if monthly_limit_fname in os.listdir(folder_path):
            limt_fh = open(limit_file_path, "r")
            for line in limt_fh:
                #print(line)
                line_space_split = line.split()
                #print(line_space_split)
                entry_val = []
                for entries in line_space_split:
                    line_colon_split = entries.split(':')
                    #print(line_colon_split)
                    entry_val.append(line_colon_split[1].split('(')[0])
                    #print(entry_val)
                report_dict[entry_val[0]][entry_val[1]][1] = int(entry_val[2])
            limt_fh.close()
        is_print_report = True
    else:
        print("Invalid Input")
        is_print_report = False

    if is_print_report:
        print_report(report_dict, is_yearly_report)
        
            

def get_entry_type(etype):
    if etype == '1':
        return 'Necessity'
    elif etype == '2':
        return 'Entertainment'
    elif etype == '3':
        return 'Vacation'
    elif etype == '4':
        return 'Car'
    elif etype == '5':
        return 'Misc'
    elif etype == '6':
        return 'Payments'
    elif etype == '7':
        return 'Deposit'
    return 'Invalid'

def get_entry_subtype(etype, esubtype):
    if etype == '1':
        if esubtype == '1':
            return 'grocery_veggies'
        elif esubtype == '2':
            return 'grocery_meat'
        elif esubtype == '3':
            return 'rent'
        elif esubtype == '4':
            return 'bills'
        elif esubtype == '5':
            return 'one_time'
    elif etype == '2':
        if esubtype == '1':
            return 'food'
        elif esubtype == '2':
            return 'movies'
        elif esubtype == '3':
            return 'party'
        elif esubtype == '4':
            return 'video_stream'
        elif esubtype == '5':
            return 'others'
    elif etype == '3':
        if esubtype == '1':
            return 'hotel'
        elif esubtype == '2':
            return 'car_rent'
        elif esubtype == '3':
            return 'gas'
        elif esubtype == '4':
            return 'tickets'
        elif esubtype == '5':
            return 'food'
        elif esubtype == '6':
            return 'others'
    elif etype == '4':
        if esubtype == '1':
            return 'maintainence'
        elif esubtype == '2':
            return 'insurance'
        elif esubtype == '3':
            return 'gas'
        elif esubtype == '4':
            return 'registration'
        elif esubtype == '5':
            return 'bills'
    elif etype == '5':
        if esubtype == '1':
            return 'makeup'
        elif esubtype == '2':
            return 'home_improve'
        elif esubtype == '3':
            return 'black_friday'
        elif esubtype == '4':
            return 'clothes'
        elif esubtype == '5':
            return 'others'
        elif esubtype == '6':
            return 'pitu_gift'
        elif esubtype == '7':
            return 'others_gift'
        elif esubtype == '8':
            return 'one_time'
        elif esubtype == '9':
            return 'celebration'
        elif esubtype == '10':
            return 'medical'
    elif etype == '6':
        if esubtype == '1':
            return 'stocks'
        elif esubtype == '2':
            return 'credit_card_payment'
        elif esubtype == '3':
            return 'investments'
        elif esubtype == '4':
            return 'india_others'
    elif etype == '7':
        if esubtype == '1':
            return 'pay'
        elif esubtype == '2':
            return 'bonus'
        elif esubtype == '3':
            return 'tax_ret'
        elif esubtype == '4':
            return 'others'
        elif esubtype == '5':
            return 'savings'
    return 'Invalid'

def write_entry(etype, esubtype, val, detail = 'NA', long_term_items = 'NA'):
    today = date.today()
    folder_name = today.strftime("%Y")
    file_name = today.strftime("%m_%Y")
    file_name = file_name + '.txt'
    print("folder = %s, file = %s " % (folder_name, file_name))
    folder_path = path + folder_name + '_folder'
    print("\nfolder_path = %s" % (folder_path))
    
    etype_name = get_entry_type(etype)
    if etype_name == 'Invalid':
        print("\nInvalid Entry Name")
        return
    
    esubtype_name = get_entry_subtype(etype, esubtype)
    if esubtype_name == 'Invalid':
        print("\nInvalid Subentry Name")
        return
    
    if os.path.isdir(folder_path):
        print("Folder Exist")
        file_path = folder_path + '\\' + file_name
        fh = open(file_path, "a+")
        fh.write("Type:%s(%s) SubType:%s(%s) Value:%s Detail:%s Date:%s LongTermItems:%s\n" % (etype_name, etype, esubtype_name, esubtype, val, detail, today.strftime("%d_%m_%Y"), long_term_items))
        fh.close()
    else:
        os.mkdir(folder_path)
        print("Folder Created")
        file_path = folder_path + '\\' + file_name
        fh = open(file_path, "a+")
        fh.write("Type:%s(%s) SubType:%s(%s) Value:%s Detail:%s Date:%s LongTermItems:%s\n" % (etype_name, etype, esubtype_name, esubtype, val, detail, today.strftime("%d_%m_%Y"), long_term_items))
        fh.close()

def write_limit_entry(is_yearly_report, year, month, etype, esubtype, val, detail = 'NA'):
    today = date.today()
    print("Write limit entries")
    file_name = '_limit.txt'
    folder_path = path + year + '_folder'

    if is_yearly_report == 'Y' or is_yearly_report == 'y':
        print("yearly")
        file_name = year + '_limit.txt'
        print("folder = %s, file = %s " % (folder_path, file_name))
    elif is_yearly_report == 'N' or is_yearly_report == 'n':
        print("monthly")
        file_name = month + '_' + year + '_limit.txt'
        print("folder = %s, file = %s " % (folder_path, file_name))
    else:
        print("Invalid Input")
        return

    etype_name = get_entry_type(etype)
    if etype_name == 'Invalid':
        print("\nInvalid Entry Name")
        return

    esubtype_name = get_entry_subtype(etype, esubtype)
    if esubtype_name == 'Invalid':
        print("\nInvalid Subentry Name")
        return

    if os.path.isdir(folder_path):
        print("Folder Exist")
        file_path = folder_path + '\\' + file_name
        if os.path.exists(file_path):
            print("Files Exist")
            fh = open(file_path, "r")
            list_of_lines = fh.readlines()
            fh.close()
            index = 0
            entry_found = False
            print(list_of_lines)
            for lines in list_of_lines:
                line_space_split = lines.split()
                entry_val = []
                #print(line_space_split)
                for entries in line_space_split:
                    line_colon_split = entries.split(':')
                    entry_val.append(line_colon_split[1].split('(')[0])
                #print(entry_val)
                if entry_val[0] == etype_name and entry_val[1] == esubtype_name:
                    entry_found = True
                    break
                index = index + 1
            entry_string = "Type:{etn}({et}) SubType:{estn}({est}) Value:{v} Detail:{d} Date:{da}\n".format(etn = etype_name, et = etype, estn = esubtype_name, est = esubtype, v = val, d = detail, da = today.strftime("%d_%m_%Y"))
            if entry_found:
                list_of_lines[index] = entry_string
            else:
                list_of_lines.append(entry_string)
            fh = open(file_path, "w")
            fh.writelines(list_of_lines)
            fh.close()
        else:
            print("Files does not Exist")
            fh = open(file_path, "a+")
            fh.write("Type:%s(%s) SubType:%s(%s) Value:%s Detail:%s Date:%s\n" % (etype_name, etype, esubtype_name, esubtype, val, detail, today.strftime("%d_%m_%Y")))
            fh.close()
    else:
        print("Folder for limit does not exist. Create an entry for the year")

def write_assigned_value_entry(year, etype, esubtype, val, detail = 'NA'):
    today = date.today()
    print("Write assigned value entries")
    file_name = year + '_assign.txt'
    folder_path = path + year + '_folder'

    etype_name = get_entry_type(etype)
    if etype_name == 'Invalid':
        print("\nInvalid Entry Name")
        return
    
    esubtype_name = get_entry_subtype(etype, esubtype)
    if esubtype_name == 'Invalid':
        print("\nInvalid Subentry Name")
        return

    if os.path.isdir(folder_path):
        print("Folder Exist")
        file_path = folder_path + '\\' + file_name
        fh = open(file_path, "a+")
        fh.write("Type:%s(%s) SubType:%s(%s) Value:%s Detail:%s Date:%s\n" % (etype_name, etype, esubtype_name, esubtype, val, detail, today.strftime("%d_%m_%Y")))
        fh.close()
    else:
        os.mkdir(folder_path)
        print("Folder Created")
        file_path = folder_path + '\\' + file_name
        fh = open(file_path, "a+")
        fh.write("Type:%s(%s) SubType:%s(%s) Value:%s Detail:%s Date:%s\n" % (etype_name, etype, esubtype_name, esubtype, val, detail, today.strftime("%d_%m_%Y")))
        fh.close()
    
def print_entry_options():
    print('EntryType \n 1: Necessity \n {1: grocery_veggies, 2: grocery_meat, 3: rent, 4: bills, 5: one_time}')
    print('\n 2: Entertainment \n {1: food, 2: movies, 3: party, 4: video_stream, 5: others}')
    print('\n 3: Vacation \n {1: hotel, 2: car_rent, 3: gas, 4: tickets, 5: food. 6: others}')
    print('\n 4: Car \n {1: maintainence, 2: insurance, 3: gas, 4: registration, 5: bills}')
    print('\n 5: Misc. \n {1: makeup, 2: home_improve, 3: black_friday, 4: clothes, 5: others, 6: pitu_gift, 7: others_gift, 8: one_time, 9: celebration, 10: medical}')
    print('\n 6: Payments \n {1: stocks, 2: credit_card_payment, 3: investments, 4: india_others}')
    print('\n 7: Deposit \n {1: pay, 2: bonus, 3: tax_ret, 4: others, 5: savings}')

def main():
    #acnt1 = spend.spending('pratik_household')
    #acnt1.get_profile_name()
    #acnt1.add_entry("necessity", "rent", 1600)
    #acnt1.get_value("necessity", "rent")
    while 1:
        print('1: EXIT, 2: ENTRY, 3: GENERATE_REPORT, 4: SET_LIMIT 5:SET_ASSIGNED_MONEY')
        option = input("Enter option: ")
        
        if option == '1':
            break
        elif option == '2':
            print_entry_options()
            entry_type = input("\nEnter Type: ")
            entry_subtype = input("\nEnter Subtype: ")
            value = input("\nEnter Value: ")
            detail = input("\nEnter Comment: ")
            if detail == "":
                detail = 'NA'
            long_term_items = input("\nEnter long term items: ")
            if long_term_items == "":
                long_term_items = 'NA'
            write_entry(entry_type, entry_subtype, value, detail, long_term_items)
        elif option == '3':
            is_yearly_report = input("\nNeed Yearly Report(Y/N)(y/n): ")
            report_year = input("\nEnter year: ")
            report_month = input("\nEnter month(1-12): ")
            generate_report(is_yearly_report, report_year, report_month)
        elif option == '4':
            is_yearly_limit = input("\nSet Yearly Limit(Y/N)(y/n): ")
            limit_year = input("\nEnter year: ")
            limit_month = input("\nEnter month(1-12): ")
            print("\nSelect the entry to set limits:")
            print_entry_options()
            entry_type = input("\nEnter Type: ")
            entry_subtype = input("\nEnter Subtype: ")
            value = input("\nEnter Value: ")
            detail = input("\nEnter Comment: ")
            if detail == "":
                detail = 'NA'
            write_limit_entry(is_yearly_limit, limit_year, limit_month, entry_type, entry_subtype, value, detail)
        elif option == '5':
            assign_year = input("\nEnter year: ")
            print("\nSelect the entry to set the assigned money:")
            print_entry_options()
            entry_type = input("\nEnter Type: ")
            entry_subtype = input("\nEnter Subtype: ")
            value = input("\nEnter Value: ")
            detail = input("\nEnter Comment: ")
            if detail == "":
                detail = 'NA'
            write_assigned_value_entry(assign_year, entry_type, entry_subtype, value, detail)

'''
1) load profile for 3 year
2) Add Entry
   - Add folder for profile
   - Add year folder in the profile folder
   - Add month file for each month entry
   Example:
   pratik_spend_plan
      - 2019_folder
        jan_entries.txt
        feb_entries.txt
        :
        dec_entries.txt
      - 2020_folder
        jan_entries.txt
        feb_entries.txt
        :
        dec_entries.txt
      - 2021
3) Generate Report for month
4) Generate Report for year
5) Get the value of the entry for the year
'''

if __name__=="__main__": 
    main() 
