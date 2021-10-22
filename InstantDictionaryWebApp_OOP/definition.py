import pandas


class Definition:
    def __init__(self, term):
        self.term = term

    def get(self):
        df = pandas.read_csv('data.csv')
        result = tuple(df.loc[df['word'] == self.term]['definition'])

        return result


d = Definition(term='sun')
