import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
from opencage.geocoder import OpenCageGeocode
from pprint import pprint
from phone_data import number, key


# getting phone number
ph_num = phonenumbers.parse(number)
print("[+] Phone Number: %s" % ph_num)

# testing phone number
is_possible = phonenumbers.is_possible_number(ph_num)
is_valid = phonenumbers.is_valid_number(ph_num)
inter_national_format = phonenumbers.format_number(ph_num, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
print("[+] IS Valid: %s" % is_valid)
print("[+] IS Possible: %s" % is_possible)
print("[+] IN Formatted: %s" % inter_national_format)

# getting country of given phone number
ch_number = phonenumbers.parse(number, "CH")
country = geocoder.description_for_number(ch_number, "en")
print("[+] Country: %s" % country)

# getting service provider of phone number
service_provider = phonenumbers.parse(number, "RO")
service_pro = carrier.name_for_number(service_provider, "en")
print("[+] Service Provider: %s" % service_pro)

# getting time zones list
gb_number = phonenumbers.parse(number, "GB")
time_zone = timezone.time_zones_for_number(gb_number)
print("[+] Time Zone: %s" % time_zone)


geocoder = OpenCageGeocode(key)
locator = geocoder.geocode(country, no_annotations=1, language='en')
first_bounds_location = locator[0]["bounds"]
first_components_location = locator[0]['components']
first_confidence_location = locator[0]['confidence']
first_geometry_location = locator[0]['geometry']

print(f"\n[+]Bounds: \n")
pprint(first_bounds_location)
print("\n[+]Components: \n")
pprint(first_components_location)
print("\n[+]Confidence: \n")
pprint(first_confidence_location)
print("\n[+]Geometry: \n")
pprint(first_geometry_location)
