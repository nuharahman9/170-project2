#include <vector>
#include <unordered_set>

class Node
{
private:
    int n;
    std::unordered_set<int> features;
    std::vector<Node> neighbors;

public:
    Node(int);
    double evaluate();
    void addFeature();
};