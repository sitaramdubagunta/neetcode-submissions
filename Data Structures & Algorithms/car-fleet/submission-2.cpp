class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        
       vector<pair<int,double>> timevector;


        for(int i  = 0 ; i < position.size() ; i++){
            double time = (double)(target-position[i])/speed[i];
            timevector.push_back({position[i] , time});
           
        }
        sort(timevector.rbegin() , timevector.rend());

        stack<double> temp;
        for(auto it : timevector){
            

            if(temp.empty() || it.second > temp.top()){
                temp.push(it.second);
            }
        }

        return temp.size();

        
    }
};
