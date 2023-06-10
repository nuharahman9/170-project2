#include "Node.h"
#include <cstdlib>

Node::Node(int n)
{
    n = n;
}

double Node::evaluate()
{
    return rand() % 100;
}

void Node::addFeature()
{
    for (int i = 0; i < n; ++i)
    {
        if (features.find(i) == features.end()) // if i is not in features
        {
            Node newNode(n);
            neighbors.push_back(newNode);
        }
    }
}