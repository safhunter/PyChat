import locale


def_coding = locale.getpreferredencoding()
print(def_coding)

with open('test_file.txt', 'r', encoding='utf-8') as f:
    for el_str in f:
        print(el_str)
