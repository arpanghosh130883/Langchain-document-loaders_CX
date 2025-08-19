# pip install chardet charset-normalizer

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader, TextLoader

# Load PDFs
pdf_loader = DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

# Load TXT files
txt_loader = DirectoryLoader(
    path='books',
    glob='*.txt',
    loader_cls=TextLoader,
    loader_kwargs={"encoding": "utf-8", "autodetect_encoding": True} # If we have .txt files with different encoding like utf-8 and utf-16 , we need to remove the hardcoded "encoding": "utf-8" and keep only "autodetect_encoding": True 
)

# Combine the two loaders
docs = list(pdf_loader.lazy_load()) + list(txt_loader.lazy_load())

# Print metadata for each document
for document in docs:
    print(document.metadata)


