import csv
import string
categoryList = ["Professors", "Food", "WiFi", "Clubs", "Library", "Advising",
                    "Wellness", "Tutoring", "Safety", "Events", "Commuting",

            "Residence", "Athletics", "Printing", "Overall", "ChangeOneThing", "BiggestStress", "BestPart"]
def interpretCSV(csvFile):
    '''Converts the CSV file to a dictionary where the
    key is the first value in the row (the name of the category)
    and the value is the list of all the ratings for that category.'''
    resultDict = {
    "Professors": [],
    "Food": [],
    "WiFi": [],
    "Clubs": [],
    "Library": [],
    "Advising": [],
    "Wellness": [],
    "Tutoring": [],
    "Safety": [],
    "Events": [],
    "Commuting": [],
    "Residence": [],
    "Athletics": [],
    "Printing": [],
    "Overall": [],
    "ChangeOneThing": [],
    "BiggestStress": [],
    "BestPart": []}
    #setting up csv reader
    with open(csvFile, newline = '') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
        for i in range(18):
            for num in range(len(rows)-1):
                currentRow = rows[num+1]
                currentCell = currentRow[i]
                currentCategory = categoryList[i]
                resultDict[currentCategory].append(currentCell)
    return resultDict


def keyWords(qualCategoryDict, catName):
    '''takes a dictionary qualCategory as input and returns a dictionary with
rating-frequency as key-value pair'''
    #should already have import string established
    uselessWords = ["a", "an", "the", "about", "above", "across", "after", "at","more","longer","better"
                    "before", "behind", "between", "by", "better" , "for", "from", "in", "into", "of", "on",
                    "over", "through", "to", "under", "with", "and", "as", "but", "or", "since",
                    "until", "while", "he", "her", "his", "i", "free", "fix","it", "me", "my", "our", "she", "that", "their", "them",
                    "they", "us", "we", "what", "which", "who", "you", "am", "are", "be", "been", "being", "did", "do",
                    "does", "is", "was", "were", "almost", "actually", "basically", "completely", "could", "definitely",
                    "even", "just", "literally", "may", "might", "much", "only", "quite", "rather", "really", "somewhat",
                    "sure", "then", "too", "totally", "very", "will", "would", "all", "any", "get", "go",
                    "has", "have", "had", "how","every" , "day", "slow", "if", "not", "so","spots","made","center","helps","made","good","equipment","options","students","make","campus","less" ,"up", "when", "where", "why", "i've"]
    diffWords = {}
    for rating in qualCategoryDict[catName]:
        separate = rating.split()
        for i in range(len(separate)):
            separate[i] = separate[i].strip(string.punctuation)
        for word in separate:
            if word.lower() in uselessWords:
                continue
            elif word.lower() not in diffWords:
                diffWords[word.lower()] = 1
            elif word.lower() in diffWords:
                diffWords[word.lower()] += 1 
    return diffWords



def maxFreqWord(wordFreq):
    '''takes a dictionary wordFreq (the result of keyWords) as input and returns the word that has the highest frequency and corresponding count in a tuple'''
    maxFreqCount = 0
    maxFreqCat = []
    for cat in wordFreq:
        if wordFreq[cat] > maxFreqCount:
            maxFreqCount = wordFreq[cat]
            maxFreqCat = [cat]
        elif wordFreq[cat] == maxFreqCount:
            maxFreqCat.append(cat)
    return maxFreqCat, maxFreqCount



def cleanQuantData(quantCategoriesDict):
    '''takes a dictionary quantCategoriesDict as input and returns a dictionary with key being the category name and value as the cleaned data in the form of list'''
    validNums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
#establishes the dictionary for cleaned data
    dataLst={}
#adds each category to the dictionary as a key and assigns empty list
    for entries in quantCategoriesDict:
       dataLst[entries] = []
#cleans data by going through previous dictionary and adding the cleaned values to dataLst
    for entry in dataLst:
        values = quantCategoriesDict[entry]
        for rating in values:
            if rating not in validNums or rating == "":
                continue
            else:
                rating = int(rating)
            if rating<=5 and rating>=1:
                dataLst[entry].append(rating)
            if rating>5 and rating<=10:
                 dataLst[entry].append(rating//2)
    return dataLst




def calAverage(quantCategoriesDict):
    '''takes a dictionary quantCategoriesDict as input and returns the category name along with its average rating in a tuple'''
    averageAssign = {}
    for category in quantCategoriesDict:
        ratings = quantCategoriesDict[category]  #is a list
        total = 0
        for value in ratings:
            total += value
        averageRating = total/len(ratings)
        averageRatingRounded= round(averageRating,3)
        averageAssign[category] = averageRatingRounded
    return averageAssign 

def mostPolarizingWord(changeOneThingWords, bestPartWords):
    '''takes the count of each word in ChangeOneThing and BestPart and sums them, then returns the word with the highest count and its count as a tuple'''
    polarizingSum = {}
    maxFreqCount = 0
    mostPolarizingWord = ""
    for word in (changeOneThingWords.keys() & bestPartWords.keys()):
        polarizingSum[word] = int(changeOneThingWords[word]) + int(bestPartWords[word])
        if polarizingSum[word] > maxFreqCount:
            maxFreqCount = polarizingSum[word]
            mostPolarizingWord = word
    return (mostPolarizingWord, maxFreqCount)

def maxRatingCat():
     '''Returns the category with maximum rating'''
     cleanQuantDataDict= cleanQuantData(quantData)
     quantDataAvgDict=calAverage(cleanQuantDataDict)
     maxRating=0
     maxRatingCat=""
     for key in quantDataAvgDict:
         rating=quantDataAvgDict[key]
         if rating>maxRating:
             maxRating=rating
             maxRatingCat=key
     return (maxRating, maxRatingCat)

#Showcase

inFile="C:\\Users\\kanik\\Downloads\\sampleStudentSurvey_Data.csv"
wholeData = interpretCSV(inFile)

quantData = {}
everyCategory = list(wholeData.keys())
for i in range(15):
    cat = everyCategory[i] 
    quantData[cat] = wholeData[cat]

qualData= {}
for i in range(15,18):
    cat = everyCategory[i] 
    qualData[cat] = wholeData[cat]

changeOneThingDict={}
changeOneThingDict["ChangeOneThing"]=qualData["ChangeOneThing"]

biggestStressDict={}
biggestStressDict["BiggestStress"]=qualData["BiggestStress"]

bestPartDict={}
bestPartDict["BestPart"]=qualData["BestPart"]

keyChangeOneThingDict=keyWords(changeOneThingDict,"ChangeOneThing")
keyBiggestStressDict=keyWords(biggestStressDict,"BiggestStress")
keyBestPartDict=keyWords(bestPartDict,"BestPart")

changeOneThingMaxFreqWord = maxFreqWord(keyChangeOneThingDict)
biggestStressMaxFreqWord = maxFreqWord(keyBiggestStressDict)
bestPartMaxFreqWord = maxFreqWord(keyBestPartDict)

cleanQuantDataDict = cleanQuantData(quantData)

avg = calAverage(cleanQuantDataDict)

mostPolWord = mostPolarizingWord(keyChangeOneThingDict,keyBestPartDict)

maxRat = maxRatingCat()
