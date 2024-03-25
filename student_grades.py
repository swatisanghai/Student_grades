import pandas as pd

# Read the CSV file
df = pd.read_csv(r"C:\Users\swati\Desktop\StudentGarde\Grades_Short.csv")


# Calculate the average of columns 'Assignment_1', 'Assignment_2', 'Quiz_1', and 'Quiz_2'
df['Assignments Average'] = df[['Assignment_1', 'Assignment_2', 'Quiz_1', 'Quiz_2']].mean(axis=1)

# Calculate the average of columns 'Mid_Term_Exam' and 'Final_Exam'
df['Exam Average'] = df[['Mid_Term_Exam', 'Final_Exam']].mean(axis=1)

# Define a function to determine letter grades based on final grade
def determine_letter_grade(final_grade):
    if final_grade > 90:
        return "A+"
    elif final_grade > 80:
        return "A"
    elif final_grade > 70:
        return "B"
    elif final_grade > 60:
        return "C"
    elif final_grade > 55:
        return "D"
    else:
        return "F"

# Apply the function to generate a new column for letter grades
df['Letter Grade'] = df['Exam Average'].apply(determine_letter_grade)

# Save the modified data as a new CSV file
df.to_csv(r"C:\Users\swati\Desktop\StudentGarde\Modified_Grades.csv", index=False)

# Display the first few rows of the modified DataFrame
print(df.head())
