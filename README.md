Pohms - resistor or not resistor detector


## Installation

- Install Poetry

- Install dependencies 

  ```bash
  poetry install --develop .
  ```

- Spawn poetry shell
  ```bash
  poetry shell
  ```
  
- Run `pohms`

  ```bash
  pohms
  ```

- You can also see the help for the detection command with:
  ```bash 
  pohms detect --help 
  ```
  ```
  Usage: pohms detect [OPTIONS]                                    

    Detect whether an image or a group of images are resistors or not.                                                                                     

  Options:                                                                                                                                                 
    --path PATH         Image or folder location  [required]                                                                                               
    --model PATH        Path of pytorch model to use
    --img-cat-bin PATH  Bin location to display image on the commandline                                                                                   
    --help              Show this message and exit.   
  ```


## Usage

- Get some images of resistors and other items and save them on the root folder

- Run image prediction:
  ```bash
  # run inside env shell
  pohms detect --path example_image.jpg

  # or using poetry run command
  poetry run pohms detect --path example_image.jpg
  ```

- Profit!


## Explore

- Run empty `ipython`
  ```bash
  poetry run ipython
  ```

- Run `ipython` with loaded info
  ```bash
  poetry run ipython -i explore.py 
  ```


## Data aquisition

- [Electronic components images](https://www.onlinecomponents.com/productsearch/)