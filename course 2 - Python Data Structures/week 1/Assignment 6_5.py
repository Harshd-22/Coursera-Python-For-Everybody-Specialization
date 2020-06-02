text = "X-DSPAM-Confidence:    0.8475";
pos = text.find("0")
s_data = text[pos:]
f_data = float(s_data)
print(f_data)