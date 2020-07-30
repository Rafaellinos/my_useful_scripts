for ip in $(cat $1); do nmap -A -F -T4 -vv $ip ; done
