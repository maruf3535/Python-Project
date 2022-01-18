import phonenumbers
from phonenumbers import timezone, geocoder, carrier
number = "+8801405803576"
number2 = phonenumbers.parse(number)
number3 = timezone.time_zones_for_number(number2)
number5 = geocoder.description_for_number(number2, 'en')
number6 = carrier.name_for_number(number2, 'en')
number7 = phonenumbers.is_possible_number(number2)
number8 = phonenumbers.is_valid_number(number2)

print("phone_number = '", number, "'") # phone_number
print("basic details of phone_number = '", number2, "'") # basic details of phone_number
print("timezone of phone_number = '", number3, "'") # timezone of phone_number
print("country_name of phone_number = '", number5, "'") # country_name of phone_number
print("carrier of phone_number (oparator name) = '", number6, "'") # carrier of phone_number (oparator name)

if number7 == True: # possibility of phone_number
    print("Is number possible? 'Yes'")
elif number7 == False:
    print("Is number possible? 'No'")

if number8 == True: # validity of phone_number
    print("Is number valid? 'Yes'")
elif number8 == False:
    print("Is number valid? 'No'")