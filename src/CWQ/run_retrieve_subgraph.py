from retrieve_subgraph.retrieve_subgraph import run as run_retrieve_subgraph
from retrieve_subgraph.build_relation_set import run as run_build_relation_set

def run():
    run_retrieve_subgraph()
    run_build_relation_set()

if __name__ == '__main__':
    run()
