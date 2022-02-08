import math

def solution(sizes, uploadingStart, v):
    if uploadingStart == []: return []
    end_times = uploadingStart.copy()
    curr_time = min(uploadingStart)
    # Iterate over curr_time, until all files uploaded
    while max(sizes) > 0:
        # Determine which files can be updated
        updatable = [1 if sizes[i] > 0 and uploadingStart[i] <= curr_time else 0 for i in range(len(sizes))]
        print("SIZES: " + str(sizes))
        for i in range(len(sizes)):
            if updatable[i]: # If file can be updated
                sizes[i] = sizes[i] - v / (sum(updatable) if sum(updatable) > 0 else 1)
                # If file is finished uploading, record end time
                if sizes[i] <= 0:
                    end_times[i] = (curr_time + 1)
        # Update current time
        curr_time += 1
    return end_times

sizes = [12, 17, 2, 27, 23]
uploadingStart = [2, 5, 8, 6, 2]
v = 9
print("\nRESULT: {0}".format(str(solution(sizes, uploadingStart, v))))
print("EXPECTED: [5, 10, 9, 11, 8]")

# print("\n-------------------------------\n")

# sizes = [21, 10]
# uploadingStart = [100, 105]
# v = 2
# print("\nRESULT: {0}".format(str(solution(sizes, uploadingStart, v))))
# print("EXPECTED: [116, 115]")
#
# print("\n-------------------------------\n")
#
# sizes = [20, 10]
# uploadingStart = [1, 1]
# v = 1
# print("RESULT: {0}".format(str(solution(sizes, uploadingStart, v))))
# print("EXPECTED: [31, 21]")
#
# print("\n-------------------------------\n")
#
# sizes = [1, 1, 1]
# uploadingStart = [10, 20, 30]
# v = 3
# print("RESULT: {0}".format(str(solution(sizes, uploadingStart, v))))
# print("EXPECTED: [11, 21, 31]")
