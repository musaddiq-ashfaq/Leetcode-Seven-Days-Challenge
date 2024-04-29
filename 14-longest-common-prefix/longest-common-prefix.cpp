class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string common = strs[0];
        if(strs.empty())
            return "";
        for(const string& str : strs)
        {
            int i = 0;
            while (i < common.length() && i < str.length() && common[i] == str[i])
                i++;
            common = common.substr(0,i);
        }
        return common;
    }
};