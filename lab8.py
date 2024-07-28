
"""lab8.ipynb

Original file is located at
    https://colab.research.google.com/drive/1uF4gDai6InIFgnaCyo5CWMIgVBlvA0_1
"""

#Name: Long Hoang
#Lab8

"""Task: Rainfall data processing"""

#upload file if using Google Colab
# from google.colab import files
# uploaded = files.upload()

def main():

  try:
    #prompt user to read in a file
    file_name = input("Please enter the file name: ")

    try:
      # Open the file to read
      file = open(file_name, 'r')

    except FileNotFoundError:
      print(f"Error: The file '{file_name}' was not found. Please check the file name and its location.")

    #if no exceptions occur, read the file
    else:
      namelist = []
      datalist = []
      #read the file line by line
      for line in file:
        #split data by space each line
        pair = line.strip().split()

        #if missing data element in the pair
        if len(pair) != 2:
          print(f"Error: Invalid line format: {line.strip()}")
          continue

        #namelist, datalist = pair[0], pair[1]

        #append data to the list after each loop
        namelist.append(pair[0])

        #filter float format for datalist
        try:
          rainfall = float(pair[1])
        except ValueError:
          print(f"Error: Invalid data format: {pair[1]} for city {pair[0]}, using 0.0 instead.")
          rainfall = 0.0

        #append data to the list after each loop
        datalist.append(rainfall)

      #calculate the highest, lowest, and average/mean of the data list
      highest = max(datalist)
      lowest = min(datalist)
      average = sum(datalist) / len(datalist)

      # Display results
      print(f"Highest Rainfall: {highest}")
      print(f"Lowest Rainfall: {lowest}")
      print(f"Average Rainfall: {average}")

    #rainfall.txt
    finally:
      file.close()
      print("File Closed..!")


  #catch all errors
  except Exception as e:
    print(f"An unexpected error occurred: {e}")


main()

# output test run


'''
Please enter the file name: abc.txt
Error: The file 'abc.txt' was not found. Please check the file name and its location.
An unexpected error occurred: local variable 'file' referenced before assignment
'''

'''
Please enter the file name: rainfall.txt
Highest Rainfall: 38.22
Lowest Rainfall: 25.81
Average Rainfall: 34.05962962962963
File Closed..!
'''

'''
Please enter the file name: rainfall_error.txt
Error: Invalid data format: 3.4.5 for city B_Unknown, using 0.0 instead.
Error: Invalid data format: 3#5 for city C_Problem, using 0.0 instead.
Highest Rainfall: 38.22
Lowest Rainfall: 0.0
Average Rainfall: 31.710689655172413
File Closed..!
'''