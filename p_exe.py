import re
import sys
import csv


mega_a = []
mega_b = []
mega_c = []
Roll_no1 = ''
Roll_no2 = ''
f = open("Prerna_1.dat", "r")
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

		c = csv.writer(open("P_output.csv", "wb"))
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
			mega_a.append(a)

			


		f1 = open("Prerna_2.dat", "r")
		for line in f1.readlines():
			line = line.strip()
			x = len(line)
			if x > 0:
				Sheet_id2 =line[24:28]
				Starting_day = line[50:52]
				Month = line[52:53]
				End_Day = line[53:55]
				Month2 = line[55:56]
				Q5a = line[56:81]
				Q5b = line[81:106]
				Q6a = line[106:131] 
				Q6b = line[131:156]
				Q7a = line[156:181]
				Q7b = line[181:206]
				Q8a = line[206:231]
				Q8b = line[231:256]
				Q9a = line[256:281]
				Q9b = line[281:306]
				Q10a = line[306:331]
				Q10b = line[331:356]
				Q11 = line[356:381]
				Q12 = line[381:406]
				Q13 = line[406:431]
				Q14 = line[431:456]
				Q15a = line[456:481]
				Q15b = line[481:506]
				
																			
				for y in range(0,25):
					student_Q5a = Q5a[y]
					student_Q5b = Q5b[y]
					student_Q6a = Q6a[y]
					student_Q6b = Q6b[y]
					student_Q7a = Q7a[y]
					student_Q7b = Q7b[y]
					student_Q8a = Q8a[y]
					student_Q8b = Q8b[y]
					student_Q9a = Q9a[y]
					student_Q9b = Q9b[y]
					student_Q10a = Q10a[y]
					student_Q10b = Q10b[y]
					student_Q11 = Q11[y]
					student_Q12 = Q12[y]
					student_Q13 = Q13[y]
					student_Q14 = Q14[y]
					student_Q15a = Q15a[y]
					student_Q15b = Q15b[y]
															#out =  'Student Roll No :' , student_roll_no,  ' Sex:', student_sex, 'Language:',student_Language, 'Number:', student_Number,'Q1',student_Q1,'Q2',student_Q2,'Q3',student_Q3,'Q4',student_Q4
					b=([Sheet_id2,Starting_day,Month,End_Day,Month2,student_Q5a,student_Q5b,student_Q6a,student_Q6b,student_Q7a,student_Q7b,student_Q8a,student_Q8b,student_Q9a,student_Q9b,student_Q10a,student_Q10b,student_Q11,student_Q12,student_Q13,student_Q14,student_Q15a,student_Q15b])
					mega_b.append(b)
					
					
			for i in range(0,25):
				mega_a[i].extend(mega_b[i])
				mega_c.append(mega_a[i])																									
		        c.writerows(mega_c)

		        print mega_c

