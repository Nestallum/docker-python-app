import pandas as pd
import numpy as np

def main():

    # Création du dataframe
    data = {
        'Nom': ['LATTAB', 'AZZAOUI'],
        'Prénom': ['Nassim', 'Mohamed'],
        'Numéro étudiant': ['123456789', '987654321']
    }

    df = pd.DataFrame(data)

    # Affichage du dataframe
    print(df)

if __name__ == "__main__":
    main()