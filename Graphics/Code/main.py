import read_elections as election
import graphic


def main():
    
    election.read_json()

    # Plotando Gender
    graphic.plot_gender()

if __name__ == "__main__":
    main()

