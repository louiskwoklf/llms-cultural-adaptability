# Evaluating Cultural Adaptability of a Large Language Model via Synthetic Personas

This repository contains the code and materials for the paper "Evaluating Cultural Adaptability of a Large Language Model via Synthetic Personas", published at the Conference on Large Modeling (COLM) 2024.

The paper explores the ability of a large language model, GPT-3.5, to simulate human profiles representing diverse nationalities within the scope of a psychological experiment. By revisiting a multi-national dataset from Bos et al. (2020) and prompting the LLM with specific human profiles, the study assesses the effectiveness of different methods in conveying nationality-related information to the model and examines how accurately the national traits are depicted in various multilingual settings.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- OpenAI API key

### Installation

Clone the repository:
\`\`\`bash
git clone https://github.com/louiskwoklf/llms-cultural-adaptability.git
\`\`\`

Install the required dependencies:
\`\`\`bash
cd llms-cultural-adaptability
pip install -r requirements.txt
\`\`\`

### Data Preparation

1. Download the dataset from the original study by Bos et al. (2020) and place it in the \`data/\` directory.
2. Update the paths in the scripts to match your local file structure.

### Running the Experiments

1. Run the script:
\`\`\`bash
python generation.py
\`\`\`

The script will simulate the responses of the GPT-3.5 model to the survey prompts.

## Results

The main findings of the paper are:

- Explicitly stating the nationality of a simulated participant (by specifying the country of residence) improves the fidelity of the simulation, allowing the model to better capture national variations in persuasion and mobilization.
- Conveying nationality traits through native language prompting is less effective, and certain languages (e.g., Greek and Hebrew) can significantly reduce the alignment with the human data.
- For modeling nationality-specific characteristics, native language prompting causes response changes that do not align with the international variations observed in humans.

## Citation

If you use this code or find the paper useful, please cite the following:

\`\`\`
tbh
\`\`\`

## Contributions and Feedback

Contributions to the codebase and feedback on the work are welcome. Please feel free to open issues or submit pull requests.

## Acknowledgments

This work was supported by the Department of Computer Science at University College London.
"""
