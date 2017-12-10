def isAnagram(wordOne, wordTwo):
    if len(wordOne) != len(wordTwo):
        return False

    match_count = 0
    for letter in wordOne:
        for l in wordTwo:
            if letter == l:
                match_count += 1
    if match_count == len(wordOne):
        return True
    return False

def isValidPassphrase(row):
    words = row.split(' ')
    for word in range(0, len(words)):
        for i in range(word + 1, len(words)):
            if words[word] == words[i]:
                return False
    return True

def isValidPassphraseAnagram(row):
    words = row.split(' ')
    for word in range(0, len(words)):
        for i in range(word + 1, len(words)):
            if words[word] == words[i]:
                return False
            if isAnagram(words[word], words[i]):
                return False
    return True

with open('input.txt', 'r') as puzzle_file:
    puzzle_input = puzzle_file.read()

valid_passphrase_count = 0
#To ensure security, a valid passphrase must contain no duplicate words.
for row in puzzle_input.split("\n"):
    if row != "":
        if isValidPassphrase(row):
            valid_passphrase_count += 1
print("Part1: " + str(valid_passphrase_count))

#For added security, yet another system policy has been put in place.
#Now, a valid passphrase must contain no two words that are anagrams
#of each other - that is, a passphrase is invalid if any word's letters
#can be rearranged to form any other word in the passphrase.
puzzle_input = ""
with open('input.txt', 'r') as puzzle_file:
    puzzle_input = puzzle_file.read()

valid_passphrase_count = 0
for row in puzzle_input.split("\n"):
    if row != "":
        if isValidPassphraseAnagram(row):
            valid_passphrase_count += 1

print("Part2: " + str(valid_passphrase_count))

testrowOne = "abcde fghgij"
testrowTwo = "abcde xyz ecdab"
testrowThree = "a ab abc abd abf abj"
testrowFour = "iiii oiii ooii oooi oooo"
testrowFive = "oiii ioii iioi iiio"
tests = {testrowOne, testrowTwo, testrowThree, testrowFour, testrowFive}

for test in tests:
    print(isValidPassphraseAnagram(test))
