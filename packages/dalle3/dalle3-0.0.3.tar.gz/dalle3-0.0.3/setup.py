# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dalle3']

package_data = \
{'': ['*']}

install_requires = \
['requests', 'selenium', 'undetected-chromedriver']

setup_kwargs = {
    'name': 'dalle3',
    'version': '0.0.3',
    'description': 'dalle3 - Pytorch',
    'long_description': '[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)\n\n# DALLE3 API\n\nDive into the world of AI-generated images with DALLE3 API! This Python package allows you to interact with the DALL-E 3 Unofficial API, enabling you to generate and download images based on your creative prompts.\n\n## Features 🌊\n-----------\n\n-   Easy to Use: With just a few lines of code, you can start generating images.\n-   Customizable: You can provide your own creative prompts to generate unique images.\n-   Automated Download: The API automatically downloads the generated images to your specified folder.\n-   Real-Time Updates: The API provides real-time logging information about the image generation and download process.\n\n## Installation 🐠\n---------------\n\nYou can install DALLE3 API using pip:\n\n```\npip install dalle3\n```\n\n\n## Usage 🐡\n--------\n\nHere\'s a simple example of how to use DALLE3 API:\n\n```python\n# Import the necessary modules\nimport logging\nfrom dalle3 import Dalle3\n\n# Set up logging\nlogging.basicConfig(level=logging.INFO)\n\n# Instantiate the Dalle3 class with your cookie value\ndalle = Dalle3("<your_cookie>")\n\n# Open the website with your query\ndalle.open_website("Fish hivemind swarm in light blue avatar anime in zen garden pond concept art anime art, happy fish")\n\n# Get the image URLs\nurls = dalle.get_urls()\n\n# Download the images to your specified folder\ndalle.download_images(urls, "images/")\n```\n\n\n## Idea to Image prototype\n- A prototype where we use GPT4 to refine a prompt -> then create an image.\n\n`python idea_to_image.py`\n\nThe script takes the following arguments:\n\n-   `--image_to_generate`: This is a required argument. It is the text prompt for the image you want to generate.\n\n-   `--openai_api_key`: This is a required argument. It is your OpenAI API key.\n\n-   `--cookie`: This is a required argument. It is your cookie value for DALLE-3.\n\n-   `--output_folder`: This is an optional argument. It is the folder where you want to save the generated images. If not provided, it defaults to\xa0`"images/"`.\n\n### Examples\n--------\n\nHere are some examples of how to use the script from the command line:\n\n#### Example 1\n\nGenerate an image with the prompt "Fish hivemind swarm in light blue avatar anime in zen garden pond concept art anime art, happy fish, anime scenery", using your OpenAI API key and cookie value, and save the images in the default folder (`"images/"`):\n\n```bash\npython idea_to_image.py --image_to_generate "Fish hivemind swarm in light blue avatar anime in zen garden pond concept art anime art, happy fish, anime scenery" --openai_api_key "your_openai_api_key" --cookie "your_cookie_value"\n```\n\n#### Example 2\n\nGenerate an image with the prompt "A futuristic city skyline at sunset", using your OpenAI API key and cookie value, and save the images in a folder named\xa0`"futuristic_city_images/"`:\n\n```bash\npython idea_to_image.py --image_to_generate "A futuristic city skyline at sunset" --openai_api_key "your_openai_api_key" --cookie "your_cookie_value" --output_folder "futuristic_city_images/"\n```\n\nRemember to replace\xa0`"your_openai_api_key"`\xa0and\xa0`"your_cookie_value"`\xa0with your actual OpenAI API key and cookie value.\n\n------\n\n## Obtaining Your Cookie 🍪\n------------------------\n\nTo use DALLE3 API, you need to obtain your cookie from Bing Image Creator. Here\'s how you can do it:\n\n1.  Go to\xa0[Bing Image Creator](https://www.bing.com/images/create)\xa0in your browser and log in to your account.\n2.  Press\xa0`Ctrl+Shift+J`\xa0(or\xa0`Cmd+Option+J`\xa0on Mac) to open developer tools.\n3.  Navigate to the\xa0`Application`\xa0section.\n4.  Click on the\xa0`Cookies`\xa0section.\n5.  Find the variable\xa0`_U`\xa0and copy its value.\n\nNow you can use this cookie value to instantiate the\xa0`Dalle3`\xa0class.\n\n## Edge Cases 🦀\n-------------\n\n-   If the\xa0`save_folder`\xa0path you provide when calling\xa0`download_images`\xa0does not exist, the function will attempt to create it. Make sure you have the necessary permissions to create directories in the specified location.\n-   If the user is not signed in on the browser that Selenium WebDriver is controlling, the script will not be able to retrieve the cookie. Make sure you\'re signed in to your Bing Image Creator account in the same browser session.\n\n## License 📜\n----------\n\nDALLE3 API is licensed under the MIT License. See the\xa0[LICENSE](https://domain.apac.ai/LICENSE)\xa0file for more details.\n\n',
    'author': 'Kye Gomez',
    'author_email': 'kye@apac.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Agora-X/DALLE3-API',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
