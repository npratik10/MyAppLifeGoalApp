import spend
from datetime import date
import os

print("Hello! Spending App")

path = "F:\\MyAppLifeGoalApp\\AppFiles\\"

def print_report(report_dict):
    type_keys = report_dict.keys()
    for t in type_keys:
        print('\n')
        print(t + ':')
        total = 0
        for st in report_dict[t]:
            print(st + ' = %d' % (report_dict[t][st]))
            total = total + report_dict[t][st]
        print('Total %s: %d' % (t, total))

def generate_report(is_yearly_report, year, month):
    report_dict = {
        "Necessity":{"grocery_veggies": 0, "grocery_meat": 0, "rent": 0, "bills": 0, "one_time": 0},
        "Entertainment":{"food": 0, "movies": 0, "party": 0, "video_stream": 0, "others": 0},
        "Vacation":{"hotel": 0, "car_rent": 0, "gas": 0, "tickets": 0, "food": 0},
        "Car":{"maintainence": 0, "insurance": 0, "gas": 0, "registration": 0, "bills": 0},
        "Misc":{"makeup": 0, "home_improve": 0, "black_friday": 0, "clothes": 0, "others": 0, "pitu_gift": 0, "others_gift": 0, "one_time": 0, "celebration": 0},
        "Payments":{"stocks": 0, "credit_card_payment": 0, "investments": 0},
        "Deposit":{"pay": 0, "bonus": 0, "tax_ret": 0, "others": 0}
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
                report_dict[entry_val[0]][entry_val[1]] = report_dict[entry_val[0]][entry_val[1]] + int(entry_val[2])
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
            report_dict[entry_val[0]][entry_val[1]] = report_dict[entry_val[0]][entry_val[1]] + int(entry_val[2])
        fh.close()
        is_print_report = True
    else:
        print("Invalid Input")
        is_print_report = False

    if is_print_report:
        print_report(report_dict)
        
            

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
    elif etype == '6':
        if esubtype == '1':
            return 'stocks'
        elif esubtype == '2':
            return 'credit_card_payment'
        elif esubtype == '3':
            return 'investments'
    elif etype == '7':
        if esubtype == '1':
            return 'pay'
        elif esubtype == '2':
            return 'bonus'
        elif esubtype == '3':
            return 'tax_ret'
        elif esubtype == '4':
            return 'others'
    return 'Invalid'

def write_entry(etype, esubtype, val):
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
        fh.write("Type:%s(%s) SubType:%s(%s) Value:%s\n" % (etype_name, etype, esubtype_name, esubtype, val))
        fh.close()
    else:
        os.mkdir(folder_path)
    

def print_entry_options():
    print('EntryType \n 1: Necessity \n {1: grocery_veggies, 2: grocery_meat, 3: rent, 4: bills, 5: one_time}')
    print('\n 2: Entertainment \n {1: food, 2: movies, 3: party, 4: video_stream, 5: others}')
    print('\n 3: Vacation \n {1: hotel, 2: car_rent, 3: gas, 4: tickets, 5: food}')
    print('\n 4: Car \n {1: maintainence, 2: insurance, 3: gas, 4: registration, 5: bills}')
    print('\n 5: Misc. \n {1: makeup, 2: home_improve, 3: black_friday, 4: clothes, 5: others, 6: pitu_gift, 7: others_gift, 8: one_time, 9: celebration}')
    print('\n 6: Payments \n {1: stocks, 2: credit_card_payment, 3: investments}')
    print('\n 7: Deposit \n {1: pay, 2: bonus, 3: tax_ret, 4: others}')

def main():
    #acnt1 = spend.spending('pratik_household')
    #acnt1.get_profile_name()
    #acnt1.add_entry("necessity", "rent", 1600)
    #acnt1.get_value("necessity", "rent")
    while 1:
        print('1: EXIT, 2: ENTRY, 3: GENERATE_REPORT, 4: SET_LIMIT')
        option = input("Enter option: ")
        
        if option == '1':
            break
        elif option == '2':
            print_entry_options()
            entry_type = input("\nEnter Type: ")
            entry_subtype = input("\nEnter Subtype: ")
            value = input("\nEnter Value: ")
            write_entry(entry_type, entry_subtype, value)
        elif option == '3':
            is_yearly_report = input("\nNeed Yearly Report(Y/N)(y/n): ")
            report_year = input("\nEnter year: ")
            report_month = input("\nEnter month(1-12): ")
            generate_report(is_yearly_report, report_year, report_month)
            

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
