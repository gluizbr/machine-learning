import pandas as pd

class SEX:
    def process_data(self):
        self.drop(
            self[
                (pd.isna(self.sexo) == False)
                & (self.sexo != 'male')
                & (self.sexo != 'Male')
                & (self.sexo != 'Female')
                & (self.sexo != 'female')
                ]
            .index)
        self.sexo = [(pd.isna(value) and value or str(value).lower()) for value in self.sexo]
        self.sexo = self.sexo.fillna(self.sexo.mode()[0])
        for i, row in self.iterrows():
            if str(row.sexo) == 'male':
                #   homem
                ifor_val = "0"
            if str(row.sexo) == 'female':
                #   mulher
                ifor_val = "1"
            self.at[i, 'sexo'] = ifor_val
        return self.sexo
