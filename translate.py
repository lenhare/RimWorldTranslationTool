import os
import shutil
from google.cloud import translate_v2 as translate
from lxml import etree

def translate_text(text):
    try:
        print(f"Translating text: {text}")
        translate_client = translate.Client()
        result = translate_client.translate(text, target_language='pt')
        translated_text = result['translatedText']
        print(f"Translated '{text}' to '{translated_text}'")
        return translated_text
    except Exception as e:
        print(f"Erro ao traduzir '{text}': {e}")
        return text

def process_xml_file(file_path, new_file_path):
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse(file_path, parser)
    root = tree.getroot()

    translation_count = 0
    translations = {} 

    for elem in root.iter():
        if isinstance(elem, etree._Comment):
            comment_text = elem.text.strip()
            if comment_text.startswith("EN:"):
                english_text = comment_text[4:].strip()
                portuguese_text = translate_text(english_text)
                
                elem.text = f"EN: {english_text}" 
                translations[english_text] = portuguese_text 
                print(f"Traduzido '{english_text}' para '{portuguese_text}'")

    for elem in root.iter():
        if elem.text and elem.text.strip() == "TODO":
            preceding_comment = elem.getprevious()
            if isinstance(preceding_comment, etree._Comment):
                comment_text = preceding_comment.text.strip()
                if comment_text.startswith("EN:"):
                    english_text = comment_text[4:].strip()
                    if english_text in translations:
                        elem.text = translations[english_text]
                        translation_count += 1

    if translation_count > 0:
        tree.write(new_file_path, pretty_print=True, encoding='utf-8', xml_declaration=True)
        print(f"Arquivo traduzido salvo em: {new_file_path}")
    else:
        shutil.copy2(file_path, new_file_path)
        print(f"Nenhuma tradução realizada para {file_path}. Arquivo copiado.")

def copy_structure_and_translate(src, dst):
    if not os.path.exists(dst):
        os.makedirs(dst)

    for root, dirs, files in os.walk(src):
        for dir in dirs:
            dest_dir = os.path.join(dst, os.path.relpath(os.path.join(root, dir), src))
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
        for file in files:
            src_file = os.path.join(root, file)
            dst_file = os.path.join(dst, os.path.relpath(src_file, src))
            if src_file.endswith('.xml'):
                process_xml_file(src_file, dst_file)
            else:
                shutil.copy2(src_file, dst_file)

# Diretórios de origem e destino
# Mude a pasta para Anomaly/DefInjected/ ou Anomaly/Keyed/ ou como preferir
src_directory = '../RimWorld-PortugueseBrazilian/Anomaly/DefInjected/'
dst_directory = 'AnomalyPTBR/DefInjected/'
copy_structure_and_translate(src_directory, dst_directory)
