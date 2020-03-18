print("Morse Code")
E = '.'
T = '-'

morse_code = dict()
morse_code['E'] = E
morse_code['T'] = T
morse_code[' '] = ' '
morse_code['I'] = morse_code['E'] + E 
morse_code['S'] = morse_code['I'] + E
morse_code['H'] = morse_code['S'] + E
morse_code['V'] = morse_code['S'] + T
morse_code['U'] = morse_code['I'] + T
morse_code['F'] = morse_code['U'] + E

morse_code['A'] = morse_code['E'] + T
morse_code['R'] = morse_code['A'] + E
morse_code['L'] = morse_code['R'] + E
morse_code['W'] = morse_code['A'] + T
morse_code['P'] = morse_code['W'] + E
morse_code['J'] = morse_code['W'] + T

morse_code['N'] = morse_code['T'] + E 
morse_code['D'] = morse_code['N'] + E
morse_code['B'] = morse_code['D'] + E
morse_code['X'] = morse_code['D'] + T
morse_code['K'] = morse_code['N'] + T
morse_code['C'] = morse_code['K'] + E
morse_code['Y'] = morse_code['K'] + T

morse_code['M'] = morse_code['T'] + T
morse_code['G'] = morse_code['M'] + E
morse_code['Z'] = morse_code['G'] + E
morse_code['Q'] = morse_code['G'] + T
morse_code['O'] = morse_code['M'] + T

#Allow user input
word = input("Enter a string to convert to morse code: ")
word_convert = word.upper()
print("The Morse Code for '{0}' is".format(word))
for i in word_convert:
    print(morse_code[i], end=' ')


