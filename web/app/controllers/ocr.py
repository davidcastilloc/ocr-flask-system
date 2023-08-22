import pytesseract
from cleantext import clean
import string


def extract_raw_text_from_recipe(route_img_recipe):
    custom_config = r'--oem 3 --psm 6 --user-words "spa.user-words"'
    raw_text = pytesseract.image_to_string(
        route_img_recipe, lang='spa', config=custom_config)
    return raw_text


def clean_raw_text(raw_text):
    cleaned_text = clean(raw_text, fix_unicode=True,
                         to_ascii=True,
                         lower=True,
                         no_line_breaks=False,
                         no_urls=True,
                         no_emails=True,
                         no_phone_numbers=True,
                         no_numbers=True,
                         no_digits=True,
                         no_currency_symbols=False,
                         no_punct=True,
                         replace_with_punct="",
                         replace_with_url="",
                         replace_with_email="",
                         replace_with_phone_number="",
                         replace_with_number="",
                         replace_with_digit="",
                         replace_with_currency_symbol="<CUR>",
                         lang="en")
    return cleaned_text


def extract_words_from_cleaned_text_and_return_list(cleaned_text):
    return [word.strip(string.punctuation) for word in cleaned_text.split() if word.strip(string.punctuation).isalnum() and len(word) > 9]


def remove_duplicates_on_list(list_words):
    return list(set(list_words))


def read_glosary_and_return_list(route_glosary='code/app/spa.user-words'):
    with open(route_glosary) as f:
        glosary = f.read()
    return glosary.split("\n")


def return_word_if_matches_on_glosary(word, glosary):
    return list(filter(lambda a: word in a, glosary))[-1]  # return last match


def get_recipe_list_items(route_uploaded_img_recipe="./app/static/img/text.png"):
    raw_text = extract_raw_text_from_recipe("./app/static/uploads/" + route_uploaded_img_recipe)
    cleaned_text = clean_raw_text(raw_text)
    words_extracted = extract_words_from_cleaned_text_and_return_list(
        cleaned_text)
    return remove_duplicates_on_list(words_extracted)
