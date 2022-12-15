# Autofill Presence

## Setup

0. cd into project directory
1. install dependencies with: `pip install -r requirements.txt` 
2. insert your credentials in: [*credentials.json*](credentials.json)

## Instructions

> The first argument is an enum and it can be:
> - Presenza
> - Smart

### Presenza

Invoke the script like this: **python** [*/path/to/autofill_presence.py*](src/autofill_presence.py) **"Presenza" "In sede" asa_1=6 asa_2=2**

 - The second argument is an enum and it can be:
	 - **In sede**
	 - **Fuori Sede**

- The third argument can have as many asa as you want with this pattern: **asa_n=x**

### Smart

Invoke the script like this: **python** [*/path/to/autofill_presence.py*](src/autofill_presence.py) **"Smart" 8 0800**

- The second argument is used for smart working hours

- The third argument is for the current datetime hours. The format in hours is, for example: **1030** *(equals 10:30)*


> When you are sure that the script works correctly, you can also start a cronjob
