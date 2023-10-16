from term import OntologyTermType
from term_collector import OntologyTermCollector

# ontology_iri = "https://github.com/EBISPOT/efo/releases/download/v3.57.0/efo.owl"
ontology_iri = "/Users/rsgoncalves/Documents/Workspace/text2term/test/test_ontology.owl"

# collector = OntologyTermCollector()

terms = OntologyTermCollector().get_ontology_terms(ontology_iri=ontology_iri, term_type=OntologyTermType.ANY)
# print(terms)
counter = 0
for term in terms.keys():
    # print(terms[term])
    # if counter == 15:
    #     break
    # print(f"Named parents of {term}: {terms[term].parents}")
    # print(terms[term].restrictions)
    if len(terms[term].restrictions) > 0:
        print(f"Complex parents of {term}: {terms[term].restrictions}")
        print()
    counter += 1

# term = terms["http://purl.obolibrary.org/obo/MONDO_0021058"]
#
# print(term)
# print(term.restrictions)
