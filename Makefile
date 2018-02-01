BASEDIR=$(CURDIR)
OUTPUTDIR=$(BASEDIR)/public
GITHUB_PAGES_BRANCH=gh-pages

help:
	@echo 'Makefile for a hugo Web site                                           '
	@echo '                                                                       '
	@echo 'Usage:                                                                 '
	@echo '   make clean                       remove the generated files         '
	@echo '   make publish                     generate site                      '
	@echo '   make github                      upload the web site via gh-pages   '
	@echo '                                                                       '
	@echo '                                                                       '

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

publish:
	hugo -b http://models.bulimov.ru

github: publish
	ghp-import -m 'Updated blog' -b $(GITHUB_PAGES_BRANCH) $(OUTPUTDIR)
	git push origin $(GITHUB_PAGES_BRANCH)
