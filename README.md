# KMP
Here is an implemention of a classic algorithm KMP.  
Used to find a pattern from text (Usually the text is very long from the pattern).

## Usage
Let's start with making an instance of the KMP object, that incude all relevant parameters:  
```kmp = KMP(P='aab', T='aabaab')```  
Then you can run the algorithm by command ```run()```  
```kmp.run()```  
Notice this command also return the number of times the pattern occurs in the text.  

## Parameters

* ```P```: the pattern as an argument, must be str
* ```T```: all text as an argument, must be str

* ```P_file_name```: reading the pattern from a txt file. default is None
* ```T_file_name```: reading the text from a txt file. default is None

* ```m```: optional, default is None. if None - the algorithm will use the whole pattern  
Otherwise, the algorithm will use indexes 1 to m. m must be greater then 1 and less then the length of P

* ```n```:optional, default is None. if None - the algorithm will use the whole text.  
Otherwise, the algorithm will use indexes 1 to n. n must be greater then 1 and less then the length of T

* ```print_occurrences```: do print the indexes where the pattern occurs, default is True

* **NOTE** that P and T has higher priority if they comes directly to the function than from a txt file
