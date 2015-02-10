#!/bin/sh

test -e ~/.applications/.qt-demos-installed && exit

. /etc/tizen-platform.conf

mkdir -p ~/.applications/desktop 2> /dev/null

changed=false

cat << EOC |
carol	samegame
bob	maroon
EOC
awk -v "user=${USER}" '$1==user{print $2}' |
while read demo
do
	if test -f "${TZ_SYS_SHARE}/qt-tizen-demo/${demo}.desktop"
	then
		cp "${TZ_SYS_SHARE}/qt-tizen-demo/${demo}.desktop" ~/.applications/desktop
		changed=true
	fi
done

$changed && pkill -U "${UID}" -USR1 tz-launcher
touch ~/.applications/.qt-demos-installed


