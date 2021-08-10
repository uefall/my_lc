class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int,int> check_set;
        vector<int> re;
        vector<int>::iterator it1 = nums.begin();
        vector<int>::iterator it2 = nums.end();
        for(int cnt=0; it1 != it2; ++it1){
            cout << *it1;
            map<int,int>::iterator check_it = check_set.begin();
            check_it = check_set.find(target-*it1);
            if (check_it != check_set.end()){
                re.insert(re.begin(), cnt);
                re.insert(re.begin(), check_set[target-*it1]);     
                break;
            }
            else
                check_set[*it1]=cnt;
            cnt++;
        }
        return re;
    }
};