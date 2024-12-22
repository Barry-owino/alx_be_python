#!/bin/bash
while True:
    weather = input("What's the weather like today? (cold/sunny/hot): ").strip().lower()

    if weather:
        if weather == "cold":
            print("It's cold! Wear a warm coat, scarf, and gloves.")
            break
        elif weather == "sunny":
            print("It's sunny! A t-shirt and sunglasses should be perfect.")
            break
        elif weather == "hot":
            print("It's hot! Wear light clothing, like shorts and a tank top.")
            break
        else:
            print("Invalid input. Please enter cold, sunny, or hot.")
    else:
        print("Input cannot be empty. Please try again.")                                                               