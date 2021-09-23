<h1 align="center"> Social Distance Detector </h1>
<h2 align="center"> A Real-Time Social Distance Monitoring Tool </h2>

[![Project Status: Active](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)

## Table of Contents
* **[Motivation](#motivation)**
* **[YOLO Theory](#yolo-theory)**
* **[Detection Output](#detection-output)**
* **[Tech Stack](#tech-stack)**
* **[Functionalities](#functionalities)**
* **[To Do and Further Improvements](#to-do-and-further-improvements)**
* **[Requriements](#requirements)**
* **[Run Locally](#run-locally)**
* **[License](#license)**
* **[Contributors](#contributors)**

## Motivation
The current COVID-19 pandemic is showing negative effects on human health as well as on social and economic life. It is a critical and challenging task to revive public life while minimizing the risk of infection. Reducing interactions between people by social distancing is an effective and prevalent measure to reduce the risk of infection and spread of the virus within a community. And so, this project will help to monitor that.

## YOLO Theory
YOLO or You Only Look Once is an algorithm that uses neural networks to provide real-time object detection. Object detection in YOLO is done as a regression problem and provides the class probabilities of the detected images. 
As the name suggests, the algorithm requires only a single forward propagation through a neural network to detect objects.

## Detection Output
<p align="center">
  <img src="https://github.com/Pranav1007/Social-Distance-Detector/blob/main/media/static/Output.gif" alt="animated" />
</p>
<br/>
<h3 align="center">A single frame from Video 1</h3>

![Detection Output 1](https://github.com/Pranav1007/Social-Distance-Detector/blob/main/media/static/Det%20OP%201.png)

<h3 align="center">A single frame from Video 2</h3>

![Detection Output 2](https://github.com/Pranav1007/Social-Distance-Detector/blob/main/media/static/Det%20OP%202.png)

## Tech Stack
* Python

## Functionalities
* Detect people who are practicing social distancing and those who are not.
* Draw a green coloured box around those who are practicing social distancing and red for those who are not.
* Display the following information :
  * The threshold values used for detection.
  * Number of people recognized.
  * Number of people who are practicing social distancing.
  * Number of people who are not practicing social distancing.

## To Do and Further Improvements
- [x] Using YOLO for Image Detection
- [x] Calculate the distance between people and categorise them as safe and unsafe
- [x] Draw green coloured boxes for those who follow social distancing and red for those who don't.
- [x] Detect and draw boxes for image, video and live stream.
- [ ] Adding Birds-Eye View for the Video
- [ ] Work on the minimum pixel distance for different media.
- [ ] Assign a score at the end of the video/stream for every person based on the time they were not socially distanced.

## Requirements
The following dependencies and modules(python) are required, to run this locally 
* os, sys, argparse
* math
* mimetypes
* numpy==1.21.2
* opencv-python==4.5.3.56

**To install the requirements run:**
```python
$ pip install -r requirements.txt
```

## Run Locally
- **Clone the GitHub repository**
```python
$ git clone git@github.com:Pranav1007/Social-Distance-Detector.git
```

- **Move to the Project Directory**
```python
$ cd Social-Distance-Detector
```

- **Create a Virtual Environment (Optional)**

   * Install Virtualenv using pip (If it is not installed)
   ```python
    $ pip install virtualenv
    ```
   * Create the Virtual Environment
   ```python
   $ virtualenv sdd
   ```
   * Activate the Virtual Environment 
   
      * In MAC OS/Linux 
      ```python
      $ source sdd/bin/activate
      ```
      * In Windows
      ```python
      $ source sdd\Scripts\activate
      ```
  
- **Install the [requirements](requirements.txt)**
```python
(sdd) $ pip install -r requirements.txt
```

- **Run the python script [run.py](run.py) along with the appropriate arguements**
```python
(sdd) $ python3 run.py -i v -p media/test.mp4
```

- **Usage**
```python
"""
    Usage:
      usage: run.py [-h] [-m MEDIA] [-p PATH]

    optional arguements:
      -h --help                 Show this screen and exit.
      -m MEDIA --media MEDIA    Media Type (image(or i), video(or v), webcam(or w))
      -p PATH --path PATH       Path of the Media File (For webcam enter any character)
"""
```

- **Other options to Edit**
```python
   """
       You can go to the utilities/config.py and change the threshold values based on the video and system requirements.
   """
   # If you want to use GPU:
   Set USE_GPU = True
   # If you want to increase or decrease the minimum threshold distance
   Modify the DIST_THRES value
   # If you want to change the Non Maximum Supression Threshold or Confidence Threshold
   Modify the NMS_THRESH or CONF_THRESH values respectively
```

- **Dectivate the Virtual Environment (after you are done)**
```python
(sdd) $ deactivate
```

## License 
[![License](https://img.shields.io/badge/License-Apache%202.0-red.svg)](https://opensource.org/licenses/Apache-2.0)
<br/>
This project is under the Apache-2.0 License License. See [LICENSE](LICENSE) for Details.

## Contributors
<table>
  <tr>
    <td align="center"><img src="https://avatars.githubusercontent.com/u/70643852?s=96&v=4" width="100px;" height="100px;" alt=""/><br/><sub><b>Pranav B Kashyap</b></sub></a><br/><p align="center">
      <p align="center">
        <a href="https://www.linkedin.com/in/pranav-b-kashyap-1994001b6/" alt="Linkedin">
          <img src="http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width = "30">
        </a>
        <a href="https://github.com/Pranav1007" alt="Github">
          <img src="http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width = "30">
        </a>
      </p>
    </td>
    <td align="center"><img src="https://avatars.githubusercontent.com/u/76976349?v=4" width="100px;" height="100px;" alt=""/><br/><sub><b>Prakhar Singh</b></sub></a><br/><p align="center">
      <p align="center">
        <a href="https://www.linkedin.com/in/prakhar-singh-0bab09202/" alt="Linkedin">
          <img src="http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width = "30">
        </a>
        <a href="https://github.com/whattheprak" alt="Github">
          <img src="http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width = "30">
        </a>
      </p>
    </td>
    <td align="center"><img src="https://avatars.githubusercontent.com/u/56482375?v=4" width="100px;" height="100px;" alt=""/><br/><sub><b>Avi Tewari</b></sub></a><br/><p align="center">
      <p align="center">
        <a href="" alt="Linkedin">
          <img src="http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width = "30">
        </a>
        <a href="https://github.com/AviTewari" alt="Github">
          <img src="http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width = "30">
        </a>
      </p>
    </td>
  </tr>
</table>
