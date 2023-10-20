# weather_bot

## Installation First, you need to clone this repository:
```bash
git clone https://github.com/Misha251994/weather_bot_1.git
```
## Then change folder:
```python
cd weather_bot
```
## Now, we will need to create and activate  a virtual environment also install all the dependencies:
### On Windows
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
### On macOS , Linux
```commandline
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
## Before start work create .env file and make:
```commandline
**BOT_TOKEN** for telegram bot -> use command /newbot in telegram chat with  BotFather
 
```
 ```
 **WEATHER_API_KEY** -> register on the site "https://openweathermap.org/" and create API Key
 ```

## To start the bot use the command:
```commandline
python main.py
```

# Usage
## Make a few steps to right work:
### Click -> Menu <-
### Choose -> /start <-
### Click -> Write city name <- , write and bot send weather forecast for choosen city
### Click -> Send location <- , send location for bot and take weather forecast (work only in mobile version)