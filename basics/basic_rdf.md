# Basics of Semantic Web Technologies: RDF

Web is built on Uniform Resource Identifiers (URIs) that uniquely identifies any resource. The Semantic Web extends this concept by using URIs to identify not only documents but also real-world objects and abstract concepts.
This allows for a more interconnected and meaningful web of data. It is made up of the following five key components:

1. **Schema**: It is the type of the data.
2. **Authority**: It controls over the namespace in URI.
3. **Path**: It is the resource identified by the URI.
4. **Query**: It provides parameters to retrieve information.
5. **Fragment**: It identifies the secondary resource.

(**Note**: Schema and Path are mandatory components of a URI, while Authority, Query, and Fragment are optional.)

A URI has two specializations known as URL and URN.

A Uniform Resource Locator (URL) is a subset of the Uniform Resource Identifier (URI) that specifies where an identified resource is available and the mechanism of retrieving it.

A Uniform Resource Name (URN) is a Uniform Resource Identifier that uses the URN scheme and does not imply the availability of the identified resource.

Both URNs (names) and URLs (locators) are URIs, and a particular URI may be both a name and a locator at the same time.

## Principles of Linked Data

<div style="text-align: right">As defined by Tim Berners Lee</div>

1. Use URIs as names for things.
2. Use HTTP URIs so that people can look up those names.
3. When someone looks up a URI, it should provide useful information.
4. Include links to other URIs so that they can discover more things.

[Source](https://www.w3.org/wiki/LinkedData)

### Linked closed data

- Data used in the company, for example, internal data of an organization.But having linked closed data opposes the principle of Linked Data, which emphasizes openness and accessibility of data on the web.

### Linked open data

- It is the data that is openly available on the web and follows the principles of Linked Data. It fosters collaboration and innovation.

## Five Star Open Data

#### ★ One Star Open Data

It is defined as the data available in the web, in any format, but with an open license. Users can access into the data and modify as per their requirements.

#### ★★ Two Star Open Data

The open data should be available in a structured machine-readable format for example in excel sheets.

#### ★★★ Three Star Open Data

Data for example that in excel sheets might require some proprietary softwares to read it. In order to win the third start, the data must be available in non-proprietary software packages. For example, CSV files instead of Excel files.

#### ★★★★ Four Star Open Data

To achieve four star open data, the data must use open standards from W3C (World Wide Web Consortium) such as RDF and SPARQL to identify things.

#### ★★★★★ Five Star Open Data

With the help of W3C standards and linked data principles, data publishers link their data to other data providing context. According to Tim Berners Lee, this is the highest quality of open data and hence it is awarded the fifth star.

## Resource Description Framework (RDF)

RDF is a set of triples which has

**Subject** -> **Predicate** -> **Object**

for example:

**Subject**: The entity (eg. Bernie Sanders)
**Predicate**: The relationship between the subject and object (eg. isSenatorOf)
**Object**: The value or another entity (eg. Vermont)

RDF standing for Resource Description Framework is a standard datamodel to exchange information. It is a framework for representing information about resources in the web. RDF uses a graph-based data model to represent relationships between resources using triples, which consist of a subject, predicate, and object.
These triples are not bound by any specific formats and hence can be serialized in various formats such as:

### RDF/XML

```xml
<xml version="1.0"?>

<rdf: RDF
xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
xmlns:schema="http://schema.org">

<rdf:Description rdf:about="http://example.org/person/Ernest_Hemingway">
    <schema:name>Ernest Hemingway</schema:name>
    <schema:birthDate>1899-07-21</schema:birthDate>
    <schema:birthPlace rdf:resource="http://dbpedia.org/resource/United_States">
</rdf:Description>
```

### RDFa

It is the RDF syntax inside HTML documents. RDFa is fundamentally different than other formats as it combines RDF with HTML making HTML documents much larger and complicated. If the application has a lot of RDF data, RDFa does not come much in handy.

```html

<div about="http://example.org/person/Ernest_Hemingway">
    <p>
    Ernest was born on
    <span property="http://schema.org/birthDate">1899-07-21</span>
    in
    <a
    property="http://schema.org/birthPlace"
    href="http://dbpedia.org/resource/United_States"
    >
    United States
    </p>
</div>
```

### Turtle

Turtle are highly human-readable and therefore is a popular serialization format for RDF data.

```turtle
@prefix ernest: <http://example.org/People/Ernest_Hemingway>.
@prefix schema: <http://schema.org>.
@prefix dbpedia:<https://dbpedia.org/resource>.

<ernest> schema:birthDate "1899-07-21"^^<http://www.w3.org/2001/XMLSchema#date>.
<ernest> schema:birthPlace <dbpedia:United_States>.
```

### N-Triples and N-Quads

It is the simple subset of Turtle. N-triples does not support prefixes, or any fancy features.

```ntriples
<http://example.org/People/Ernest_Hemingway> <http://schema.org/birthDate> "1899-07-21"^^<http://www.w3.org/2001/XMLSchema#date> .
<http://example.org/People/Ernest_Hemingway> <http://schema.org/birthPlace> <https://dbpedia.org/resource/United_States> .
```

### JSON-LD

JSON is the most popular way to serialize data in web applications. JSON-LD is the extension of JSON and is valid JSON as well. We can convert plain JSON to RDF just by adding @context.

```JSON
{

    @context:{
        "schema": "http://schema.org/",
        "dbpedia": "https://dbpedia.org/resource/",
    },

    @id:"http://example.org/People/Ernest_Hemingway",
    "schema:birthDate":"1899-07-21",
    "schema:birthPlace": {"@id":"dbpedia:United_States"}
}
```

JSON-LD is easy to read and can be familiar to those who are not used to semantic web technologies.

## For our project

We will be using Turtle as our RDF serialization format due to its human readability, ease of use, and wide adaptation in the semantic web community.

This is the basics of RDF and we will be using more of it in our pipeline explain each and every minute detail.
