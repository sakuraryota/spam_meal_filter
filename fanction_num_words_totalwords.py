import sys
import MeCab

input_file = sys.argv[1]
mecab = MeCab.Tagger('-Owakati')

def reading_file(input_file):
	
	lines = []
	with open(input_file,'r')as fp:
		for line in fp:
			lines.append(line)
	
	return lines



def separate_word_and_documents(lines):
	
	words_list = []
	for mail in lines:
		label,document = mail.split(',')
		document = document.rstrip()
		words = mecab.parse(document).split(' ')
		words_list.extend(words)		
	return words_list


def maiking_w2f(word_list):
	
	w2f = {}
	for word in word_list:
		w2f[word] = w2f.get(word,0)+1
	return w2f

def count_num_total_word(w2f):
	
	total_w2f = 0
	for i in w2f:#/error
		total_w2f += i
	return total_w2f


def write_pw():
	with open('pw.txt', "w") as fp:
		for label in w2f.keys():
			f.write(w2f /total_w2f )

	
def main():
	

	lines = reading_file(input_file)
	word_list = separate_word_and_documents(lines)
	w2f = maiking_w2f(word_list)
	total_w2f = count_num_total_word(w2f)

main()
