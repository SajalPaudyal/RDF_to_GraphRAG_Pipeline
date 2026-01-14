import pandas as pd
from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF, RDFS, XSD

NS = Namespace("http://www.semanticweb.org/sajalpaudyal/ontologies/2026/lemonde100/")

LE_MONDE_DS = "../data/books.csv"
OUTPUT_FILE = "books_ranking.ttl"

def create_uri_id(text) -> str:
    if pd.isna(text):
        return "Unknown"
    return str(text).strip().replace(" ","_").replace("/", "_").replace("'","").replace("-","_")


def handle_split_values(row_value, book_uri, property_uri, class_type, cache_type):
    if pd.isna(row_value): return
    
    items = [item.strip() for item in str(row_value).split(",")]
    
    
    for item_name in items:
        item_id = create_uri_id(item_name)
        item_uri = NS[item_id]
                
        g.add((book_uri, property_uri, item_uri))
        
        
        if item_id not in cache_type:
            g.add((item_uri, RDF.type, class_type))
            g.add((item_uri, RDFS.label, Literal(item_name)))
            cache_type.add(item_id)
        

g = Graph()
g.bind("ns", NS)
g.bind("rdf", RDF)

print(f"Reading {LE_MONDE_DS}")
df = pd.read_csv(LE_MONDE_DS)

authors_cache = set()
genres_cache = set()
language_cache = set()

print(f"converting data")

for index, row in df.iterrows():
    
    book_id = f"Book_{int(row['No'])}"
    book_URI = NS[book_id]
    
    g.add((book_URI, RDF.type, NS.Book))
    
    g.add((book_URI, NS.title, Literal(row['Title'])))
    g.add((book_URI, RDFS.label, Literal(row['Title']))) 
    
    try:
        ranking_value = int(row.get('Ranking', row.get('No', 0)))
        g.add((book_URI, NS.leMondeRank, Literal(ranking_value, datatype=XSD.integer)))
    except:
        pass
    
    
    g.add((book_URI, NS.description, Literal(row['Description'])))
    g.add((book_URI, RDFS.comment, Literal(row['Description'])))
    
    
    year_val = str(row['Year'])
    g.add((book_URI, NS.publicationYear, Literal(year_val, datatype=XSD.gYear)))
    
    rating_val = float(row['GoodRead_rating'])
    g.add((book_URI, NS.goodReadRating, Literal(rating_val, datatype=XSD.decimal)))
    
    
    handle_split_values(row["Author"], book_uri=book_URI, property_uri=NS.hasAuthor, class_type=NS.Author, cache_type=authors_cache)
    handle_split_values(row["Genre"], book_uri=book_URI, property_uri=NS.hasGenre, class_type=NS.Genre, cache_type=genres_cache)
    handle_split_values(row["Language"], book_uri=book_URI, property_uri=NS.inLanguage, class_type=NS.Language, cache_type=language_cache)

g.serialize(destination=OUTPUT_FILE, format='turtle')
print(f"Successfully created a new RDF data file")