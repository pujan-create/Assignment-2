import pandas as pd
import scipy.stats as st
import math
import numpy as np



# read csv into a DataFrame
df = pd.read_csv("Ass2.csv")

# inspect DataFrame content
print("Content of DataFrame: ")
print(df.info())
print(df.head())
print("")

# split DataFrame into two subsets: 
# df1: Pd_Group
# df2: Healthy Group
df1 = df[df["Group"] == 1]
df2 = df[df["Group"] == 0]


# select relevant column from each DataFrame
sample1_1 = df1["jitter%"].to_numpy()
sample1_2= df1["jitter_mircoseconds"].to_numpy()
sample1_3= df1["jitter_rap"].to_numpy()
sample1_4 = df1["jitter_ppq5"].to_numpy()
sample1_5= df1["jitter_ddp"].to_numpy()
sample1_6= df1["shimmer%"].to_numpy()
sample1_7= df1["shimmer_db"].to_numpy()
sample1_8= df1["shimmer_apq3"].to_numpy()
sample1_9= df1["shimmer_apq5"].to_numpy()
sample1_10= df1["shimmer_apq11"].to_numpy()
sample1_11= df1["shimmer_dda"].to_numpy()
sample1_12= df1["harmonicity_nhr_and_hnr"].to_numpy()
sample1_13= df1["harmonicity_nhr"].to_numpy()
sample1_14= df1["harmonicity_hnr"].to_numpy()
sample1_15= df1["pitch_median"].to_numpy()
sample1_16= df1["pitch_mean"].to_numpy()
sample1_17= df1["pitch_sd"].to_numpy()
sample1_18= df1["pitch_min"].to_numpy()
sample1_19= df1["pitch_max"].to_numpy()
sample1_20= df1["pulse_number"].to_numpy()
sample1_21= df1["pulse_periods"].to_numpy()
sample1_22= df1["pulse_mean_period"].to_numpy()
sample1_23= df1["pulse_sd_period"].to_numpy()
sample1_24= df1["voice_fraction"].to_numpy()
sample1_25= df1["voice_number"].to_numpy()
sample1_26= df1["voice_degree"].to_numpy()




sample2_1 = df2["jitter%"].to_numpy()
sample2_2= df2["jitter_mircoseconds"].to_numpy()
sample2_3= df2["jitter_rap"].to_numpy()
sample2_4 = df2["jitter_ppq5"].to_numpy()
sample2_5= df2["jitter_ddp"].to_numpy()
sample2_6= df2["shimmer%"].to_numpy()
sample2_7= df2["shimmer_db"].to_numpy()
sample2_8= df2["shimmer_apq3"].to_numpy()
sample2_9= df2["shimmer_apq5"].to_numpy()
sample2_10= df2["shimmer_apq11"].to_numpy()
sample2_11= df2["shimmer_dda"].to_numpy()
sample2_12= df2["harmonicity_nhr_and_hnr"].to_numpy()
sample2_13= df2["harmonicity_nhr"].to_numpy()
sample2_14= df2["harmonicity_hnr"].to_numpy()
sample2_15= df2["pitch_median"].to_numpy()
sample2_16= df2["pitch_mean"].to_numpy()
sample2_17= df2["pitch_sd"].to_numpy()
sample2_18= df2["pitch_min"].to_numpy()
sample2_19= df2["pitch_max"].to_numpy()
sample2_20= df2["pulse_number"].to_numpy()
sample2_21= df2["pulse_periods"].to_numpy()
sample2_22= df2["pulse_mean_period"].to_numpy()
sample2_23= df2["pulse_sd_period"].to_numpy()
sample2_24= df2["voice_fraction"].to_numpy()
sample2_25= df2["voice_number"].to_numpy()
sample2_26= df2["voice_degree"].to_numpy()



# compute basic statistics for two samples
print("\n Computing basic statistics of sample 1(pd_individuals)")

