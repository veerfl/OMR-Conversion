import re
import sys
import csv

f = open("Prerna_1.dat", "r")
mega_a = []
mega_b = []
mega_c = []
Roll_no1 = ''
Roll_no2 = ''

lines = f.readlines()
for line in lines[:-1]:
	line = line.strip()
	x = len(line)
	if x > 0:
		Sheet =line[1:24]
		Sheet_id = line[24:28]
		U_Dise = line[46:57]
		class_code = line[57:58]
		Section_code = line[58:59]
		Roll_no1 = line[59:84]
		Roll_no2 = line[84:109] 
		sex = line[109:134]
		Language = line[134:159]
		Number = line[159:184]
		Q1 = line[184:209]
		Q2 = line[209:234]
		Q3 = line[234:259]
		Q4 = line[259:284]


		c = csv.writer(open("1.csv", "wb"))
		c.writerow(["Sheet_id","U_Dise","class code","Section code","Student Roll No","student sex","student Language","student Number","Q1","Q2","Q3","Q4","Sheet_id2","Starting day","Month","End Day","Month2","Q5a","Q5b","Q6a","Q6b","Q7a","Q7b","Q8a","Q8b","Q9a","Q9b","Q10a","Q10b","Q11","Q12","Q13","Q14","Q15a","Q15b"])
	
      
		for j in range(0,25):
			student_roll_no = Roll_no1[j] + Roll_no2[j]
			student_sex = sex[j]
			student_Language = Language[j]
			student_Number = Number[j]
			student_Q1 = Q1[j]
			student_Q2 = Q2[j]
			student_Q3 = Q3[j]
			student_Q4 = Q4[j]
			a=([Sheet_id,U_Dise,class_code,Section_code,student_roll_no,student_sex,student_Language,student_Number,student_Q1,student_Q2,student_Q3,student_Q4])
			print a

		