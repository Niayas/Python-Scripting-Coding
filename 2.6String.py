import random as r
import os
def generatePhrase():
    nouns=("puppy","car","rabbit","girl","monkey")
    verbs=("runs","hits","jumps","drives","barfs")
    adverbs=("crazily","dutifully","foolishly","merrily","occasionally")
    adjectives=("adorable","clueless","dirty","odd","stupid")
    articles=("the","a","an")

    pickNoun=nouns[r.randint(0,len(nouns)-1)]
    pickVerb=verbs[r.randint(0,len(verbs)-1)]
    pickAdverb=adverbs[r.randint(0,len(adverbs)-1)]
    pickAdjective=adjectives[r.randint(0,len(adjectives)-1)]
    pickArticles=articles[r.randint(0,len(articles)-1)]

    sentence=pickArticles+" "+pickAdjective+" "+pickNoun+" "+pickVerb+" "+pickAdverb
    

    return sentence
def maskSentence(original):
    masked=[]
    for char in original:
        if char == " ":
            masked.append(" ")
        else: masked.append("-")
    return masked

def printCharList(characterList):
    for letter in characterList:
        print(letter,end="")
        
def replaceLetter(original,masked,letter):
    position=0
    letter=letter.upper()
    while position !=-1:
        position=original.find(letter,position,len(original))
        if position != -1:
            masked[position]=letter
            position+=1
    return masked
        
def main():
    os.system("cls")
    sentence=generatePhrase()
    sentence=sentence.upper()
    print(sentence)
    
    #print(sentence)
    masked=maskSentence(sentence)
    printCharList(masked)

    while "-" in masked:
        #os.system("cls")
        letter=input("Try guessing a letter: ")
        masked=replaceLetter(sentence,masked,letter)
        printCharList(masked)

    print("Congratulations!! you won")
    
main()
