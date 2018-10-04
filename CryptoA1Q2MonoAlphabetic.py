class Frequency:
    def __init__(self, letter, frequency):
        self.letter = letter
        self.frequency = frequency
    def increment(self):
        self.frequency += 1
    def convertToDecimal(self, totalCharacters):
        self.frequency = (self.frequency / totalCharacters)
    def equals(self, newLetter):
        return self.letter == newLetter
    def __str__(self):
        return self.letter + ': ' + str(self.frequency)
    def __repr__(self):
        return self.letter + ': ' + str(self.frequency)

MODE = "SHIFT" #"VIGENERE"/"SHIFT"/"MONOALPHABETIC"
FREQUENCY_SUM_OF_SQUARES = 0.065

ENGLISH_LETTER_FREQUENCIES = [
    Frequency('e', 0.127),
    Frequency('t', 0.091),
    Frequency('a', 0.082),
    Frequency('o', 0.075),
    Frequency('i', 0.070),
    Frequency('n', 0.067),
    Frequency('s', 0.063),
    Frequency('h', 0.061),
    Frequency('r', 0.060),
    Frequency('d', 0.043),
    Frequency('l', 0.040),
    Frequency('c', 0.028),
    Frequency('u', 0.028),
    Frequency('w', 0.024),
    Frequency('m', 0.024),
    Frequency('f', 0.022),
    Frequency('y', 0.020),
    Frequency('g', 0.020),
    Frequency('p', 0.019),
    Frequency('b', 0.015),
    Frequency('v', 0.010),
    Frequency('k', 0.008),
    Frequency('j', 0.002),
    Frequency('x', 0.002),
    Frequency('z', 0.001),
    Frequency('q', 0.001)
]

CIPHERTEXT = "JGRMQOYGHMVBJWRWQFPWHGFFDQGFPFZRKBEEBJIZQQOCIBZKLFAFGQVFZFWWEOGWOPFGFHWOLPHLRLOLFDMFGQWBLWBWQOLKFWBYLBLYLFSFLJGRMQBOLWJVFPFWQVHQWFFPQOQVFPQOCFPOGFWFJIGFQVHLHLROQVFGWJVFPFOLFHGQVQVFILEOGQILHQFQGIQVVOSFAFGBWQVHQWIJVWJVFPFWHGFIWIHZZRQGBABHZQOCGFHX"

frequencyList = [
   Frequency('A', 0),
   Frequency('B', 0),
   Frequency('C', 0),
   Frequency('D', 0),
   Frequency('E', 0),
   Frequency('F', 0),
   Frequency('G', 0),
   Frequency('H', 0),
   Frequency('I', 0),
   Frequency('J', 0),
   Frequency('K', 0),
   Frequency('L', 0),
   Frequency('M', 0),
   Frequency('N', 0),
   Frequency('O', 0),
   Frequency('P', 0),
   Frequency('Q', 0),
   Frequency('R', 0),
   Frequency('S', 0),
   Frequency('T', 0),
   Frequency('U', 0),
   Frequency('V', 0),
   Frequency('W', 0),
   Frequency('X', 0),
   Frequency('Y', 0),
   Frequency('Z', 0),
]

def sortByFrequency(x):
    return -x.frequency


# main program
def monoAlphabetic():
    for i in CIPHERTEXT:
        for j in frequencyList:
            if j.equals(i):
                j.increment()

    print(frequencyList)

    for j in frequencyList:
        j.convertToPercentage(len(CIPHERTEXT))

    frequencyList = sorted(frequencyList, key=sortByFrequency)
    print(frequencyList)

    plaintext = list(CIPHERTEXT)
    for index, item in enumerate(frequencyList):
        currLetter = item.letter
        for index2, j in enumerate(plaintext):
            if j == currLetter:
    #            print("Currletter:" + currLetter + "  " + j + "  " + str(j == currLetter))
                plaintext[index2] = ENGLISH_LETTER_FREQUENCIES[index].letter
        print(''.join(plaintext))
    print()
    print(''.join(plaintext))


def sumOfSquares(array):
    result = 0;
    for i in array:
        result = result + (array[i]**2)
    return result
#shift and monoalphabetic shouldnt make a difference?

def shiftLetters(stream, offset):
    newStream = ''
    for i in stream:
        asciiVal = ord(stream[i]) + offset
        if asciiVal > ord('z'):
            asciiVal = asciiVal - ord('z') % 26 + (ord('a') - 1)
        newStream[i] = chr(asciiVal)
    return newStream

def findLetter(char):
    for charFrequency in ENGLISH_LETTER_FREQUENCIES:
        if char == str.lower(charFrequency.letter)
            return charFrequency

def shiftCipher(stream):
    closestFreqOffset = 0
    closestFreq = 1

    #for all j (potential offset aka potential value of k)
    for j in range(0,25):

        shiftedStream = shiftLetters(stream, j)
        #get frequency
        for i in shiftedStream:
            for j in frequencyList:
                if j.equals(i):
                    j.increment()

        print(frequencyList)

        for j in frequencyList:
            j.convertToDecimal(len(stream))
        #calculate i sub j for every letter?
        frequencyCalc = 0
        for char in frequencyList:
            equivChar = findLetter(char.letter)
            frequencyCalc = frequencyCalc + (equivChar.frequency * char.frequency)
        #if calculation is closer to the frequency of english letters sum of squares
        # keep track of that calculation and our current best option for the shift
        if FREQUENCY_SUM_OF_SQUARES - abs(frequencyCalc) < closesetFreq:
            closestFreq = FREQUENCY_SUM_OF_SQUARES - abs(frequencyCalc)
            closestFreqOffset = j
    #return most likely value
    return closestFreqOffset

if MODE == "MONOALPHABETIC":
    monoAlphabetic()
elif MODE === "VIGENERE":
    #for each possible key length 1 to m length
    #for each
    streamArr = "";
    #split streams
        #need to increment for vigenere though: key length = 1,2,3,4...
    for stream in streamArr:
        shift(stream)
    #generate sum of squares
elif MODE === "SHIFT":
    streamArr == "this is a sentence"
    shiftCipher(streamArr)