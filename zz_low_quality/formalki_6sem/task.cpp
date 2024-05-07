#include "api.hpp"
#include <string>
#include <iostream>
#include <cctype>
#include <vector>
#include <set>
#include <algorithm>

std::vector<int> char_index, operator_index, operator_priority;
std::vector<std::set<int>> followpos;

class Tree {
public:
    int index;
    char symbol;
    bool nullable = NULL;
    std::set<int> firstpos, lastpos;
    Tree *left = nullptr;
    Tree *right = nullptr;

    Tree(char symbol, int index, Tree *left, Tree *right) : symbol(symbol), index(index), left(left), right(right) {}

    ~Tree() { delete left; delete right; }

    void calculate_nullable_firstpos_lastpos() {
        if (left  != nullptr) { left ->calculate_nullable_firstpos_lastpos(); }
        if (right != nullptr) { right->calculate_nullable_firstpos_lastpos(); }

        if (symbol == '\n')   { nullable = true; }
        else if (std::isalnum(symbol)) { nullable = symbol == '#';
                firstpos.insert(index); lastpos.insert(index);}
        else switch (symbol)
        {
        case '|':
            nullable = left->nullable || right->nullable;
            firstpos = left->firstpos;
            firstpos.insert(right->firstpos.begin(), right->firstpos.end());
            lastpos = left->lastpos;
            lastpos.insert(right->lastpos.begin(), right->lastpos.end());
            break;
        case '.':
            nullable = left->nullable && right->nullable;
            firstpos = left->firstpos;
            if (left->nullable) { firstpos.insert(right->firstpos.begin(), right->firstpos.end()); }
            lastpos = right->lastpos;
            if (right->nullable) { lastpos.insert(left->lastpos.begin(), left->lastpos.end()); } 
            break;
        case '*':
            nullable = true;
            firstpos = left->firstpos;  lastpos = left->lastpos;
            break;
        default:
            nullable = symbol == '#';
            firstpos.insert(index); lastpos.insert(index);
            break;
        }

    };

    void calculate_followpos() {
        if (left != nullptr) {
            left->calculate_followpos();
        }
        if (right != nullptr) {
            right->calculate_followpos();
        }
        if (symbol == '*') {
            for (auto &item: left->lastpos) {
                followpos[item].insert(left->firstpos.begin(), left->firstpos.end());
            }
        } else if (symbol == '.') {
            for (auto &item: left->lastpos) {
                followpos[item].insert(right->firstpos.begin(), right->firstpos.end());
            }
        }
    }

};

Tree *rec_tree(const std::string &s, int start, int end) {
//    minify aka remove ()
    int offset = 0;
    while (s[start + offset] == '(' && s[end - offset] == ')') {
        offset += 1;
        int count = 0;
        bool is_end = false;
        for (char &symbol: s.substr(start + offset, end - start + 1 - 2 * offset)) {
            if (symbol == '(') {
                count++;
            } else if (symbol == ')') {
                count--;
                if (count < 0) {
                    is_end= true;
                    offset--;
                    break;
                }
            }
        }
        if (is_end) {
            break;
        }
    }
    start += offset;
    end -= offset;

//    get the least priority operator
    int min_index = -1;
    for (int i = 0; i < operator_index.size(); i++) {
        if (operator_index[i] < start) {
            continue;
        }
        if (operator_index[i] > end) {
            break;
        }
        if (operator_priority[i] != 0) {
            if (min_index == -1 || operator_priority[i] <= operator_priority[min_index]) {
                min_index = i;
            }
        }
    }
    Tree *tree = nullptr;
    if (min_index != -1) {
        char cur_operator = s[operator_index[min_index]];
        if (cur_operator == '|' || cur_operator == '.' || cur_operator == '*') {
            tree = new Tree(cur_operator, 0, nullptr, nullptr);
            tree->left = rec_tree(s, start, operator_index[min_index] - 1);
            if (cur_operator == '|' || cur_operator == '.') {
                tree->right = rec_tree(s, operator_index[min_index] + 1, end);
            }
        } else {
            std::cout << "ERROR!!!!" << std::endl;
        }
    } else {
        if (start == end) {
            int index_in_char_index = 0;
            while (char_index[index_in_char_index] != start) {
                index_in_char_index++;
            }
            tree = new Tree(s[start], index_in_char_index, nullptr, nullptr);
        } else if (start > end) {
            tree = new Tree('\n', -1, nullptr, nullptr);
        } else {
            std::cout << "ERROR!!!!" << std::endl;
        }
    }

    return tree;
}


Tree *create_tree(const std::string &s) {
    char_index = std::vector<int>();
    operator_index = std::vector<int>();

    for (int i = 0; i < s.size(); i++) {
        if (isalnum(s[i]) || s[i] == '#') {
            char_index.push_back(i);
        } else {
            operator_index.push_back(i);
        }
    }

    operator_priority = std::vector<int>(operator_index.size());

    int cur_priority = 0;
    for (int i = 0; i < operator_index.size(); i++) {
        if (s[operator_index[i]] == '(') {
            cur_priority += 4;
            operator_priority[i] = 0;
        } else if (s[operator_index[i]] == ')') {
            cur_priority -= 4;
            operator_priority[i] = 0;
        } else if (s[operator_index[i]] == '|') {
            operator_priority[i] = 1 + cur_priority;
        } else if (s[operator_index[i]] == '.') {
            operator_priority[i] = 2 + cur_priority;
        } else if (s[operator_index[i]] == '*') {
            operator_priority[i] = 3 + cur_priority;
        }
    }

    return rec_tree(s, 0, s.size() - 1);
}


DFA re2dfa(const std::string &s) {
    std::string s1 = '(' + s + ")#";

    for (int i = s1.size() - 1; i > 0; i--) {
        if (s1[i] != '*' && s1[i] != '|' && s1[i - 1] != '|' && s1[i] != ')' && s1[i - 1] != '(') {
            s1.insert(i, ".");
        }
    }

    Tree *root = create_tree(s1);

    root->calculate_nullable_firstpos_lastpos();

    followpos = std::vector<std::set<int>>(char_index.size());
    std::vector<std::set<int>> &followpos1 = followpos;
    std::vector<int> &char_index1 = char_index;


    root->calculate_followpos();

    Alphabet alphabet = Alphabet(s);
    DFA res = DFA(alphabet);

    std::vector<std::set<int>> states;
    states.push_back(root->firstpos);

    res.create_state(std::to_string(0), root->nullable);
    res.set_initial(std::to_string(0));
    for (int index = 0; index < states.size(); index++) {
        for (auto &alpha_from_alphabet: alphabet) {
            std::set<int> new_state;
            for (auto &index_alpha_in_cur_state: states[index]) {
                if (s1[char_index[index_alpha_in_cur_state]] == alpha_from_alphabet) {
                    new_state.insert(followpos[index_alpha_in_cur_state].begin(),
                                     followpos[index_alpha_in_cur_state].end());
                }
            }

            if (!new_state.empty()) {
                int index_to = 0;
                for (; index_to < states.size(); index_to++) {
                    if (states[index_to] == new_state) {
                        break;
                    }
                } //existing state
                if (index_to == states.size()) {
                    //new state
                    index_to = states.size();
                    states.push_back(new_state);
                    res.create_state(std::to_string(index_to), new_state.count(char_index.size() - 1) == 1);
                }
                res.set_trans(std::to_string(index), alpha_from_alphabet, std::to_string(index_to));
            }
        }
    }

    return res;
}