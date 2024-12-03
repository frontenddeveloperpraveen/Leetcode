class Solution{

public static void main(String[] args) {
    
    String s = "pwwkew";

    int max = 0;

    String temp = "";



    for(int i = 0; i<s.length(); i++){

        for(int j = i; j<s.length(); j++){

            char check = s.charAt(j) ;
            if(temp.contains(String.valueOf(check))){

                if(max < temp.length())
                max = temp.length(); 
                break;

            }else{
                temp = temp + s.charAt(j);
            }
        

        }
        temp = "";


    }

    System.err.println(max);



}



}