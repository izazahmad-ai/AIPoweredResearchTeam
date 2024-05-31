
# AI-Powered Research Team

Welcome to the AI-Powered Research Team project! This repository contains the code for an AI-based team that automates the process of creating a research article. The team is composed of three agents: Supervisor, Co-Supervisor, and Student.

## Overview

This project allows users to input a research topic, and the AI agents collaboratively work on generating a complete research article in Word format. The current version focuses on the communication among agents and the creation of a structured document with sections such as the abstract, introduction, literature review, background work, proposed methodology, results, conclusion, and references.

## Features

- **Three AI Agents**: Supervisor, Co-Supervisor, and Student.
- **Automated Research Workflow**: Input a research topic, and the AI team handles the rest.
- **Seamless Collaboration**: Agents work together to create and review each section of the research article.
- **Output**: Generates a Word document with the research article.

## Future Enhancements

- **Improved Content Quality**: Aim for 90% content quality in the next version.
- **Enhanced Problem Identification**: Help researchers with problem identification.
- **Advanced Input Handling**: Accept multiple articles and related topics to start comprehensive research.

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Install required packages

### Installation

1. Clone the repository or download

2. Create a `.env` file in the root directory and add your OpenAI API key:
   \```
   OPENAI_API_KEY=your_openai_api_key
   \```

3. Run the main script:
   \```
   python main.py
   \```

## Usage

1. Run the main script.
2. Enter the research topic when prompted.
3. The AI agents will process the topic and generate a research article.
4. The final document will be saved as `Research_Article_on_<topic>.docx`.

## Example

\```
Enter the research topic: Image Segmentation
Processing section: Literature Review
...
Research article has been generated and saved as final_article.docx
\```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

No lincense.

## Contact

For any questions or feedback, please reach out to (izazkhattak7@gmail.com).
