from django.shortcuts import render
from django.http import HttpResponse
import random

def models_list(request):
    # Initialize or retrieve the counters from the session
    counter_8th_roll = request.session.get('counter_3rd_roll', 0)
    counter_7th_roll = request.session.get('counter_7th_roll', 0)

    # Generate a random number
    random_number = random.randint(0, 36)

    # Check if it's the 7th roll, force color to "green" (0) and reset counter
    if counter_7th_roll % 7 == 0:
        color = "green"
        random_number = 0  # Force the green number to be 0
        counter_7th_roll = 0
    # Check if it's the 3rd roll, force color to "red" and reset counter
    elif counter_8th_roll % 3 == 0:
        random_number = 34
        color = "red"
    else:
        # For other rolls, use a 50% chance for black or red
        color_probability = random.random()
        color = "green" if random_number == 0 else ("black" if color_probability < 0.5 else "red")

    # Increment the counters
    counter_8th_roll += 1
    counter_7th_roll += 1

    # Save the counters to the session
    request.session['counter_3rd_roll'] = counter_8th_roll
    request.session['counter_7th_roll'] = counter_7th_roll

    html_content = f"<p style='color:{color}'> Random number: {random_number}</p>"
    return HttpResponse(html_content)