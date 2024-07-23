import json
import os
import pandas as pd
import zipfile
import google.generativeai as genai
from io import StringIO
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv('API_KEY')

# Configure the API key for Gemini
genai.configure(api_key=api_key)

# Define the prompt for the Gemini API
gemini_prompt = """
Create a set of school district rostering data in CSV format according to the provided specifications. The set should include the following files: schools.csv, teachers.csv, students.csv, sections.csv,enrollments.csv, and staff.csv. The data should have the following characteristics:
- 5 Schools
- 5 Teachers per School
- 2 Staff per School
- 5 Sections per School with different grade levels
- 1 of the sections for each school should have 2 teachers
- 10 students per class
- 1 of the students in each section belongs to multiple sections in the school
- All IDs fields that are IDs or numbers must be unique
- All email addresses must be unique and realistic
- No two first names across all files can be the same
- No two last names across all files can be the same

The columns for each file should include:

### schools.csv
- school_id
- school_name
- school_number
- state_id
- low_grade
- high_grade
- principal
- principal_email
- school_address
- school_city
- school_state
- school_zip
- school_phone

### teachers.csv
- school_id
- teacher_id
- teacher_number
- state_teacher_id
- teacher_email
- first_name
- middle_name
- last_name
- title

### students.csv
- school_id
- student_id
- student_number
- email_address
- state_id
- last_name
- middle_name
- first_name
- grade
- gender
- dob

### sections.csv
- school_id
- section_id
- teacher_id
- teacher_2_id
- name
- section_number
- grade

### enrollments.csv
- school_id
- section_id
- student_id

### staff.csv
- school_id
- staff_id
- staff_email
- first_name
- last_name
- department
- title
"""

# Generate data using the Gemini API
response = genai.GenerativeModel('gemini-1.5-flash-latest').generate_content(
    gemini_prompt,
    generation_config=genai.GenerationConfig(
        response_mime_type="application/json",
        temperature=0.5
    )
)

# Extract the generated data from the API response
candidates = response.candidates
content = candidates[0].content.parts[0].text
print(content)
# print(type(content))
# Convert the JSON string to a Python dictionary
data_dict = json.loads(content)
# print(data_dict)
csv_data = data_dict

# # Directory to save CSV files
output_dir = 'school_district_data'
os.makedirs(output_dir, exist_ok=True)

# # Save each DataFrame to a CSV file
for filename, csv_string in data_dict.items():
# Convert the CSV string to a pandas DataFrame
    df = pd.read_csv(StringIO(csv_string))
    
# Save the DataFrame to a CSV file
    filepath = os.path.join(output_dir, filename)
    df.to_csv(filepath, index=False)
    print(f"Saved {filename}")

# print("All CSV files have been created and saved successfully.")
