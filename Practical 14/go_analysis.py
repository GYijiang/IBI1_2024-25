import xml.dom.minidom
import xml.sax
from datetime import datetime
import os

class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_data = ""
        self.namespace = ""
        self.term_id = ""
        self.term_name = ""
        self.is_a_count = 0
        self.results = {
            'molecular_function': {'max': 0, 'terms': []},
            'biological_process': {'max': 0, 'terms': []},
            'cellular_component': {'max': 0, 'terms': []}
        }

    def startElement(self, tag, attrs):
        self.current_data = tag
        if tag == "term":
            self.is_a_count = 0

    def characters(self, content):
        if self.current_data == "namespace":
            self.namespace = content.lower().replace(" ", "_")
        elif self.current_data == "id":
            self.term_id = content
        elif self.current_data == "name":
            self.term_name = content

    def endElement(self, tag):
        if tag == "is_a":
            self.is_a_count += 1
        elif tag == "term":
            if self.namespace in self.results:
                if self.is_a_count > self.results[self.namespace]['max']:
                    self.results[self.namespace]['max'] = self.is_a_count
                    self.results[self.namespace]['terms'] = [self.term_name]
                elif self.is_a_count == self.results[self.namespace]['max']:
                    self.results[self.namespace]['terms'].append(self.term_name)
        self.current_data = ""

def sax_parser(xml_file):
    print("\n— Starting Analysis with SAX API —")
    start_time = datetime.now()
    
    handler = GOHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(xml_file)
    
    for ns, data in handler.results.items():
        print(f"Max count for {ns}: {data['max']} for {data['terms']}")
    
    end_time = datetime.now()
    print(f"— Analysis completed in {round((end_time - start_time).total_seconds(), 2)} seconds —")
    return end_time - start_time

def dom_parser(xml_file):
    print("\n— Starting Analysis with DOM API —")
    start_time = datetime.now()
    
    dom = xml.dom.minidom.parse(xml_file)
    results = {
        'molecular_function': {'max': 0, 'terms': []},
        'biological_process': {'max': 0, 'terms': []},
        'cellular_component': {'max': 0, 'terms': []}
    }
    
    terms = dom.getElementsByTagName('term')
    for term in terms:
        try:
            namespace = term.getElementsByTagName('namespace')[0].firstChild.data.lower().replace(" ", "_")
            if namespace not in results:
                continue
                
            term_name = term.getElementsByTagName('name')[0].firstChild.data
            is_a_count = len(term.getElementsByTagName('is_a'))
            
            if is_a_count > results[namespace]['max']:
                results[namespace]['max'] = is_a_count
                results[namespace]['terms'] = [term_name]
            elif is_a_count == results[namespace]['max']:
                results[namespace]['terms'].append(term_name)
        except:
            continue
    
    for ns, data in results.items():
        print(f"Max count for {ns}: {data['max']} for {data['terms']}")
    
    end_time = datetime.now()
    print(f"— Analysis completed in {round((end_time - start_time).total_seconds(), 2)} seconds —")
    return end_time - start_time

if __name__ == "__main__":
    xml_file = "go_obo.xml"
    if not os.path.exists(xml_file):
        print(f"Error: File {xml_file} not found!")
    else:
        dom_time = dom_parser(xml_file)
        sax_time = sax_parser(xml_file)
        
        time_diff = abs(dom_time.total_seconds() - sax_time.total_seconds())
        faster = "SAX" if sax_time < dom_time else "DOM"
        print(f"\n{faster} parser is faster by {round(time_diff, 2)} seconds")