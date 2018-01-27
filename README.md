# Sources for models.bulimov.ru site

Uses [Hugo static site generator](gohugo.io)


## Setting things up

* Install hugo 1.9+
* Install *ghp-import* using `pip3 install ghp-import`


## Publishing

```
hugo && \
ghp-import -m 'Updated blog' -b gh-pages public && \
git push origin gh-pages
```


## License

[!by-sa](//i.creativecommons.org/l/by-sa/4.0/80x15.png) [Creative Commons Attribution-ShareAlike 4.0 International License, except where indicated otherwise.](https://creativecommons.org/licenses/by-sa/4.0/)
