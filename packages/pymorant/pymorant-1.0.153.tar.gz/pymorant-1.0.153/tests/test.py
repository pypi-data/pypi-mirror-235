
import sys
sys.path.append('/Users/artbrare/Documents/Morant/py_morant/src')
from pymorant import llm # noqa

if __name__ == '__main__':

    categorias = ["es_solicitud", "no_es_solicitud"]

    texto = "me llamo chuchin" # noqa

    data_asignar = llm.asignar_una_categoria(
        texto,
        categorias,
        "gpt-4",
        "",
    )

    print(data_asignar)
