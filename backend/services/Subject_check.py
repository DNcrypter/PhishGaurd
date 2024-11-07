# services/subject_check.py

def load_malicious_subjects(filepath='malicious_subjects.txt'):
    """
    Loads malicious subject lines from a text file.

    Parameters:
        filepath (str): Path to the file containing malicious subject lines.
    
    Returns:
        list: A list of malicious subject lines or an empty list if the file is not found.
    """
    try:
        with open(filepath, 'r') as file:
            subjects = [line.strip() for line in file if line.strip()]
        return subjects
    except FileNotFoundError:
        print(f"Warning: Malicious subjects file '{filepath}' not found.")
        return []
    except Exception as e:
        print(f"Error loading malicious subjects: {str(e)}")
        return []

def check_subject_for_malicious_content(email_subject):
    """
    Checks if the email subject contains any known malicious phrases.

    Parameters:
        email_subject (str): The subject line of the email.
    
    Returns:
        dict: A dictionary containing a score based on malicious content found, type of check,
              details of malicious phrases found, and any error encountered.
    """
    try:
        # Load the dataset of malicious subjects
        malicious_subjects = load_malicious_subjects()

        # Error handling if dataset is empty
        if not malicious_subjects:
            return {
                "score": 0,
                "type": "Subject Check",
                "error": "Malicious subjects dataset is empty or not loaded."
            }

        # Check if the email subject matches any malicious patterns
        score = 0
        found_subjects = []

        for malicious_subject in malicious_subjects:
            if malicious_subject.lower() in email_subject.lower():
                score += 1
                found_subjects.append(malicious_subject)

        return {
            "score": score,
            "type": "Subject Check",
            "details": found_subjects if found_subjects else "No malicious subjects detected",
            "error": None
        }

    except AttributeError:
        # Handle case where email_subject is None or not a string
        return {
            "score": 0,
            "type": "Subject Check",
            "error": "Invalid input: email subject must be a non-empty string."
        }
    except Exception as e:
        # General error handling for any other unexpected errors
        return {
            "score": 0,
            "type": "Subject Check",
            "error": f"An unexpected error occurred: {str(e)}"  # Fixed here
        }
