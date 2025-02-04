
from connection import run_query

actors = [
    "CREATE (a:Actor {name: 'Tom Hanks'})",
    "CREATE (a:Actor {name: 'Meryl Streep'})",
    "CREATE (a:Actor {name: 'Tom Cruise'})",
    "CREATE (a:Actor {name: 'Julia Roberts'})",
]

movies = [
    "CREATE (m:Movie {title: 'Forrest Gump', year: 1994})",
    "CREATE (m:Movie {title: 'The Post', year: 2017})",
    "CREATE (m:Movie {title: 'Top Gun', year: 1986})",
    "CREATE (m:Movie {title: 'Pretty Woman', year: 1990})",
]

for actor in actors:
    run_query(actor)

for movie in movies:
    run_query(movie)

relationships = [
    "MATCH (a:Actor {name: 'Tom Hanks'}), (m:Movie {title: 'Forrest Gump'}) CREATE (a)-[:ACTED_IN]->(m)",
    "MATCH (a:Actor {name: 'Tom Hanks'}), (m:Movie {title: 'The Post'}) CREATE (a)-[:ACTED_IN]->(m)",
    "MATCH (a:Actor {name: 'Meryl Streep'}), (m:Movie {title: 'The Post'}) CREATE (a)-[:ACTED_IN]->(m)",
    "MATCH (a:Actor {name: 'Tom Cruise'}), (m:Movie {title: 'Top Gun'}) CREATE (a)-[:ACTED_IN]->(m)",
    "MATCH (a:Actor {name: 'Julia Roberts'}), (m:Movie {title: 'Pretty Woman'}) CREATE (a)-[:ACTED_IN]->(m)",
]

for relationship in relationships:
    run_query(relationship)