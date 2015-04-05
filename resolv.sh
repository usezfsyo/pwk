#!/bin/bash

if [ -z "$1" ]; then
	echo "[*] Resolves dns name of ip addresses"
	echo "[*] Usage: $0 <txt file of ip addresses, one per line>"
	exit 0
fi

for ip in $(cat $1); do
nslookup $ip |grep "name" |cut -d" " -f3 && echo $ip;
done
