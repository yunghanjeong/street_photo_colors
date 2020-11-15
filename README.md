# Street Photography Color Analyzer
The main goal of this repository to study the color compositiion of street photography posted on r/streetphotography

## Procedure
1. Obtain reddit posts with image urls using PRAW.
2. Obtain binary image data from urls using io and requests libraries
3. Calculated most common color sets
4. Convert and sort color sets
5. Plot color swatches

## Medium Article
[article](https://yungh-jeong.medium.com/colors-of-street-photography-from-reddit-d5f2f3253e3c?sk=ae29bc3acab69d8dece9b5934e78ecea)

## Repository Structure
    .
    ├── src                             # source code for custom functions
    ├── images                          # contained matplotlib plots  
    ├── reddit_scrape_praw.ipynb        # notebook for analysis
    └── README.md

## Author
Yung Han Jeong
