I am using Python **3.8.18**

In the required requirements.txt, following packages cannot be installed:

- chumpy: `requires legacy setup.py installation from git repo`

- open3d : version: 0.12.0 attempts to use *sklearn* which has been removed and renamed to *scikit-learn*

- wrapt : `requires legacy setup.py installation`

- termcolor : `requires legacy setup.py installation`

- StereoVision : `requires legacy setup.py installation`

- PyOpenGL: `requires legacy setup.py installation`

- pycrypto : `included in python3-dev`

- pycairo : `requires apt packages: no pip install necessary` 

    - libcairo2-dev 
    
    - pkg-config

    - python3-dev

#### Most likely scenario. The author of the repository used global pip freeze to generate requirements.txt

Additional package: **human-body-prior**

First need to generate the data.
Then copy male data (gender and shape files) from `data/my-dataset/generated`` to `data/nomo/prepared/<male/female>`

Then fit the model (hasn't done this step)

Then, run demo

Fix required:

- Due to mistake n training, the model is inversely trained with weight generates.

- fat people for small weights and thin people.

- The start ranges are:

| gender | height range (metres) | start limit for slimmest | end limit for obesely fat |
| --- | --- | --- | --- |
| male | 1.7 - 1.9 | 120 | -1 |
| male | 1.5 - 1.7 | 80 | |
| male | 1.2 - 1.5 | 30 | |

Since, it is really difficult to re-train the model; workaround will be to determine a equation to handle that translation using gender and weight to calculate the usable value
