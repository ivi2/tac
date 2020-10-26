"""Query Wikidata for protected heritage building in Brussels"""

import argparse

from SPARQLWrapper import SPARQLWrapper, JSON

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filter', type=str, help='Filtering on name')
parser.add_argument('-n', '--number', type=int, help='Number of rows to display')

def get_rows():
    """Retrieve results from SPARQL"""
    endpoint = "https://query.wikidata.org/bigdata/namespace/wdq/sparql"
    sparql = SPARQLWrapper(endpoint)

    statement = """
    SELECT DISTINCT ?item ?itemLabel ?itemId  where {
        ?item wdt:P3600 ?itemId. 
        ?item wdt:P31 wd:Q3947 .

        SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
    }
    """

    sparql.setQuery(statement)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    rows = results['results']['bindings']
    print(f"\n{len(rows)} Brussels protected buildings found\n")
    return rows

def show(rows, name_filter=None, n=10):
    """Display n buildings (default=10)"""
    # date_format = "%Y-%m-%dT%H:%M:%SZ"
    if name_filter:
        rows = [row for row in rows if name_filter in row['itemLabel']['value'].lower()]
    print(f"Displaying the first {n}:\n")
    for row in rows[:n]:
        building_id = row['itemId']['value']
        print(f"{row['itemLabel']['value']} ({building_id})")

if __name__ == "__main__":
    args = parser.parse_args()
    my_rows = get_rows()
    my_filter = args.filter if args.filter else None
    number = args.number if args.number else 10
    show(my_rows, my_filter, number)
