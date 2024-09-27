# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 12:08:55 2023

@author: macse
"""

import tkinter as tk
from tkinter import ttk
import re

root = tk.Tk()

textBox = tk.Text(root)
bigramFreq = {}
trigramFreq = {}

#Load corpus and store word frequencies
def load_corpus(filename):
    freq = {}
    
    global wordProb
    
    totalWords = 0
    count = 0
    
    #Read every sentence of the corpus individually
    for piece in open(filename, encoding="utf-8").read().lower().split("\n"):    
        
        count = 0
        previousWord, wordBefore = "", ""
        
        for words in piece.split():
                
            #Get words from the characters - words can include letters, apostrophes or hyphens
            #Based on Goodrich (2013)'s method (see reference list in report)
            word = ''.join(c for c in words if (c.isalpha() or c == "'" or c == "-"))
            
            if word:
                freq[word] = 1 + freq.get(word, 0)
                
            if count == 0:
                #Do nothing
                pass
            
            #Fill in the bigrams
            elif count == 1:
                bigram = previousWord + " " + word
                bigramFreq[bigram] = 1 + bigramFreq.get(bigram, 0)
            
            #Fill both bigram and trigram
            else:
                bigram = previousWord + " " + word
                bigramFreq[bigram] = 1 + bigramFreq.get(bigram, 0)
                
                trigram = wordBefore + " " + previousWord + " " + word
                trigramFreq[trigram] = 1 + trigramFreq.get(trigram, 0)
                
            #Update before next iteration
            count += 1
            wordBefore = previousWord
            previousWord = word
                
    #Next, count the number of total words in the corpus (float since we will divide with this number)
    totalWords = float(sum(freq.values()))
    
    #Calculate and store probabilities for all words
    wordProb = {word: float(freq[word]) / totalWords for word in freq.keys()}
    
# ----- EDIT DISTANCE ALGORITHM - BASED ON NORVIG'S SPELLCHECKER (https://norvig.com/spell-correct.html)  -----    
    
#Given a word, return all words with a Levenshtein distance of 1
def edit_distance_1(word):
    #NOTE - 'k', 'q', 'v', 'x' and 'z' are not in the Welsh language    
    letters = "abcdefghijlmnoprstuwyâêîôûŷŵ"
    
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    delete = [left + right[1:] for left, right in splits if right]
    transpose = [left + right[1] + right[0] + right[2:] for left, right in splits if len(right) > 1]
    replace = [left + c + right[1:] for left, right in splits if right for c in letters]
    insert = [left + c + right for left, right in splits for c in letters]
    
    return set(delete + transpose + replace + insert)

#After generating all words within the Levenshtein distance, check which words actually exist (i.e. in the corpus) and return their probability
def real_words(words):     
    return {w : wordProb.get(w) for w in words if w in wordProb}

#Check whether words are spelled correctly 
def check(word):
    if word in wordProb or word == "":
        return("Word is spelled correctly")
    
    #Firstly check all possible words within Levenshtein distance of 1
    nearbyWords = edit_distance_1(word)
    
    #Find all words included in corpus
    real = real_words(nearbyWords)
    
    #If there aren't enough words with Levenshtein distance of 1, check for those with 2
    if len(real) < 5:
        #Give priority to words with Levenshtein distance of 1 (increase their probability)
        for k in real.keys():
            wordProb[k] += 1.0
        
        #Include words that have Levenshtein distance of 2
        for words in nearbyWords:
            real.update(real_words(edit_distance_1(words)))
    
    
    #Check whether any real words were found
    if len(real) > 0:    
        #Sort the real words by word probability
        bestSuggestions = sorted(real.items(), key=lambda item: item[1], reverse=True)
        top5 = []
        for count, item in enumerate(bestSuggestions):
            if count == 5:
                break
            
            top5.append(item[0])
        return top5
    else:
        return("Word is spelled incorrectly - no suggestions found")
        
# ---------------- Checking Real Word Errors --------------------------

def check_real_word_error(wordBefore, previousWord, currentWord):
    #Despite being the previous word, this word is the center of the checks
    alternatives = real_words(edit_distance_1(previousWord))

    leftTotal = 0
    rightTotal = 0
    trigramTotal = 0
    
    #Count the number of occurrences of each bigram/trigram
    for possibleWord in alternatives:    
        #Check left bigram
        possibleLBigram = wordBefore + " " + possibleWord
        lFrequency = bigramFreq.get(possibleLBigram)
        if lFrequency:
            leftTotal += lFrequency 
        
        #Check right bigram
        possibleRBigram = possibleWord + " " + currentWord
        rFrequency = bigramFreq.get(possibleRBigram)
        if rFrequency:
            rightTotal += rFrequency
    
        #Check trigram
        possibleTrigram = wordBefore + " " + possibleWord + " " + currentWord
        triFrequency = trigramFreq.get(possibleTrigram)
        if triFrequency:
            trigramTotal += triFrequency
    
    correctWordProbability = {}
    
    for possibleWord in alternatives:
        
        #Calculate probability of each word being the most suitable
        possibleLBigram = wordBefore + " " + possibleWord
        if bigramFreq.get(possibleLBigram):
            leftProbability = float(bigramFreq.get(possibleLBigram)) / leftTotal
        else:
            leftProbability = 0
        
        possibleRBigram = possibleWord + " " + currentWord
        if bigramFreq.get(possibleRBigram):
            rightProbability = float(bigramFreq.get(possibleRBigram)) / rightTotal
        else:
            rightProbability = 0
            
        
        possibleTrigram = wordBefore + " " + possibleWord +  " " + currentWord
        if trigramFreq.get(possibleTrigram):
            trigramProbability = float(trigramFreq.get(possibleTrigram)) / trigramTotal
        else:
            trigramProbability = 0
        
        correctWordProbability[possibleWord] = leftProbability + rightProbability + trigramProbability
        
    #Discover whether the most probable word matches the word that was entered
    best = max(correctWordProbability.items(), key = lambda item: item[1])
    bestWord = best[0]
    
    #If probabilities are the same, just keep the original word
    if correctWordProbability.get(bestWord) == correctWordProbability.get(previousWord):
        bestWord = previousWord
    
    return bestWord
    
#------------------------ GUI WINDOW ----------------------------------
def window():
    
    #Window Setup
    
    root.geometry("1080x720")
    root.title("Welsh Spell Checker")
    
    
    #Ensure this window always pops up (rather than behind other windows)
    root.attributes('-topmost', 1)    
    
    title = tk.Label (root, text="Spell Checker", font = (None, 50, 'bold'))
    title.pack()
    
    inputLabel = tk.Label(root, text="Enter word:", font = (None, 18))
    inputLabel.pack()
    
    textBox.pack()
    
    #When the button is pressed, we pass the value to the check function
    button = tk.Button(root, text="Check Spelling", command=submit, font = (None, 14))
    button.pack(pady = 10)
    
    root.mainloop()

def submit():
    #Return the result from the check
    inputText = textBox.get(1.0, "end-1c").lower()
    
    
    #Split the string using characters that split up the sentences e.g. commas, full stops, question marks etc.
    text = re.split(r'[.,!?;:()]', inputText)
    allCorrect = True
    
    for sentence in text:    
        count = 0
        previousWord = ""
        wordBefore = ""
        
        for word in sentence.split():
            count += 1
            #Check for errors            
            top5 = check(word)
                
            if count > 2:
                #Only check for real word errors when all words are spelled correctly 
                if len(real_words({wordBefore, previousWord, word})) == 3:
                    bestWord = check_real_word_error(wordBefore, previousWord, word)
                    
                    if bestWord != previousWord:
                        allCorrect = False
                        
                        realWordFrame = tk.Frame(root)
                        
                        suggestionLabel = tk.Label(realWordFrame, text = "Potential Error - Did you mean: ", font=(None, 14))
                        suggestionLabel.pack()
                        
                        exampleSentenceText = wordBefore + " " + bestWord + " " + word
                        exampleSentence = tk.Label(realWordFrame, text = exampleSentenceText, font = (None, 14))
                        exampleSentence.pack()
                        
                        buttonFrame = tk.Frame(realWordFrame)
        
                        acceptChange = tk.IntVar()
                        acceptChange.set(0)
                        
                        acceptButton = tk.Button(buttonFrame, text="Accept", command=lambda: acceptChange.set(1), font = (None, 14))
                        acceptButton.grid(row = 0, column = 0, padx=10, pady = 10)
                
                        ignoreButton = tk.Button(buttonFrame, text="Ignore", command=lambda: acceptChange.set(2), font = (None, 14))
                        ignoreButton.grid(row=0, column=1, padx=10, pady = 10)
                
                        buttonFrame.pack()
                        
                        realWordFrame.pack()
                        
                        realWordFrame.wait_variable(acceptChange)
                        
                         #Accepting the change
                        if acceptChange.get() == 1:
                            wholeText = textBox.get(1.0, "end-1c")
                            oldTrigram = wordBefore + " " + previousWord + " " + word
                            
                            textBox.delete(1.0, "end-1c")
                            textBox.insert(1.0, wholeText.replace(oldTrigram, exampleSentenceText, 1))
                            
                            #Update the check
                            previousWord = bestWord
                            
                            
                            close(realWordFrame)
                    
                        if acceptChange.get() == 2:
                            close(realWordFrame)
    
    
                        
            #If everything is correct, place label underneath box
            if(top5 == "Word is spelled correctly"):
                    pass
                        
                        
            #Incorrect spelling but no suggestions - give message but don't move on until acknowledgement
            elif top5 == "Word is spelled incorrectly - no suggestions found":
                allCorrect = False
                acknowledge = tk.IntVar()
                acknowledge.set(0)
                noSuggestFrame = tk.Frame(root)
                
                noSuggestionText = "Mispelled Word - " + word + ", no suggestions found"
                noSuggestion = tk.Label(noSuggestFrame, text = noSuggestionText, font = (None, 14))
                noSuggestion.pack()
                
                okButton = tk.Button(noSuggestFrame, text = "OK", command=lambda: acknowledge.set(1), font = (None, 14))
                okButton.pack()
                
                noSuggestFrame.pack()
                
                #Wait - don't contine the program until the user presses "OK"
                noSuggestFrame.wait_variable(acknowledge)
                
                close(noSuggestFrame)
                        
                    
            #If there are suggestions, list them underneath the box
            else:
                allCorrect = False
                suggestionsFrame = tk.Frame(root)
            
                descriptionText = "Misspelled Word - " + word + ", possible words include:"
                description = tk.Label(suggestionsFrame, text = descriptionText, font = (None, 14))
                description.pack()
                
                combo = ttk.Combobox(suggestionsFrame, font = (None, 14))
                combo['values'] = top5
                combo.current(0)
                combo.pack()
                buttonFrame = tk.Frame(suggestionsFrame)
        
                acceptChange = tk.IntVar()
                acceptChange.set(0)
                acceptButton = tk.Button(buttonFrame, text="Accept", command=lambda: acceptChange.set(1), font = (None, 14))
                acceptButton.grid(row = 0, column = 0, padx=10, pady = 10)
                
                ignoreButton = tk.Button(buttonFrame, text="Ignore", command=lambda: acceptChange.set(2), font = (None, 14))
                ignoreButton.grid(row=0, column=1, padx=10, pady = 10)
                
                buttonFrame.pack()
                
                suggestionsFrame.pack()
                
                #Pause the program until either the "Accept" or "Ignore" button is pressed
                suggestionsFrame.wait_variable(acceptChange)
                
                
                #Accepting the change
                if acceptChange.get() == 1:
                    wholeText = textBox.get(1.0, "end-1c")
                       
                    textBox.delete(1.0, "end-1c")
                    textBox.insert(1.0, wholeText.replace(word, combo.get(), 1))
                    close(suggestionsFrame)
                    
                if acceptChange.get() == 2:
                    close(suggestionsFrame)
            
            
            #Set up the next iteration
            if count > 1:
                wordBefore = previousWord
            
            previousWord = word
            
    #After looping through the whole entry box, we check whether allCorrect has been changed
    #If allCorrect is true, we display a message saying that it's correct
    if allCorrect == True:
        correctFrame = tk.Frame(root)
        suggestions = tk.Label(correctFrame, text = "Everything is spelt correctly", font = (None, 14))
        suggestions.pack()
                      
        okButton = tk.Button(correctFrame, text = "OK", command=lambda: close(correctFrame), font = (None, 14))
        okButton.pack()
                        
        correctFrame.pack()
            

#Closes the window that gets passed to it
def close(window):
    window.destroy()
    
if __name__ == "__main__":
    load_corpus("corpus.txt")
    window()