class Engine:
    def __init__(self) -> None:
        self._mixture_translit = str.maketrans(
            "аеёорсухАВЕЁЗКМНОРСТХ",  # кириллица
            "aeeopcyxABEE3KMHOPCTX",  # латиница
        )

    def generate_mixture(self, text: str):
        return text.translate(self._mixture_translit)
