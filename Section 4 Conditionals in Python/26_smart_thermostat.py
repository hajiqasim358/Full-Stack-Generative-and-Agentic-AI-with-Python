device_status = input("Enter the device status (Active, Inactive): ").lower()
temperature = float(input("Enter current temperature: "))

if device_status == "active":
    if temperature > 35:
        print("High temperature detected!")
    else:
        print("Temperature is normal.")
else:
    print("Device inactive! Please activate the device to check the temperature.")