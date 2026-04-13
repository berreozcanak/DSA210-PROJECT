import csv
import random
from datetime import datetime, timedelta

def main():
    headers = ["Timestamp", "Total score", "What is your current year of study? ", "What is your current year of study?  [Score]", "What is your current year of study?  [Feedback]", "What is your department? ", "What is your department?  [Score]", "What is your department?  [Feedback]", "  On average, how many hours do you study per day?  ", "  On average, how many hours do you study per day?   [Score]", "  On average, how many hours do you study per day?   [Feedback]", "  Where do you primarily study?  ", "  Where do you primarily study?   [Score]", "  Where do you primarily study?   [Feedback]", "  How would you describe the typical noise level of your environment?  ", "  How would you describe the typical noise level of your environment?   [Score]", "  How would you describe the typical noise level of your environment?   [Feedback]", "  Do you listen to audio/music while studying?  ", "  Do you listen to audio/music while studying?   [Score]", "  Do you listen to audio/music while studying?   [Feedback]", "  Do you usually study alone or with others?  ", "  Do you usually study alone or with others?   [Score]", "  Do you usually study alone or with others?   [Feedback]", "On a scale of 1–10, how would you rate your level of focus in this environment?", "On a scale of 1–10, how would you rate your level of focus in this environment? [Score]", "On a scale of 1–10, how would you rate your level of focus in this environment? [Feedback]", "On a scale of 1–10, how productive do you feel your sessions usually are?  ", "On a scale of 1–10, how productive do you feel your sessions usually are?   [Score]", "On a scale of 1–10, how productive do you feel your sessions usually are?   [Feedback]", "What is your current GPA range?  ", "What is your current GPA range?   [Score]", "What is your current GPA range?   [Feedback]", "How many hours of sleep did you get last night (or on average)?  (Only numbers)", "How many hours of sleep did you get last night (or on average)?  (Only numbers) [Score]", "How many hours of sleep did you get last night (or on average)?  (Only numbers) [Feedback]", "  What is your average daily phone screen time (in hours)?    (Only numbers)", "  What is your average daily phone screen time (in hours)?    (Only numbers) [Score]", "  What is your average daily phone screen time (in hours)?    (Only numbers) [Feedback]", "How would you rate your current stress level this semester?", "How would you rate your current stress level this semester? [Score]", "How would you rate your current stress level this semester? [Feedback]"]
    
    departments = ["Computer Science", "Engineering", "Business", "Psychology", "Design", "Economics", "Industrial Engineering"]
    years = ["1st year", "2nd year", "3rd year", "4th year"]
    study_locations = ["Home", "Library", "Cafe", "Dorm", "Puplic study area"]
    audio_options = ["No", "Yes, Instrumental (Lo-fi, Classical)", "Yes, Lyrical (Pop, Rock)", "Yes, Ambient (White noise, Nature)", "Yes, Other"]
    social_options = ["Alone", "With friends", "Around people but working independently"]
    gpa_ranges = ["Below 2.0", "2.0-2.5", "2.5-3.0", "3.0-3.5", "3.5-4.0"]
    study_hours_options = ["0-2 hours", "2-4 hours", "4-6 hours", "6+ hours"]

    rows = []
    base_time = datetime(2026, 4, 1)

    for i in range(122):
        # Generate correlated variables
        loc = random.choice(study_locations)
        if loc == "Library":
            noise = random.choice([1, 2])
        elif loc == "Cafe":
            noise = random.choice([3, 4, 5])
        elif loc in ["Home", "Dorm"]:
            noise = random.choice([1, 2, 3, 4])
        else:
            noise = random.choice([2, 3])

        audio = random.choice(audio_options)
        
        base_focus = 7
        if noise >= 4:
            base_focus -= min(2, base_focus - 1)
        if noise == 1:
            base_focus += min(1, 10 - base_focus)
            
        if noise >= 3 and audio in ["Yes, Instrumental (Lo-fi, Classical)", "Yes, Ambient (White noise, Nature)"]:
            base_focus += min(1, 10 - base_focus) 
        elif noise < 3 and audio == "Yes, Lyrical (Pop, Rock)":
            base_focus -= min(1, base_focus - 1) 
            
        sleep = random.randint(4, 9)
        if sleep < 6:
            base_focus -= min(1, base_focus - 1)
            
        focus = max(1, min(10, base_focus + random.choice([-1, 0, 1])))
        productivity = max(1, min(10, focus + random.choice([-1, 0, 1])))
        
        study_hours = random.choice(study_hours_options)
        stress = random.randint(4, 7)
        if sleep < 6: stress += 1
        if study_hours == "6+ hours": stress += 1
        if productivity < 5: stress += 1
        stress = max(1, min(10, stress))

        screen_time = random.randint(2, 8)
        
        t = base_time + timedelta(days=random.randint(0, 12), hours=random.randint(8, 22), minutes=random.randint(0, 59))
        time_str = t.strftime("%Y/%m/%d %I:%M:%S %p GMT+3")
        
        row = [
            time_str, "0.00 / 0", 
            random.choice(years), "-- / 0", "",         # year
            random.choice(departments), "-- / 0", "",   # dept
            study_hours, "-- / 0", "",                  # hours
            loc, "-- / 0", "",                          # loc
            str(noise), "-- / 0", "",                   # noise
            audio, "-- / 0", "",                        # audio
            random.choice(social_options), "-- / 0", "",# social
            str(focus), "-- / 0", "",                   # focus
            str(productivity), "-- / 0", "",            # productivity
            random.choice(gpa_ranges), "-- / 0", "",    # gpa
            str(sleep), "-- / 0", "",                   # sleep
            str(screen_time), "-- / 0", "",             # screen time
            str(stress), "-- / 0", ""                   # stress
        ]
        rows.append(row)

    output_file = "Blank Quiz.csv"
    with open(output_file, "w", encoding="utf-8", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
    print("Overwritten Blank Quiz.csv with exactly correct options generated freshly! (150 rows)")

if __name__ == "__main__":
    main()
