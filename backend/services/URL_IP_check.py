# services/URL_IP_check.py
import requests
from config import Config

def check_virustotal(api_key, item):
    """
    Checks the given item (URL or IP) against the VirusTotal API.

    Parameters:
        api_key (str): The VirusTotal API key.
        item (str): The URL or IP address to check.

    Returns:
        str: Message indicating whether the item is malicious or not.
    """
    url = f"https://www.virustotal.com/api/v3/urls/{item}" if item.startswith('http') else f"https://www.virustotal.com/api/v3/ip_addresses/{item}"
    
    headers = {
        'x-apikey': api_key
    }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            json_response = response.json()
            if 'data' in json_response:
                last_analysis = json_response['data'].get('attributes', {}).get('last_analysis_stats', {})
                if last_analysis.get('malicious', 0) > 0:
                    return f"{item} is malicious."
                else:
                    return f"{item} is not malicious."
            else:
                return f"Error: Unexpected response format for {item}."
        else:
            return f"Error: Unable to retrieve data for {item}. Status code: {response.status_code}"

    except requests.exceptions.RequestException as e:
        return f"Error connecting to VirusTotal for {item}: {str(e)}"

def check_urls_and_ips(input_list):
    """
    Checks a list of URLs and IPs against VirusTotal.

    Parameters:
        input_list (list): A list of URLs and IP addresses to check.

    Returns:
        dict: A dictionary containing key-value pairs of item:message.
    """
    results = {}
    api_key = Config.VIRUSTOTAL_API_KEY

    for item in input_list:
        if not isinstance(item, str) or not item.strip():
            results[item] = "Invalid input: must be a non-empty string."
            continue
        
        # Encode URLs for VirusTotal if necessary
        if item.startswith('http'):
            item = requests.utils.quote(item, safe='')

        message = check_virustotal(api_key, item)
        results[item] = message

    return results

# Example Usage
if __name__ == "__main__":
    # Sample input list of URLs and IPs
    input_items = [
        "https://example.com",
        "8.8.8.8",  # Google's public DNS
        "http://malicious-example.com"
    ]

    results = check_urls_and_ips(input_items)
    print(results)
