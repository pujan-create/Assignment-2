# project overview
 The main aim of this project is to determine the set of salient variables (features) that could 
be used to distinguish people with PD from those that are healthy.Data files containing various featuers for both PD-individuals and healthy- individuals are provided in a CSV file. 
# project Data 
Project data Ass2.csv is provided where the data is transformed into a better format to be able to do the analysis accurately.
# Approaches

Three approaches are taken and are completed  in steps in the given python code above.
1) Centeral limit theorm:
   Histogram were created for the data provided where it can be seen in the presentation that the data are uniform and can be analyzed using the central limit theorm.
   some of the histogram are provided in the presentation slide and are described in the presentation.
2) summary statistics:
   This approach is taken in order to find the mean , median and standard deviation . Columns for PD_individuals starts from 1_1 to 1_26 whereas  for healthy individuals it 
   starts from 2_1 to 2_26

3) Calculating CI:
    This approach is taken just to calculate the confidence interval between the mean of each variables for both PD and healthy individuals. The significance of this 
    approach is to know range data for each variables to compare the data  of a new  person and decide if they are suffering from parkinson's disease .
4) two sample -t test
   This is the most important part of the analysis where hypotheseis testing is done between two sample datas(PD_individuals and healthy individuals) . A hypothesis testing 
   is carried where null hypothesis(Both samples have similar feature which are not significant variables) is set to have p-value > 0.05  and alternative hypothesis(Sample 
   feature are different from one another which are set to be significant) is set to have p-value < 0.05.

# Results

After the analysis it has been found that 16 variables are significant and could be used to distinguish people with PD from those that are healthy whereas, There is no enough evidence to support the reamaining 10  variables to be significant.

 The variables that are significant are:

   Jitter%
	  Jitter mircoseconds,
	  Jitter rap,
	  Jitter ppq5,
	  Gitter ddp,
	  Shimmer apq11,
	  Harmonicity nhr hnr,
	  Harmonicity nhr,
	  Pitch median,
	  Pitch mean,
	  Pitch sd,
	  Pitch max,
	  Pulse mean period,
	  Voice fracetion,
	  Voice number,
	  Voice degree

 The variables that are significant are:

   Shimmer%
	  Shimmer db,
	  Shimmer apq3,
	  Shummer apq5,
	  Shimmer dda,
	  Harmonicity hnr,
	  Pitch min,
	  Pulse number,
	  Pulse periods,
	  Pulse sd period 



# conclusion
From all the Analysis that has been carried, we have come to a conclusion that the above mentioned 16 variables are significant  and can be used to distinguish people with PD from those that are healthy whereas,  The reamaining 10  variables are not significant to distinguish as they donot provide enough evidence..

