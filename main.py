wordlist = []
vowels = "aeiou"

print("Welcome to the Mad Libs Story Maker!\n\nPlease enter words of the following type:\n")

wordlist.append(input("Adjective: "))
wordlist.append(input("Living creature- fictional or not: "))
wordlist.append(input("Verb- ends in S: "))
wordlist.append(input("Event: "))
wordlist.append(input("Verb- base form: "))
wordlist.append(input("Adjective: "))
wordlist.append(input("He or she: "))
wordlist.append(input("Adverb: "))
wordlist.append(input("Verb- present ends in S:"))
wordlist.append(input("Adjective: "))
wordlist.append(input("Noun: "))
wordlist.append(input("Adjective- ends in ness: "))
wordlist.append(input("Verb- present ends in ed: "))
wordlist.append(input("Structure: "))

print("\nkA", wordlist[0], wordlist[1], wordlist[2], ("in an" if wordlist[3][0] in vowels else "in a"),
      wordlist[3], "to", wordlist[4],"the character from the", wordlist[5], "creature.\n" +
      wordlist[6].capitalize() + wordlist[7], wordlist[8], "for the", wordlist[9], wordlist[10], "so that",
      wordlist[11], "can be", wordlist[12], "to the", wordlist[13] + ".")