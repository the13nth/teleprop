# Teleprompter App

This is a simple teleprompter application built with Flask that allows you to upload a text file and then displays the text on the screen sentence by sentence. It also includes a timer and video recording functionality.

## Features

- Upload a text file to be used as the script for the teleprompter.
- Start, pause, and stop the teleprompter.
- Navigate to the previous and next sentences.
- Record a video while the teleprompter is running.
- Download the recorded video.

## How to Use

1. Ensure you have Python and Flask installed on your machine.
2. Clone this repository to your local machine.
3. Navigate to the project directory in your terminal.
4. Run `export FLASK_APP=app.py` to set the application.
5. Run `flask run` to start the application.
6. Open your web browser and navigate to `http://localhost:5000`.
7. Upload a text file using the "Upload" button.
8. Click the "Start" button to start the teleprompter and video recording.
9. Use the "Last Sentence" and "Next Sentence" buttons to navigate through the sentences.
10. Click the "Pause" button to pause the teleprompter and video recording.
11. Click the "Stop" button to stop the teleprompter and video recording and download the recorded video.

## Requirements

This application requires Python and Flask. The video recording feature requires a web browser that supports the MediaRecorder API.

## License

This project is licensed under the MIT License.
