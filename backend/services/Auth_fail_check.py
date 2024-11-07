# services/Auth_fail_check.py

def check_spf(spf_result):
    """
    Check if SPF authentication has failed.

    Parameters:
        spf_result (str): The SPF result to check.

    Returns:
        dict: A dictionary with the SPF status and message.
    """
    try:
        if spf_result.lower() == 'fail':
            return {
                "spf": "fail",
                "message": "SPF authentication failed."
            }
        return {
            "spf": "pass",
            "message": "SPF authentication passed."
        }
    except Exception as e:
        return {
            "spf": "error",
            "message": f"Error checking SPF: {str(e)}"
        }

def check_dmarc(dmarc_result):
    """
    Check if DMARC authentication has failed.

    Parameters:
        dmarc_result (str): The DMARC result to check.

    Returns:
        dict: A dictionary with the DMARC status and message.
    """
    try:
        if dmarc_result.lower() == 'fail':
            return {
                "dmarc": "fail",
                "message": "DMARC authentication failed."
            }
        return {
            "dmarc": "pass",
            "message": "DMARC authentication passed."
        }
    except Exception as e:
        return {
            "dmarc": "error",
            "message": f"Error checking DMARC: {str(e)}"
        }

def check_dkim(dkim_result):
    """
    Check if DKIM authentication has failed.

    Parameters:
        dkim_result (str): The DKIM result to check.

    Returns:
        dict: A dictionary with the DKIM status and message.
    """
    try:
        if dkim_result.lower() == 'fail':
            return {
                "dkim": "fail",
                "message": "DKIM authentication failed."
            }
        return {
            "dkim": "pass",
            "message": "DKIM authentication passed."
        }
    except Exception as e:
        return {
            "dkim": "error",
            "message": f"Error checking DKIM: {str(e)}"
        }

def check_authentication_results(artifacts):
    """
    Check authentication results from a list of artifacts.

    Parameters:
        artifacts (list): A list containing SPF, DMARC, and DKIM results.

    Returns:
        dict: A summary of authentication checks with their results and messages.
    """
    results = {}

    # Process the artifacts array
    for artifact in artifacts:
        if 'spf' in artifact:
            results.update(check_spf(artifact['spf']))
        if 'dmarc' in artifact:
            results.update(check_dmarc(artifact['dmarc']))
        if 'dkim' in artifact:
            results.update(check_dkim(artifact['dkim']))
    
    return results

# Example Usage
if __name__ == "__main__":
    # Sample artifacts array with authentication results
    artifacts = [
        {'spf': 'fail', 'dmarc': 'pass', 'dkim': 'fail'},
        {'spf': 'pass', 'dmarc': 'fail', 'dkim': 'pass'}
    ]

    # Check results for each artifact
    for index, artifact in enumerate(artifacts):
        auth_results = check_authentication_results([artifact])  # Pass each artifact as a list
        print(f"Results for artifact {index + 1}: {auth_results}")
