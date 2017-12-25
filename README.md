# FUSION
Efficient Multistream Classification using Direct DensIty Ratio Estimation

## Synopsis
Traditional data stream classification assumes that data is generated from a single non-stationary process. On the contrary, multistream classification problem involves two independent non-stationary data generating processes. One of them is the source stream that continuously generates labeled data. The other one is the target stream that generates unlabeled test data from the same domain. The distributions represented by the source stream data is biased compared to that of the target stream. Moreover, these streams may have asynchronous concept drifts between them. The multistream classification problem is to predict the class labels of target stream instances, while utilizing labeled data available on the source stream. This kind of scenario is often observed in real-world applications due to scarcity of labeled data. FUSION provides an efficient solution for multistream classification by fusing drift detection into online data adaptation. Theoretical analysis and experiment results show its effectiveness. Please refer to the paper (mentioned in the reference section) for further details. 

## Requirements
ECHO requires that-
* Input file will be provided in a ARFF format.
* All the features need to be numeric. If there is a non-numeric featues, those can be converted to numeric features using standard techniques.
* Features should be normalized to get better performance. 

## Environment
* Java SDK v1.7+
* Weka 3.6+
* Common Math library v2.2
* Apache Logging Services v1.2.15

All of above except java sdk are included inside SRC_ECHO_v_0_1 & DIST_ECHO_v_0_1 folder.

## Execution
To execute the program in a windows operating system:
1. Open a command prompt inside DIST_ECHO_v_0_1 folder folder.
2. Run the command ``java -jar ECHO_v_0_1.jar [OPTION(S)]''

## Option(s):
* -F 
 * Input file path. Do not include file extension .arff in the file path.
 
## Optional option(s):
* -S
 * Size of warm-up period chunks. Default is 2000 instances.
* -L
 * Maximum number of models in the ensemble. Default value is 6.
* -U
 * Value for confidence threshold. Please refer to the paper for description of confidence threshold. Default value is 0.90.
* -D
 * use 1 here to execute ECHO-D, 0 to execute ECHO-F. Please refer to the paper for description about ECHO-D, and ECHO-F. Default value is 1.
* -T
 * Labeling delay in number of instances. Default value for classification only is 1. Use appropriate value for novel class detection.
* -C
 * Classification delay in number of instances. Default value for classification only is 0. Use appropriate value for novel class detection.
* -W
 * Maximum allowable window size. Default value is 3000.
* -A
 * Sensitivity (denoted by alpha). Default value is 0.001.
* -G
 * Value of gamma, which is used to calculate the cushion period. Default value is 0.5. 
* -R 
 * Relaxation parameter. It is used in the change detection procedure. Default value is same as the value of Sensitivity.


## Output
### Console output
* The program shows progress or any change point detected in console. 
* At the end, it reports percentage of labeled data used.

### File output
1. .log file contains important debug information.
2. .tmpres file contains the error rates for each chunk.  There are six columns as follows:
 * Chunk #= The current chunk number. Each chunk contains 1000 instances.
 * FP= How many existing class instances misclassified as novel class in this chunk.
 * FN= How many novel class instances misclassified as existing class in this chunk.
 * NC= How many novel class instances are actually there in this chunk.
 * Err = How many instances are misclassified (including FP and FN) in this chunk.
 * GlobErr = % Err (cumulative) upto the current chunk.
3. .res file contains the summary result, i.e., the following error rates:
 * FP% = % of existing class instances misclassified as novel
 * FN% = % of novel class instances misclassified as existing class instances.
 * NC (total) = total number of (actual) novel class instances.
 * ERR% = % classification error (including FP, FN, and misclassification within existing class).

## Reference
[FUSION: An Online Method for Multistream Classification](https://dl.acm.org/citation.cfm?id=3132886&dl=ACM&coll=DL&CFID=1020200191&CFTOKEN=12773057)
