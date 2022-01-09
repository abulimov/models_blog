# Sources for models.bulimov.ru site

Uses [Hugo static site generator](gohugo.io)


## Setting things up

* Install hugo 1.9+
* Install *ghp-import* using `pip3 install ghp-import`


## Adding new content

### Post

`hugo new post/some-slug.md`


### Picture

Install 'Wand' module for python with `pip3 install Wand`, and use provided script:
`./add_img.py some-slug /path/to/new/file_1.jpg /path/to/new/file_2.jpg`


## Linting

Install [**Vale**](https://github.com/errata-ai/vale), run `make check`.


## Publishing

```
make github
```


## License

![by-sa](https://i.creativecommons.org/l/by-sa/4.0/80x15.png) [Creative Commons Attribution-ShareAlike 4.0 International License, except where indicated otherwise.](https://creativecommons.org/licenses/by-sa/4.0/)
