import read_elections as election
import graphic


class Data:
    def __init__(self):
        self.candidate = []

class Candidate:    
   def __init__(self):
        self.name = ''


def main():
    
    election.read_json()

    # Plotando Gender
    graphic.plot_gender()

if __name__ == "__main__":
    main()

