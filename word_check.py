
def word_check(answer, correct_word1, allow_the):
	if len(answer) != 0:
		check = 0
		if allow_the:
			the_check = []
			for n in range(4):
				the_check.append(answer[n])
			
			the = 0
			if 't' in the_check:
				the += 1
			if 'h' in the_check:
				the += 1
			if 'e' in the_check:
				the += 1
			if ' ' in the_check:
				the += 1

			if correct_word1[0] == 't' and correct_word1[1] == 'h' and correct_word1[2] == 'e' and the < 3:
				correct_word = ''
				for n in range(4, len(correct_word1)):
					correct_word += correct_word1[n]
			else:
				correct_word = correct_word1
		else:
			correct_word = correct_word1
			
		for i in range(len(answer)):
			try:
				if answer[i] == correct_word[i]:
					check += 1
				elif answer[i] == correct_word[i - 1]:
					check += 1
				elif answer[i] == correct_word[i + 1]:
					check += 1
			except:
				try:
					if answer[i] == correct_word[i - 1]:
						check += 1
				except:
					pass
		check /= len(correct_word)

		if correct_word in answer:
			check = 1


		return(check)
        
#INPUT        
answer = input('Enter answer: ')

allow_the = '1'
while allow_the.lower() != 'y' and allow_the.lower() != 'n': 
	allow_the = input("Allow user to miss 'the' in anwser (y/n): ")
if allow_the == 'y':
	allow_the = True
else:
	allow_the = False
	
print(word_check(answer,'the hello',allow_the))
