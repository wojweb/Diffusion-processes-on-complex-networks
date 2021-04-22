import utils
import sys
import networkx as nx

class InputError(Exception):
    pass

if __name__ == "__main__":
    
    try:
        if sys.argv[1] == 'generate_random':
            g = utils.random_graph_generator(int(sys.argv[2]), float(sys.argv[3]))
            nx.write_edgelist(g, sys.argv[4])
            
        elif sys.argv[1] == 'generate_watts_strogatz':
            g = utils.watts_strogatz_graph_generator(int(sys.argv[2]), float(sys.argv[3]))
            nx.write_edgelist(g, sys.argv[4])

        elif sys.argv[1] == 'generate_barbasi_albert':
            g = utils.barabasi_albert_generator(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
            nx.write_edgelist(g, sys.argv[5])
        elif sys.argv[1] == 'properties':
            g = nx.read_edgelist(sys.argv[2])
            utils.properties(g)
        elif sys.argv[1] == 'show':
            g = nx.read_edgelist(sys.argv[2])
            utils.show(g, sys.argv[3])
        else:
            raise InputError
    except (InputError, IndexError):
        print("Proper semantics:\n"
                "python main.py generate_random <N> <p> <output file path>\n"
                "python main.py generate_watts_strogatz <N> <p> <output file path>\n"
                "python main.py generate_barbasi_albert <N> <n> <link_per_new_node> <output_file_path>\n"
                "python main.py properties <path to graph>\n"
                "python main.py show <path to graph> <output figure path>")