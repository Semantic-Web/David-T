
# coding: utf-8

# In[129]:

import rdflib
import pandas as pd
import rdflib.graph as g
import rdflib.plugins.sparql as sparql
from tabulate import tabulate
import os
from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib import plugin
from rdflib import Namespace, BNode, Literal, URIRef
from rdflib.namespace import *
from rdflib.graph import Graph, ConjunctiveGraph
from rdflib.plugins.memory import IOMemory
from pprint import pformat
from IPython.lib.pretty import pprint
from pandas import *
from pylab import *


# In[130]:

#Getting RDF datasets 
#"Infant Mortality Rate by Race" and the "US infant Population by state/region"
g = rdflib.Graph()

#Parsing Datasets
g.parse("datasets/Infant_Mortality_byRace_Totals1.rdf")
g.parse("datasets/us_infant_pop_totals_2010_2014.rdf")
g.serialize(format='pretty-xml')
print("graph has %s statements." % len(g))


# In[131]:

for s, p, o in g:
   if (s, p, o) not in g:
       raise Exception("It better be!")


# In[135]:

#Printing Raw RDF DCAT Data
print( g.serialize(format='pretty-xml') )


# In[139]:

#Displaying Classes and Distinct URI's for each subject
print("\n\n------------------------ Printing Out RDF Data -----------------------------------------------\n")

qClass = g.query("""SELECT DISTINCT ?class WHERE { ?s  a ?class.} """)
#Printing Years
print ("CLASS\n------")
for r in qClass:
    print (r[0])  
print ("----------------------------------------------")
    
qProperties = g.query("""SELECT DISTINCT ?property WHERE 
{ ?s  ?property ?o.} LIMIT 25 OFFSET 0 """)
#Printing Properties
print ("URIs\n------")
for r in qProperties:
    print (r[0])
    
    


# In[167]:

#Running Query to show the infant Mortality Rate by race in 2013
qMortality = g.query("""
    SELECT DISTINCT ?year ?race_ethnicity ?count 
    WHERE
     
        { ?s ds:year ?year. 
            ?s ds:race_ethnicity ?race_ethnicity.
            ?s ds:count ?count.
        }   

    ORDER BY DESC(?year)
    """)

#Print out Query
print("-------------------------------------------Total Deaths----------------------------------\n")
headers = ['YEAR', 'ETHNICITY','Total Deaths']
print tabulate(qMortality,headers)


# In[ ]:




# In[170]:

#Running Query to show the US infant Population sorted by Region
qTest = g.query("""
    SELECT DISTINCT ?region ?state ?race ?popestimate2013 
    WHERE 
        {?s ds1:region ?region.
         ?s ds1:state ?state. 
         ?s ds1:race ?race.
         ?s ds1:popestimate2013 ?popestimate2013. FILTER(?year=\"2013\")
         }
    ORDER BY ASC (?region)
    """)
print("----------------------------Infant US Population by State----------------------------------\n")
headers = ['REGION', 'RACE', 'POPULATION','AGE']
print tabulate(qPopulation,headers)


# In[169]:

#Running Query to show the infant Mortality Rate by race from 2004 - 2013
qMortality = g.query("""
    SELECT DISTINCT ?year ?race_ethnicity ?count ?total_livebirths_denominator ?rate 
    WHERE
    { 
        { ?s ds:year ?year. 
            ?s ds:race_ethnicity ?race_ethnicity.
            ?s ds:count ?count.
            ?s ds:total_livebirths_denominator ?total_livebirths_denominator.
            ?s ds:rate ?rate. 
        }   
        UNION
        {
            ?popestimate2013 ds1:popestimate2013 ?popestimate2013 .
            ?region ds1:region ?region.
        } 
    }ORDER BY DESC(?year)
    """)

#Print out Query
print("----------------------------Infant Mortality Rate----------------------------------")
headers = ['YEAR', 'ETHNICITY','Total Deaths','Total Births','Total Deaths Rate']
print tabulate(qMortality,headers)


# In[165]:

#Combining Datasets to find which race has the highest Mortality rate for 2013
qMortality = g.query("""
    SELECT DISTINCT ?year ?race_ethnicity ?count ?total_livebirths_denominator ?rate 
    WHERE { 
       {?s ds:year ?year. ?s ds:race_ethnicity ?race_ethnicity.?s ds:count ?count.
        ?s ds:total_livebirths_denominator ?total_livebirths_denominator.
        ?s ds:rate ?rate. FILTER(?year = \"2013\")}   
        UNION
        {?popestimate2013 ds1:popestimate2013 ?popestimate2013 .?region ds1:region ?region. } }ORDER BY DESC(?year)""")

#Print out Query
print("----------------------------Infant Mortality Rate 2013----------------------------------\n")
headers = ['YEAR', 'ETHNICITY','Total Deaths','Total Births','Total Deaths Rate']
print tabulate(qMortality,headers)

