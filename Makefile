#! /usr/bin/gmake -f
# @author: Philippe Coval <philippe.coval@open.eurogiciel.org>
package?=qt-tizen
DESTDIR?=/usr/local/opt/${package}

default: all

%:
	@echo "todo: $@"

install: rootfs
	cd $< \
	&& find . -type d | while read file ; do \
	  install -d "${DESTDIR}/$${file}" ; \
	done

	cd $< \
	&& find . -type f | while read file ; do \
	  install "$${file}" "${DESTDIR}/$${file}" ; \
	done
