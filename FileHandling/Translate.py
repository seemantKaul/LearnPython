from googletrans import Translator

FILE_LOCATION = r'D:\Study\Python\FileHandling'
translator = Translator()


def translate_to_hindi(txt):
    return translator.translate(txt, 'hi')


with open(fr"{FILE_LOCATION}\translateSource.txt", "r") as file:
    list_line = []
    while a := file.readline():
        list_line.append(a)
    with open(fr"{FILE_LOCATION}\translated_file.txt", "a", encoding='utf-8') as trans_file:
        for tr in list_line:
            print(translate_to_hindi(tr).text)
            trans_file.write(f"{translate_to_hindi(tr).origin} --> {translate_to_hindi(tr).text}\n")
        print("Done writing to file")
