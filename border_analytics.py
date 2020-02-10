import csv
import math


def readInput(filename):
    """
    return the first line and other lines seperately as a list
    param: filename
    type: a string with the filename and the surffix
    """
    assert isinstance(filename, str)
    file = open(filename,newline='')
    head = []
    rows = []
    read = csv.reader(file)
    for i in read:
        rows.append(i)
    head.extend([rows[0][3],rows[0][4],rows[0][5],rows[0][6],"Average"])
    return head, rows

def getSum(file):
    """
    return a list with clean-up information and also the sum
    param: file
    type:  list
    """
    assert isinstance(file, list)
    result = []
    hash_map = dict() # Store the total number of specific (Date+Measure+Boarder)
    
    # Aggregate the data and get sum
    for i in range(1, len(file)):
        key = (file[i][3], file[i][4], file[i][5])
        if key not in hash_map:
            hash_map[key] = int(file[i][6])  
            result.append([file[i][3], file[i][4], file[i][5]])
        else:
            hash_map[key] += int(file[i][6])
            
    # Append the sum to the result
    for i in range(0, len(result)):
        result[i].append(hash_map[(result[i][0],result[i][1],result[i][2])])
    return result


def sortData(InputData):
    """
    return a sorted list in descending order by 1.Date 2. Value 3. Measure 4. Border
    param: InputData
    type:  list
    """
    assert isinstance(InputData, list)
    InputData.sort(key=lambda i:(i[1], i[3], i[2], i[0]),  reverse=True)
    return InputData


def getAverage(result):
    """
    return the list with sum and average
    param: result
    type:  list
    """
    assert isinstance(result, list)
    i = 0
    while i < len(result):
        x = 0
        result[i].append(0)
        # If "Date" is not in January., then calculate the average
        if (int(result[i][1][:2])-1) != 0:
            for n in range(i+1, len(result)):
                # If following rows can meet specific criteria, then calculate average
                if result[n][0] == result[i][0] and result[n][2] == result[i][2]:
                    x += int(result[n][3])
            result[i][4] = x // (int(result[i][1][:2])-1)
        i += 1
    return result

def insertHead(result, head):
    """
    return the final result with first line of the list is the head
    param: result
    type:  list
    param: head
    type:  list
    """
    assert isinstance(result, list)
    assert isinstance(head, list)
    result.insert(0,head)
    return result

def writeOutput(result, filename):
    """
    write the data into the specific filename
    param: result
    type:  list
    param: filename
    type:  string
    """
    assert isinstance(result, list)
    assert isinstance(filename, str)
    report = open(filename,'w',newline = '')
    with open(filename,'wb',newline = '') as report:
        filewriter = csv.writer(report)
        filewriter.writerows(result)


if __name__ == "__main__":
    InputFile = "../insight_testsuite/tests/test_1/input/Border_Crossing_Entry_Data.csv" 
    OutputFile = "../insight_testsuite/tests/test_1/output/report.csv"

    head, InputFile = readInput(InputFile)
    MidResult = getSum(InputFile)
    MidResult = sortData(MidResult)
    MidResult = getAverage(MidResult)
    Result = insertHead(MidResult, head)
    writeOutput(Result, OutputFile)
#     for i in range(len(Result)):
#         print(Result[i])