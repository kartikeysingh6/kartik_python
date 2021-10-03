package Arrays;

import javax.lang.model.util.ElementScanner6;

public class sort0and1 {
public static void main(String[] args) {
    
    int arr[]={0,1,2,0,2,1,2,0,1};
    int x1=0,x2=0,x3=0;
    for(int i:arr){
        if(i==0)
          x1++;
        else if(i==1)
          x2++;
        else
          x3++;
    }
    int k=0;
    for(int i=0;i<x1;i++)
      arr[k++]=0;
    for(int i=0;i<x2;i++)
      arr[k++]=1;
    for(int i=0;i<x3;i++)
      arr[k++]=2;
  for(int i:arr)
    System.out.print(i+" ");
}

    
}
