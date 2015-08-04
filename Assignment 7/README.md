Assignment 7 Top Ranked Florida Colleges by Population:
--------------------------------------------------------
I received data of the top largest schools in Florida and used GeoNames to find each of their exact addresses 

CSV Table Top Populated Florida Schools:
-----------
![tag](https://raw.githubusercontent.com/Semantic-Web/David-T/master/Assignment%207/top10FloridaSchools.png)

Code to Find School Addresses:
-------------------------------
![tag](https://raw.githubusercontent.com/Semantic-Web/David-T/master/Assignment%207/GeonamesCodeForAddresses.png)

Addresses:
----------
![tag](https://raw.githubusercontent.com/Semantic-Web/David-T/master/Assignment%207/AddressesForTop10FloridaSchools.png)

Graph:
------
![tag](https://raw.githubusercontent.com/Semantic-Web/David-T/master/Assignment%207/Graph.png)

Description:
--------------
See the write up on "Apps based on geonames" in the Project Topics list. Explore this link: http://www.geonames.org/export/ . GeoNames is offering a wide range of sophisticated web services. The list can be found here: http://www.geonames.org/export/ws-overview.html . Here are libraries in various languages:  http://www.geonames.org/export/client-libraries.html  . Java is supported; Python does not seem to be. Explore any of the web services app for an objective and write Java/Python code for achieving that. It does not have to be the perfect end product. Ideally, you should be looking at the database as RDF statements and using a tool such as Fuxi or Jena. If you wish to use RegEx (regular expression) for parsing, knowing the ontology format, that is OK too.
Please use only one of these two languages (Java or Python, if you can find somewhere else a library; you can actually write one based on RegEx. It is well explained in an online free book ("Think Python") by Downey).

Apps based on geonames
Geonames site has API support for accessing their semantic database. Here are some relevant links 
-	http://www.geonames.org/about , 
-	http://www.programmableweb.com/news/123-database-apis-geonames-freebase-and-yahoo-query-language/2012/05/23  
o	(a link to show the popularity of the site forapp developers) 
-	http://www.geonames.org/ontology/documentation.html   
o	(about the ontology),  
-	http://datahub.io/dataset/geonames-semantic-web  
o	(rdf schema and examples) 
-	http://www.geonames.org/ontology/ontology_v3.1.rdf
-	http://www.geonames.org/source-code/javadoc/  
o	(geonames APIs). 
A Project based on geonames would use this geonames data and combine it with any data at data.gov, to give us some specifics. Examples: List of lakes in order of their size, pollution, etc; List of cities in order of their industry output, academic population, etc. Look at the apps created by other users to get some ideas. You may use Python or Java.

Linked Data
The Features in the GeoNames Semantic Web are interlinked with each other. Depending on applicability the following documents are available for a Feature :
The children (countries for a continent, administrative subdivisions for a country, ...). As an example the children of France : http://sws.geonames.org/3017382/contains.rdf
The neighbors (neighboring countries). As an example the neighbors of France :http://sws.geonames.org/3017382/neighbours.rdf
Nearby features. Nearby to the Eiffel Tower are Champ de Mars,Trocadéro - Palais de Chaillot, ...:http://sws.geonames.org/6254976/nearby.rdf


Entry Points into the GeoNames Semantic Web
There are several ways how you can enter the GeoNames Semantic Web :
•	start from mother earth and follow the Linked Data links.
•	use the geonames search webservice with the type=rdf parameter option.
•	download the database dump and construct the url for the features using the pattern "http://sws.geonames.org/geonameId/"
•	RDF dump with 10113356 features and about 150 mio rdf triples (2015 04 21). The dump has one rdf document per toponym on every line of the file. Note: The file is pretty large. Make sure the tool you use to uncompress is able to deal with the size and does not stop after 2GB, an issue that happens with some old (windows) tool versions.
Experiment:
-	Give a List of lakes in order of their size, pollution, etc; 
-	List of cities in order of their industry output, academic population,
