import pandas as pd
from datetime import date

from utils import convert_countrycode, convert_personnummer, convert_postnr, \
    clean_pii_comments, convert_mc_groups_to_io_groups, one_mc_groupto_io

data = {'Fruits': ['BANANA','APPLE','','WATERMELON','PEAR'],
        'Fruits2': ['BANANA','APPLE','MANGO','WATERMELON','PEAR'],
        'Price': [0.5,1,1.5,2.5,1]
        }

df = pd.DataFrame(data, columns = ['Fruits','Fruits2', 'Price'])

#df['Fruits'] = df['Fruits'].str.lower()
df['Fruits'] = df['Fruits'].apply(lambda x:x.lower())
df['Fruits2'] = df['Fruits2'].str.casefold()

print (df)

assert ('HISINGS BACKA'.title() == "Hisings Backa")
assert ('GÖTEBORG'.title() == "Göteborg")

# Verify convert_postnr
assert (convert_postnr(0) == "0")
assert (convert_postnr(12345) == "123 45")
assert (convert_postnr('543 21') == "543 21")

# Verify clean_pii_comments
assert (clean_pii_comments("1234 Test1") == "Test1")
assert (clean_pii_comments("2008 Test2") == "2008 Test2")
assert (clean_pii_comments("-1234 Test3") == "Test3")
assert (clean_pii_comments("-1234Test4") == "Test4")
assert (clean_pii_comments("2013 Test5") == "2013 Test5")
assert (clean_pii_comments("-123s4Test6") == "-123s4Test6")
assert (clean_pii_comments("123s4Test7") == "123s4Test7")
assert (clean_pii_comments("-7134se Johan") == "se Johan")
assert (clean_pii_comments("") == "")

# Test group handling
print(convert_mc_groups_to_io_groups("Orientering, Medlemmar"))
assert (convert_mc_groups_to_io_groups("Orientering, Medlemmar") == "MC_OL, MC_Medlemmar")
assert (convert_mc_groups_to_io_groups("Orientering, Medlemmar, Senior") == "MC_OL, MC_Medlemmar, Senior")
print(convert_mc_groups_to_io_groups("styrelsen, Medlemmar"))
assert (convert_mc_groups_to_io_groups("styrelsen, Medlemmar") == "Styrelse SFK, MC_Medlemmar")
assert (convert_mc_groups_to_io_groups("Huvudsektion,styrelsen, Medlemmar") == "MC_Huvudsektion, Styrelse SFK, MC_Medlemmar")

# Dates

today = date.today()
today = date.fromisoformat("2020-03-01")
date_today = today.strftime("%Y-%m-%d")
print(date_today)