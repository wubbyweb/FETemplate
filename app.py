import gradio as gr

def send_numbers_to_api(text):
    """
    Processes the input text, sends a POST request to the specified API with the numbers,
    and returns the response (if any).

    Args:
        text (str): The input text containing multiple line-separated numbers.

    Returns:
        str (optional): The response from the API, if available.
    """

    # Split the input text into a list of numbers
    numbers = text.strip().splitlines()

    # Validate input (optional, customize error message as needed)
    if not all(num.isdigit() for num in numbers):
        return "Invalid input: Please enter only numbers separated by line breaks."

    # Replace with the actual API URL and any necessary headers/authentication
    api_url = "http://your-api-endpoint.com/process_numbers"
    headers = {'Content-Type': 'application/json'}  # Example header, adjust as needed

    # Convert numbers to JSON (or format required by your API)
    data = {'numbers': numbers}

    # Send POST request (using an HTTP library like requests)
    import requests
    response = requests.post(api_url, headers=headers, json=data)

    # Check for successful response and return the content
    if response.status_code == 200:
        return response.text
    else:
        return f"API error: {response.status_code} - {response.text}"

interface = gr.Interface(
    fn=send_numbers_to_api,
    inputs="textbox",  # Rectangular textbox with multiple line support
    outputs="text",
    css="""
        .gr-interactive-component textarea {
            height: 150px;  /* Adjust height as desired */
            width: 300px;  /* Adjust width as desired */
        }
    """
)

interface.launch(share=True)  # Launch the Gradio interface and share the link
