# Youtube-Video-Summarizer

## Overview
The **YouTube Video Summarizer** is a Streamlit-based web application that allows users to input a YouTube video link and get a detailed summary of the video's transcript. The app uses OpenAI's GPT models (via LangChain) to generate concise and meaningful summaries. It also includes a question-answering feature, enabling users to ask specific questions about the video content.


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
  
- Gemini Pro model api key (Note: Ensure you have the necessary credentials and permissions to access the Gemini Pro API).
  
- Obtain API credentials from the makersuit platform.

- Create a file named .env in the project root directory.

- Add the following lines to .env:
  ```bash
   GOOGLE_API_KEY= "your_api_key"
   ```
