from utils.score_cheet import scores

class CCI_Score():
    def __init__(self, **patient_data):
        self.age = 0
        self.infarct = 0
        self.fcc = 0
        self.pvd = 0
        self.cva = 0
        self.dementia = 0
        self.copd = 0
        self.ctd = 0
        self.pud = 0
        self.liver = 0
        self.diabetes = 0
        self.hemiplegia = 0
        self.ckd = 0
        self.tumor = 0
        self.leukemia = 0
        self.lymphoma = 0
        self.hiv = 0
        for key, value in patient_data.items():
            setattr(self, key, value)

    def calculate_score(self):
        score = 0
        for condition in list(self.__dict__.keys()):
            score += scores[condition][self.__dict__[condition]]
        print(score)