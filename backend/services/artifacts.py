import email
import re
from email import policy
from email.parser import BytesParser

def parse_eml_file(eml_file_path):
    """
    Parse an .eml file and collect specified artifacts.

    Parameters:
        eml_file_path (str): The path to the .eml file.
    
    Returns:
        dict: A dictionary containing the collected artifacts.
    """
    artifacts = {
        "subject_address": None,
        "subject_line": None,
        "reply_to": None,
        "message_id": None,
        "date_time": None,
        "authentication_status": None,
        "content_type": None,
        "meta_data": {},
        "mail_server": None
    }

    try:
        # Read the .eml file
        with open(eml_file_path, 'rb') as eml_file:
            # Parse the email
            msg = BytesParser(policy=policy.default).parse(eml_file)

            # Collect artifacts
            artifacts["subject_address"] = msg['From']
            artifacts["subject_line"] = msg['Subject']
            artifacts["reply_to"] = msg['Reply-To']
            artifacts["message_id"] = msg['Message-ID']
            artifacts["date_time"] = msg['Date']
            artifacts["authentication_status"] = msg.get('Authentication-Results', None)
            artifacts["content_type"] = msg.get_content_type()

            # Extract meta data
            for key, value in msg.items():
                if key not in artifacts and key not in ['From', 'Subject', 'Reply-To', 'Message-ID', 'Date', 'Authentication-Results']:
                    artifacts["meta_data"][key] = value

            # Collect mail server information if present in headers
            mail_server = msg.get('X-Mailer')  # You can check other headers as needed
            artifacts["mail_server"] = mail_server

    except FileNotFoundError:
        print(f"Error: The .eml file '{eml_file_path}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred while parsing the .eml file: {str(e)}")

    return artifacts

# Example Usage
if __name__ == "__main__":
    eml_path = 'path/to/your/file.eml'  # Update with your .eml file path
    result = parse_eml_file(eml_path)
    for key, value in result.items():
        print(f"{key}: {value}")
