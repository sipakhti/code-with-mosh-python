from collections import OrderedDict

fav_lang = OrderedDict()

fav_lang["jen"] = "python"
fav_lang["sarah"] = "c"
fav_lang["edward"] = "ruby"
fav_lang["phill"] = "python"

for name, language in fav_lang.items():
    print(f"{name.title()}'s favourite language is {language.title()}. ")


