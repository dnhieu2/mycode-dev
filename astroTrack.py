#!/user/bin/python3

import requests

astrourl = 'http://api.open-notify.org/astros.json'

def main():
    url = requests.get(astrourl)
    astrodict = url.json()

    #print("\n\nConverted Python data")
    #print(astrodict)

    print ('\n\nPeople in Space: ', astrodict['number'], '\n---------------------------------')

    for every_astronaut_dict in astrodict["people"]:
        print(f"{every_astronaut_dict['name']} is on {every_astronaut_dict['craft']}")

if __name__ == "__main__":
    main()
