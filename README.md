# Speedy-gau

`speedy-gau.py` is a Python script that extracts URLs from a given domain with speed and efficiency. It is specifically designed to provide faster processing times compared to similar tools such as GAU or getAllUrls, while also delivering consistently reliable and accurate results.

## Requirements

- Python 3.x
- `requests` module (`pip install requests`)
- `selenium` module (`pip install selenium`)
- `os` module (`pip install os`)
- `re` module (`pip install re`)
- `argparse` module (`pip install argparse`)
- `json` module (`pip install json`)


## Usage

1. Clone this repository: `git clone https://github.com/your-username/speedy-gau.git`
2. Navigate to the cloned directory: `cd speedy-gau`
3. Run the script and specify the target URL: `python3 speedy-gau.py -u www.example.com`
- This will extract all the URLs from the website and save them to a file named `urls_yyyy-mm-dd-hh-mm-ss.txt` in the current directory.
4. You can also specify a custom output file name: `python speedy-gau.py -u www.example.com -o myurls.txt`
- This will save the extracted URLs to a file named `myurls.txt`.

## Notes

- This script is intended for educational and ethical use only. Please do not use it for any illegal or malicious activities.

- While we have designed this tool to be faster than GAU and similar tools, the actual speed of the tool will depend on various factors, such as the size of the website, the complexity of the web pages, the number of URLs to extract, and the performance of the system running the script.

- Use at your own risk.
