class Solution {

    function twoSum(array $nums, $target) {
        
        $count=count($nums);
        if($nums){
        for($i=0;$i<$count;$i++){
            for($j=$i+1;$j<$count;$j++){
                $sum=$nums[$i]+$nums[$j];
          if ($sum==$target){
              return array($i,$j);
          } 
        
            }
        }
        }
    }
}

