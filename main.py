from my_functions import build_person, build_experiment

if __name__ == "__main__":
    subject = build_person("Elias", "Maier", "male", 21)
    name_of_supervisor = "Dr. Müller"
    
    print(build_experiment("Experiment 1", "21-03-2024", name_of_supervisor, subject))
    