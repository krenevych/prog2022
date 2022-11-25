donor = input()
recipient = input()

freq_donor = {c: donor.count(c) for c in donor}
freq_recipient = {c: recipient.count(c) for c in recipient}

# print(freq_donor)
# print(freq_recipient)

for ch, count in freq_recipient.items():
    if count > freq_donor[ch]:
        print("No")
        break
else:
    print("Ok")
