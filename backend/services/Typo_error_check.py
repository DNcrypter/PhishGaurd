# services/typo_error_check.py

import re

def analyze_typo_errors(email_content):
    """
    Analyzes email content for common typos associated with phishing attacks.
    
    Parameters:
        email_content (str): The content of the email as a string.
    
    Returns:
        dict: A dictionary with a 'score' for typos found and a 'details' list of identified issues.
    """
    try:
        # Define common phishing typos and variations
        typo_patterns = {
            "amazon": ["amzon", "amazn", "aamazon"],
            "paypal": ["paypa1", "paypol", "paypall"],
            "google": ["gogle", "goog1e", "googIe"],
            "microsoft": ["microsft", "micorsoft", "microsof"],
        }

        score = 0
        details = []

        # Check for typos in the email content
        for correct_term, typos in typo_patterns.items():
            for typo in typos:
                # Using regex to check for typo in a case-insensitive manner
                if re.search(rf'\b{typo}\b', email_content, re.IGNORECASE):
                    score += 1
                    details.append(f"Typo found: '{typo}' (intended: '{correct_term}')")

        return {
            "score": score,
            "type": "Typo Detection",
            "details": details
        }

    except AttributeError:
        # Handling case where email_content is None or not a string
        return {
            "score": 0,
            "type": "Typo Detection",
            "error": "Invalid input: email content must be a non-empty string"
        }
    except Exception as e:
        # General error handling
        return {
            "score": 0,
            "type": "Typo Detection",
            "error": f"An unexpected error occurred: {str(e)}"
        }
