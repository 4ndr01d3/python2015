dna = "tacgtcaTgtcgaTTTtagcttttTTTTacgtcagtacgtcagtcagtgactgctagttttcgatgcatgctaggctag"

#Creating a uppercase copy of my DNA
copydna=""
for i in range(len(dna)):
    if dna[i]=="a":
        copydna=copydna+"A"
    elif dna[i]=="c":
        copydna=copydna+"C"
    elif dna[i]=="g":
        copydna=copydna+"G"
    elif dna[i]=="t":
        copydna=copydna+"T"
    else:
        copydna=copydna+dna[i]


#Reverse by using negative indexes
reverse=""
for i in range(1,len(copydna)+1):
    reverse = reverse + copydna[-i]

#Reverse by using negative indexes
reverse2=""
for i in range(len(copydna)):
    reverse2 =  copydna[i] + reverse2



#RNA
rna=""
for i in range(len(reverse)):
    if reverse[i] == "T":
        rna = rna + "U"
    else:
        rna = rna + reverse[i]

countG = 0
countA = 0
countU = 0
countC = 0
for i in range(len(rna)):
    if rna[i] == "G":
        countG = countG+1
    if rna[i] == "A":
        countA = countA+1
    if rna[i] == "U":
        countU = countU+1
    if rna[i] == "C":
        countC = countC+1


GC_ratio = (countG+countC)/len(rna)

print (dna)
print (dna.upper())
print (copydna)
print (reverse)
print (reverse2)
print (copydna[::-1])
print (reverse==reverse2)
print (rna)
print(reverse.replace("T","U"))
print ("There are",countG,"Gs")
print ("There are",countA,"As")
print ("There are",countC,"Cs")
print ("There are",countU,"Us")
print("The length of my sequence is",countG+countC+countA+countU)
print("The length of my sequence is",len(rna))
print("The GC ratio of my sequence is", GC_ratio)