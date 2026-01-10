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

