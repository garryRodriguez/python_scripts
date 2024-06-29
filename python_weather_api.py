#!/usr/bin/python3

# Author: Garry Rodriguez
# Date: June 29, 2024
# Description: Weather app in python

# import the module
#import asyncio.windows_events  ### uncomment this if on windows machine
import python_weather
import asyncio
import os

async def check_weather():
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        weather = await client.get('cebu')

        print(weather.temperature)

        for daily in weather.daily_forecasts:
            print(daily)

            for hourly in weather.hourly_forecasts:
                print(f'--> {hourly!r}')

if __name__('__main__'):
    #if os.name == 'nt':
        # Uncomment below code for windows machine
        # asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

        # To run in linux machine
    asyncio.run(check_weather())
    
        #asyncio.run(check_weather())