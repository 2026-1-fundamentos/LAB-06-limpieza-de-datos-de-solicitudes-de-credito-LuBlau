"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""

import os

import pandas as pd # type: ignore

def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """

    df = pd.read_csv(
        "files/input/solicitudes_de_credito.csv",
        sep=";",
    )

    df = df.drop(columns=["Unnamed: 0"])

    df["sexo"] = df["sexo"].str.lower().str.strip()

    df["tipo_de_emprendimiento"] = (
        df["tipo_de_emprendimiento"]
        .str.lower()
        .str.strip()
    )

    df["idea_negocio"] = (
        df["idea_negocio"]
        .str.lower()
        .str.strip()
        .str.replace("_", " ", regex=False)
        .str.replace("-", " ", regex=False)
        .str.replace(r"\s+", " ", regex=True)
    )

    df["barrio"] = (
        df["barrio"]
        .str.lower()
        .str.strip()
        .str.replace("_", " ", regex=False)
        .str.replace("-", " ", regex=False)
        .str.replace(r"\s+", " ", regex=True)
    )

    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].fillna(
        df["tipo_de_emprendimiento"].mode()[0]
    )

    df["barrio"] = df["barrio"].fillna(df["barrio"].mode()[0])

    os.makedirs("files/output", exist_ok=True)

    df.to_csv(
        "files/output/solicitudes_de_credito.csv",
        sep=";",
        index=False,
    )


if __name__ == "__main__":
    pregunta_01()