Python-Google-Image-Search
==========================

This is a quick tool which enables you to search Google Images from python with a simple one-line command.

Use:
    
1. Place the .py file in your directory and write " from image_search import * " at the top of the file you want to use this module in.
    
2. Get a list of image results by calling 

    image_search("my query", n)
    

where n is the amount of results you want.

    
That's it!
    
    
    

Getting embed code for an image:
    
The original use for this module was to scrape images and automatically embed them into a web page, so 
I provide an 

    embeddable_image("query", n) 
    
function for convenience. This returns a list of n amount of HTML embed codes
for the images. It was suitable for my purpose, maybe it'll help you!
    
    
I hope this simple pair of functions helps you in some way!
    
    
