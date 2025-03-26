# BPMN Workflow Visualizer

A simple web-based visualizer for BPMN (Business Process Model and Notation) workflow diagrams.

## Features

- Visualize BPMN workflow diagrams in a web browser
- Print workflow diagrams
- Lightweight server implementation using Python
- Support for standard BPMN XML files

## Getting Started

### Prerequisites

- Python 3.6 or higher

### Installation

1. Clone this repository
   ```
   git clone https://github.com/your-username/bpmn-workflow-visualizer.git
   cd bpmn-workflow-visualizer
   ```

2. (Optional) Create a virtual environment
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

### Usage

1. Place your BPMN files in the `data/bpmn/` directory
2. Run the server:
   ```
   python visualizer.py
   ```
3. The application will open in your web browser automatically at http://localhost:8000

## Project Structure

- `visualizer.py` - Python server implementation
- `index.html` - Main web interface
- `workflow.svg` - SVG visualization of the workflow
- `bpmn.min.js` - BPMN.js library (minimized)
- `bpmn.min.css` - BPMN.js styles (minimized)
- `data/bpmn/` - Directory for BPMN files

## License

This project is licensed under the MIT License - see the LICENSE file for details. 