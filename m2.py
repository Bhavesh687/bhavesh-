import phonenumbers
from phonenumbers import geocoder, carrier, timezone

# Enter the mobile number with country code (e.g., +91 for India, +1 for USA)
number = "+919247291794"

# Parse the number
parsed_number = phonenumbers.parse(number)

# Get country/region
location = geocoder.description_for_number(parsed_number, "en")

# Get service provider
service_provider = carrier.name_for_number(parsed_number, "en")

# Get possible timezones
time_zones = timezone.time_zones_for_number(parsed_number)

# Output the info
print("Phone Number:", number)
print("Location (Region):", location)
print("Carrier:", service_provider)
print("Time Zones:", time_zones)
