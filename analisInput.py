import dataControl as data
class AnalyseInput:
    source = "https://spaceplace.nasa.gov/all-about-neptune/en/"
    planets = ["Mercury", "Venus", "Earth", "Mars", "Juipeter", "Saturn", "Uranus", "Neptune"]
    dwarfPlanets = ["Pluto", "Ceres", "Makemake", "Haumea", "Eris"]
    pDictionary = { "Mercury" :
    """
    Mercury is the smallest planet in our solar system. It’s just a little bigger than Earth’s moon.
    It is the closest planet to the sun, but it’s actually not the hottest. Venus is hotter.
    Along with Venus, Earth, and Mars, Mercury is one of the rocky planets.
    It has a solid surface that is covered with craters. It has a thin atmosphere, and it doesn’t have any moons.
    Mercury likes to keep things simple. This small planet spins around slowly compared to Earth, so one day lasts a long time.
    Mercury takes 59 Earth days to make one full rotation. A year on Mercury goes by fast.
    Because it’s the closest planet to the sun, it doesn’t take very long to go all the way around.
    It completes one revolution around the sun in just 88 Earth days. If you lived on Mercury, you’d have a birthday every three months!
    A day on Mercury is not like a day here on Earth. For us, the sun rises and sets each and every day.
    Because Mercury has a slow spin and short year, it takes a long time for the sun to rise and set there.
    Mercury only has one sunrise every 180 Earth days! Isn't that weird?""",
    "Venus": """
    Even though Venus isn't the closest planet to the sun, it is still the hottest.
    It has a thick atmosphere full of the greenhouse gas carbon dioxide and clouds made of sulfuric acid.
    The gas traps heat and keeps Venus toasty warm.
    In fact, it's so hot on Venus, metals like lead would be puddles of melted liquid.
    Venus looks like a very active planet.
    It has mountains and volcanoes.
    Venus is similar in size to Earth.
    Earth is just a little bit bigger.
    Venus is unusual because it spins the opposite direction of Earth and most other planets.
    And its rotation is very slow.
    It takes about 243 Earth days to spin around just once.
    Because it's so close to the sun, a year goes by fast.
    It takes 225 Earth days for Venus to go all the way around the sun. 
    That means that a day on Venus is a little longer than a year on Venus.
    Since the day and year lengths are similar, one day on Venus is not like a day on Earth. 
    Here, the sun rises and sets once each day. 
    But on Venus, the sun rises every 117 Earth days. 
    That means the sun rises two times during each year on Venus,
    even though it is still the same day on Venus! 
    And because Venus rotates backwards, the sun rises in the west and sets in the east.
    Just like Mercury, Venus doesn’t have any moons.
    """}
    

    def __init__(self):
        print("Class initalized")

    def readInput(self, inputText):
        hold = inputText.split(" ")

        for i in hold:
            if i == "Mercury":
                hold = data.getData('planet', 'Mercury', 'info')
                return hold
                #return(self.pDictionary["Mercury"])
            elif i == "Venus":
                return(self.pDictionary["Venus"])
            
        return("Nothing Found")

    def giveResponse(self, text):
        return 0


if __name__ == "__main__":
    test = AnalyseInput()
    print(test.readInput("Mercury"))
    print("\n")
    print(test.readInput("Venus"))
    print("\n")
    print(test.readInput("Hello"))
