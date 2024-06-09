import chardet
import codecs

with open('temp_data.json', 'rb') as f:
    result = chardet.detect(f.read())
    encoding = result['encoding']
    print(f"Detected encoding: {encoding}")

with codecs.open('temp_data.json', 'r', encoding=encoding) as f_in:
    with codecs.open('data.json', 'w', encoding='utf-8') as f_out:
        for line in f_in:
            f_out.write(line)
