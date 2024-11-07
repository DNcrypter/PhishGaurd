# services/Same_domain_check.py

from urllib.parse import urlparse

def extract_domain(email):
    """
    Extract the domain from an email address.

    Parameters:
        email (str): The email address from which to extract the domain.
    
    Returns:
        str: The domain extracted from the email address, or None if the email is invalid.
    """
    try:
        if "@" in email:
            return email.split("@")[1].strip()
        return None
    except Exception as e:
        print(f"Error extracting domain from email '{email}': {str(e)}")
        return None

def check_same_domain(artifact):
    """
    Check if the 'From:' and 'Reply-To:' domains are the same.

    Parameters:
        artifact (dict): A dictionary containing the 'From:' and 'Reply-To:' fields.
    
    Returns:
        dict: A dictionary indicating whether the domains are the same or different, along with messages.
    """
    try:
        from_email = artifact.get('From')
        reply_to_email = artifact.get('Reply-To')

        if not from_email or not reply_to_email:
            return {
                "same_domain": None,
                "message": "From or Reply-To field is missing."
            }

        from_domain = extract_domain(from_email)
        reply_to_domain = extract_domain(reply_to_email)

        if from_domain is None or reply_to_domain is None:
            return {
                "same_domain": None,
                "message": "Invalid email format in From or Reply-To."
            }

        if from_domain.lower() == reply_to_domain.lower():
            return {
                "same_domain": True,
                "message": "Domains are the same."
            }
        else:
            return {
                "same_domain": False,
                "message": "Domains are suspicious."
            }
    except Exception as e:
        return {
            "same_domain": None,
            "message": f"An error occurred while checking domains: {str(e)}"
        }

# Example Usage
if __name__ == "__main__":
    # Sample artifact with From and Reply-To fields
    artifact = {
        'From': 'user@example.com',
        'Reply-To': 'no-reply@anotherdomain.com'
    }

    result = check_same_domain(artifact)
    print(result)