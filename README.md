# School District Data Generation Project

This project generates a set of school district rostering data in CSV format using the Gemini API.

## Requirements

- Python 3.6 or later but before Python 3.12 (I was unable to get 3.12 to work with google.generativeai)
- `python-dotenv` library
- `pandas` library
- `google-generativeai` library

## Setup

1. **Clone the repository**:
    ```sh
    git clone https://github.com/slicctor/genai_district.git
    cd <repository_directory>
    ```

2. **Create a virtual environment**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows: .\\venv\\Scripts\\activate
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Create a `.env` file** with your Gemini API key:
    ```env
    API_KEY=your_gemini_api_key
    ```
You can generate an API key here: https://aistudio.google.com/app/apikey

## Usage

Run the script to generate the CSV files:

```sh
python genai_district.py
```

Temperature affects the randomness of the output, which can give better results if higher. However, it can also affect the formatting which can cause errors

Below is the current prompt being fed into the model. If you try upping the number of records per file, you may run into issues because Gemini has an output character limit, which will break the CSV generator.

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