s_score = input("Enter Score: ")

i_score = float(s_score)

if i_score <= 1.0 and i_score >= 0.9 :
    print("A")
elif i_score < 0.9 and i_score >= 0.8 :
    print("B")
elif i_score < 0.8 and i_score >= 0.7 :
    print("C")
elif i_score < 0.7 and i_score >= 0.6 :
    print("D")    
elif i_score < 0.6 and i_score >= 0.0 :
    print("F")
else :
    print("error")  