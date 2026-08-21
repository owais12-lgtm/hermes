---
title: "Environmental Sensor"
description: "Gets data from a BME690 environmental sensor (Temperature, Humidity, Pressure, IAQ, bVOC, CO₂) and displays it on a 0.96\" OLED screen, controlled by a Xiao RP2040. Also includes an LED matrix for looks — it's just super cool!"
created_at: "2026-08-20"
---

# June 8th: Sensor Hunting and First Schematic

Today I worked on finding some cool sensors I could use for my project. I went through a whole list of options, including wind speed trackers, rain sensors, and about a hundred different air quality and humidity sensors. It was really fun, but honestly not that useful in the end.

I settled on a specific sensor with a lot of functions: the **BME690**. It has temperature, humidity, and pressure sensing, plus a bunch of other gas-related features I might find useful.

I then worked on the schematic and had to make my own symbol for it, since no one has published symbols for this sensor.

After that, I had to watch a tutorial on how to make a footprint, since no one has those either. Once I got those done, I moved on to making the PCB and routing it.

I found a bunch of empty space on one side of the PCB that I couldn't fill with other components, so I decided to add an LED matrix!
<img width="764" height="809" alt="image" src="https://github.com/user-attachments/assets/fc1dbc12-bcba-485b-bf76-c2cc6ee461d2" />

![Image 1](https://cdn.hackclub.com/01a01f79-5555-788d-981d-39b5cb872101/image.png)
![Image 2](https://cdn.hackclub.com/01a01f79-5824-7765-a88a-32092d874649/image.png)
![Image 3](https://cdn.hackclub.com/01a01f79-5aca-7c24-9fa8-b5e0db4c95bf/image.png)
![Image 4](https://cdn.hackclub.com/01a01f79-5da0-7f82-8f8c-2ee32fef2fa0/image.png)
![Image 5](https://cdn.hackclub.com/01a01f79-609d-7d62-b050-eba3571c7769/image.png)
![Image 6](https://cdn.hackclub.com/01a01f79-6403-7bcc-ad93-8c93f66bca6f/image.png)

**Total time spent: 3h**
