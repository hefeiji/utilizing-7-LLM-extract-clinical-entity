# utilizing-7-LLM-extract-clinical-entity
utilizing 7 LLM extract clinical entity
Step 1: Establish the Local Environment
1. Create Python 3.11.5 environment using Conda in VSCode terminal.
2. Ensure availability of Pandas, Times, and Requests packages, installing them if necessary.
3. Prepare the Excel spreadsheet: Cell A1 is labeled “input”, with inputs recorded in column A, starting from row 2; Cell B1 is labeled “output”, with outputs recorded in column B, aligned row-wise with the corresponding inputs.
4. Put The Excel file (file format xlsx) and Python script in same root directory.
Step 2: Develop a Python script in VSCode to execute processing workflow
1. Import necessary libraries: pandas, requests, and time.
2. Define ask-silicon(input) function：
2.1. Send a POST request to the Siliconflow API with a given input.
2.2. Parse and returns the response content.
2.3. Handle exceptions and returns "N/A" if error occurs.
3. Define main() function:
3.1. Read the Excel file stores inputs. 
3.2. Iterate through each row in the Excel file.
3.3. Check if the "output" column is null.
3.4. Execute ask-silicon(input) function and updates the Excel with the output.
3.5. Sleep for 1 second to control the API call frequency.
3.6. Save the data frame to "inputs_processed.xlsx" after each iteration.
4. Execute main() function if the script runs directly.
