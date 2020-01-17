import os

txt_files = []

def get_dirlist(path):
    dirlist = os.listdir(path)
    return dirlist

def get_txt_files(path, prefix=""):
    if prefix == "":
        #print("Folder listing for: ", path)
        prefix = "| "

    dirlist = get_dirlist(path)
    for file in dirlist:
        fullname = os.path.join(path, file)
        if os.path.isdir(fullname):
            get_txt_files(fullname, prefix + "| ")
        else:
            tmp = file.rfind('.')
            sub_str = file[tmp:]
            if sub_str == '.txt':
                txt_files.append(fullname)

    return txt_files
