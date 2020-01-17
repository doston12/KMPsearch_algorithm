import file_finder
import kmp
import file_reader

pattern = "life"
path = "D:/docs"

txt_files = file_finder.get_txt_files(path)

for file in txt_files:
    content = file_reader.read_file_content(file)
    pattern_found = kmp.KMPSearch(pattern, content)
    for pat in pattern_found:
        print(file + " : " + pat)

