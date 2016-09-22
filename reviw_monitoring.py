import re
import sys
import csv
list1 = []
list2 = []
list3 = []

f = open("r.dat", "rb")
wr = csv.writer(open("review.csv", "wb"))
#wr.writerow(["District_code","Block_code","School_code","class_code","Section_code","Student Roll No","student_sex","student_Language","student_Number","Q1","Q2","Q3","Q4"])

for lines in f.readlines():
	lines = lines.strip()
	x = len(lines)
	if x > 0:
		Sheet =lines[1:39]
		you_are = lines[40:41]
		Date = lines[41:47]
		u_dise = lines[47:58]
		Num_students = lines[58:61]
		Num_girls = lines[61:64]
		Num_boys = lines[64:67]
		Num_CWSN = lines[67:69] 
		Num_rooms_used = lines[69:71]
		Num_teachers = lines[71:73]
		Num_special_edu = lines[73:75]
		Num_vacent_teacher_post = lines[75:76]
		Num_unattended_class = lines[76:77]
		Drinking_water_facility = lines[77:78]
		Electricity = lines[78:79]
		playground= lines[79:80]
		seperate_toilets = lines[80:81]
		School_toilets_clean = lines[81:82]
		Seperate_kitchen = lines[82:83]
		ICT_facility = lines[83:84]
		Rural_urban = lines[84:85]
		which_class_1 = lines[85:86]
		Classroom_observed= lines[86:87]
		Q_encouraged = lines[87:88]
		QA_satisfied = lines[88:89]
		Activity_class = lines[89:90]
		Use_blackboard = lines[90:91]
		Trained_in_last_12 =lines[91:92]
		student_intrest_class = lines[92:93]
		Use_TLM = lines[93:94]
		Performs_ABL = lines[94:95]
		CCE_checklist = lines[95:96]
		has_lesson_pln = lines[96:97]
		Assessment_sheet = lines[97:98]
		Teaching_quality = lines[98:99]
		Teachers_PMIS = lines[99:104]
		which_class_2 = lines[104:105]
		Classroom_observed_2 = lines[105:106]
		Q_encouraged_2 = lines[106:107]
		QA_satisfied_2 = lines[107:108]
		Activity_class_2 = lines[108:109]
		Use_blackboard_2 = lines[109:110]
		Trained_in_last_12_2 =lines[110:111]
		student_intrest_class_2 = lines[111:112]
		Use_TLM_2 = lines[112:113]
		Performs_ABL_2 = lines[113:114]
		CCE_checklist_2 = lines[114:115]
		has_lesson_pln_2 = lines[115:116]
		Assessment_sheet_2 = lines[116:117]
		Teaching_quality_2 = lines[117:118]
		Teachers_PMIS_2 = lines[118:123]
		which_class_3 = lines[123:124]
		Classroom_observed_3 = lines[124:125]
		Q_encouraged_3 = lines[125:126]
		QA_satisfied_3 = lines[126:127]
		Activity_class_3 = lines[127:128]
		Use_blackboard_3 = lines[128:129]
		Trained_in_last_12_3 =lines[129:130]
		student_intrest_class_3 = lines[130:131]
		Use_TLM_3 = lines[131:132]
		Performs_ABL_3 = lines[132:133]
		CCE_checklist_3 = lines[133:134]
		has_lesson_pln_3 = lines[134:135]
		Assessment_sheet_3 = lines[135:136]
		Teaching_quality_3 = lines[136:137]
		Teachers_PMIS_3 = lines[137:142]
		which_class_4 = lines[142:143]
		Classroom_observed_4 = lines[143:144]
		Q_encouraged_4 = lines[144:145]
		QA_satisfied_4 = lines[145:146]
		Activity_class_4 = lines[146:147]
		Use_blackboard_4 = lines[147:148]
		Trained_in_last_12_4 =lines[148:149]
		student_intrest_class_4 = lines[149:150]
		Use_TLM_4 = lines[150:151]
		Performs_ABL_4 = lines[151:152]
		CCE_checklist_4 = lines[152:153]
		has_lesson_pln_4 = lines[153:154]
		Assessment_sheet_4 = lines[154:155]
		Teaching_quality_4 = lines[155:156]
		Teachers_PMIS_4 = lines[156:161]
		Rate_overall_quality = lines[161:162]
		parent_community = lines[162:163]
		teacher_deliver_admin_work = lines[163:164]
		Attendance_register = lines[164:165]
		Aadhaar = lines[165:166]
		SMC_meeting = lines[166:167]
		complete_SDP = lines[167:168]
		VER_maintained = lines[168:169]
		braille_books = lines[169:170]
		RTE = lines[170:171]
		evaluation_CCE = lines [171:172]
		report_card_maintained = lines[172:173]
		RMSA_portal = lines[173:174]
		civil_work = lines[174:175]
		calender_activity = lines[175:176]
		Bal_sabha = lines[176:177]
		SC = lines[177:178]
		ST = lines[178:179]
		CWSN = lines[179:180]
		no_students_class3 = lines[180:182]
		GradeA_hindi = lines [182:184]
		GradeB_hindi = lines [184:186]
		GradeC_hindi = lines [186:188]
		GradeD_hindi = lines [188:190]
		GradeE_hindi = lines [190:192]
		GradeA_Math = lines [192:194]
		GradeB_Math = lines [194:196]
		GradeC_Math = lines [196:198]
		GradeD_Math = lines [198:200]
		GradeE_Math = lines [200:202]
		no_students_class5 = lines[202:204]
		GradeA_hindi_5 = lines [204:206]
		GradeB_hindi_5 = lines [206:208]
		GradeC_hindi_5 = lines [208:210]
		GradeD_hindi_5 = lines [210:212]
		GradeE_hindi_5 = lines [212:214]
		GradeA_Math_5 = lines [214:216]
		GradeB_Math_5 = lines [216:218]
		GradeC_Math_5 = lines [218:220]
		GradeD_Math_5 = lines [220:222]
		GradeE_Math_5 = lines [222:224]
		no_students_class8 = lines[224:226]
		GradeA_science_8 = lines [226:228]
		GradeB_science_8 = lines [228:230]
		GradeC_science_8 = lines [230:232]
		GradeD_science_8 = lines [232:234]
		GradeE_science_8 = lines [234:236]
		GradeA_Math_8 = lines [236:238]
		GradeB_Math_8 = lines [238:240]
		GradeC_Math_8 = lines [240:242]
		GradeD_Math_8 = lines [242:244]
		GradeE_Math_8 = lines [244:246]
		G1_amt_received = lines [246:249]
		G1_amt_spent = lines [249:252]
		G2_amt_received = lines[252:255]
		G2_amt_spent = lines[255:258]
		G3_amt_received = lines [258:261]
		G3_amt_spent = lines[261:264]
		 

		
		
		
		out=([you_are,Date,u_dise,Num_students,Num_girls,Num_boys,Num_CWSN,Num_rooms_used,Num_teachers,Num_special_edu,Num_vacent_teacher_post,Num_unattended_class,Drinking_water_facility,Electricity\
			,playground,seperate_toilets,School_toilets_clean,Seperate_kitchen,ICT_facility,Rural_urban,which_class_1,Classroom_observed,QA_satisfied,Q_encouraged,Activity_class,Use_blackboard,Trained_in_last_12\
			,student_intrest_class,Use_TLM,Performs_ABL,CCE_checklist,has_lesson_pln,Assessment_sheet,Teaching_quality,Teachers_PMIS\
			,which_class_2,Classroom_observed_2,Q_encouraged_2,QA_satisfied_2,Activity_class_2,Use_blackboard_2,Trained_in_last_12_2,student_intrest_class_2,Use_TLM_2,Performs_ABL_2,CCE_checklist_2,has_lesson_pln_2,Assessment_sheet_2,Teaching_quality_2,Teachers_PMIS_2\
			,which_class_3,Classroom_observed_3,Q_encouraged_3,QA_satisfied_3,Activity_class_3,Use_blackboard_3,Trained_in_last_12_3,student_intrest_class_3,Use_TLM_3,Performs_ABL_3,CCE_checklist_3,has_lesson_pln_3,Assessment_sheet_3,Teaching_quality_3,Teachers_PMIS_3\
			,which_class_4,Classroom_observed_4,Q_encouraged_4,QA_satisfied_4,Activity_class_4,Use_blackboard_4,Trained_in_last_12_4,student_intrest_class_4,Use_TLM_4,Performs_ABL_4,CCE_checklist_4,has_lesson_pln_4,Assessment_sheet_4,Teaching_quality_4,Teachers_PMIS_4\
			,Rate_overall_quality,parent_community,teacher_deliver_admin_work,Attendance_register,Aadhaar,SMC_meeting,complete_SDP,VER_maintained,braille_books,RTE,evaluation_CCE,report_card_maintained,RMSA_portal,civil_work,calender_activity,Bal_sabha,SC,ST,CWSN\
			,no_students_class3,GradeA_hindi,GradeB_hindi,GradeC_hindi,GradeD_hindi,GradeE_hindi,GradeA_Math,GradeB_Math,GradeC_Math,GradeD_Math,GradeE_Math\
			,no_students_class5,GradeA_hindi_5,GradeB_hindi_5,GradeC_hindi_5,GradeD_hindi_5,GradeE_hindi_5,GradeA_Math_5,GradeB_Math_5,GradeC_Math_5,GradeD_Math_5,GradeE_Math_5\
			,no_students_class8,GradeA_science_8,GradeB_science_8,GradeC_science_8,GradeD_science_8,GradeE_science_8,GradeA_Math_8,GradeB_Math_8,GradeC_Math_8,GradeD_Math_8,GradeE_Math_8\
			,G1_amt_received,G1_amt_spent,G2_amt_received,G2_amt_spent,G3_amt_received,G3_amt_spent])


		print(out)
		wr.writerow(out)
		

		#print out[138]
		


		


		
			




		#print out
		

			


			
			



		
			
		
			

		

   			
				
			#c.writerow([District_code,Block_code,School_code,class_code,Section_code,student_roll_no,student_sex,student_Language,student_Number,student_Q1,student_Q2,student_Q3,student_Q4])
			
		#c.writerow([you_are,Date,u_dise,Num_students,Num_girls,Num_boys,Num_CWSN,Num_rooms_used,Num_teachers,Num_special_edu,Num_vacent_teacher_post,Num_unattended_class,Drinking_water_facility,Electricity\
			   #,playground,seperate_toilets,School_toilets_clean,Seperate_kitchen,ICT_facility,Rural_urban,which_class_1,Classroom_observed,QA_satisfied,Q_encouraged,Activity_class,Use_blackboard,Trained_in_last_12\
			   #,student_intrest_class,Use_TLM,Performs_ABL,CCE_checklist,has_lesson_pln,Assessment_sheet,Teaching_quality,Teachers_PMIS\
			   #,which_class_2,Classroom_observed_2,Q_encouraged_2,QA_satisfied_2,Activity_class_2,Use_blackboard_2,Trained_in_last_12_2,student_intrest_class_2,Use_TLM_2,Performs_ABL_2,CCE_checklist_2,has_lesson_pln_2,Assessment_sheet_2,Teaching_quality_2,Teachers_PMIS_2\
			   #,which_class_3,Classroom_observed_3,Q_encouraged_3,QA_satisfied_3,Activity_class_3,Use_blackboard_3,Trained_in_last_12_3,student_intrest_class_3,Use_TLM_3,Performs_ABL_3,CCE_checklist_3,has_lesson_pln_3,Assessment_sheet_3,Teaching_quality_3,Teachers_PMIS_3\
			   #,which_class_4,Classroom_observed_4,Q_encouraged_4,QA_satisfied_4,Activity_class_4,Use_blackboard_4,Trained_in_last_12_4,student_intrest_class_4,Use_TLM_4,Performs_ABL_4,CCE_checklist_4,has_lesson_pln_4,Assessment_sheet_4,Teaching_quality_4,Teachers_PMIS_4\
			   #,Rate_overall_quality,parent_community,teacher_deliver_admin_work,Attendance_register,Aadhaar,SMC_meeting,complete_SDP,VER_maintained,braille_books,RTE,evaluation_CCE,report_card_maintained,RMSA_portal,civil_work,calender_activity,Bal_sabha,SC,ST,CWSN\
			   #,no_students_class3,GradeA_hindi,GradeB_hindi,GradeC_hindi,GradeD_hindi,GradeE_hindi,GradeA_Math,GradeB_Math,GradeC_Math,GradeD_Math,GradeE_Math\
			   #,no_students_class5,GradeA_hindi_5,GradeB_hindi_5,GradeC_hindi_5,GradeD_hindi_5,GradeE_hindi_5,GradeA_Math_5,GradeB_Math_5,GradeC_Math_5,GradeD_Math_5,GradeE_Math_5\
			   #,no_students_class8,GradeA_science_8,GradeB_science_8,GradeC_science_8,GradeD_science_8,GradeE_science_8,GradeA_Math_8,GradeB_Math_8,GradeC_Math_8,GradeD_Math_8,GradeE_Math_8\
			   #,G1_amt_received,G1_amt_spent,G2_amt_received,G2_amt_spent,G3_amt_received,G3_amt_spent])
			 
		#c.writerow([out])

		
			


			



 
