import os
import deepl
from markdown import markdown
import html2text


def translate_files():
    for root, dirs, files in os.walk("patterns"):
        for file in files:
            if file.endswith('system.md'):
                file_path = os.path.join(root, file)
                if os.stat(file_path).st_size > 0:
                    translation = translate_file(file_path)
                    write_path = build_write_path(file_path)
                    write_translation(write_path, translation)
                    exit(0)


def translate_file(file_path):
    print("reading: " + file_path)
    with open(file_path, 'r') as file:
        original_markdown = file.read()
        original_html = convert_to_html(original_markdown)
        translated_html = translator.translate_text(original_html, target_lang="DE", tag_handling="html").text
        translated_markdown = convert_to_markdown(translated_html)
        return translated_markdown


def convert_to_html(original_markdown):
    return markdown(original_markdown)


def convert_to_markdown(translated_html):
    return html2text.handle(translated_html)


def build_write_path(file_path):
    # remove the .md from the end of the file name
    # then append "_de.md"
    name, ext = os.path.splitext(file_path)
    return name + "_de.md"


def write_translation(file_path, translation):
    print("writing: " + file_path)
    with open(file_path, 'w') as f:
        f.write(translation)


def cleanup():
    for root, dirs, files in os.walk("patterns"):
        for file in files:
            if file.endswith('_de.md'):
                os.remove(os.path.join(root, file))


def init_deepl():
    auth_token = os.getenv('DEEPL_AUTH_TOKEN')
    if not auth_token or auth_token.isspace():
        print("Deepl Auth token not found. Please set environment variable DEEPL_AUTH_TOKEN")
        exit(1)
    else:
        print("Found Deepl Auth token! Continuing...")
        return deepl.Translator(auth_token)


translator = init_deepl()
html2text = html2text.HTML2Text()

cleanup()
translate_files()