# The basic statistics of PD individuals are :
x_bar1_1 = st.tmean(sample1_1)
s1_1 = st.tstd(sample1_1)
n1_1 = len(sample1_1)
print("\t Statistics of sample 1_1: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar1_1, s1_1, n1_1))
x_bar1_2 = st.tmean(sample1_2)
s1_2= st.tstd(sample1_2)
n1_2 = len(sample1_2)
print("\t Statistics of sample 1_2: %.6f (mean), %.6f (std. dev.), and %d (n)." % (x_bar1_2, s1_2, n1_2))
x_bar1_3 = st.tmean(sample1_3)
s1_3 = st.tstd(sample1_3)
n1_3 = len(sample1_3)
print("\t Statistics of sample 1_3: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar1_3, s1_3, n1_3))
x_bar1_4 = st.tmean(sample1_4)
s1_4 = st.tstd(sample1_4)
n1_4 = len(sample1_4)
print("\t Statistics of sample 1_4: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar1_4, s1_4, n1_4))
x_bar1_5 = st.tmean(sample1_5)
s1_5 = st.tstd(sample1_5)
n1_5 = len(sample1_5)
print("\t Statistics of sample 1_5: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar1_5, s1_5, n1_5))
x_bar1_6 = st.tmean(sample1_6)
s1_6 = st.tstd(sample1_6)
n1_6 = len(sample1_6)
print("\t Statistics of sample 1_6: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar1_6, s1_6, n1_6))
x_bar1_7 = st.tmean(sample1_7)
s1_7 = st.tstd(sample1_7)
n1_7 = len(sample1_7)
print("\t Statistics of sample 1_7: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar1_7, s1_7, n1_7))
x_bar1_8 = st.tmean(sample1_8)
s1_8 = st.tstd(sample1_8)
n1_8 = len(sample1_8)
print("\t Statistics of sample 1_8: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar1_8, s1_8, n1_8))
x_bar1_9 = st.tmean(sample1_9)
s1_9 = st.tstd(sample1_9)
n1_9 = len(sample1_9)
print("\t Statistics of sample 1_9: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar1_9, s1_9, n1_9))
x_bar1_10 = st.tmean(sample1_10)
s1_10 = st.tstd(sample1_10)
n1_10 = len(sample1_10)
print("\t Statistics of sample 1_10: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar1_10, s1_10, n1_10))
x_bar1_11 = st.tmean(sample1_11)
s1_11 = st.tstd(sample1_11)
n1_11 = len(sample1_11)
print("\t Statistics of sample 1_11: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar1_11, s1_11, n1_11))
x_bar1_12 = st.tmean(sample1_12)
s1_12 = st.tstd(sample1_12)
n1_12 = len(sample1_12)
print("\t Statistics of sample 1_12: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar1_12, s1_12, n1_12))
x_bar1_13= st.tmean(sample1_13)
s1_13 = st.tstd(sample1_13)
n1_13 = len(sample1_13)
print("\t Statistics of sample 1_13: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar1_13, s1_13, n1_13))
x_bar1_14 = st.tmean(sample1_14)
s1_14= st.tstd(sample1_14)
n1_14= len(sample1_14)
print("\t Statistics of sample 1_14: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar1_14, s1_14, n1_14))
x_bar1_15 = st.tmean(sample1_15)
s1_15 = st.tstd(sample1_15)
n1_15= len(sample1_15)
print("\t Statistics of sample 1_15: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar1_15, s1_15, n1_15))
x_bar1_16 = st.tmean(sample1_16)
s1_16 = st.tstd(sample1_16)
n1_16 = len(sample1_16)
print("\t Statistics of sample 1_16: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar1_16, s1_16, n1_16))
x_bar1_17 = st.tmean(sample1_17)
s1_17 = st.tstd(sample1_17)
n1_17 = len(sample1_17)
print("\t Statistics of sample 1_17: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar1_17, s1_17, n1_17))
x_bar1_18 = st.tmean(sample1_18)
s1_18 = st.tstd(sample1_18)
n1_18 = len(sample1_18)
print("\t Statistics of sample 1_18: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar1_18, s1_18, n1_18))
x_bar1_19 = st.tmean(sample1_19)
s1_19= st.tstd(sample1_19)
n1_19 = len(sample1_19)
print("\t Statistics of sample 1_19: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar1_19, s1_19, n1_19))
x_bar1_20 = st.tmean(sample1_20)
s1_20 = st.tstd(sample1_20)
n1_20 = len(sample1_20)
print("\t Statistics of sample 1_20: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar1_20, s1_20, n1_20))
x_bar1_21 = st.tmean(sample1_21)
s1_21 = st.tstd(sample1_21)
n1_21 = len(sample1_21)
print("\t Statistics of sample 1_21: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar1_21, s1_21, n1_21))
x_bar1_22 = st.tmean(sample1_22)
s1_22 = st.tstd(sample1_22)
n1_22 = len(sample1_22)
print("\t Statistics of sample 1_22: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar1_22, s1_22, n1_22))
x_bar1_23 = st.tmean(sample1_23)
s1_23 = st.tstd(sample1_23)
n1_23 = len(sample1_23)
print("\t Statistics of sample 1_23: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar1_23, s1_23, n1_23))
x_bar1_24 = st.tmean(sample1_24)
s1_24 = st.tstd(sample1_24)
n1_24 = len(sample1_24)
print("\t Statistics of sample 1_24: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar1_24, s1_24, n1_24))
x_bar1_25 = st.tmean(sample1_25)
s1_25 = st.tstd(sample1_25)
n1_25 = len(sample1_25)
print("\t Statistics of sample 1_25: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar1_25, s1_25, n1_25))
x_bar1_26 = st.tmean(sample1_26)
s1_26 = st.tstd(sample1_26)
n1_26 = len(sample1_26)
print("\t Statistics of sample 1_26: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar1_26, s1_26, n1_26))


print("\n Computing basic statistics of sample 2(non-pd_individuals)")
# The basic statistics for Healthy Individuals:
x_bar2_1 = st.tmean(sample2_1)
s2_1 = st.tstd(sample2_1)
n2_1 = len(sample2_1)
print("\t Statistics of sample 2_1: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar2_1, s2_1, n2_1))
x_bar2_2 = st.tmean(sample2_2)
s2_2= st.tstd(sample2_2)
n2_2 = len(sample2_2)
print("\t Statistics of sample 2_2: %.6f (mean), %.6f (std. dev.), and %d (n)." % (x_bar2_2, s2_2, n2_2))
x_bar2_3 = st.tmean(sample2_3)
s2_3 = st.tstd(sample2_3)
n2_3 = len(sample2_3)
print("\t Statistics of sample 2_3: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar2_3, s2_3, n2_3))
x_bar2_4 = st.tmean(sample2_4)
s2_4 = st.tstd(sample2_4)
n2_4 = len(sample2_4)
print("\t Statistics of sample 2_4: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar2_4, s2_4, n2_4))
x_bar2_5 = st.tmean(sample2_5)
s2_5 = st.tstd(sample2_5)
n2_5 = len(sample2_5)
print("\t Statistics of sample 2_5: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar2_5, s2_5, n2_5))
x_bar2_6 = st.tmean(sample2_6)
s2_6 = st.tstd(sample2_6)
n2_6 = len(sample2_6)
print("\t Statistics of sample 2_6: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar2_6, s2_6, n2_6))
x_bar2_7 = st.tmean(sample2_7)
s2_7 = st.tstd(sample2_7)
n2_7 = len(sample2_7)
print("\t Statistics of sample 2_7: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar2_7, s2_7, n2_7))
x_bar2_8 = st.tmean(sample2_8)
s2_8 = st.tstd(sample2_8)
n2_8 = len(sample2_8)
print("\t Statistics of sample 2_8: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar2_8, s2_8, n2_8))
x_bar2_9 = st.tmean(sample2_9)
s2_9 = st.tstd(sample2_9)
n2_9 = len(sample2_9)
print("\t Statistics of sample 2_9: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar2_9, s2_9, n2_9))
x_bar2_10 = st.tmean(sample2_10)
s2_10 = st.tstd(sample2_10)
n2_10 = len(sample2_10)
print("\t Statistics of sample 2_10: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar2_10, s2_10, n2_10))
x_bar2_11 = st.tmean(sample2_11)
s2_11 = st.tstd(sample2_11)
n2_11 = len(sample2_11)
print("\t Statistics of sample 2_11: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar2_11, s2_11, n2_11))
x_bar2_12 = st.tmean(sample2_12)
s2_12 = st.tstd(sample2_12)
n2_12 = len(sample2_12)
print("\t Statistics of sample 2_12: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar2_12, s2_12, n2_12))
x_bar2_13= st.tmean(sample2_13)
s2_13 = st.tstd(sample2_13)
n2_13 = len(sample2_13)
print("\t Statistics of sample 2_13: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar2_13, s2_13, n2_13))
x_bar2_14 = st.tmean(sample2_14)
s2_14= st.tstd(sample2_14)
n2_14= len(sample2_14)
print("\t Statistics of sample 2_14: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar2_14, s2_14, n2_14))
x_bar2_15 = st.tmean(sample2_15)
s2_15 = st.tstd(sample2_15)
n2_15= len(sample2_15)
print("\t Statistics of sample 2_15: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar2_15, s2_15, n2_15))
x_bar2_16 = st.tmean(sample2_16)
s2_16 = st.tstd(sample2_16)
n2_16 = len(sample2_16)
print("\t Statistics of sample 2_16: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar2_16, s2_16, n2_16))
x_bar2_17 = st.tmean(sample2_17)
s2_17 = st.tstd(sample2_17)
n2_17 = len(sample2_17)
print("\t Statistics of sample 2_17: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar2_17, s2_17, n2_17))
x_bar2_18 = st.tmean(sample2_18)
s2_18 = st.tstd(sample2_18)
n2_18 = len(sample2_18)
print("\t Statistics of sample 2_18: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar2_18, s2_18, n2_18))
x_bar2_19 = st.tmean(sample2_19)
s2_19= st.tstd(sample2_19)
n2_19 = len(sample2_19)
print("\t Statistics of sample 2_19: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar2_19, s2_19, n2_19))
x_bar2_20 = st.tmean(sample2_20)
s2_20 = st.tstd(sample2_20)
n2_20 = len(sample2_20)
print("\t Statistics of sample 2_20: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar2_20, s2_20, n2_20))
x_bar2_21 = st.tmean(sample2_21)
s2_21 = st.tstd(sample2_21)
n2_21 = len(sample2_21)
print("\t Statistics of sample 2_21: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar2_21, s2_21, n2_21))
x_bar2_22 = st.tmean(sample2_22)
s2_22 = st.tstd(sample2_22)
n2_22 = len(sample2_22)
print("\t Statistics of sample 2_22: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar2_22, s2_22, n2_22))
x_bar2_23 = st.tmean(sample2_23)
s2_23 = st.tstd(sample2_23)
n2_23 = len(sample2_23)
print("\t Statistics of sample 2_23: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar2_23, s2_23, n2_23))
x_bar2_24 = st.tmean(sample2_24)
s2_24 = st.tstd(sample2_24)
n2_24 = len(sample2_24)
print("\t Statistics of sample 2_24: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar2_24, s2_24, n2_24))
x_bar2_25 = st.tmean(sample2_25)
s2_25 = st.tstd(sample2_25)
n2_25 = len(sample2_25)
print("\t Statistics of sample 2_25: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar2_25, s2_25, n2_25))
x_bar2_26 = st.tmean(sample2_26)
s2_26 = st.tstd(sample2_26)
n2_26 = len(sample2_26)
print("\t Statistics of sample 2_26: %.3f (mean), %.3f (std. dev.), and %d (n)." % (x_bar2_26, s2_26, n2_26))


# To find confidence intervals( at 95% confidence level)for all the rows in the csv
print("\n calculating all the confidence intervals across different variable for PD_individuals")

Confidence_lvl = 0.95    # we are calculating the confidence interval at confidence level 95%
z_score= 1.96            # z-score at 95% confidence level



margin_of_error1_1 = z_score * (s1_1 / math.sqrt(n1_1))
confidence_interval1_1= [x_bar1_1 - margin_of_error1_1 , x_bar1_1 + margin_of_error1_1]
print("\t confidence interval for jitter%: ", confidence_interval1_1) 

margin_of_error1_2 = z_score * (s1_2 / math.sqrt(n1_2))
confidence_interval1_2= [x_bar1_2 - margin_of_error1_2, x_bar1_2 + margin_of_error1_2]
print("\t confidence interval for jitter_microseconds: ", confidence_interval1_2) 

margin_of_error1_3 = z_score * (s1_3 / math.sqrt(n1_3))
confidence_interval1_3= [x_bar1_3 - margin_of_error1_3, x_bar1_3 + margin_of_error1_3]
print("\t confidence interval for jitter_rap: ", confidence_interval1_3) 

margin_of_error1_4 = z_score * (s1_4 / math.sqrt(n1_4))
confidence_interval1_4= [x_bar1_4 - margin_of_error1_4, x_bar1_4 + margin_of_error1_4]
print("\t confidence interval for jitter_ppq5: ", confidence_interval1_4) 

margin_of_error1_5 = z_score * (s1_5 / math.sqrt(n1_5))
confidence_interval1_5= [x_bar1_5 - margin_of_error1_5, x_bar1_5 + margin_of_error1_5]
print("\t confidence interval for jitter_ddp: ", confidence_interval1_5) 

margin_of_error1_6 = z_score * (s1_6 / math.sqrt(n1_6))
confidence_interval1_6= [x_bar1_6 - margin_of_error1_6, x_bar1_6 + margin_of_error1_6]
print("\t confidence interval for shimmer%: ", confidence_interval1_6) 

margin_of_error1_7 = z_score * (s1_7 / math.sqrt(n1_7))
confidence_interval1_7= [x_bar1_7 - margin_of_error1_7, x_bar1_7 + margin_of_error1_7]
print("\t confidence interval for shimmer_db: ", confidence_interval1_7) 

margin_of_error1_8 = z_score * (s1_8 / math.sqrt(n1_8))
confidence_interval1_8= [x_bar1_8 - margin_of_error1_8, x_bar1_8 + margin_of_error1_8]
print("\t confidence interval for shimmer_apq3: ", confidence_interval1_8) 

margin_of_error1_9 = z_score * (s1_9 / math.sqrt(n1_9))
confidence_interval1_9= [x_bar1_9 - margin_of_error1_9, x_bar1_9 + margin_of_error1_9]
print("\t confidence interval for shimmer_apq5: ", confidence_interval1_9) 

margin_of_error1_10 = z_score * (s1_10 / math.sqrt(n1_10))
confidence_interval1_10= [x_bar1_10 - margin_of_error1_10, x_bar1_10 + margin_of_error1_10]
print("\t confidence interval for shimmer_apq10: ", confidence_interval1_10) 

margin_of_error1_11 = z_score * (s1_11 / math.sqrt(n1_11))
confidence_interval1_11= [x_bar1_11 - margin_of_error1_11, x_bar1_11 + margin_of_error1_11]
print("\t confidence interval for shimmer_dda: ", confidence_interval1_11)

margin_of_error1_12 = z_score * (s1_12 / math.sqrt(n1_12))
confidence_interval1_12= [x_bar1_12 - margin_of_error1_12, x_bar1_12 + margin_of_error1_12]
print("\t confidence interval for harmonicity_nhr_and_hnr: ", confidence_interval1_12)
 
margin_of_error1_13 = z_score * (s1_13 / math.sqrt(n1_13))
confidence_interval1_13= [x_bar1_13 - margin_of_error1_13, x_bar1_13 + margin_of_error1_13]
print("\t confidence interval for harmonicity_nhr: ", confidence_interval1_13) 

margin_of_error1_14 = z_score * (s1_14 / math.sqrt(n1_14))
confidence_interval1_14= [x_bar1_14 - margin_of_error1_14, x_bar1_14 + margin_of_error1_14]
print("\t confidence interval for harmonicity_hnr: ", confidence_interval1_14) 

margin_of_error1_15 = z_score * (s1_15 / math.sqrt(n1_15))
confidence_interval1_15= [x_bar1_15 - margin_of_error1_15, x_bar1_15 + margin_of_error1_15]
print("\t confidence interval for pitch_median: ", confidence_interval1_15) 

margin_of_error1_16 = z_score * (s1_16 / math.sqrt(n1_16))
confidence_interval1_16= [x_bar1_16 - margin_of_error1_16, x_bar1_16 + margin_of_error1_16]
print("\t confidence interval for pitch_mean: ", confidence_interval1_16) 

margin_of_error1_17 = z_score * (s1_17 / math.sqrt(n1_17))
confidence_interval1_17= [x_bar1_17 - margin_of_error1_17, x_bar1_17 + margin_of_error1_17]
print("\t confidence interval for pitch_sd: ", confidence_interval1_17) 
margin_of_error1_18 = z_score * (s1_18 / math.sqrt(n1_18))
confidence_interval1_18= [x_bar1_18 - margin_of_error1_18, x_bar1_18 + margin_of_error1_18]
print("\t confidence interval for pitch_min: ", confidence_interval1_18) 
margin_of_error1_19 = z_score * (s1_19 / math.sqrt(n1_19))
confidence_interval1_19= [x_bar1_19 - margin_of_error1_19, x_bar1_19 + margin_of_error1_19]
print("\t confidence interval for pitch_max: ", confidence_interval1_19) 
margin_of_error1_20 = z_score * (s1_20 / math.sqrt(n1_20))
confidence_interval1_20= [x_bar1_20 - margin_of_error1_20, x_bar1_20 + margin_of_error1_20]
print("\t confidence interval for pulse_number: ", confidence_interval1_20) 
margin_of_error1_21 = z_score * (s1_21 / math.sqrt(n1_21))
confidence_interval1_21= [x_bar1_21 - margin_of_error1_21, x_bar1_21 + margin_of_error1_21]
print("\t confidence interval for pulse_period: ", confidence_interval1_21) 
margin_of_error1_22 = z_score * (s1_22 / math.sqrt(n1_22))
confidence_interval1_22= [x_bar1_22 - margin_of_error1_22, x_bar1_22 + margin_of_error1_22]
print("\t confidence interval for pulse_mean_period: ", confidence_interval1_22)
margin_of_error1_23 = z_score * (s1_23 / math.sqrt(n1_23))
confidence_interval1_23= [x_bar1_23 - margin_of_error1_23, x_bar1_23 + margin_of_error1_23]
print("\t confidence interval for pulse_sd_period: ", confidence_interval1_23)
margin_of_error1_24 = z_score * (s1_24 / math.sqrt(n1_24))
confidence_interval1_24= [x_bar1_24 - margin_of_error1_24, x_bar1_24 + margin_of_error1_24]
print("\t confidence interval for voice_fraction: ", confidence_interval1_24)
margin_of_error1_25 = z_score * (s1_25 / math.sqrt(n1_25))
confidence_interval1_25= [x_bar1_25 - margin_of_error1_25, x_bar1_25 + margin_of_error1_25]
print("\t confidence interval for voice_number: ", confidence_interval1_25)
margin_of_error1_26 = z_score * (s1_26 / math.sqrt(n1_26))
confidence_interval1_26= [x_bar1_26 - margin_of_error1_26, x_bar1_26 + margin_of_error1_26]
print("\t confidence interval for Voice_degree: ", confidence_interval1_26)




print("\n calculating all the confidence intervals across different variable for non-PD individuals")   # These are the CI calculation for non-PD individuals


margin_of_error2_1 = z_score * (s2_1 / math.sqrt(n2_1))
confidence_interval2_1= [x_bar2_1 - margin_of_error2_1 , x_bar2_1 + margin_of_error2_1]
print("\t confidence interval for jitter%: ", confidence_interval2_1) 
margin_of_error2_2 = z_score * (s2_2 / math.sqrt(n2_2))
confidence_interval2_2= [x_bar2_2 - margin_of_error2_2, x_bar2_2 + margin_of_error2_2]
print("\t confidence interval for jitter_microseconds: ", confidence_interval2_2) 
margin_of_error2_3 = z_score * (s2_3 / math.sqrt(n2_3))
confidence_interval2_3= [x_bar2_3 - margin_of_error2_3, x_bar2_3 + margin_of_error2_3]
print("\t confidence interval for jitter_rap: ", confidence_interval2_3) 
margin_of_error2_4 = z_score * (s2_4 / math.sqrt(n2_4))
confidence_interval2_4= [x_bar2_4 - margin_of_error2_4, x_bar2_4 + margin_of_error2_4]
print("\t confidence interval for jitter_ppq5: ", confidence_interval2_4) 
margin_of_error2_5 = z_score * (s2_5 / math.sqrt(n2_5))
confidence_interval2_5= [x_bar2_5 - margin_of_error2_5, x_bar2_5 + margin_of_error2_5]
print("\t confidence interval for jitter_ddp: ", confidence_interval2_5) 
margin_of_error2_6 = z_score * (s2_6 / math.sqrt(n2_6))
confidence_interval2_6= [x_bar2_6 - margin_of_error2_6, x_bar2_6 + margin_of_error2_6]
print("\t confidence interval for shimmer%: ", confidence_interval1_6) 
margin_of_error2_7 = z_score * (s2_7 / math.sqrt(n2_7))
confidence_interval2_7= [x_bar2_7 - margin_of_error2_7, x_bar2_7 + margin_of_error2_7]
print("\t confidence interval for shimmer_db: ", confidence_interval2_7) 
margin_of_error2_8 = z_score * (s2_8 / math.sqrt(n2_8))
confidence_interval2_8= [x_bar2_8 - margin_of_error2_8, x_bar2_8 + margin_of_error2_8]
print("\t confidence interval for shimmer_apq3: ", confidence_interval2_8) 
margin_of_error2_9 = z_score * (s2_9 / math.sqrt(n2_9))
confidence_interval2_9= [x_bar2_9 - margin_of_error2_9, x_bar2_9 + margin_of_error2_9]
print("\t confidence interval for shimmer_apq5: ", confidence_interval2_9) 
margin_of_error2_10 = z_score * (s2_10 / math.sqrt(n2_10))
confidence_interval2_10= [x_bar2_10 - margin_of_error2_10, x_bar2_10 + margin_of_error2_10]
print("\t confidence interval for shimmer_apq10: ", confidence_interval2_10) 
margin_of_error2_11 = z_score * (s2_11 / math.sqrt(n2_11))
confidence_interval2_11= [x_bar2_11 - margin_of_error2_11, x_bar2_11 + margin_of_error2_11]
print("\t confidence interval for shimmer_dda: ", confidence_interval2_11)
margin_of_error2_12 = z_score * (s2_12 / math.sqrt(n2_12))
confidence_interval2_12= [x_bar2_12 - margin_of_error2_12, x_bar2_12 + margin_of_error2_12]
print("\t confidence interval for harmonicity_nhr_and_hnr: ", confidence_interval2_12) 
margin_of_error2_13 = z_score * (s2_13 / math.sqrt(n2_13))
confidence_interval2_13= [x_bar2_13 - margin_of_error2_13, x_bar2_13 + margin_of_error2_13]
print("\t confidence interval for harmonicity_nhr: ", confidence_interval2_13) 
margin_of_error2_14 = z_score * (s2_14 / math.sqrt(n2_14))
confidence_interval2_14= [x_bar2_14 - margin_of_error2_14, x_bar2_14 + margin_of_error2_14]
print("\t confidence interval for harmonicity_hnr: ", confidence_interval2_14) 
margin_of_error2_15 = z_score * (s2_15 / math.sqrt(n2_15))
confidence_interval2_15= [x_bar2_15 - margin_of_error2_15, x_bar2_15 + margin_of_error2_15]
print("\t confidence interval for pitch_median: ", confidence_interval2_15) 
margin_of_error2_16 = z_score * (s2_16 / math.sqrt(n2_16))
confidence_interval2_16= [x_bar2_16 - margin_of_error2_16, x_bar2_16 + margin_of_error2_16]
print("\t confidence interval for pitch_mean: ", confidence_interval2_16) 
margin_of_error2_17 = z_score * (s2_17 / math.sqrt(n2_17))
confidence_interval2_17= [x_bar2_17 - margin_of_error2_17, x_bar2_17 + margin_of_error2_17]
print("\t confidence interval for pitch_sd: ", confidence_interval2_17) 
margin_of_error2_18 = z_score * (s2_18 / math.sqrt(n2_18))
confidence_interval2_18= [x_bar2_18 - margin_of_error2_18, x_bar2_18 + margin_of_error2_18]
print("\t confidence interval for pitch_min: ", confidence_interval2_18) 
margin_of_error2_19 = z_score * (s2_19 / math.sqrt(n2_19))
confidence_interval2_19= [x_bar2_19 - margin_of_error2_19, x_bar2_19 + margin_of_error2_19]
print("\t confidence interval for pitch_max: ", confidence_interval2_19) 
margin_of_error2_20 = z_score * (s2_20 / math.sqrt(n2_20))
confidence_interval2_20= [x_bar2_20 - margin_of_error2_20, x_bar2_20 + margin_of_error2_20]
print("\t confidence interval for pulse_number: ", confidence_interval2_20) 
margin_of_error2_21 = z_score * (s2_21 / math.sqrt(n2_21))
confidence_interval2_21= [x_bar2_21 - margin_of_error2_21, x_bar2_21 + margin_of_error2_21]
print("\t confidence interval for pulse_period: ", confidence_interval2_21) 
margin_of_error2_22 = z_score * (s2_22 / math.sqrt(n2_22))
confidence_interval2_22= [x_bar2_22 - margin_of_error2_22, x_bar2_22 + margin_of_error2_22]
print("\t confidence interval for pulse_mean_period: ", confidence_interval2_22)
margin_of_error2_23 = z_score * (s2_23 / math.sqrt(n2_23))
confidence_interval2_23= [x_bar2_23 - margin_of_error2_23, x_bar2_23 + margin_of_error2_23]
print("\t confidence interval for pulse_sd_period: ", confidence_interval2_23)
margin_of_error2_24 = z_score * (s2_24 / math.sqrt(n2_24))
confidence_interval2_24= [x_bar2_24 - margin_of_error2_24, x_bar2_24 + margin_of_error2_24]
print("\t confidence interval for voice_fraction: ", confidence_interval2_24)
margin_of_error2_25 = z_score * (s2_25 / math.sqrt(n2_25))
confidence_interval2_25= [x_bar2_25 - margin_of_error2_25, x_bar2_25 + margin_of_error2_25]
print("\t confidence interval for voice_number: ", confidence_interval2_25)
margin_of_error2_26 = z_score * (s2_26 / math.sqrt(n2_26))
confidence_interval2_26= [x_bar2_26 - margin_of_error2_26, x_bar2_26 + margin_of_error2_26]
print("\t confidence interval for Voice_degree: ", confidence_interval2_26)

# jitter% 2 sample t test 


t_stats, p_val1 = st.ttest_ind_from_stats(x_bar1_1, s1_1, n1_1, x_bar2_1, s2_1, n2_1, equal_var=False, alternative='two-sided')
print("\n Computing t* of gitter _%_...")
print("\t t-statistic (t*): %.3f" % t_stats)

print("\n Computing p-value  of gitter _%_...")
print("\t p-value : %.6f" % p_val1)

print("\n Conclusion:")
if p_val1 < 0.05:
    print("\t We reject the null hypothesis so we can conclude that these data are different from each other hence can be considered.")
else:
    print("\t We accept the null hypothesis so we can conclude that these data are similar so we donot consider this feature.")

# jitter microseconds sample t test 

t_stats, p_val2 = st.ttest_ind_from_stats(x_bar1_2, s1_2, n1_2, x_bar2_2, s2_2, n2_2, equal_var=False, alternative='two-sided')
print("\n Computing t* ...")
print("\t t-statistic (t*): %.3f" % t_stats)

print("\n Computing p-value ...")
print("\t p-value: %.6f" % p_val2)

print("\n Conclusion:")
if p_val2 < 0.05:
    print("\t We reject the null hypothesis so we can conclude that these data are different from each other hence can be consdered.")
else:
    print("\t We accept the null hypothesis so we can conclude that these data are similar so we donot consider this feature.")

# jitter R.A.P sample t test 


t_stats, p_val3 = st.ttest_ind_from_stats(x_bar1_3, s1_3, n1_3, x_bar2_3, s2_3, n2_3, equal_var=False, alternative='two-sided')
print("\n Computing t* ...")
print("\t t-statistic (t*): %.3f" % t_stats)

print("\n Computing p-value ...")
print("\t p-value: %.6f" % p_val3)

print("\n Conclusion:")
if p_val3 < 0.05:
    print("\t We reject the null hypothesis so we can conclude that these data are different from each other hence can be consdered.")
else:
    print("\t We accept the null hypothesis so we can conclude that these data are similar so we donot consider this feature.")
    
# jitter ppq5 sample t test 

t_stats, p_val4 = st.ttest_ind_from_stats(x_bar1_4, s1_4, n1_4, x_bar2_4, s2_4, n2_4, equal_var=False, alternative='two-sided')
print("\n Computing t* ...")
print("\t t-statistic (t*): %.3f" % t_stats)

print("\n Computing p-value ...")
print("\t p-value: %.6f" % p_val4)

print("\n Conclusion:")
if p_val4 < 0.05:
    print("\t We reject the null hypothesis so we can conclude that these data are different from each other hence can be consdered.")
else:
    print("\t We accept the null hypothesis so we can conclude that these data are similar so we donot consider this feature.")



# Gitter ddp sample t test 

t_stats, p_val5 = st.ttest_ind_from_stats(x_bar1_5, s1_5, n1_5, x_bar2_5, s2_5, n2_5, equal_var=False, alternative='two-sided')
print("\n Computing t* ...")
print("\t t-statistic (t*): %.3f" % t_stats)

print("\n Computing p-value ...")
print("\t p-value: %.6f" % p_val5)

print("\n Conclusion:")
if p_val5 < 0.05:
    print("\t We reject the null hypothesis so we can conclude that these data are different from each other hence can be consdered.")
else:
    print("\t We accept the null hypothesis so we can conclude that these data are similar so we donot consider this feature.")

# shimmer % sample t test 

t_stats, p_val6 = st.ttest_ind_from_stats(x_bar1_6, s1_6, n1_6, x_bar2_6, s2_6, n2_6, equal_var=False, alternative='two-sided')
print("\n Computing t* ...")
print("\t t-statistic (t*): %.3f" % t_stats)

print("\n Computing p-value ...")
print("\t p-value: %.6f" % p_val6)

print("\n Conclusion:")
if p_val6 < 0.05:
    print("\t We reject the null hypothesis so we can conclude that these data are different from each other hence can be consdered.")
else:
    print("\t We accept the null hypothesis so we can conclude that these data are similar so we donot consider this feature.")


# shimmer db sample t test 

t_stats, p_val7 = st.ttest_ind_from_stats(x_bar1_7,  s1_7, n1_7, x_bar2_7, s2_7, n2_7, equal_var=False, alternative='two-sided')
print("\n Computing t* ...")
print("\t t-statistic (t*): %.3f" % t_stats)

print("\n Computing p-value ...")
print("\t p-value: %.6f" % p_val7)

print("\n Conclusion:")
if p_val7 < 0.05:
    print("\t We reject the null hypothesis so we can conclude that these data are different from each other hence can be consdered.")
else:
    print("\t We accept the null hypothesis so we can conclude that these data are similar so we donot consider this feature.")
    


# shimmer apq3 sample t test 

t_stats, p_val8 = st.ttest_ind_from_stats(x_bar1_8,  s1_8, n1_8, x_bar2_8, s2_8, n2_8, equal_var=False, alternative='two-sided')
print("\n Computing t* ...")
print("\t t-statistic (t*): %.3f" % t_stats)

print("\n Computing p-value ...")
print("\t p-value: %.6f" % p_val8)

print("\n Conclusion:")
if p_val8 < 0.05:
    print("\t We reject the null hypothesis so we can conclude that these data are different from each other hence can be consdered.")
else:
    print("\t We accept the null hypothesis so we can conclude that these data are similar so we donot consider this feature.")

# shimmer apq5

t_stats, p_val9 = st.ttest_ind_from_stats(x_bar1_9,  s1_9, n1_9, x_bar2_9, s2_9, n2_9, equal_var=False, alternative='two-sided')
print("\n Computing t* ...")
print("\t t-statistic (t*): %.3f" % t_stats)

print("\n Computing p-value ...")
print("\t p-value: %.6f" % p_val9)

print("\n Conclusion:")
if p_val9 < 0.05:
    print("\t We reject the null hypothesis so we can conclude that these data are different from each other hence can be consdered.")
else:
    print("\t We accept the null hypothesis so we can conclude that these data are similar so we donot consider this feature.")
    
    
 # shimmer apq11 sample t test    

t_stats, p_val10 = st.ttest_ind_from_stats(x_bar1_10,  s1_10, n1_10, x_bar2_10, s2_10, n2_10, equal_var=False, alternative='two-sided')
print("\n Computing t* ...")
print("\t t-statistic (t*): %.3f" % t_stats)

print("\n Computing p-value ...")
print("\t p-value: %.6f" % p_val10)

print("\n Conclusion:")
if p_val10 < 0.05:
    print("\t We reject the null hypothesis so we can conclude that these data are different from each other hence can be consdered.")
else:
    print("\t We accept the null hypothesis so we can conclude that these data are similar so we donot consider this feature.")
    
 # shimmmer dda sample t test    

t_stats, p_val11 = st.ttest_ind_from_stats(x_bar1_11,  s1_11, n1_11, x_bar2_11, s2_11, n2_11, equal_var=False, alternative='two-sided')
print("\n Computing t* ...")
print("\t t-statistic (t*): %.3f" % t_stats)

print("\n Computing p-value ...")
print("\t p-value: %.6f" % p_val11)

print("\n Conclusion:")
if p_val11 < 0.05:
    print("\t We reject the null hypothesis so we can conclude that these data are different from each other hence can be consdered.")
else:
    print("\t We accept the null hypothesis so we can conclude that these data are similar so we donot consider this feature.")
    
# harmonocity nhr and hnr sample t test 

    
t_stats, p_val12 = st.ttest_ind_from_stats(x_bar1_12,  s1_12, n1_12, x_bar2_12, s2_12, n2_12, equal_var=False, alternative='two-sided')
print("\n Computing t* ...")
print("\t t-statistic (t*): %.3f" % t_stats)

print("\n Computing p-value ...")
print("\t p-value: %.6f" % p_val12)

print("\n Conclusion:")
if p_val12 < 0.05:
    print("\t We reject the null hypothesis so we can conclude that these data are different from each other hence can be consdered.")
else:
    print("\t We accept the null hypothesis so we can conclude that these data are similar so we donot consider this feature.")
    
 # harmonicity nhr sample t test 
    
t_stats, p_val13 = st.ttest_ind_from_stats(x_bar1_13,  s1_13, n1_13, x_bar2_13, s2_13, n2_13, equal_var=False, alternative='two-sided')
print("\n Computing t* ...")
print("\t t-statistic (t*): %.3f" % t_stats)

print("\n Computing p-value ...")
print("\t p-value: %.6f" % p_val13)

print("\n Conclusion:")
if p_val13 < 0.05:
    print("\t We reject the null hypothesis so we can conclude that these data are different from each other hence can be consdered.")
else:
    print("\t We accept the null hypothesis so we can conclude that these data are similar so we donot consider this feature.")

# harmonicity hnr sample t test 

t_stats, p_val14 = st.ttest_ind_from_stats(x_bar1_14,  s1_14, n1_14, x_bar2_14, s2_14, n2_14, equal_var=False, alternative='two-sided')
print("\n Computing t* ...")
print("\t t-statistic (t*): %.3f" % t_stats)

print("\n Computing p-value ...")
print("\t p-value: %.6f" % p_val14)

print("\n Conclusion:")
if p_val14 < 0.05:
    print("\t We reject the null hypothesis so we can conclude that these data are different from each other hence can be consdered.")
else:
    print("\t We accept the null hypothesis so we can conclude that these data are similar so we donot consider this feature.")

# pitch median sample t test  

t_stats, p_val15 = st.ttest_ind_from_stats(x_bar1_15,  s1_15, n1_15, x_bar2_15, s2_15, n2_15, equal_var=False, alternative='two-sided')
print("\n Computing t* ...")
print("\t t-statistic (t*): %.3f" % t_stats)

print("\n Computing p-value ...")
print("\t p-value: %.6f" % p_val15)

print("\n Conclusion:")
if p_val15 < 0.05:
    print("\t We reject the null hypothesis so we can conclude that these data are different from each other hence can be consdered.")
else:
    print("\t We accept the null hypothesis so we can conclude that these data are similar so we donot consider this feature.")

# pitch mean sample t test 

t_stats, p_val16 = st.ttest_ind_from_stats(x_bar1_16,  s1_16, n1_16, x_bar2_16, s2_16, n2_16, equal_var=False, alternative='two-sided')
print("\n Computing t* ...")
print("\t t-statistic (t*): %.3f" % t_stats)

print("\n Computing p-value ...")
print("\t p-value: %.6f" % p_val16)

print("\n Conclusion:")
if p_val16 < 0.05:
    print("\t We reject the null hypothesis so we can conclude that these data are different from each other hence can be consdered.")
else:
    print("\t We accept the null hypothesis so we can conclude that these data are similar so we donot consider this feature.")

# pitch sd sample t test 

t_stats, p_val17 = st.ttest_ind_from_stats(x_bar1_17,  s1_17, n1_17, x_bar2_17, s2_17, n2_17, equal_var=False, alternative='two-sided')
print("\n Computing t* ...")
print("\t t-statistic (t*): %.3f" % t_stats)

print("\n Computing p-value ...")
print("\t p-value: %.6f" % p_val17)

print("\n Conclusion:")
if p_val17 < 0.05:
    print("\t We reject the null hypothesis so we can conclude that these data are different from each other hence can be consdered.")
else:
    print("\t We accept the null hypothesis so we can conclude that these data are similar so we donot consider this feature.")
    
# pitch min sample t test     

t_stats, p_val18 = st.ttest_ind_from_stats(x_bar1_18,  s1_18, n1_18, x_bar2_18, s2_18, n2_18, equal_var=False, alternative='two-sided')
print("\n Computing t* ...")
print("\t t-statistic (t*): %.3f" % t_stats)

print("\n Computing p-value ...")
print("\t p-value: %.6f" % p_val18)

print("\n Conclusion:")
if p_val18 < 0.05:
    print("\t We reject the null hypothesis so we can conclude that these data are different from each other hence can be consdered.")
else:
    print("\t We accept the null hypothesis so we can conclude that these data are similar so we donot consider this feature.")
    
  # pitch max sample t test   

t_stats, p_val19 = st.ttest_ind_from_stats(x_bar1_19,  s1_19, n1_19, x_bar2_19, s2_19, n2_19, equal_var=False, alternative='two-sided')
print("\n Computing t* ...")
print("\t t-statistic (t*): %.3f" % t_stats)

print("\n Computing p-value ...")
print("\t p-value: %.6f" % p_val19)

print("\n Conclusion:")
if p_val19 < 0.05:
    print("\t We reject the null hypothesis so we can conclude that these data are different from each other hence can be consdered.")
else:
    print("\t We accept the null hypothesis so we can conclude that these data are similar so we donot consider this feature.")

# pulse number sample t test 

t_stats, p_val20 = st.ttest_ind_from_stats(x_bar1_20,  s1_20, n1_20, x_bar2_20, s2_20, n2_20, equal_var=False, alternative='two-sided')
print("\n Computing t* ...")
print("\t t-statistic (t*): %.3f" % t_stats)

print("\n Computing p-value ...")
print("\t p-value: %.6f" % p_val20)

print("\n Conclusion:")
if p_val20 < 0.05:
    print("\t We reject the null hypothesis so we can conclude that these data are different from each other hence can be consdered.")
else:
    print("\t We accept the null hypothesis so we can conclude that these data are similar so we donot consider this feature.")


 # pulse periods sample t test


t_stats, p_val21 = st.ttest_ind_from_stats(x_bar1_21,  s1_21, n1_21, x_bar2_21, s2_21, n2_21, equal_var=False, alternative='two-sided')
print("\n Computing t* ...")
print("\t t-statistic (t*): %.3f" % t_stats)

print("\n Computing p-value ...")
print("\t p-value: %.6f" % p_val21)

print("\n Conclusion:")
if p_val21 < 0.05:
    print("\t We reject the null hypothesis so we can conclude that these data are different from each other hence can be consdered.")
else:
    print("\t We accept the null hypothesis so we can conclude that these data are similar so we donot consider this feature.")


    # Pulse mean period sample t test 
    
t_stats, p_val22 = st.ttest_ind_from_stats(x_bar1_22,  s1_22, n1_22, x_bar2_22, s2_22, n2_22, equal_var=False, alternative='two-sided')
print("\n Computing t* ...")
print("\t t-statistic (t*): %.3f" % t_stats)

print("\n Computing p-value ...")
print("\t p-value: %.6f" % p_val22)

print("\n Conclusion:")
if p_val22 < 0.05:
    print("\t We reject the null hypothesis so we can conclude that these data are different from each other hence can be consdered.")
else:
    print("\t We accept the null hypothesis so we can conclude that these data are similar so we donot consider this feature.")

# pulse sd period sample t test 
t_stats, p_val23 = st.ttest_ind_from_stats(x_bar1_23,  s1_23, n1_23, x_bar2_23, s2_23, n2_23, equal_var=False, alternative='two-sided')
print("\n Computing t* ...")
print("\t t-statistic (t*): %.3f" % t_stats)

print("\n Computing p-value ...")
print("\t p-value: %.6f" % p_val23)

print("\n Conclusion:")
if p_val23 < 0.05:
    print("\t We reject the null hypothesis so we can conclude that these data are different from each other hence can be consdered.")
else:
    print("\t We accept the null hypothesis so we can conclude that these data are similar so we donot consider this feature.")

# voice fraction sample t test      
t_stats, p_val24 = st.ttest_ind_from_stats(x_bar1_24,  s1_24, n1_24, x_bar2_24, s2_24, n2_24, equal_var=False, alternative='two-sided')
print("\n Computing t* ...")
print("\t t-statistic (t*): %.3f" % t_stats)

print("\n Computing p-value ...")
print("\t p-value: %.6f" % p_val24)

print("\n Conclusion:")
if p_val24 < 0.05:
    print("\t We reject the null hypothesis so we can conclude that these data are different from each other hence can be consdered.")
else:
    print("\t We accept the null hypothesis so we can conclude that these data are similar so we donot consider this feature.")
  
# Voice number sample t test     
t_stats, p_val25 = st.ttest_ind_from_stats(x_bar1_25,  s1_25, n1_25, x_bar2_25, s2_25, n2_25, equal_var=False, alternative='two-sided')
print("\n Computing t* ...")
print("\t t-statistic (t*): %.3f" % t_stats)

print("\n Computing p-value ...")
print("\t p-value: %.6f" % p_val25)

print("\n Conclusion:")
if p_val25 < 0.05:
    print("\t We reject the null hypothesis so we can conclude that these data are different from each other hence can be consdered.")
else:
    print("\t We accept the null hypothesis so we can conclude that these data are similar so we donot consider this feature.")

# voice degree sample t test       
t_stats, p_val26 = st.ttest_ind_from_stats(x_bar1_26,  s1_26, n1_26, x_bar2_26, s2_26, n2_26, equal_var=False, alternative='two-sided')
print("\n Computing t* ...")
print("\t t-statistic (t*): %.3f" % t_stats)

print("\n Computing p-value ...")
print("\t p-value: %.6f" % p_val26)

print("\n Conclusion:")
if p_val26 < 0.05:
    print("\t We reject the null hypothesis so we can conclude that these data are different from each other hence can be consdered.")
else:
    print("\t We accept the null hypothesis so we can conclude that these data are similar so we donot consider this feature.")
    
    

 
variables ={'Jitter%':p_val1,
            'Jitter mircoseconds':p_val2, 
            'Jitter rap':p_val3,
            'Jitter ppq5':p_val4, 
            'Gitter ddp':p_val5, 
            'Shimmer%':p_val6,
            'Shimmer db':p_val7,
            'Shimmer apq3':p_val8,
            'Shummer apq5':p_val9,
            'Shimmer apq11':p_val10,
            'Shimmer dda':p_val11,
            'Harmonicity nhr hnr':p_val12,
            'Harmonicity nhr':p_val13,
            'Harmonicity hnr':p_val14,
            'Pitch median':p_val15,
            'Pitch mean':p_val16,
            'Pitch sd':p_val17,
            'Pitch min':p_val18,
            'Pitch max':p_val19,
            'Pulse number':p_val20,
            'Pulse periods':p_val21,
            'Pulse mean period':p_val22,
            'Pulse sd period':p_val23,
            'Voice fracetion':p_val24,
            'Voice number':p_val25,
            'Voice degree':p_val26,
            
            
            } 


# Below codes are responsible for printing the significant and non significant variables which were analyzed above during hypothesis testing



print("\n Result of overall  analysis")


    
    
significant_variables = []
non_significant_variables = []


for  key , value  in variables.items():
     if value < 0.05:
        significant_variables.append(key)
       
     else:
        non_significant_variables.append(key)
        
  
print("\nThese are the significant variables which provide enough evidence to distinguish between people sufferring from PD and Healthy person")  
        
for item in significant_variables:
    print("\t ",  item)
    
    
print("\n These are the variables which donot provide enough evidence to distinguish between people sufferring from PD and Healthy person") 

for item in non_significant_variables:
    print("\t ",  item)
    
    

 
 





















