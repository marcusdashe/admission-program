"""
    An Admission Program to calculate the aggregate score 
    and tell the students the faculty and department 
    he or she is likely to be admitted

    Criteria for Admission

    0 - 49 No admission
    50 - 54 Agric Dept.
    55 - 60 Botany and Zoology Dept.
    61 - 70 CS, Physiology & Stats
    71 - 74 Pharmacy, Physiology & Nursing
    75 - 79 Banking & Finance, Accounting & Insurance 
    80 & Above Medicine & Law
"""


def main():
    aggregate = []
    while True:
        score = input("What is your aggregate[+]")
        if score == "q": 
            break
        aggregate.append(int(score))
    dept_faulty = tell_student_faculty_dept(aggregate)
    if dept_faulty.startswith("No Admission"): print("No admission given")
    print(f"You have been offered admission into either {dept_faulty}")



def tell_student_faculty_dept(aggre_list: list):
    sum_score = sum(aggre_list)
    if 0 <= sum_score <= 49:
        return "No Admission"
    elif  49 < sum_score <= 54:
        return "Agric Dept."
    elif 54 < sum_score <= 60:
        return "Botany and Zoology Dept."
    elif 60 < sum_score <= 70:
        return "CS Dept. and Psycology and Statistics"
    elif 70 < sum_score <= 74:
        return "Pharmacy and Physiology and Nursing"
    elif 75 < sum_score <= 79:
        return "Banking and Finance and Accounting"
    elif sum_score >= 80:
        return "Medicine and Law"
    else:
        None

