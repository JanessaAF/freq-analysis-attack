class Frequency:
    def __init__(self, letter, frequency):
        self.letter = letter
        self.frequency = frequency
    def increment(self):
        self.frequency += 1
    def convertToPercentage(self, totalCharacters):
        self.frequency = (self.frequency / totalCharacters) * 100
    def equals(self, newLetter):
        return self.letter == newLetter
    def __str__(self):
        return self.letter + ': ' + str(self.frequency)
    def __repr__(self):
        return self.letter + ': ' + str(self.frequency)

MODE = "SHIFT" #"VIGENERE"/"SHIFT"/"MONOALPHABETIC"

ENGLISH_LETTER_FREQUENCIES = [
    Frequency('e', 12.7),
    Frequency('t', 9.1),
    Frequency('a', 8.2),
    Frequency('o', 7.5),
    Frequency('i', 7.0),
    Frequency('n', 6.7),
    Frequency('s', 6.3),
    Frequency('h', 6.1),
    Frequency('r', 6.0),
    Frequency('d', 4.3),
    Frequency('l', 4.0),
    Frequency('c', 2.8),
    Frequency('u', 2.8),
    Frequency('w', 2.4),
    Frequency('m', 2.4),
    Frequency('f', 2.2),
    Frequency('y', 2.0),
    Frequency('g', 2.0),
    Frequency('p', 1.9),
    Frequency('b', 1.5),
    Frequency('v', 1.0),
    Frequency('k', 0.8),
    Frequency('j', 0.2),
    Frequency('x', 0.2),
    Frequency('z', 0.1),
    Frequency('q', 0.1)
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

#shift and monoalphabetic shouldnt make a difference?
def shift():


def vigenere():

if MODE == "MONOALPHABETIC":
    monoAlphabetic()
elif MODE == "SHIFT":
    shift()
elif MODE == "VIGENERE":
    vigenere()