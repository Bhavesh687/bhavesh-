import phonenumbers
from phonenumbers import geocoder, carrier, timezone

# Replace this with the phone number you want to look up (with country code)
number = "+14155552671"

# Parse the number
parsed_number = phonenumbers.parse(number)

# Get location (geographical)
location = geocoder.description_for_number(parsed_number, "en")

# Get carrier
sim_carrier = carrier.name_for_number(parsed_number, "en")

# Get timezones
time_zones = timezone.time_zones_for_number(parsed_number)

print("Number:", number)
print("Location:", location)
print("Carrier:", sim_carrier)
print("Timezones:", time_zones)
