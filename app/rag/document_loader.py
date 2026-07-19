from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_core.documents import Document


def load_documents(data_dir:str ="data/knowledge_base")->list[Document]:
    """
    Load all the supported documents from the knoweledge_base directory.
    currently supports:
    - .txt
    - .pdf
    """
    documents = []

    knoweledge_path = Path(data_dir)

    if not knoweledge_path.exists():
        return FileNotFoundError(
            f"Knoweledge base folder not found :{knoweledge_path}"
        )
    # .itedir-> means go through every file
    for file in sorted(knoweledge_path.iterdir()):
        if file.suffix == ".txt":
            loader = TextLoader(str(file), encoding="utf-8")
            documents.extend(loader.load())
        elif file.suffix == ".pdf":
            loader = PyPDFLoader(str(file), encoding ="utf-8")
            documents.extend(loader.load())

    return documents

