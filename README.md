# Agent Interaction Script

This repository contains a script that allows users to interact with an agent, ask questions, and receive answers based on uploaded files. The script utilizes the langchain library and the OpenAI Completion API for generating answers.

## Getting Started

To get started with this script, follow the steps below:

### Prerequisites

- Python 3.x
- langchain library (install using `pip install langchain`)
- OpenAI Python library (install using `pip install openai`)

### Installation

1. Clone the repository:

2. Navigate to the project directory:

3. Install the required Python dependencies:

### Usage

1. Run the script:

2. Follow the prompts to interact with the agent:
- Enter your question when prompted.
- Provide the path to the file you want to upload.

3. The agent will generate an answer based on your question and the content of the uploaded file.

4. Continue the interaction by asking more questions or uploading different files.

### Configuration

- You can adjust the parameters of the `generate_answer` function in the `agent_script.py` file to modify the behavior of the agent, such as response length, temperature, and top-p values.

### Error Handling

The script includes error handling to gracefully handle potential exceptions that may occur during file processing or API requests. It uses try-except blocks to ensure the script continues to run smoothly even if errors occur.

### Input Validation

The script performs input validation to check for valid user input and handle any unexpected inputs gracefully.

### Additional Customization

Feel free to customize the `extract_file_content` function to handle your specific file types and extract relevant information accordingly.

## Contributing

Contributions to this project are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
