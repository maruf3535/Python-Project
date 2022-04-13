from countryinfo import CountryInfo
coun_nm = input("Enter your country: ")
country = CountryInfo(coun_nm)
print("Capital: ", country.capital())
print("currencies: ", country.currencies())
print("languages: ", country.languages())
print("borders: ", country.borders())
print("others names: ", country.alt_spellings())
