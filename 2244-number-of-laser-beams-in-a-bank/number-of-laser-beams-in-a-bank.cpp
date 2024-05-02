int count_ones(string s){
    int c =0;
    for(int i=0;i<s.length();i++)
    {
        if(s[i]=='1')
            c++;
    }
    return c;
}
class Solution {
public:
    int numberOfBeams(vector<string>& bank) {
        vector<int> ones_counter(bank.size());
        bool flag = false; 
        for (int i = 0; i < bank.size(); i++) {
            ones_counter[i] = count_ones(bank[i]);
            if (ones_counter[i] > 0) {
                flag = true; 
            }
        }
        if (!flag)
            return 0; 
        int i = 0, p = i+1,res=0;
        while(p<ones_counter.size())
        {
            if(i!=p && ones_counter[i]!=0 && ones_counter[p]!=0)
            {
                res = res + ones_counter[i]*ones_counter[p];
                i++;p++;
            }
            else if(ones_counter[i]==0)
                i++;
            else if(ones_counter[p]==0)
                p++;
            else
                p++;
        }
        return res;
    }
};