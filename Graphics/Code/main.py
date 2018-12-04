import read_elections as election
import read_facebook as facebook
import graphic



def loadJson():    
    election.read_json()
    facebook.readJson() 

def main():
    
    loadJson()
    # Plotando Gender
    # graphic.plot_gender()
    graphic.plot_region()
    # graphic.plot_like()
    # graphic.talking_about()
    # graphic.plot_age()
    # graphic.plot_education()

if __name__ == "__main__":
    main()

