"""
Dict_word_space_count{
	word:count

}
"""
dict_word_space_count={}

file_text = open("test.txt")

for line in file_text:
	#split line up based on spaces

	word_split = line.split(" ")
		
	#print (word_split)
		

	#go over each of the items in our list 
	for word in word_split:
		#print("This is the word:", word)
		
		
		#if the key already exists in the dictionary then drop into the loop
		#grab the current value of count and bump it up by one
		
		if dict_word_space_count.get(word) == None:
			dict_word_space_count[word]=1
		
		
		
		#if no error then we are going to assume the key does not exist in the dictionary
		#append it to the dictionary with both key=word and value(1)
		else:
			#print("I'm in the else loop")
			counter = 1
		
			temp = dict_word_space_count[word]
			#print("I am temp unbroken: ",temp)
			
			counter = temp
			#print ("I am the intial counter: ", counter)
			counter+=1
			#print("The counter increased: ", counter)
			dict_word_space_count[word]=counter


for i, number in dict_word_space_count.items():
	print "%s %d"%(i, number) 
#print (dict_word_space_count)