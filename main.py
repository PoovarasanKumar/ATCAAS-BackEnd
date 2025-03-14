from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
from Auth import authenticate_user 
from cookies import generate_cookies
from Agents.UserStoryToTestCase import Get_TestCasesFromUserStory
from Agents.TestCasesToFlow import Get_Flow
from Agents.TestDataGeneration import Get_TestData
from Agents.CodeGeneration import Get_Code
from Agent1 import Get_TestCases
from sampleoutput import Get_SampleOutput
import json

app = Flask(__name__)
CORS(app)


@app.route('/process', methods=['POST'])
def process_input():
    try:
        # Get the input data
        testcaseType = request.form['testcaseType']
        frameworkType = request.form['frameworkType']
        input = request.form['userStory']
        testData = request.form['testData']
        automationIdTemplate = request.form['automationIdTemplate']
        additionalDetails = request.form['additionalDetails']


        print("Testcase Type: " + testcaseType)
        print("Framework Type: " + frameworkType)
        print("Input: " + input)
        print("Test Data: " + testData)
        
        # code, testData, flow = Get_SampleOutput(input)
        
        # response = {
        #     "frameworkType": frameworkType,
        #     "automationCode": code,
        #     "testData": testData,
        #     "flowData": flow
        # }

        # return jsonify(response)

        auth_response = authenticate_user()
        generate_cookies()

        #print(outputtestData)

        autotemp = "\n {Autoamtion id template:{\n " +automationIdTemplate+ "}\n}";
        additionalDetails = "\nAdditional Details:{\n " +additionalDetails+ "}\n}";
        test_data_info = "*** Important : output should only contain the generated test data in CSV format ***\n";
        flow_info = "*** Important : flow should not contain verify action, if test case says verify pease ignore that step ***\n";
        code_info = "*** Important : don;t use RPA.Desktop library use PRA.Windows Library***\n";
        code_info2 = code_info + "*** Important : Add this variables in top #${UPLOAD_FILE_NAME}  filename \n ${CSV_FILE_PATH}  csvfilepath\n"; 
        code_info3 = code_info2 + "*** Important : don;t use 'RPA.Windows.Select From List By Label' for dropdown instead use/ 'RPA.Windows.Click  id:__\n RPA.Windows.Click    _value\n'";

        user_stryinput = input  + "\n " + additionalDetails

        outputtestData =  Get_TestData(testData + "\n" )

        if(testcaseType != "Testcases"):
            testcases = Get_TestCasesFromUserStory(user_stryinput)
            flow_content = Get_Flow(testcases + autotemp + flow_info)
            # print("User story " +result)
        else:
            print("Testcases")
            flow_content = Get_Flow(user_stryinput + autotemp + flow_info)
            # print(result)

        # # print(flow_contevnt)
        # outputtestData = "{'testData': 'testData'}"
        # flow_content = "{'flow': 'flow'}"

        # # testcasetocodeOuptut = Get_Code(result + outputtestData)
        code_content = Get_Code(flow_content +"/n" + outputtestData +"/n" + code_info3)

        response = {
            "frameworkType": frameworkType,
            "automationCode": code_content,
            "testData": outputtestData,
            "flowData": flow_content
        }

        # response = {
        #     "frameworkType": frameworkType,
        #     "automationCode": "",
        #     "testData": outputtestData,
        #     "flowData": ""
        # }

        
        return jsonify(response)

    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 400

    
