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

## Usage

Run the script to generate the CSV files:

```sh
python genai_district.py
