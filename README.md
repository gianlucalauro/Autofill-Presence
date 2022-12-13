# Autofill Presence

## Setup

0. cd into project directory
1. install dependencies with: `pip install -r requirements.txt` 
2. insert your credentials in: *credentials.json*

## Instructions
Invoke the script like this: **python** */path/to/autofill_presence.py* **"In sede" asa_1=6 asa_2=2**

 - The first argument is an enum and it can be:
	 - In sede
	 - Fuori Sede

- The second argument can have as many asa as you want with this pattern: asa_n=x

> When you are sure that the script works correctly, you can also start a cronjob
