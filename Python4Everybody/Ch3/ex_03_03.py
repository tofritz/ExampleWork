score = input("Enter Score: ")
try :
    fscore = float(score)
except :
    print("Please enter a score between 0.00 and 1.00")
    quit()

if fscore >= 0.9 :
    print("A")
elif fscore >= 0.8 :
    print("B")
elif fscore >= 0.7 :
    print("C")
elif fscore >= 0.6 :
    print("C")
else :
    print("F")
