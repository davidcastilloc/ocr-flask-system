import pytesseract
def extract_text_from_recipe(route_img_recipe):
    custom_config = r'--oem 3 --psm 6 --user-words "spa.user-words"'
    items = pytesseract.image_to_string(route_img_recipe, lang='spa', config=custom_config).lower().split(" ")
    items_filtered = [item for item in items if len(item) > 8]
    return items_filtered
