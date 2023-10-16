# Web-Scraping-Cookie-Handler
This Python script provides functionality to handle cookie acceptances during web scraping using Pyppeteer and asyncio. It generates and clicks on the accept cookie button based on the provided or stored XPath.


## Usefulness
Web scraping often involves interacting with websites that have cookie acceptance pop-ups. These pop-ups can hinder the automation process. This Python script offers a solution by automating the handling of cookie acceptances. By providing or generating the correct XPath, this script ensures that your web scraping automation can seamlessly navigate websites with cookie accept buttons. It simplifies the scraping process, making it easier for developers to collect data from websites that implement cookie consent mechanisms.


## Key Benefits
- **Automation:** Automates the process of accepting cookies during web scraping, saving time and effort for developers.
- **Flexibility:** Allows developers to provide a specific XPath or generate one dynamically, providing flexibility in handling different types of cookie acceptance buttons.
- **Reliability:** Handles various scenarios, including retries and error logging, ensuring robustness in the face of unexpected issues.


## Prerequisites
- Python
- asyncio
- pyppeteer


## Usage
click_success, xpath_generated = await handle_cookie_accept_xpath(
                                        accept_cookie_xpath=accept_cookie_xpath ->str,
                                        page=page ->(pyppeteer page instace), accept_cookie_button=True ->bool
                                    )

## Returns:
    Tuple:
          success(bool): True if the button is accepted/clicked, False otherwise.
          xpath(string/None): XPath if found, None if not.


Feel free to integrate this script into your web scraping projects to streamline the data collection process and focus on extracting valuable insights from websites.
