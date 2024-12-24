from scholarly import scholarly
from scholarly import ProxyGenerator
from datetime import datetime
import json

def main():
    # pg = ProxyGenerator()
    # pg.FreeProxies()
    # scholarly.use_proxy(pg)

    author: dict = scholarly.search_author_id('9O25UpUAAAAJ')
    scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])

    first_publication = author['publications'][0]
    first_publication_filled = scholarly.fill(first_publication)

    cite_1 = first_publication_filled['num_citations']
    cite_2 = author['citedby'] - cite_1

    cite_data = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "cite_wideband": cite_2,
        "cite_practical": cite_1,
    }
    with open(f'scholar_data.json', 'w') as outfile:
        json.dump(cite_data, outfile, ensure_ascii=False)
    
if __name__ == "__main__":
    main()