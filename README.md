# Sources for models.bulimov.ru site

Uses [Hugo static site generator](gohugo.io)


## Setting things up

* Install hugo 1.9+
* Install *ghp-import* using `pip3 install ghp-import`


## Adding new content

### Post

`hugo new post/some-slug.md`


### Picture

Single:

`convert image.jpg -strip -resize 1920 static/images/models/some-slug/image_1920.jpg`

Multiple:

`for i in img1.jpg img2.jpg; do convert $i -strip -resize 1920 "static/images/models/some-slug/${i%.*}_1920.jpg"; done`




## Publishing

```
make github
```


## License

![by-sa](https://i.creativecommons.org/l/by-sa/4.0/80x15.png) [Creative Commons Attribution-ShareAlike 4.0 International License, except where indicated otherwise.](https://creativecommons.org/licenses/by-sa/4.0/)
