def append_to_file(path, extra_text):
    with open(path, 'w', encoding='utf-8') as file:
        file.write(extra_text)

additional_text = "Hechas, pues, estas prevenciones, no quiso aguardar más tiempo a poner en efeto su pensamiento..."

append_to_file('quixote_chapter2.txt', additional_text)