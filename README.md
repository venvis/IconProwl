

<p align="center">WebIconFinder : An unofficial  API for scraping images off IconFinder.com for web development.</p>
<div align="center">
<img src="https://uploads-ssl.webflow.com/5d9ba0eb5f6edb77992a99d0/5e1ef88d24ceb82897e14ec0_182503-512%20(1).png" style="border:1px solid white;" height="100" width="100">
</div>



## Initiate the Class  

```python

#To scrape for normal icons , create an instance of the class IconFinder with the name of the image to search  , for example : 

find_icon=IconFinder("mail")
```

###  1 : Scrape web links of images

```python

#To scrape for links of images , call the images() function from the initialized class , for example : 

find_icon=IconFinder("mail")
find_icon.images()
```

###  2 : Get Links to download and edit images

```python

#To scrape for links of images to download locally  , call the get_links() function from the initialized class , for example : 

find_icon=IconFinder("mail")
find_icon.get_links()
```

<div align="center">
<img src="bs4.png" style="border:1px solid white;" height="220" width="300">
</div>
