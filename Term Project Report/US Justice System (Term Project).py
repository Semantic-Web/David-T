
# coding: utf-8

# In[207]:

import rdflib
import numpy as np
import pylab
import os
import matplotlib.pyplot as plt
import matplotlib
import FuXi
from pandas import *
import pandas
from IPython.lib.pretty import pprint
from rdflib import Variable, Namespace
from rdflib import plugin,RDF,RDFS,URIRef,URIRef,Literal,Variable
from tabulate import tabulate


# In[62]:

#Getting RDF datasets 
#Parsing Datasets
g = rdflib.Graph()
g.parse("datasets/the-counted.rdf")
g.parse("datasets/US-Population.rdf")
pop = read_csv('datasets/US-Population')
g.serialize(format='pretty-xml')
print("graph has %s statements." % len(g))


# In[171]:

#Getting Police Death Statistics 
#Displaying RDF Model
for s, p, o in g:
   if (s, p, o) not in g:
       raise Exception("It better be!")
#Printing Raw RDF DCAT Data
print( g.serialize(format='n3') )
#print out head out data
pop.head(2)


# In[172]:

#Grouping Population By Race and Total Count for each Race
races = pop.groupby('RACE')[('POPESTIMATE2014')].sum().order()
#Pretty printing data 
population = DataFrame(races[::-1])
print '                     US population for each Race                                     '
print '----------------------------------------------------------------------------'
#pprint(population)
headersp = ['RACE' , 'TOTAL POPULATION']
print tabulate(population,headers, tablefmt="fancy_grid",floatfmt=".0f")


# In[173]:

#Displaying the names, gender, and ethnicity of people killed by police so far in 2015
#Running SPARQL Query to aggregaete RDF data
policeKillings = g.query("""
    SELECT DISTINCT ?name ?gender ?raceethnicity ?age ?armed ?state  
    WHERE{  
            ?s ds:name ?name.
            ?s ds:gender ?gender.
            ?s ds:raceethnicity ?raceethnicity.
            ?s ds:age ?age.
            ?s ds:armed ?armed.
            ?s ds:state ?state.} 
    ORDER BY ASC(?state)
    LIMIT 50
    """)
#Print out Query
print("-----------------------------People Who got Killed by Police in 2015------------------------\n")
headers = ['NAME', 'GENDER','ETHNICITY','AGE','ARMED','STATE']
#deathsByRace = tabulate(policeKillings,headers, tablefmt="fancy_grid")
deathsByRace = tabulate(policeKillings,headers)
print deathsByRace


# In[174]:

#Displaying the number of deaths for each race
#Running SPARQL Query to aggregaete RDF data
tbr = g.query("""
    SELECT DISTINCT ?raceethnicity (COUNT(?raceethnicity) AS ?rCount)
    WHERE{?s ds:raceethnicity ?raceethnicity.}
    GROUP BY ?raceethnicity 
    ORDER BY DESC(?rCount)
    """)
#Print out Query
print("-----------------------------Total Deaths by Police ordered by Race------------------------\n")
headers2 = ['RACE','TOTAL DEATHS' ]
print tabulate(tbr,headers2,tablefmt="fancy_grid")


# In[213]:

#Verifying Data with csv file
tc = read_csv('datasets/the-counted')
totalDeaths = tc.groupby(['raceethnicity']).size().order()
td = DataFrame(totalDeaths[::-1])
print tabulate(td,headers2,tablefmt="fancy_grid")
print"    COMPARING GRAPHS FOR TOTAL RATES\n                 "
print tabulate(population,headersp, tablefmt="fancy_grid",floatfmt=".0f")
ttr = DataFrame()
print"\n---------------------OVERALL TOTAL DEATH RATE by PEOPLE KILLED BY THE POLICE------------------------"
print tabulate([["RACE","TOTAL DEATH RATE BY POLICE"],["White",3.2],["Black",9.6],["Asian",1.23],["American Indian",4.97],["Native Hawaiian",1.7]]
               ,headers="firstrow",floatfmt=".2f",tablefmt="fancy_grid")

