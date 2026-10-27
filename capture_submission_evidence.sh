#!/usr/bin/env bash
set -euo pipefail
# Run in Srushti's Coursera Theia project to create actual text evidence.
cd /home/project/final_project
mkdir -p submission_evidence
cp EmotionDetection/emotion_detection.py submission_evidence/2a_emotion_detection
cp EmotionDetection/emotion_detection.py submission_evidence/3a_output_formatting
cp test_emotion_detection.py submission_evidence/5a_unit_testing
cp server.py submission_evidence/6a_server
cp EmotionDetection/emotion_detection.py submission_evidence/7a_error_handling_function
cp server.py submission_evidence/7b_error_handling_server
cp server.py submission_evidence/8a_server_modified

echo "Capturing real interpreter, tests and static-analysis output..."
{
 printf '$ cd /home/project/final_project\n$ python3\n'
 python3 -c "import sys; print(sys.version); from emotion_detection import emotion_detector; print(emotion_detector('I am really mad about this'))"
 printf '$ exit()\n$ python3 test_emotion_detection.py\n'
 python3 test_emotion_detection.py 2>&1
} | tee submission_evidence/2b_application_creation
{
 printf '$ cd /home/project/final_project\n$ python3 -c "from emotion_detection import emotion_detector; print(emotion_detector(\\\"I am glad this happened\\\"))"\n'
 python3 -c "from emotion_detection import emotion_detector; print(emotion_detector('I am glad this happened'))"
} | tee submission_evidence/3b_formatted_output_test
{
 printf '$ cd /home/project/final_project\n$ python3 -c "from EmotionDetection.emotion_detection import emotion_detector; print(emotion_detector(\\\"I am very angry\\\"))"\n'
 python3 -c "from EmotionDetection.emotion_detection import emotion_detector; print(emotion_detector('I am very angry'))"
} | tee submission_evidence/4b_packaging_test
{
 printf '$ cd /home/project/final_project\n$ python3 test_emotion_detection.py\n'
 python3 test_emotion_detection.py 2>&1
} | tee submission_evidence/5b_unit_testing_result
{
 printf '$ cd /home/project/final_project\n$ pylint server.py\n'
 pylint server.py 2>&1
} | tee submission_evidence/8b_static_code_analysis
echo 'Evidence saved in /home/project/final_project/submission_evidence'
