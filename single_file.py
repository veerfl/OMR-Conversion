import re
import sys
import csv


f = open("22.dat", "r")
for line in f.readlines():
	line = line.strip()
	x = len(line)
	if x > 0:
		Sheet =line[1:39]
		you_are = line[40:41]
		Date = line[41:47]
		u_dise = line[47:58]
		Num_students = line[58:61]
		Num_girls = line[61:64]
		Num_boys = line[64:67]
		Num_CWSN = line[67:69] 
		Num_rooms_used = line[69:71]
		Num_teachers = line[71:73]
		Num_special_edu = line[73:75]
		Num_vacent_teacher_post = line[75:76]
		Num_unattended_class = line[76:77]
		Drinking_water_facility = line[77:78]
		Electricity = line[78:79]
		playground= line[79:80]
		seperate_toilets = line[80:81]
		School_toilets_clean = line[81:82]
		Seperate_kitchen = line[82:83]
		ICT_facility = line[83:84]
		Rural_urban = line[84:85]
		which_class_1 = line[85:86]
		Classroom_observed= line[86:87]
		Q_encouraged = line[87:88]
		QA_satisfied = line[88:89]
		Activity_class = line[89:90]
		Use_blackboard = line[90:91]
		Trained_in_last_12 =line[91:92]
		student_intrest_class = line[92:93]
		Use_TLM = line[93:94]
		Performs_ABL = line[94:95]
		CCE_checklist = line[95:96]
		has_lesson_pln = line[96:97]
		Assessment_sheet = line[97:98]
		Teaching_quality = line[98:99]
		Teachers_PMIS = line[99:104]
		which_class_2 = line[104:105]
		Classroom_observed_2 = line[105:106]
		Q_encouraged_2 = line[106:107]
		QA_satisfied_2 = line[107:108]
		Activity_class_2 = line[108:109]
		Use_blackboard_2 = line[109:110]
		Trained_in_last_12_2 =line[110:111]
		student_intrest_class_2 = line[111:112]
		Use_TLM_2 = line[112:113]
		Performs_ABL_2 = line[113:114]
		CCE_checklist_2 = line[114:115]
		has_lesson_pln_2 = line[115:116]
		Assessment_sheet_2 = line[116:117]
		Teaching_quality_2 = line[117:118]
		Teachers_PMIS_2 = line[118:123]
		which_class_3 = line[123:124]
		Classroom_observed_3 = line[124:125]
		Q_encouraged_3 = line[125:126]
		QA_satisfied_3 = line[126:127]
		Activity_class_3 = line[127:128]
		Use_blackboard_3 = line[128:129]
		Trained_in_last_12_3 =line[129:130]
		student_intrest_class_3 = line[130:131]
		Use_TLM_3 = line[131:132]
		Performs_ABL_3 = line[132:133]
		CCE_checklist_3 = line[133:134]
		has_lesson_pln_3 = line[134:135]
		Assessment_sheet_3 = line[135:136]
		Teaching_quality_3 = line[136:137]
		Teachers_PMIS_3 = line[137:142]
		which_class_4 = line[142:143]
		Classroom_observed_4 = line[143:144]
		Q_encouraged_4 = line[144:145]
		QA_satisfied_4 = line[145:146]
		Activity_class_4 = line[146:147]
		Use_blackboard_4 = line[147:148]
		Trained_in_last_12_4 =line[148:149]
		student_intrest_class_4 = line[149:150]
		Use_TLM_4 = line[150:151]
		Performs_ABL_4 = line[151:152]
		CCE_checklist_4 = line[152:153]
		has_lesson_pln_4 = line[153:154]
		Assessment_sheet_4 = line[154:155]
		Teaching_quality_4 = line[155:156]
		Teachers_PMIS_4 = line[156:161]
		Rate_overall_quality = line[161:162]
		parent_community = line[162:163]
		teacher_deliver_admin_work = line[163:164]
		Attendance_register = line[164:165]
		Aadhaar = line[165:166]
		SMC_meeting = line[166:167]
		complete_SDP = line[167:168]
		VER_maintained = line[168:169]
		braille_books = line[169:170]
		RTE = line[170:171]
		evaluation_CCE = line [171:172]
		report_card_maintained = line[172:173]
		RMSA_portal = line[173:174]
		civil_work = line[174:175]
		calender_activity = line[175:176]
		Bal_sabha = line[176:177]
		SC = line[177:178]
		ST = line[178:179]
		CWSN = line[179:180]
		no_students_class3 = line[180:182]
		GradeA_hindi = line [182:184]
		GradeB_hindi = line [184:186]
		GradeC_hindi = line [186:188]
		GradeD_hindi = line [188:190]
		GradeE_hindi = line [190:192]
		GradeA_Math = line [192:194]
		GradeB_Math = line [194:196]
		GradeC_Math = line [196:198]
		GradeD_Math = line [198:200]
		GradeE_Math = line [200:202]
		no_students_class5 = line[202:204]
		GradeA_hindi_5 = line [204:206]
		GradeB_hindi_5 = line [206:208]
		GradeC_hindi_5 = line [208:210]
		GradeD_hindi_5 = line [210:212]
		GradeE_hindi_5 = line [212:214]
		GradeA_Math_5 = line [214:216]
		GradeB_Math_5 = line [216:218]
		GradeC_Math_5 = line [218:220]
		GradeD_Math_5 = line [220:222]
		GradeE_Math_5 = line [222:224]
		no_students_class8 = line[224:226]
		GradeA_science_8 = line [226:228]
		GradeB_science_8 = line [228:230]
		GradeC_science_8 = line [230:232]
		GradeD_science_8 = line [232:234]
		GradeE_science_8 = line [234:236]
		GradeA_Math_8 = line [236:238]
		GradeB_Math_8 = line [238:240]
		GradeC_Math_8 = line [240:242]
		GradeD_Math_8 = line [242:244]
		GradeE_Math_8 = line [244:246]
		G1_amt_received = line [246:249]
		G1_amt_spent = line [249:252]
		G2_amt_received = line[252:255]
		G2_amt_spent = line[255:258]
		G3_amt_received = line [258:261]
		G3_amt_spent = line[261:264]
		 

		c = csv.writer(open("review.csv", "wb"))
		#c.writerow(["District_code","Block_code","School_code","class_code","Section_code","Student Roll No","student_sex","student_Language","student_Number","Q1","Q2","Q3","Q4"])

		
		
		out =  you_are,Date,u_dise,Num_students,Num_girls,Num_boys,Num_CWSN,Num_rooms_used,Num_teachers,Num_special_edu,Num_vacent_teacher_post,Num_unattended_class,Drinking_water_facility,Electricity\
			   ,playground,seperate_toilets,School_toilets_clean,Seperate_kitchen,ICT_facility,Rural_urban,which_class_1,Classroom_observed,QA_satisfied,Q_encouraged,Activity_class,Use_blackboard,Trained_in_last_12\
			   ,student_intrest_class,Use_TLM,Performs_ABL,CCE_checklist,has_lesson_pln,Assessment_sheet,Teaching_quality,Teachers_PMIS\
			   ,which_class_2,Classroom_observed_2,Q_encouraged_2,QA_satisfied_2,Activity_class_2,Use_blackboard_2,Trained_in_last_12_2,student_intrest_class_2,Use_TLM_2,Performs_ABL_2,CCE_checklist_2,has_lesson_pln_2,Assessment_sheet_2,Teaching_quality_2,Teachers_PMIS_2\
			   ,which_class_3,Classroom_observed_3,Q_encouraged_3,QA_satisfied_3,Activity_class_3,Use_blackboard_3,Trained_in_last_12_3,student_intrest_class_3,Use_TLM_3,Performs_ABL_3,CCE_checklist_3,has_lesson_pln_3,Assessment_sheet_3,Teaching_quality_3,Teachers_PMIS_3\
			   ,which_class_4,Classroom_observed_4,Q_encouraged_4,QA_satisfied_4,Activity_class_4,Use_blackboard_4,Trained_in_last_12_4,student_intrest_class_4,Use_TLM_4,Performs_ABL_4,CCE_checklist_4,has_lesson_pln_4,Assessment_sheet_4,Teaching_quality_4,Teachers_PMIS_4\
			   ,Rate_overall_quality,parent_community,teacher_deliver_admin_work,Attendance_register,Aadhaar,SMC_meeting,complete_SDP,VER_maintained,braille_books,RTE,evaluation_CCE,report_card_maintained,RMSA_portal,civil_work,calender_activity,Bal_sabha,SC,ST,CWSN\
			   ,no_students_class3,GradeA_hindi,GradeB_hindi,GradeC_hindi,GradeD_hindi,GradeE_hindi,GradeA_Math,GradeB_Math,GradeC_Math,GradeD_Math,GradeE_Math\
			   ,no_students_class5,GradeA_hindi_5,GradeB_hindi_5,GradeC_hindi_5,GradeD_hindi_5,GradeE_hindi_5,GradeA_Math_5,GradeB_Math_5,GradeC_Math_5,GradeD_Math_5,GradeE_Math_5\
			   ,no_students_class8,GradeA_science_8,GradeB_science_8,GradeC_science_8,GradeD_science_8,GradeE_science_8,GradeA_Math_8,GradeB_Math_8,GradeC_Math_8,GradeD_Math_8,GradeE_Math_8\
			   ,G1_amt_received,G1_amt_spent,G2_amt_received,G2_amt_spent,G3_amt_received,G3_amt_spent
		print out
			#c.writerow([District_code,Block_code,School_code,class_code,Section_code,student_roll_no,student_sex,student_Language,student_Number,student_Q1,student_Q2,student_Q3,student_Q4])
			
		c.writerow([you_are,Date,u_dise,Num_students,Num_girls,Num_boys,Num_CWSN,Num_rooms_used,Num_teachers,Num_special_edu,Num_vacent_teacher_post,Num_unattended_class,Drinking_water_facility,Electricity\
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
			 

		
			


			



 