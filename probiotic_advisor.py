# probiotic_app.py

class Probiotic:
    def __init__(self, name, strains, target_symptoms):
        self.name = name
        self.strains = strains
        self.target_symptoms = target_symptoms

    def matches_symptom(self, symptom):
        return symptom.lower() in [s.lower() for s in self.target_symptoms]


class ProbioticAdvisor:
    def __init__(self):
        self.probiotics = self._load_probiotics()

    def _load_probiotics(self):
        # Simulated database
        return [
            Probiotic("GutBoost+", ["Lactobacillus acidophilus"], ["bloating", "constipation"]),
            Probiotic("ImmuneShield", ["Bifidobacterium lactis"], ["cold", "weak immunity"]),
            Probiotic("MoodZen", ["Lactobacillus rhamnosus"], ["stress", "anxiety"]),
            Probiotic("Digestify", ["Saccharomyces boulardii"], ["diarrhea", "IBS"]),
        ]

    def recommend(self, symptoms):
        recommendations = []
        for symptom in symptoms:
            for prob in self.probiotics:
                if prob.matches_symptom(symptom):
                    recommendations.append((symptom, prob))
        return recommendations


def main():
    print("🦠 Welcome to the Probiotic Advisor!")
    symptoms_input = input("Please enter your symptoms (comma-separated): ")
    symptoms = [s.strip() for s in symptoms_input.split(",")]

    advisor = ProbioticAdvisor()
    recs = advisor.recommend(symptoms)

    if not recs:
        print("Sorry, no specific probiotics found for your symptoms.")
    else:
        print("\nRecommended Probiotics:")
        for symptom, prob in recs:
            print(f" - For '{symptom}', consider: {prob.name} ({', '.join(prob.strains)})")

if __name__ == "__main__":
    main()
