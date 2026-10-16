usage = float(input("Enter the usage in kWh: "))
if usage < 0:
    print("Invalid usage")
else:
    if usage <= 100:
        azn_per_kwh = 0.08
    elif usage <= 300:
        azn_per_kwh = 0.12
    elif usage > 300:
        azn_per_kwh = 0.15
        bill = usage * azn_per_kwh
        print(usage, azn_per_kwh, bill)