def anagram(n,ch_list,not_used, words,word_list):
	for i in range(len(ch_list)):
		if not_used[i]:
			if n == 1:
				if words+ch_list[i] not in word_list:
					print(words+ch_list[i])
					word_list.append(words+ch_list[i])
			else:
				not_used[i] = False
				anagram(n-1,ch_list,not_used, words+ch_list[i],word_list)
				not_used[i] = True
			
			

def main():
	strr = input("input a string\n")
	ch_list = []
	words = ""
	word_list = []
	
	for i in range(len(strr)):
		ch_list.append(strr[i])

	not_used = [True] * len(strr)

	anagram(len(strr),ch_list,not_used,words,word_list)


main()