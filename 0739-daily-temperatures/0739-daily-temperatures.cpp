#include <vector>
#include <stack>
using namespace std;

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temp) {
        stack<int> stack;
        int n= temp.size();
        vector<int> res(n, 0);
        for( int i =0; i<n; i++){
            while(stack.size()>0 && temp[i]> temp[stack.top()]){
                int index = stack.top();
                stack.pop();
                res[index] = i-index;
            }
            stack.push(i);
        }
        return res;
    }
};