import os
import requests
import json

from aiogram import Router, F
from aiogram.enums import ContentType
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from dotenv import load_dotenv

from src.keyboards.keyboard import take_choice_kb


load_dotenv()

router = Router()

#start command
@router.message(Command(commands=['start']))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {message.from_user.full_name}!", reply_markup=take_choice_kb())

#cancel command
@router.message(Command(commands=['cancel']))
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(text="Command is cancel", reply_markup=ReplyKeyboardRemove())

#handler which answer on text "Write city name"
@router.message(F.text =="Write city name")
async def answer_on_click_city_name_button(message:Message):
    await message.answer("Write city name where you want to know weather forecast")


#handler that retuen weather forecast
@router.message(F.content_type == ContentType.LOCATION)
@router.message(F.text)
async def send_weather_forecast(message: Message):
    try:
        weather_api_key = os.getenv("WEATHER_API_KEY")

        if message.location is not None:
            location = message.location
            latitude = location.latitude
            longitude = location.longitude
            url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={weather_api_key}&units=metric'
        else:
            city = message.text
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"

        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            city = data['name']
            weather = data['weather'][0]['main']
            temperature = data['main']['temp']
            wind = data['wind']['speed']
            humidity = data['main']['humidity']

            response_message = f"Hi, this is your weather forecast in {city}:\n"
            response_message += f"Outside the window now: {weather}\n"
            response_message += f"Temperature is {temperature}°C\n"
            response_message += f"Wind speed is {wind} and humidity is {humidity}%\n"
            response_message += "Be careful and have a nice day."

            await message.reply(response_message)
        else:
            await message.answer("Weather data not found. Please try again later.")
    except Exception as ex:
        print(ex)
        await message.answer("Something went wrong. Please try again later.")



