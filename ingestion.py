
import os
from dotenv import load_dotenv

from pinecone import Pinecone
from langchain_core.embeddings import Embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_unstructured import UnstructuredLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()


# Pinecone Llama Embeddings
class LlamaEmbeddings(Embeddings):

    def __init__(self):
        self.pc = Pinecone(
            api_key=os.environ["PINECONE_API_KEY"]
        )

        self.model = "llama-text-embed-v2"
        self.dimension = 2048

    def embed_documents(self, texts):
        result = self.pc.inference.embed(
            model=self.model,
            inputs=texts,
            parameters={
                "input_type": "passage",
                "dimension": self.dimension,
                "truncate": "END"
            }
        )

        return [item.values for item in result.data]

    def embed_query(self, text):
        result = self.pc.inference.embed(
            model=self.model,
            inputs=[text],
            parameters={
                "input_type": "query",
                "dimension": self.dimension,
                "truncate": "END"
            }
        )

        return result.data[0].values


if __name__ == "__main__":

    print("Loading document...")

    loader = UnstructuredLoader(
        file_path="./mediumblog1.txt",
        chunking_strategy="basic",
        max_characters=1000000
    )

    documents = loader.load()

    print("Splitting document...")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )

    texts = text_splitter.split_documents(documents)

    print(f"Created {len(texts)} chunks")

    print("Initializing Llama embeddings...")

    embeddings = LlamaEmbeddings()

    print("Checking embedding dimensions...")

    test_vector = embeddings.embed_query("Test embedding dimension")

    print(f"Embedding dimension: {len(test_vector)}")

    assert len(test_vector) == 2048, "Incorrect embedding dimension!"

    print("Ingesting into Pinecone...")

    PineconeVectorStore.from_documents(
        documents=texts,
        embedding=embeddings,
        index_name=os.environ["INDEX_NAME"]
    )

    print("Ingestion completed successfully!")
