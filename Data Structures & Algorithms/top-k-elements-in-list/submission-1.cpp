class Solution {
public:
    struct Data {
        int val;
        int count;
    };

    struct Compare {
        bool operator()(Data a, Data b) const {
            return a.count < b.count;   // max-heap
        }
    };

    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> ans;
        priority_queue<Data, vector<Data>, Compare> pq; 
        map<int, Data> m;

        for(auto &x: nums) {
            if(!m.count(x)) {
                m[x] = {x, 1};
            } else {
                m[x].count++;
            }
        }

        for(auto &x: m) {
            pq.push(x.second);
        }

        int cnt = 0;
        while(!pq.empty() && cnt < k) {
            auto x = pq.top();
            pq.pop();
            ans.push_back(x.val);
            cnt++;
        }

        return ans;
        
    }
};
