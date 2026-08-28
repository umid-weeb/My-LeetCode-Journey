package main
import (
    "fmt"
    "sort"
)
func lengthOfLIS(nums []int) int {
  if len(nums)==0{
    return 0
  }

  var tails []int
  var tails_indices []int

  perent := make([]int, len(nums))
  for i := range perent{
    perent[i] = -1
  }

  for i , num := range nums {
    idx := sort.SearchInts(tails, num)

    if idx == len(tails){
        tails = append(tails, num)
        tails_indices = append(tails_indices, i)
    } else{
        tails[idx] = num
        tails_indices[idx] = i
    }

    if idx>0{
        perent[i] = tails_indices[idx-1]
    }

  }
  var result []int
  current := tails_indices[len(tails_indices)-1]
  for current != -1{
    result = append(result, nums[current])
    current = perent[current]
  }

  return len(result)
}