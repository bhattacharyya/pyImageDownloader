# pyImageDownloader
Download images from 4chan, reddit, imgur and twitter

All you need is python installed in your machine. You don't need to install additional libraries for these scripts to work.

The scripts scrape the HTML page containing the image file names rather than use the specific API. So in many cases all possible images may not be downloaded. For example you will get a max of 60 images downloaded from Imgur instead of the full album.

Usage:

`python 4chan_getthread.py threadType threadId` (e.g. python 4chan_getthread.py hr 2463159)

`python imgur_getalbum.py albumName`

`python reddit_getalbum.py subredditName`

`python twitter_getpics.py twitterHandle`

Options:
--ftype : yes downloads the files along with the file type appended (e.g. .jpg or .png). It is not recommended unless necessary. The image viewers do a better job of automatically figuring out the file type. Default option is "no"

--limit : (integer) limits the number of files downloaded. This saves bandwidth and space. The limit is for new files. If limit is 10, it will download 10 files that don't already exist in the folder.

Folders 4chan_imagebot & reddit_imgurbot contain the GUI downloaders for reddit albums and 4chan threads. It is recommended to use command lines if possible. Improvements on the GUI versions are going on.

Finally, it is easy to modify the scripts for use on many other websites.
