import re

job_skills = {
    "data analyst": ["python", "excel", "sql", "power bi", "statistics"],
    "python developer": ["python", "oop", "git", "flask", "django"]
}

def extract_skills(text):
    text = text.lower()
    found_skills = set()
    for role in job_skills:
        for skill in job_skills[role]:
            if re.search(rf"\b{skill}\b", text):
                found_skills.add(skill)
    return found_skills

resume_text = input("write your resume text here:\n").lower()
role = input("Enter job role (data analyst / python developer): ").lower()

required = set(job_skills.get(role, []))
found = extract_skills(resume_text)

matched = found & required
missing = required - found

score = (len(matched) / len(required)) * 100 if required else 0

print("\nMatched Skills:", matched)
print("Missing Skills:", missing)
print(f"Skill Match Score: {score:.2f}%")
