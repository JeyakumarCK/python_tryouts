import os

def rename_files():
    file_list = os.listdir(r'C:\JK\Udacity\Python\Msg')
    print file_list
    saved_path = os.getcwd()
    os.chdir(r'C:\JK\Udacity\Python\Msg')
    for file_name in file_list:
        print file_name
        print file_name.translate(None, "0123456789")
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)
    #end of rename_files()

rename_files()
    
print 'Program execution completed'