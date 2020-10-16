import os
import random

r=random.randint(0,11)

jokes=[	'I went to the zoo the other day. There was only a dog in it – it was a shihtzu',
		'My mother-in-law fell down a wishing well. I was amazed – I never knew they worked',
		'Patient: Doctor, I have a pain in my eye whenever I drink tea. Doctor: Take the spoon out of the mug before you drink',
		'What is the longest word in english language?. Smiles because there is a mile between first and last letters.',
		'In Which Battle Did Napoleon Died?. His Last Battle.',
		'What Can You Never Eat For Breakfast?. Lunch and dinner',
		'Man: Hey call me a taxi. Guy: Sure, Hey taxi whats up',
		"Girl said to man: You look very funny wearing that belt. He replied, I would look even funnier if I didn't wear it.",
		"Father: What did you do today to help your mother?. Son: I dried the dishes. Daughter: And I helped pick up the pieces.",
		"Man said to God: Why did you make women so beautiful?. God said to man: So that you will love them. Man said to God: But why did you make them so dumb?.God said to man: So that they will love you.",
		"Student: Teacher will you punish me for something that I didn't do?. Teacher: Of course not. Student: Well, I didn't do my homework",
		"Man asks god: how long is a million years for you?. God: about a minute. Man: how much is a million dollar worth to you?. God: about a penny. Man asks: God, may I hava a penny?. God replied: Wait a minute."
]

a=str(jokes[r])

#creats/overwrite the speak.vbs file
file=open("speak.vbs","w")

#creates the vbs file that speaks unicode for " is U+0022
file.write("Dim userInput\nuserInput = \u0022"+a+"\u0022\nSet Sapi = Wscript.CreateObject(\u0022SAPI.SpVoice\u0022)\nSapi.speak userInput")

#closes the vbs file
file.close()

print(a)

#executes the file
os.system("speak.vbs")	#The process cannot access the file because it is being used by another process.

#plays ba dum tss music
try:
    os.system("music.vbs")
except:
    print("Ba Dum Tsss...")
