# RDF to GraphRAG Pipeline

This repository contains a pipeline of converting CSV Data (List of top 100 books of the century as ranked by Le Monde - the most popular newspaper in France). 

## Folder structure

- `data/`: Contains the CSV data file.
- `code/`
   - `ontology_creator.py`: [ontology_creator.py](./code/ontology_creator.py) contains the code to convert CSV data to RDF triples using the `rdflib` library.
   - `langchain_graphdb.ipynb`: [langchain_graphdb.ipynb](./code/langchain_graphdb.ipynb) contains the code to interact with a Graph Database using LangChain framework.
- `rules/`: Contains the ontology rules for RDF created using [`protégé`](https://protege.stanford.edu/) tool.
- `.env`: Contains environment variables for authentication and database connection.
- `requirements.txt`: Lists the Python dependencies required for the project.

## Pipeline Description
1. **Data Preparation**: The CSV file containing the list of top 100 books is stored in the `data/` folder.
2. **Creating a OWL Ontology**: You can refer to [`owl basics`](./basics/basic_owl.md) to understand what is OWL ontology and how can it go hand on hand with RDF. 
3. **Creating the OWL Ontology using Protégé**: The OWL ontology is created using the Protégé tool, defining classes, properties, and individuals for the book domain. The process is described (for this project) in the [`protege_basics`](./basics/protege_basics.md) file. But it will give you a proper guideline to create the entire ontology from scratch to any project you desire.
4. **Converting CSV to RDF Triples**: We reads the CSV file and convert each row into RDF triples based on the defined ontology using the `python-rdflib` library.
5. ****Storing RDF Triples in Graph Database**: The generated RDF triples are stored in a Graph Database (`GraphDB`) for efficient querying and retrieval. You just need to import the RDF file into the GraphDB repository.
6. **Interacting with Graph Database using LangChain**: The documentation from [`langchain`](https://docs.langchain.com/oss/python/integrations/graphs/ontotext) notebook gives step by step process to interact with the Graph Database using the LangChain framework.

## Environment Variables
The `.env` file contains the following environment variables
- `HF_TOKEN`: Hugging Face authentication token.
- `GRAPHDB_URL`: URL of the GraphDB instance.
- `GRAPH_DB_USERNAME`: Username for the Graph Database.
- `GRAPH_DB_PASSWORD`: Password for the Graph Database.

## Requirements
The required Python packages are listed in the `requirements.txt` file. You can install them using:
```python
pip install -r requirements.txt
```

## Usage
1. Ensure you have set up the `.env` file with the necessary environment variables.
2. Create the OWL ontology using Protégé and save it in the `rules/` folder.
3. Run the `ontology_creator.py` script to generate RDF triples from the CSV data.
4. Import the generated RDF file and OWL ontology into your GraphDB repository.
5. Use the `langchain_graphdb.ipynb` notebook to interact with the Graph Database using LangChain.


## Note
- In my example to interact with the Graph Database GraphDB with LangChain, I have used the local instance of GraphDB. 
- The language model we have used the `GLM 4.7` model by the `Z.ai` available on Hugging Face. There are more efficient models (I used this just to try out it's capabilities and efficiency with SPARQL). You can know further about it from the official [HuggingFace documentation](https://huggingface.co/zai-org/GLM-4.7-FP8) page.