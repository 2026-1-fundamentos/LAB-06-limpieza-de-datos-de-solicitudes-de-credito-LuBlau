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

def pregunta_01():
    df = pd.read_csv(
        "files/input/solicitudes_de_credito.csv",
        sep=";",
    )

    df = df.drop(columns=["Unnamed: 0"])

    columnas_texto = [
        "sexo",
        "tipo_de_emprendimiento",
        "idea_negocio",
        "barrio",
        "línea_credito",
    ]

    for columna in columnas_texto:
        df[columna] = (
            df[columna]
            .str.lower()
            .str.strip()
            .str.replace("_", " ", regex=False)
            .str.replace("-", " ", regex=False)
            .str.replace(r"\s+", " ", regex=True)
        )

    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].fillna(
        df["tipo_de_emprendimiento"].mode()[0]
    )

    df["barrio"] = df["barrio"].fillna(
        df["barrio"].mode()[0]
    )

    df["comuna_ciudadano"] = df["comuna_ciudadano"].replace(
        {
            50.0: 5.0,
            60.0: 6.0,
            70.0: 7.0,
            80.0: 8.0,
            90.0: 9.0,
        }
    )

    df["línea_credito"] = df["línea_credito"].replace(
        {
            "microempresarial": "microempresarial",
            "empresarial ed.": "empresarial",
            "empresarial ed": "empresarial",
            "empresarial ed. ": "empresarial",
            "empresarial ed ": "empresarial",
            "empresarial ed": "empresarial",
            "juridica y cap.semilla": "juridica y cap semilla",
            "juridica y cap semilla": "juridica y cap semilla",
            "juridica cap.semilla": "juridica y cap semilla",
            "juridica cap semilla": "juridica y cap semilla",
            "soli diaria": "solidaria",
        }
    )

    df["monto_del_credito"] = (
        df["monto_del_credito"]
        .astype(str)
        .str.replace(r"[^0-9]", "", regex=True)
    )

    df = df[df["estrato"] != 0]

    df = df.drop_duplicates()

    os.makedirs("files/output", exist_ok=True)

    df.to_csv(
        "files/output/solicitudes_de_credito.csv",
        sep=";",
        index=False,
    )


if __name__ == "__main__":
    pregunta_01()