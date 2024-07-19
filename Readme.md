# Meroshare IPO Automation Script

This Python script uses Selenium to automate the process of applying for IPOs on the Meroshare platform. It logs into your Meroshare account, navigates to the MyAsba section, and applies for available IPOs/FPOs if they meet specific criteria.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- Chrome browser
- ChromeDriver compatible with your Chrome version
- Required Python packages listed in `requirements.txt`


## Usages

Follow the mentioned procedure to run this project in your local system.
 - Clone or Download the Repository
```bash
    git clone https://github.com/santoshvandari/MeroshareIPOFiller.git
    cd MeroshareIPOFiller
```
 - Create the Virtual Environment Before installing the requirements. 
 ```Bash
    python3 -m virtualenv venv #For Linux User
 ```
  - Activate the Virtual Environment
  ```bash
    source venv/bin/activate  #For Linux and MAC User
     Note: It is not Necessary to Create Virtual Environment but recommanded.
  ``` 
 - Install the Requirements
```bash
    pip install -r requirements.txt
```
 - Update `.env` File With your Information. 
 ```bash
   #Sample
   USER_NAME=<Enter Your Username>
   PASSWORD=<Enter Your Password>
   DPCAPITAL=<Enter Your Bank Details> (Like: NIC ASIA BANK LIMITED (13700))
   CRN=L<Enter Your CRN Number>
   TRANSACTIONPIN=<Enter Your Transaction Pin>
 ```
 - Run the Script
 ```bash
    python3 main.py
 ```

## Contributing
We welcome contributions! If you'd like to contribute to this Mero Share IPO Filler Script, please check out our [Contribution Guidelines](Contribution.md).

## Code of Conduct
Please review our [Code of Conduct](CodeOfConduct.md) before participating in this app.

## License
This project is licensed under the MIT [License](LICENSE).