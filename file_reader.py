import kmp

def read_file_content(path):
    try:
        file_reader = open(path, "r")
        return file_reader.read()
    except Exception as e:
        print("Error occurred when file was opened: " + str(e))