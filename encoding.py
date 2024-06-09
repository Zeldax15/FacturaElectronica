import codecs

with codecs.open('temp_data.json', 'r', encoding='ISO-8859-1') as f_in:
    with codecs.open('data.json', 'w', encoding='utf-8') as f_out:
        for line in f_in:
            f_out.write(line)
