#include "api.hpp"
#include <string>
#include <algorithm>
#include <vector>
#include <map>

class GraphNode {
public:
    std::map<int, std::string> node_out;
    std::set<int> node_in;
};


std::string dfa2re(DFA &d) {
    std::vector<std::string> filenodes;
    std::map<std::string, int> nodes_to_int;
    std::string otvet;
    std::vector<int> queue_to_delete;
    Alphabet alphabet = d.get_alphabet();
    for (auto &state: d.get_states()) {
        filenodes.push_back(state);
    }
    filenodes.push_back("start");
    filenodes.push_back("end");

    int zero = 0;
    for (int i = zero; i < filenodes.size(); i++) {
        nodes_to_int[filenodes[i]] = i;
        //printf("%d,%s  ",nodes_to_int[filenodes[i]],filenodes[i] );
    }

    int one = 1;
    std::vector<GraphNode> graph_nodes(filenodes.size());
    for (auto &cur_state: d.get_states()) {
        for (auto &alpha: alphabet) {
            if (d.has_trans(cur_state, alpha)) {
                std::string to_state = d.get_trans(cur_state, alpha);
                graph_nodes[nodes_to_int[to_state]].node_in.insert(nodes_to_int[cur_state]);
                if (graph_nodes[nodes_to_int[cur_state]].node_out[nodes_to_int[to_state]].empty()) {
                    graph_nodes[nodes_to_int[cur_state]].node_out[nodes_to_int[to_state]] = alpha;
                } else {
                    graph_nodes[nodes_to_int[cur_state]].node_out[nodes_to_int[to_state]] +=
                            "|" + std::string(1, alpha);
                }

            }
        }
    }

    int two = 2;
    graph_nodes[nodes_to_int[d.get_initial_state()]].node_in.insert(graph_nodes.size() - two);
    graph_nodes[graph_nodes.size() - two].node_out[nodes_to_int[d.get_initial_state()]] = "";

    for (auto &node_st: d.get_final_states()) {
        graph_nodes[nodes_to_int[node_st]].node_out[graph_nodes.size() - one] = "";
        graph_nodes[graph_nodes.size() - one].node_in.insert(nodes_to_int[node_st]);
    }

    std::vector<std::pair<int, int> > nodeprior(filenodes.size() - two);
    for (int i = zero; i < filenodes.size() - two; i++) {
        nodeprior[i] = std::make_pair(i, graph_nodes[i].node_in.size() + graph_nodes[i].node_out.size());
    }

    std::sort(nodeprior.begin(), nodeprior.end(), [](auto &left, auto &right) {
        return left.second < right.second;
    });

    for (auto &[index, priority]: nodeprior) {
        queue_to_delete.push_back(index);
    }

    for (auto &del_index_node: queue_to_delete) {
        for (auto &q_state_index: graph_nodes[del_index_node].node_in) 
        {
            if (q_state_index != del_index_node) {

            GraphNode n_list_node_s = graph_nodes[q_state_index];
            n_list_node_s.node_out.erase(del_index_node);
            for (auto &[p_state_index, p_transition]: graph_nodes[del_index_node].node_out) {
                std::string n_izmenenie;
                if (graph_nodes[p_state_index].node_in.count(q_state_index) == one) { 
                    if (graph_nodes[q_state_index].node_out[p_state_index].size() > one) {
                        n_izmenenie += "(" + graph_nodes[q_state_index].node_out[p_state_index] + ")|";
                    } else {
                        n_izmenenie += graph_nodes[q_state_index].node_out[p_state_index] + "|";
                    }
                }
                if (graph_nodes[q_state_index].node_out[del_index_node].size() > one) { 
                    n_izmenenie += "(" + graph_nodes[q_state_index].node_out[del_index_node] + ")";
                } else {
                    n_izmenenie += graph_nodes[q_state_index].node_out[del_index_node];
                }
                if (graph_nodes[del_index_node].node_in.count(del_index_node) == one) { 
                    n_izmenenie += "(" + graph_nodes[del_index_node].node_out[del_index_node] + ")*";
                }
                if (p_transition.size() > one) { 
                    n_izmenenie += "(" + p_transition + ")";
                } else {
                    n_izmenenie += p_transition;
                }

                if (q_state_index == p_state_index) {
                    n_list_node_s.node_in.insert(q_state_index);
                } else {
                    graph_nodes[p_state_index].node_in.insert(q_state_index);
                }
                n_list_node_s.node_out[p_state_index] = n_izmenenie;
            }
            graph_nodes[q_state_index] = n_list_node_s;
                                    }
        }

        for (auto &[p_state_index, p_transition]: graph_nodes[del_index_node].node_out) {
            graph_nodes[p_state_index].node_in.erase(del_index_node);
        }
    }

    otvet = graph_nodes[graph_nodes.size() - two].node_out[graph_nodes.size() - one];
    return otvet;
}