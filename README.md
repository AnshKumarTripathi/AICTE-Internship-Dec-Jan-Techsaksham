# Human Pose Estimation Web App
   ```sh
   Note: I havent included the whole dataset as it was too large for me to upload.
   ```
This repository contains the code for a web-based application that performs human pose estimation on uploaded images using machine learning techniques, specifically leveraging the OpenPose model with OpenCV in a Streamlit environment.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Objectives](#objectives)
- [Installation](#installation)
- [Usage](#usage)
- [Requirements](#requirements)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction
The Human Pose Estimation Web App is designed to provide an accessible and user-friendly tool for identifying and visualizing human poses in images. This tool can be used in various fields, such as sports, healthcare, and entertainment, to enhance performance analysis and monitoring.

## Features
- Upload images for pose estimation
- Visual feedback on detected human poses
- Supports multiple people in a single image
- User-friendly web interface using Streamlit
- Free public access through deployment on Streamlit Sharing

## Objectives
1. Create a user-friendly web application for human pose estimation.
2. Implement the OpenPose model using OpenCV for accurate pose estimation.
3. Deploy the application for public access, enabling widespread use and testing.
4. Utilize the application in various fields, such as sports, healthcare, and entertainment.
5. Offer a tool for physical therapy and rehabilitation by tracking and analyzing body movements.
6. Develop a solution for ergonomic assessments and workplace safety.

## Installation
Follow these steps to set up and run the application locally:

1. **Clone the Repository:**
   ```sh
   git clone (https://github.com/AnshKumarTripathi/AICTE-Internship-Dec-Jan-Techsaksham)
   ```

2. **Set Up a Virtual Environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Download OpenPose Model Files:**
   Download the following files and place them in the `models/pose/coco/` directory:
   - pose_deploy_linevec.prototxt: https://github.com/CMU-Perceptual-Computing-Lab/openpose/raw/master/models/pose/coco/pose_deploy_linevec.prototxt
   - pose_iter_440000.caffemodel: https://drive.google.com/uc?id=1U90QxGLMNSLNE8j0iKdeG5hGTvQ5bfab

5. **Run the Streamlit App:**
   ```sh
   streamlit run app.py
   ```

## Usage
1. Open your web browser and go to `http://localhost:8501`.
2. Upload an image using the provided interface.
3. The application will display the image with detected human poses visualized.

## Requirements
- **Hardware Requirements:**
  - Processor: Intel i5 or higher
  - RAM: 8 GB or more
  - Storage: 256 GB SSD or more
  - Graphics Card: NVIDIA GPU with CUDA support (optional for improved performance)

- **Software Requirements:**
  - Operating System: Windows, macOS, or Linux
  - Python: Version 3.6 to 3.9
  - Libraries:
    - Streamlit
    - OpenCV
    - NumPy
    - Pillow

## Project Structure
```
human-pose-estimation-web-app/
├── models/
│   └── pose/
│       └── coco/
│           ├── pose_deploy_linevec.prototxt
│           └── pose_iter_440000.caffemodel
├── app.py
├── requirements.txt
└── README.md
```

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request or open an issue to improve the project.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
This project was created by Ansh Kumar Tripathi under the guidance of mentor P. Raja during the AICTE Internship on AI: Transformative Learning with TechSaksham – a joint CSR initiative of Microsoft & SAP.

---
