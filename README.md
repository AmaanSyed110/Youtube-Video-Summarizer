# Youtube-Video-Summarizer

## Overview
The **YouTube Video Summarizer** is a web-based application that generates concise summaries of YouTube videos, allowing users to quickly grasp the key points without watching the entire video. By inputting a YouTube link, the app utilizes the Gemini Pro LLM to analyze and extract important content from the video, delivering a text-based summary in real time. Built using the Streamlit framework, the application offers a user-friendly interface, making it accessible for both technical and non-technical users. This tool is ideal for efficiently summarizing lengthy or complex videos.

## Demo Video
[streamlit-app-2024-09-01-17-09-54.webm](https://github.com/user-attachments/assets/88b5b1ce-1c80-4bea-8555-18599c22521b)

## Tech Stack
- **Python**: The core programming language used for developing backend logic and integrating with AI models.

- **Streamlit**: Framework for creating the interactive web interface where users can input YouTube links and view video summaries.
  
- **Gemini Pro LLM**: The language model employed for analyzing video content and generating summaries.
  
- **Langchain**: A framework that facilitates interaction with Gemini Pro LLM, optimizing language model performance and integrating additional tools as needed.
  
## Features
- **YouTube Link Input**: Allows users to enter a YouTube video URL to initiate the summarization process.
  
- **Automated Content Analysis**: Utilizes Gemini Pro LLM to analyze video content and generate a concise summary.
  
- **Interactive Interface**: Built with Streamlit, providing a user-friendly platform for entering links and viewing summaries.
  
- **Real-Time Summarization**: Processes videos and delivers summaries quickly, enhancing user efficiency and experience.
  
## Requirements
- Python 3.10
  
- Gemini Pro model api key (Note: Ensure you have the necessary credentials and permissions to access the Gemini Pro API)
  
- Obtain API credentials from the makersuit platform.

- Create a file named .env in the project root directory.

- Add the following lines to .env:
  ```bash
   GOOGLE_API_KEY= "your_api_key"
   ```
