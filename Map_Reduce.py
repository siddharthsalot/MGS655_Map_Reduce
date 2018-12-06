def Mapper(vowel, word):
    """
       Mapper function which takes input as a vowel and a word
       in which count of the vowel needs to be determined
       Inputs:
           string   vowel(Key/url)   Singler character. Possible values: a,e,i,o,u,A,E,I,O,U
           string   word(values)     The word in which count of vowel is determined
       Output:
           returns a dictionary with vowel as the key and its corresponding
           count in word as value.
    """
    vowelCount = {}
    vowelCount.update({vowel: word.count(vowel)})
    if(word.count(vowel) > 0):
        return vowelCount
    else:
        return {}

def Reducer(word, vowelCount):
    """
       Reducer function which takes Intermediate output of mapper as input
       Inputs:
           string   vowel(Key/url)   Singler character. Possible values: a,e,i,etc.
           string   word(values)     The word in which count of vowel is determined
       Output:
           returns a dictionary with vowel as the key and its corresponding
           count in word as value.
    """
    totalVowelCount = 0
    reducerOutput = {}
    for vc in vowelCount:
        for key,value in vc.iteritems():
            totalVowelCount += value

    reducerOutput.update({word: totalVowelCount})
    return reducerOutput
        
## Input test string
testString = """My introduction to the world of Nature was a painful one.
                Aged five, I was coming down the spiral staircase from the
                roof of our bungalow, when inadvertently I dislodged a beehive
                under one of the steps. I was immediately attacked by a swarm
                of angry bees, who proceeded to sting me on my face, arms and legs.
                I got down the stairs and ran indoors screaming for help.
                [Adapted from ""Nature"", Ruskin Bond] """

## Split input string into a word list
wordList = testString.split()

## Create an intermediate output dictionary. Each output of the mapper will be stored in this list.
intermediateOutput = {}

## Create final output list containing words and their corresponding vowels
final_output = []

## Iterate through each word in the wordlist and pass it to the mapper function
for word in wordList:
    totalCount = 0
    wordVowelCount = []
    for vowel in 'aeiou':
        mapEmit = (Mapper(vowel, word.lower()))
        if(mapEmit):
            wordVowelCount.append(mapEmit.copy())
    if((len(wordVowelCount) > 0) and not intermediateOutput.has_key(word)):
        intermediateOutput.update({word: wordVowelCount})

for word in wordList:
    if(intermediateOutput.has_key(word)):
        final_output.append(Reducer(word, intermediateOutput[word]))

print "Intermediate Values:- ", intermediateOutput
print "\nReducer Output:- ", final_output
