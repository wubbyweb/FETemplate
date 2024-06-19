# FETemplate
Front End Template using gradio, module to import into various AI projects as a quickstart
This Gradio web application allows you to submit multiple line-separated numbers and send them to an HTTP API for processing.

## Features
- Accepts multiple lines of numbers as input.
- Sends the numbers to a specified API via a POST request (configurable).
- Displays the response from the API (if available).

## How to Use
- Clone the repository: If you haven't already, clone this repository to your local machine.
- Install dependencies: Run pip install gradio requests (replace requests with your preferred HTTP library if needed) to install the required libraries.
- Update API details: In the send_numbers_to_api function, replace the placeholders with your actual API URL, any necessary headers, and the data format expected by your API.
- Run the application: Execute the Python script (e.g., main.py) to launch the Gradio interface.
- Enter numbers: Type your numbers, each one on a separate line, in the text box.
- Click submit: Click the "submit" button to send the numbers to the API.
- View response: The response from the API (if any) will be displayed below the text box.

## Customization
You can adjust the size and styling of the text box using the provided CSS code in the script.
Modify the send_numbers_to_api function to customize the data processing logic according to your needs.

## Dependencies
gradio
requests (or your preferred HTTP library)

##License
[Include license information here, e.g., MIT License]